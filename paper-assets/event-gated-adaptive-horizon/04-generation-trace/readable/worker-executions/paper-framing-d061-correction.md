# paper framing d061 correction

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_framing-d061-correction_20260515T233429.log`
- **Structured JSON:** [`5202bff3fab2b67ac573.json`](../../sessions/52/5202bff3fab2b67ac573.json)

## Before a recorded user message

53 recorded events

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
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
  "uuid": "d453375f-1ae8-4f2a-bba9-e590a92d75d1",
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
    "resetsAt": 1778905200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "37eeba86-5b2e-4f59-b54c-20d100f667cb",
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to read and modify `paper_framing.md` for the event-gated-adaptive-horizon project. Let me start by reading the file using the MCP tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "1ed3f590-eae4-446c-8098-ccd612f85c2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEWrKMhHEKRXDYdYEMqSjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12291,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12291
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

### Assistant

_source line 5_

先读取 paper_framing.md 完整内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "4359d398-6e3e-45e8-9cec-7dcf458ecb9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEWrKMhHEKRXDYdYEMqSjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12291,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12291
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NLDx99RjoqAyWCsQkmkacV`</summary>

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "f298235f-e4cb-49e4-be4a-4f154301877a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEWrKMhHEKRXDYdYEMqSjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12291,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12291
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

_source line 7 · 2026-05-15T23:34:43.075Z_

<details><summary>↩ Tool result · `toolu_01NLDx99RjoqAyWCsQkmkacV`</summary>

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "eeb2a904-85e6-4ed8-8891-cfef09eaadde",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Vp9H8AWyJdohNZQYsumqSx`</summary>

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "ecea858f-7cb4-4511-9f27-047d6d8c8be0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJwxdQLth2dmcFkcAeW7eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 24132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
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

_source line 9 · 2026-05-15T23:34:45.862Z_

<details><summary>↩ Tool result · `toolu_01Vp9H8AWyJdohNZQYsumqSx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\n\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\n\\n原假设\\\"dt=1 imagination = practical mitigation\\\"被**否证**。跨 seed 数据：\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\n- **独立 seed 崩溃率: 1/2 (50%)**\\n\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\n\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\n\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\n\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\n|------|---------------------|---------------------|\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\n\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\n\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\"seed 2 本身不稳定\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\n\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\n|------|-------------------|------------|------|\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\n\\n**C6 最终状态: PARTIALLY FALSIFIED**\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\n- 崩溃是配置导致的，不是 seed 特异性\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\n\\n**论文表述建议**: \\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\"\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\n\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\n\\n### 6. Implications for Future Work\\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\\n\\n### Priority Actions Before Submission\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \\\"multiple vulnerability pathways\\\" (CIVO Pathway A + non-CIVO Pathway B)\\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\n\", \"total_chars\": 33051, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "5dbe15c2-76d0-439a-93dd-4d74ec70f5b8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\\\n\\\\n## Title Candidates\\\\n\\\\n1. **\\\\\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\\\\\"**\\\\n2. ~~**\\\\\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\\\\\"**~~ (deprecated — \\\\\\\"delusional critic\\\\\\\" conflicts with Lu et al. 2018)\\\\n3. **\\\\\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\\\\\"** ← preferred after D037 terminology decision\\\\n4. **\\\\\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\\\\\"**\\\\n\\\\n**⚠️ D037 术语决定**: \\\\\\\"delusional critic\\\\\\\" → **\\\\\\\"conditioning-induced value overestimation\\\\\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\\\\\"delusional critic\\\\\\\" → \\\\\\\"conditioning-induced value overestimation\\\\\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\\\n\\\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\\\\\"known failure class 的 specific instance\\\\\\\" 升级为 \\\\\\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\\\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\\\n\\\\n## Venue\\\\n\\\\n**CoRL 2026** — Deadline: 2026-05-29\\\\n\\\\n## Narrative Positioning\\\\n\\\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\\\n\\\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\\\n\\\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\\\n\\\\n---\\\\n\\\\n## Core Claims\\\\n\\\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\\\n\\\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\\\n\\\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\\\n\\\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\\\n\\\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\\\n\\\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\\\n\\\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\\\n\\\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\\\n\\\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\\\\\"point of no return\\\\\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\\\n\\\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\\\n| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |\\\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\\\n\\\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\\\\\"eliminates\\\\\\\" 改为 \\\\\\\"significantly delays and reduces\\\\\\\"。推荐方案仍是 008e_v3（C6）**。\\\\n\\\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\\\n\\\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\\\n|-------|------------|------------|---------|---------------|---------------|------------|\\\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\\\n\\\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\\\n\\\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\\\n\\\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\\\n\\\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\\\n\\\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\\\n\\\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\\\n\\\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\\\n\\\\n### C4: Longer dt amplifies the problem\\\\n\\\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\\\n\\\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\\\n\\\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\\\n\\\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\\\n\\\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\\\n\\\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\\\n\\\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\\\n\\\\n原假设\\\\\\\"dt=1 imagination = practical mitigation\\\\\\\"被**否证**。跨 seed 数据：\\\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\\\n- **独立 seed 崩溃率: 1/2 (50%)**\\\\n\\\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\\\n\\\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\\\n\\\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\\\n\\\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\\\n|------|---------------------|---------------------|\\\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\\\n\\\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\\\n\\\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\\\\\"seed 2 本身不稳定\\\\\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\\\n\\\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\\\n|------|-------------------|------------|------|\\\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\\\n\\\\n**C6 最终状态: PARTIALLY FALSIFIED**\\\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\\\n- 崩溃是配置导致的，不是 seed 特异性\\\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\\\n\\\\n**论文表述建议**: \\\\\\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\\\\\"\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\\\n\\\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\\\n\\\\n---\\\\n\\\\n## Story Arc\\\\n\\\\n### 1. Introduction\\\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\\\n\\\\n### 2. Background & Related Work\\\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\\\n- World-model RL (Dreamer family, IRIS, TWM)\\\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\\\n\\\\n### 3. Methodology\\\\n- DreamerV3 as base architecture\\\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\\\n\\\\n### 4. Results\\\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\\\\\"smoking gun\\\\\\\" comparison (008c vs 008d)\\\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\\\n- **Finding 4**: Longer dt amplifies (C4)\\\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\\\n\\\\n### 5. Discussion\\\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\\\\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\\\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\\\n\\\\n### 6. Implications for Future Work\\\\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\\\\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\\\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\\\n- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\\\\n- Need for diagnostic methodology in temporal abstraction research\\\\n\\\\n---\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1: \\\\\\\"Limited to one environment / one base algorithm\\\\\\\"\\\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\\\n\\\\n### R2: \\\\\\\"No proposed solution — what's the actionable takeaway?\\\\\\\"\\\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\\\\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\\\\n\\\\n### R3: \\\\\\\"Value/eval ratio is a crude proxy for overestimation\\\\\\\"\\\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\\\n\\\\n### R4: \\\\\\\"The factorial design is incomplete — missing cells in the grid\\\\\\\"\\\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\\\n\\\\n### R5: \\\\\\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\\\\\"\\\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\\\n\\\\n### R6: \\\\\\\"All results from a single seed — how robust are the conclusions?\\\\\\\"\\\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\\\n\\\\n### R7: \\\\\\\"The factorial design confounds dt_embedding training with training data composition\\\\\\\"\\\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\\\n\\\\n### R8: \\\\\\\"008f reward prediction degradation undermines the causal control\\\\\\\"\\\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\\\\\"去掉 dt_embedding → 不崩塌\\\\\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\\\n\\\\n---\\\\n\\\\n## Experiment Coverage Assessment\\\\n\\\\n| Claim | Evidence Status | Gaps |\\\\n|-------|----------------|------|\\\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\\\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\\\\n\\\\n### Priority Actions Before Submission\\\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\\\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\\\\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\\\\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \\\\\\\"multiple vulnerability pathways\\\\\\\" (CIVO Pathway A + non-CIVO Pathway B)\\\\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\\\\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\\\\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\\\\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\\\\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\\\\n\\\\n---\\\\n\\\\n## Key Figures (Planned)\\\\n\\\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\\\n\\\", \\\"total_chars\\\": 33051, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\n\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\n\\n原假设\\\"dt=1 imagination = practical mitigation\\\"被**否证**。跨 seed 数据：\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\n- **独立 seed 崩溃率: 1/2 (50%)**\\n\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\n\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\n\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\n\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\n|------|---------------------|---------------------|\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\n\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\n\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\"seed 2 本身不稳定\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\n\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\n|------|-------------------|------------|------|\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\n\\n**C6 最终状态: PARTIALLY FALSIFIED**\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\n- 崩溃是配置导致的，不是 seed 特异性\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\n\\n**论文表述建议**: \\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\"\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\n\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\n\\n### 6. Implications for Future Work\\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\\n\\n### Priority Actions Before Submission\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \\\"multiple vulnerability pathways\\\" (CIVO Pathway A + non-CIVO Pathway B)\\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\n\", \"total_chars\": 33051, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Now I have the full content of paper_framing.md. Let me carefully make all the required modifications:

**A. C2 evidence table — 016e 行**: Replace the SGS row in the C2 evidence table
**B. Section 6 safeguard (a)**: Replace the safeguard text
**C. 全文搜索修正**: Fix all "SGS delays/partially effective" expressions
**D. 新增梯度分解段落**: Add after RSSM Fidelity Table
**E. 016e/008d entropy comparison**: Add notes where needed


I'm loading the file locally to make these precise edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "60060157-dcf9-483b-9c1a-e708a2eed752",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UGdCpMsrhgL87DDER1QwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12644,
      "cache_read_input_tokens": 24903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12644
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

文件已读取（33051 字符）。现在逐项修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "69367b24-471b-4251-bbfd-4024b7f5db03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UGdCpMsrhgL87DDER1QwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12644,
      "cache_read_input_tokens": 24903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12644
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

<details open><summary>🔧 Tool call — Read · `toolu_01KrA9tYjWYDddotJHfNghsE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "6c3a4582-5409-4ba0-9041-57c8791692f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UGdCpMsrhgL87DDER1QwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12644,
      "cache_read_input_tokens": 24903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12644
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

_source line 13 · 2026-05-15T23:34:54.724Z_

<details><summary>↩ Tool result · `toolu_01KrA9tYjWYDddotJHfNghsE`</summary>

```text
1	# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL
2	
3	## Title Candidates
4	
5	1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
6	2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
7	3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
8	4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**
9	
10	**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。
11	
12	**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。
13	
14	## Venue
15	
16	**CoRL 2026** — Deadline: 2026-05-29
17	
18	## Narrative Positioning
19	
20	This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*
21	
22	The contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.
23	
24	We scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.
25	
26	---
27	
28	## Core Claims
29	
30	### C1: Variable-rate imagination in DreamerV3 consistently degrades performance
31	
32	Temporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.
33	
34	| Evidence | Experiment | Key Metric |
35	|----------|-----------|------------|
36	| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |
37	| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |
38	| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
39	| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |
40	
41	**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.
42	
43	### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk
44	
45	**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**
46	
47	The trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:
48	
49	- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)
50	- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)
51	- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb
52	
53	**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。
54	
55	**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a "point of no return" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).
56	
57	The trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).
58	
59	| Evidence | Experiment | Key Metric |
60	|----------|-----------|------------|
61	| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |
62	| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |
63	| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |
64	| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |
65	| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |
66	| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |
67	| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |
68	| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |
69	| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |
70	
71	**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 "eliminates" 改为 "significantly delays and reduces"。推荐方案仍是 008e_v3（C6）**。
72	
73	**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**
74	
75	| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
76	|-------|------------|------------|---------|---------------|---------------|------------|
77	| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |
78	| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |
79	| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |
80	
81	**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。
82	
83	**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.
84	
85	### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance
86	
87	When dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).
88	
89	| Evidence | Experiment | Key Metric |
90	|----------|-----------|------------|
91	| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |
92	| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |
93	| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |
94	| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |
95	| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |
96	
97	**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.
98	
99	**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).
100	
101	**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.
102	
103	### C4: Longer dt amplifies the problem
104	
105	Increasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.
106	
107	| Evidence | Experiment | Key Metric |
108	|----------|-----------|------------|
109	| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |
110	| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
111	| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |
112	
113	**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.
114	
115	### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause
116	
117	Subsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.
118	
119	| Evidence | Experiment | Key Metric |
120	|----------|-----------|------------|
121	| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |
122	| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |
123	| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |
124	| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |
125	| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |
126	
127	**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.
128	
129	### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself
130	
131	**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。
132	
133	原假设"dt=1 imagination = practical mitigation"被**否证**。跨 seed 数据：
134	- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）
135	- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）
136	- **独立 seed 崩溃率: 1/2 (50%)**
137	
138	对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。
139	
140	**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**
141	
142	Reviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：
143	
144	| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |
145	|------|---------------------|---------------------|
146	| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |
147	| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |
148	| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |
149	| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |
150	| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |
151	
152	**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。
153	
154	**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 "seed 2 本身不稳定" 假说。**008e_v3_s2 的崩溃是配置导致的**。
155	
156	| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |
157	|------|-------------------|------------|------|
158	| 85K | 618.7 | 715.2 | 008e_v3 略高 |
159	| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |
160	| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |
161	
162	**C6 最终状态: PARTIALLY FALSIFIED**
163	- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）
164	- 崩溃是配置导致的，不是 seed 特异性
165	- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性
166	
167	**论文表述建议**: "Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop."
168	
169	| Evidence | Experiment | Key Metric |
170	|----------|-----------|------------|
171	| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |
172	| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |
173	| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |
174	| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |
175	| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |
176	| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |
177	| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |
178	
179	**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。
180	
181	---
182	
183	## Story Arc
184	
185	### 1. Introduction
186	- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)
187	- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction
188	- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?
189	- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop
190	
191	### 2. Background & Related Work
192	- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)
193	- World-model RL (Dreamer family, IRIS, TWM)
194	- Variable-rate planning in world models (few prior works, mostly positive framing)
195	- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)
196	
197	### 3. Methodology
198	- DreamerV3 as base architecture
199	- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating
200	- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines
201	- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves
202	
203	### 4. Results
204	- **Finding 1**: All dt>1 configurations degrade (C1)
205	- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the "smoking gun" comparison (008c vs 008d)
206	- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)
207	- **Finding 4**: Longer dt amplifies (C4)
208	- **Finding 5**: Horizon/subsample effects are secondary (C5)
209	- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)
210	
211	### 5. Discussion
212	- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)
213	- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源
214	- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量
215	- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt
216	- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL
217	- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)
218	- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.
219	
220	### 6. Implications for Future Work
221	- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy
222	- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)
223	- RSSM prediction quality must improve before variable-rate imagination is viable
224	- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation
225	- Need for diagnostic methodology in temporal abstraction research
226	
227	---
228	
229	## Anticipated Reviewer Concerns
230	
231	### R1: "Limited to one environment / one base algorithm"
232	**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.
233	**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.
234	
235	### R2: "No proposed solution — what's the actionable takeaway?"
236	**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.
237	**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).
238	
239	### R3: "Value/eval ratio is a crude proxy for overestimation"
240	**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.
241	**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.
242	
243	### R4: "The factorial design is incomplete — missing cells in the grid"
244	**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.
245	**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.
246	
247	### R5: "Novelty concern — model exploitation / value overestimation in MBRL is well-known"
248	**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.
249	
250	### R6: "All results from a single seed — how robust are the conclusions?"
251	**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.
252	**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.
253	**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.
254	
255	### R7: "The factorial design confounds dt_embedding training with training data composition"
256	**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).
257	**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.
258	
259	### R8: "008f reward prediction degradation undermines the causal control"
260	**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是"去掉 dt_embedding → 不崩塌"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。
261	**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。
262	
263	---
264	
265	## Experiment Coverage Assessment
266	
267	| Claim | Evidence Status | Gaps |
268	|-------|----------------|------|
269	| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |
270	| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |
271	| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |
272	| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |
273	| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |
274	| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |
275	
276	### Priority Actions Before Submission
277	1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed
278	2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed
279	3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x
280	4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.
281	5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.
282	6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as "multiple vulnerability pathways" (CIVO Pathway A + non-CIVO Pathway B)
283	6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.
284	7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger
285	8. **Cheetah Run cross-environment** — P0 priority, addresses R1
286	9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table
287	10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost
288	
289	---
290	
291	## Key Figures (Planned)
292	
293	1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)
294	2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes
295	3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis
296	4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse
297	5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)
298	6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）
299	7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.
300	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "f36005c5-a4ae-448f-a645-57eb79eef2d4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
      "content": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
      "numLines": 300,
      "startLine": 1,
      "totalLines": 300
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
Now I have the full file. Let me make all the required modifications:

**A. C2 evidence table — 016e 行** (line 68): Replace the SGS row
**B. Section 6 safeguard (a)** (line 224): Replace the safeguard text
**C. 全文搜索修正**: Fix all "SGS delays/partially effective" expressions
**D. 新增梯度分解段落**: Add after RSSM Fidelity Table (after line 81)
**E. 016e/008d entropy comparison**: Add notes where needed


**F. Line 283 (6.5 priority item)**: Update the "SGS delays CIVO onset ~50K steps" reference
**G. Search and replace all instances**: "SGS delays onset ~50K steps", "raises peak 2x", and related phrases throughout the document

, including the Chinese versions at line 224

Now I'm cross-referencing the exact text to ensure I capture all occurrences — the English version mentions the delay and peak increase, while the Chinese section discusses the reward gradient pathway as a contributing factor. I need to make sure these are all updated consistently across both language sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "98e42cd7-72ae-408a-ae94-ba3552ded66e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NFh9io8N3Bv4qA9BsQgif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12930,
      "cache_read_input_tokens": 37547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12930
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

文件已读取。现在执行 5 项修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "7f9e8c2e-fe48-4db3-8e0d-3aa3d1a0f05f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NFh9io8N3Bv4qA9BsQgif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12930,
      "cache_read_input_tokens": 37547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12930
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

<details open><summary>🔧 Tool call — Edit · `toolu_01VMc6rQcReyFt36H8SvrtzE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "old_string": "| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |",
  "new_string": "| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "11b3fd24-1863-4462-9bf7-b7aaeb3a2c42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NFh9io8N3Bv4qA9BsQgif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12930,
      "cache_read_input_tokens": 37547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12930
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

_source line 17 · 2026-05-15T23:35:18.983Z_

<details><summary>↩ Tool result · `toolu_01VMc6rQcReyFt36H8SvrtzE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "730b1f53-2f92-440a-a06f-b46926e91c69",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
    "oldString": "| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |",
    "newString": "| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |",
    "originalFile": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
    "structuredPatch": [
      {
        "oldStart": 65,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " | **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |",
          " | **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |",
          " | **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |",
          "-| **SGS (reward detach) 不阻断 CIVO** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. SGS delays onset ~50K steps (008d@45K vs 016e@95K) and raises peak 2x (327 vs 167), but collapse is more severe (NVE 10.42x vs 4.12x). **Reward gradient pathway is a contributing factor (explains delay) but not the sole root cause** — CIVO operates at representation level through world model training. |",
          "+| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |",
          " | RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |",
          " ",
          " **⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。"
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

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01M8jfYiLEHDsmjrERe3qUpk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "old_string": "- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation",
  "new_string": "- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "d7f0b22a-316b-4577-ad61-10472d3dc615",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139nXvkQkwTqRxg8iFTytbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 50477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1277
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

_source line 19 · 2026-05-15T23:35:28.258Z_

<details><summary>↩ Tool result · `toolu_01M8jfYiLEHDsmjrERe3qUpk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "7503c80e-0c53-4190-95f3-8d37f764a36d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
    "oldString": "- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation",
    "newString": "- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation",
    "originalFile": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
    "structuredPatch": [
      {
        "oldStart": 221,
        "oldLines": 7,
        "newStart": 221,
        "newLines": 7,
        "lines": [
          " - **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy",
          " - Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)",
          " - RSSM prediction quality must improve before variable-rate imagination is viable",
          "-- Potential safeguards: (a) ~~detach dt_embedding gradients from critic~~ **已实测否定（exp_016e: reward_dt_emb_detach=True, v/e=658%@95K）— SGS 延迟崩溃 ~50K 步并提高峰值 2x（327 vs 167），说明 reward 梯度通路是贡献因素之一，但阻断它不足以防止 CIVO。根因在 representation level：world model training 本身将 dt>1 dynamics 编码进 dt_emb，使 critic 在 imagination 中系统性高估。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation",
          "+- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation",
          " - Need for diagnostic methodology in temporal abstraction research",
          " ",
          " ---"
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01GDUjWVofBhJtUhSrmRUpSX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "old_string": "**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。",
  "new_string": "**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "46d3623b-b84f-4072-9b51-86c935c48004",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151bKzjKBGZFDNftEY2cgKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 51754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 572
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

_source line 21 · 2026-05-15T23:35:41.827Z_

<details><summary>↩ Tool result · `toolu_01GDUjWVofBhJtUhSrmRUpSX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "d396fe78-6209-4a41-bea2-6ae45b3adce9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
    "oldString": "**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。",
    "newString": "**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。",
    "originalFile": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
    "structuredPatch": [
      {
        "oldStart": 80,
        "oldLines": 6,
        "newStart": 80,
        "newLines": 20,
        "lines": [
          " ",
          " **解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。",
          " ",
          "+**dt_emb Gradient Decomposition (D061)**",
          "+",
          "+梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：",
          "+",
          "+| Source | Grad Norm | Fraction |",
          "+|--------|-----------|----------|",
          "+| Observation decoders (orientations, velocity, height) | 1.505 | 93% |",
          "+| KL dynamics | 0.119 | 7% |",
          "+| Cont head | ~0 (included in decoder total) | <1% |",
          "+| **Reward head** | **0.000** | **0%** |",
          "+| **Total** | **1.624** | **100%** |",
          "+",
          "+这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。",
          "+",
          " **Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.",
          " ",
          " ### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance"
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

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01XCNwFR4HFWbLDPvMpFLWoF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "old_string": "6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.",
  "new_string": "6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "2ce64079-13fe-46b2-8229-f3020718a699",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011F1T7FTeXd8vMrZiESzJGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 52326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 678
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

_source line 23 · 2026-05-15T23:35:46.999Z_

<details><summary>↩ Tool result · `toolu_01XCNwFR4HFWbLDPvMpFLWoF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "1c49a4e1-8cf8-475f-8be9-99bf53c89006",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
    "oldString": "6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.",
    "newString": "6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。",
    "originalFile": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
    "structuredPatch": [
      {
        "oldStart": 294,
        "oldLines": 7,
        "newStart": 294,
        "newLines": 7,
        "lines": [
          " 4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.",
          " 5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.",
          " 6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)",
          "-6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: SGS delays CIVO onset ~50K steps (peak 327@75K vs 008d peak 167@35K) but does not prevent collapse (31.7@95K, NVE=10.42x). Reward gradient pathway is contributing factor (partial) but not sole root cause. CIVO is representation-level.",
          "+6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。",
          " 7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger",
          " 8. **Cheetah Run cross-environment** — P0 priority, addresses R1",
          " 9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table"
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

_source line 24_

现在搜索是否还有残留的 "SGS delays"/"partially effective"/"delays onset ~50K"/"raises peak 2x" 表述。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "820d7585-2210-4cfd-95d7-68ea50840c10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LZ8CKKUHxpojtkizUn869",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 53004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 553
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

<details open><summary>🔧 Tool call — Grep · `toolu_012qGqV8xzzgmvWeVa9z3FY8`</summary>

```json
{
  "pattern": "SGS delay|partially effective|delays onset|raises peak|reward gradient pathway is a contributing|SGS 延迟|贡献因素",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "4a543bbf-1a25-4c14-b67b-6471cbb82e84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LZ8CKKUHxpojtkizUn869",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 53004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 553
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

_source line 26 · 2026-05-15T23:35:50.988Z_

<details><summary>↩ Tool result · `toolu_012qGqV8xzzgmvWeVa9z3FY8`</summary>

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "720e44f3-0b73-4705-8731-2d7ca108ce59",
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

_source line 27_

残留表述已全部清除。现在检查是否有 016e/008d entropy 差异归因于 SGS 效果的段落（任务 E）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "5fbcc98a-7c44-464b-9e2d-ab9c15819244",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Soh6nZCBZHM2eMiMddy7Qf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 53557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01QkuQofm7YPBXpPUg4dUfYv`</summary>

```json
{
  "pattern": "016e.*entropy|entropy.*016e|016e.*008d.*entropy|008d.*016e.*entropy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "678ed05b-ff47-4657-bcc5-56792ad33230",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Soh6nZCBZHM2eMiMddy7Qf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 53557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 29 · 2026-05-15T23:35:55.460Z_

<details><summary>↩ Tool result · `toolu_01QkuQofm7YPBXpPUg4dUfYv`</summary>

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "6ecf4dfd-1015-40bf-8255-495459aee45c",
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

_source line 30_

文件中没有 016e/008d entropy 对比段落，无需加注。现在保存到项目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "1e1e5208-c91b-4710-8fa2-5ee1a9e459b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBxvsuW7yvmE6zTnBihKTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 53786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_015VHRyqQ1J1SUt9Mcw9U514`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "45cea35c-c5ea-4666-8fa3-c17732c70844",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBxvsuW7yvmE6zTnBihKTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 53786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
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

_source line 32 · 2026-05-15T23:35:59.091Z_

<details><summary>↩ Tool result · `toolu_015VHRyqQ1J1SUt9Mcw9U514`</summary>

```text
1	# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL
2	
3	## Title Candidates
4	
5	1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
6	2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
7	3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
8	4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**
9	
10	**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。
11	
12	**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。
13	
14	## Venue
15	
16	**CoRL 2026** — Deadline: 2026-05-29
17	
18	## Narrative Positioning
19	
20	This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*
21	
22	The contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.
23	
24	We scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.
25	
26	---
27	
28	## Core Claims
29	
30	### C1: Variable-rate imagination in DreamerV3 consistently degrades performance
31	
32	Temporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.
33	
34	| Evidence | Experiment | Key Metric |
35	|----------|-----------|------------|
36	| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |
37	| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |
38	| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
39	| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |
40	
41	**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.
42	
43	### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk
44	
45	**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**
46	
47	The trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:
48	
49	- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)
50	- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)
51	- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb
52	
53	**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。
54	
55	**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a "point of no return" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).
56	
57	The trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).
58	
59	| Evidence | Experiment | Key Metric |
60	|----------|-----------|------------|
61	| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |
62	| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |
63	| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |
64	| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |
65	| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |
66	| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |
67	| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |
68	| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |
69	| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |
70	
71	**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 "eliminates" 改为 "significantly delays and reduces"。推荐方案仍是 008e_v3（C6）**。
72	
73	**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**
74	
75	| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
76	|-------|------------|------------|---------|---------------|---------------|------------|
77	| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |
78	| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |
79	| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |
80	
81	**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。
82	
83	**dt_emb Gradient Decomposition (D061)**
84	
85	梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：
86	
87	| Source | Grad Norm | Fraction |
88	|--------|-----------|----------|
89	| Observation decoders (orientations, velocity, height) | 1.505 | 93% |
90	| KL dynamics | 0.119 | 7% |
91	| Cont head | ~0 (included in decoder total) | <1% |
92	| **Reward head** | **0.000** | **0%** |
93	| **Total** | **1.624** | **100%** |
94	
95	这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。
96	
97	**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.
98	
99	### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance
100	
101	When dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).
102	
103	| Evidence | Experiment | Key Metric |
104	|----------|-----------|------------|
105	| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |
106	| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |
107	| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |
108	| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |
109	| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |
110	
111	**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.
112	
113	**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).
114	
115	**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.
116	
117	### C4: Longer dt amplifies the problem
118	
119	Increasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.
120	
121	| Evidence | Experiment | Key Metric |
122	|----------|-----------|------------|
123	| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |
124	| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
125	| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |
126	
127	**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.
128	
129	### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause
130	
131	Subsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.
132	
133	| Evidence | Experiment | Key Metric |
134	|----------|-----------|------------|
135	| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |
136	| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |
137	| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |
138	| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |
139	| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |
140	
141	**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.
142	
143	### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself
144	
145	**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。
146	
147	原假设"dt=1 imagination = practical mitigation"被**否证**。跨 seed 数据：
148	- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）
149	- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）
150	- **独立 seed 崩溃率: 1/2 (50%)**
151	
152	对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。
153	
154	**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**
155	
156	Reviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：
157	
158	| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |
159	|------|---------------------|---------------------|
160	| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |
161	| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |
162	| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |
163	| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |
164	| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |
165	
166	**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。
167	
168	**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 "seed 2 本身不稳定" 假说。**008e_v3_s2 的崩溃是配置导致的**。
169	
170	| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |
171	|------|-------------------|------------|------|
172	| 85K | 618.7 | 715.2 | 008e_v3 略高 |
173	| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |
174	| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |
175	
176	**C6 最终状态: PARTIALLY FALSIFIED**
177	- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）
178	- 崩溃是配置导致的，不是 seed 特异性
179	- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性
180	
181	**论文表述建议**: "Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop."
182	
183	| Evidence | Experiment | Key Metric |
184	|----------|-----------|------------|
185	| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |
186	| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |
187	| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |
188	| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |
189	| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |
190	| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |
191	| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |
192	
193	**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。
194	
195	---
196	
197	## Story Arc
198	
199	### 1. Introduction
200	- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)
201	- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction
202	- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?
203	- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop
204	
205	### 2. Background & Related Work
206	- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)
207	- World-model RL (Dreamer family, IRIS, TWM)
208	- Variable-rate planning in world models (few prior works, mostly positive framing)
209	- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)
210	
211	### 3. Methodology
212	- DreamerV3 as base architecture
213	- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating
214	- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines
215	- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves
216	
217	### 4. Results
218	- **Finding 1**: All dt>1 configurations degrade (C1)
219	- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the "smoking gun" comparison (008c vs 008d)
220	- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)
221	- **Finding 4**: Longer dt amplifies (C4)
222	- **Finding 5**: Horizon/subsample effects are secondary (C5)
223	- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)
224	
225	### 5. Discussion
226	- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)
227	- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源
228	- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量
229	- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt
230	- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL
231	- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)
232	- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.
233	
234	### 6. Implications for Future Work
235	- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy
236	- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)
237	- RSSM prediction quality must improve before variable-rate imagination is viable
238	- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation
239	- Need for diagnostic methodology in temporal abstraction research
240	
241	---
242	
243	## Anticipated Reviewer Concerns
244	
245	### R1: "Limited to one environment / one base algorithm"
246	**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.
247	**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.
248	
249	### R2: "No proposed solution — what's the actionable takeaway?"
250	**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.
251	**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).
252	
253	### R3: "Value/eval ratio is a crude proxy for overestimation"
254	**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.
255	**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.
256	
257	### R4: "The factorial design is incomplete — missing cells in the grid"
258	**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.
259	**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.
260	
261	### R5: "Novelty concern — model exploitation / value overestimation in MBRL is well-known"
262	**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.
263	
264	### R6: "All results from a single seed — how robust are the conclusions?"
265	**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.
266	**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.
267	**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.
268	
269	### R7: "The factorial design confounds dt_embedding training with training data composition"
270	**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).
271	**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.
272	
273	### R8: "008f reward prediction degradation undermines the causal control"
274	**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是"去掉 dt_embedding → 不崩塌"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。
275	**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。
276	
277	---
278	
279	## Experiment Coverage Assessment
280	
281	| Claim | Evidence Status | Gaps |
282	|-------|----------------|------|
283	| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |
284	| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |
285	| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |
286	| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |
287	| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |
288	| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |
289	
290	### Priority Actions Before Submission
291	1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed
292	2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed
293	3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x
294	4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.
295	5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.
296	6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as "multiple vulnerability pathways" (CIVO Pathway A + non-CIVO Pathway B)
297	6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。
298	7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger
299	8. **Cheetah Run cross-environment** — P0 priority, addresses R1
300	9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table
301	10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost
302	
303	---
304	
305	## Key Figures (Planned)
306	
307	1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)
308	2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes
309	3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis
310	4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse
311	5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)
312	6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）
313	7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.
314	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "f88f78d2-c9e4-4628-828d-6fc95efe26c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
      "content": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
      "numLines": 314,
      "startLine": 1,
      "totalLines": 314
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
All edits are in place. Let me verify all changes by reading the modified content. The file looks correct with all 5 modifications applied:

1. **A** (line 68): C2 evidence table 016e row ✅ — replaced with "Reward SGS = no-op" framing
2. **B** (line 238): Section 6 safeguard (a) ✅ — replaced with "架构层面无效" + gradient decomposition
3. **C**: All "SGS delays"/"partially effective" expressions ✅ — grep returned no matches


4. **D** (lines 83-95): New gradient decomposition paragraph ✅ — inserted after RSSM Fidelity Table
5. **E**: No 016e/008d entropy comparison exists ✅ — no action needed

Now I'll save the file via the MCP tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "82b5ceb8-b839-4d68-a21b-1102712ab8cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9THR5fiRdnJVNECtkFaFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13114,
      "cache_read_input_tokens": 54014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13114
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

_source line 34_

所有本地编辑已完成，验证无残留。现在通过 MCP 保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "150a8025-4941-4f42-b575-41206c64df03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9THR5fiRdnJVNECtkFaFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13114,
      "cache_read_input_tokens": 54014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13114
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01S7opzZVnfBZaNis9ynSaUb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "196df214-d0e7-4a41-917b-a82e851eb5b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9THR5fiRdnJVNECtkFaFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13114,
      "cache_read_input_tokens": 54014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13114
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

_source line 36 · 2026-05-15T23:36:09.112Z_

<details><summary>↩ Tool result · `toolu_01S7opzZVnfBZaNis9ynSaUb`</summary>

```text
1	# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "a0b8d730-e520-453f-8206-bbd6709dbe3d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
      "content": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 314
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cqnq17ugRcugHRtzFZhot9`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "description": "Read full file content for MCP save"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "6ead1bb7-db3f-4608-9e21-ac7df20de448",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RU2TiZAQfKbxVUYZ5NGifJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 67128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 386
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

_source line 38 · 2026-05-15T23:36:12.505Z_

<details><summary>↩ Tool result · `toolu_01Cqnq17ugRcugHRtzFZhot9`</summary>

```text
&lt;persisted-output>
Output too large (35.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/bbmqj73v0.txt

Preview (first 2KB):
# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL

## Title Candidates

1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**

**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。

**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。

## Venue

**CoRL 2026** — Deadline: 2026-05-29

## Narrative Positioning

This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "1acb65f5-055c-4771-9b72-c0a0fc2a649b",
  "tool_use_result": {
    "stdout": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/bbmqj73v0.txt",
    "persistedOutputSize": 36194
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01WSqC2XFDndTddVuZztEhTK`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/bbmqj73v0.txt",
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "6a2a5aeb-cc31-4126-b912-94bc964c1b14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcD7hRFbM4W2KdhS6BuwHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 815,
      "cache_read_input_tokens": 67514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 815
      },
      "output_tokens": 65,
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

_source line 40 · 2026-05-15T23:36:15.451Z_

<details><summary>↩ Tool result · `toolu_01WSqC2XFDndTddVuZztEhTK`</summary>

```text
1	# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "718eb581-2b00-4ed0-8e72-55fb8c9ddd68",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/bbmqj73v0.txt",
      "content": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 314
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01KfLzFE4GZKF1sE2Ahu4BjX`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "11741edd-2e74-45dc-b5b4-06bfc9594ef2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKHcdxmes5imX9MtkT9P17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 68329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 290
      },
      "output_tokens": 55,
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

_source line 42 · 2026-05-15T23:36:18.402Z_

<details><summary>↩ Tool result · `toolu_01KfLzFE4GZKF1sE2Ahu4BjX`</summary>

```text
36194 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "3cbb613b-3887-44a4-b009-4427a0b2dab5",
  "tool_use_result": {
    "stdout": "36194 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md",
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_011Z91gj4Nsn1AD3cRxge7he`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md | head -c 40000",
  "description": "Read full file for MCP save"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "99c991f7-5387-42e0-ba6b-d6bf98fca88c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpeSzCsSKCPdHzn8do99mo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 68619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 163
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

_source line 44 · 2026-05-15T23:36:21.530Z_

<details><summary>↩ Tool result · `toolu_011Z91gj4Nsn1AD3cRxge7he`</summary>

```text
&lt;persisted-output>
Output too large (35.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/b450v0nxz.txt

Preview (first 2KB):
# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL

## Title Candidates

1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**

**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。

**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。

## Venue

**CoRL 2026** — Deadline: 2026-05-29

## Narrative Positioning

This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*

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
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "2e509f75-c286-4227-8f9f-9e89d17acb7e",
  "tool_use_result": {
    "stdout": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/b450v0nxz.txt",
    "persistedOutputSize": 36194
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
The file is too large for preview but I have it locally. Let me read the full content from the persisted file and pass it to save_project_file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "75d67960-0717-44dc-813c-aef34bf34b58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEifFPfsyKYjx5xi6k8m49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 68782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 821
      },
      "output_tokens": 13,
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

_source line 46_

文件已在本地编辑完成（36194 bytes）。用 save_project_file 保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "c39f4d82-1805-4d7e-9dd8-9edb1360abfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEifFPfsyKYjx5xi6k8m49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 68782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 821
      },
      "output_tokens": 13,
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

<details open><summary>🔧 Tool call — Read · `toolu_01Anjdefa6GY7iWNpPSqkept`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/b450v0nxz.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "72349d45-ade7-4b8e-a8c6-ba41aed5e017",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEifFPfsyKYjx5xi6k8m49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 68782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 821
      },
      "output_tokens": 13,
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

_source line 48 · 2026-05-15T23:36:26.984Z_

<details><summary>↩ Tool result · `toolu_01Anjdefa6GY7iWNpPSqkept`</summary>

```text
1	# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL
2	
3	## Title Candidates
4	
5	1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
6	2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
7	3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
8	4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**
9	
10	**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。
11	
12	**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。
13	
14	## Venue
15	
16	**CoRL 2026** — Deadline: 2026-05-29
17	
18	## Narrative Positioning
19	
20	This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*
21	
22	The contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.
23	
24	We scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.
25	
26	---
27	
28	## Core Claims
29	
30	### C1: Variable-rate imagination in DreamerV3 consistently degrades performance
31	
32	Temporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.
33	
34	| Evidence | Experiment | Key Metric |
35	|----------|-----------|------------|
36	| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |
37	| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |
38	| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
39	| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |
40	
41	**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.
42	
43	### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk
44	
45	**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**
46	
47	The trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:
48	
49	- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)
50	- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)
51	- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb
52	
53	**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。
54	
55	**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a "point of no return" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).
56	
57	The trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).
58	
59	| Evidence | Experiment | Key Metric |
60	|----------|-----------|------------|
61	| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |
62	| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |
63	| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |
64	| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |
65	| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |
66	| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |
67	| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |
68	| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |
69	| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |
70	
71	**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 "eliminates" 改为 "significantly delays and reduces"。推荐方案仍是 008e_v3（C6）**。
72	
73	**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**
74	
75	| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
76	|-------|------------|------------|---------|---------------|---------------|------------|
77	| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |
78	| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |
79	| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |
80	
81	**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。
82	
83	**dt_emb Gradient Decomposition (D061)**
84	
85	梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：
86	
87	| Source | Grad Norm | Fraction |
88	|--------|-----------|----------|
89	| Observation decoders (orientations, velocity, height) | 1.505 | 93% |
90	| KL dynamics | 0.119 | 7% |
91	| Cont head | ~0 (included in decoder total) | <1% |
92	| **Reward head** | **0.000** | **0%** |
93	| **Total** | **1.624** | **100%** |
94	
95	这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。
96	
97	**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.
98	
99	### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance
100	
101	When dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).
102	
103	| Evidence | Experiment | Key Metric |
104	|----------|-----------|------------|
105	| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |
106	| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |
107	| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |
108	| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |
109	| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |
110	
111	**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.
112	
113	**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).
114	
115	**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.
116	
117	### C4: Longer dt amplifies the problem
118	
119	Increasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.
120	
121	| Evidence | Experiment | Key Metric |
122	|----------|-----------|------------|
123	| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |
124	| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
125	| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |
126	
127	**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.
128	
129	### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause
130	
131	Subsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.
132	
133	| Evidence | Experiment | Key Metric |
134	|----------|-----------|------------|
135	| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |
136	| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |
137	| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |
138	| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |
139	| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |
140	
141	**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.
142	
143	### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself
144	
145	**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。
146	
147	原假设"dt=1 imagination = practical mitigation"被**否证**。跨 seed 数据：
148	- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）
149	- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）
150	- **独立 seed 崩溃率: 1/2 (50%)**
151	
152	对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。
153	
154	**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**
155	
156	Reviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：
157	
158	| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |
159	|------|---------------------|---------------------|
160	| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |
161	| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |
162	| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |
163	| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |
164	| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |
165	
166	**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。
167	
168	**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 "seed 2 本身不稳定" 假说。**008e_v3_s2 的崩溃是配置导致的**。
169	
170	| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |
171	|------|-------------------|------------|------|
172	| 85K | 618.7 | 715.2 | 008e_v3 略高 |
173	| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |
174	| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |
175	
176	**C6 最终状态: PARTIALLY FALSIFIED**
177	- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）
178	- 崩溃是配置导致的，不是 seed 特异性
179	- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性
180	
181	**论文表述建议**: "Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop."
182	
183	| Evidence | Experiment | Key Metric |
184	|----------|-----------|------------|
185	| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |
186	| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |
187	| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |
188	| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |
189	| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |
190	| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |
191	| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |
192	
193	**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。
194	
195	---
196	
197	## Story Arc
198	
199	### 1. Introduction
200	- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)
201	- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction
202	- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?
203	- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop
204	
205	### 2. Background & Related Work
206	- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)
207	- World-model RL (Dreamer family, IRIS, TWM)
208	- Variable-rate planning in world models (few prior works, mostly positive framing)
209	- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)
210	
211	### 3. Methodology
212	- DreamerV3 as base architecture
213	- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating
214	- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines
215	- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves
216	
217	### 4. Results
218	- **Finding 1**: All dt>1 configurations degrade (C1)
219	- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the "smoking gun" comparison (008c vs 008d)
220	- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)
221	- **Finding 4**: Longer dt amplifies (C4)
222	- **Finding 5**: Horizon/subsample effects are secondary (C5)
223	- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)
224	
225	### 5. Discussion
226	- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)
227	- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源
228	- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量
229	- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt
230	- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL
231	- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)
232	- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.
233	
234	### 6. Implications for Future Work
235	- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy
236	- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)
237	- RSSM prediction quality must improve before variable-rate imagination is viable
238	- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation
239	- Need for diagnostic methodology in temporal abstraction research
240	
241	---
242	
243	## Anticipated Reviewer Concerns
244	
245	### R1: "Limited to one environment / one base algorithm"
246	**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.
247	**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.
248	
249	### R2: "No proposed solution — what's the actionable takeaway?"
250	**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.
251	**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).
252	
253	### R3: "Value/eval ratio is a crude proxy for overestimation"
254	**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.
255	**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.
256	
257	### R4: "The factorial design is incomplete — missing cells in the grid"
258	**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.
259	**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.
260	
261	### R5: "Novelty concern — model exploitation / value overestimation in MBRL is well-known"
262	**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.
263	
264	### R6: "All results from a single seed — how robust are the conclusions?"
265	**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.
266	**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.
267	**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.
268	
269	### R7: "The factorial design confounds dt_embedding training with training data composition"
270	**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).
271	**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.
272	
273	### R8: "008f reward prediction degradation undermines the causal control"
274	**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是"去掉 dt_embedding → 不崩塌"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。
275	**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。
276	
277	---
278	
279	## Experiment Coverage Assessment
280	
281	| Claim | Evidence Status | Gaps |
282	|-------|----------------|------|
283	| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |
284	| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |
285	| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |
286	| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |
287	| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |
288	| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |
289	
290	### Priority Actions Before Submission
291	1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed
292	2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed
293	3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x
294	4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.
295	5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.
296	6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as "multiple vulnerability pathways" (CIVO Pathway A + non-CIVO Pathway B)
297	6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。
298	7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger
299	8. **Cheetah Run cross-environment** — P0 priority, addresses R1
300	9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table
301	10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost
302	
303	---
304	
305	## Key Figures (Planned)
306	
307	1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)
308	2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes
309	3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis
310	4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse
311	5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)
312	6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）
313	7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.
314	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "fe6ea89d-1eb3-48ec-a050-db0462af7e96",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8/tool-results/b450v0nxz.txt",
      "content": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n",
      "numLines": 314,
      "startLine": 1,
      "totalLines": 314
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

内容确认无误。通过 MCP 保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "71484301-708e-4f54-8db9-5b6cf6db5966",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143dQ7xFHXE9fiZmnc8MQga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13207,
      "cache_read_input_tokens": 69603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13207
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

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01Hrfa7ECPzgLrUGHjzqoAHJ`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_framing.md",
  "content": "# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\n\n## Title Candidates\n\n1. **\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\"**\n2. ~~**\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\"**~~ (deprecated — \"delusional critic\" conflicts with Lu et al. 2018)\n3. **\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"** ← preferred after D037 terminology decision\n4. **\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\"**\n\n**⚠️ D037 术语决定**: \"delusional critic\" → **\"conditioning-induced value overestimation\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\"delusional critic\" → \"conditioning-induced value overestimation\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\n\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \"known failure class 的 specific instance\" 升级为 \"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\"**。TAWM 是强化 novelty 的最关键参考文献。\n\n## Venue\n\n**CoRL 2026** — Deadline: 2026-05-29\n\n## Narrative Positioning\n\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\n\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\n\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\n\n---\n\n## Core Claims\n\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\n\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\n\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\n\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\n\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\n\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\n\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\n\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\n\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \"point of no return\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\n\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\n\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \"eliminates\" 改为 \"significantly delays and reduces\"。推荐方案仍是 008e_v3（C6）**。\n\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\n\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\n\n**dt_emb Gradient Decomposition (D061)**\n\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\n\n| Source | Grad Norm | Fraction |\n|--------|-----------|----------|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\n| KL dynamics | 0.119 | 7% |\n| Cont head | ~0 (included in decoder total) | <1% |\n| **Reward head** | **0.000** | **0%** |\n| **Total** | **1.624** | **100%** |\n\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\n\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\n\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\n\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\n\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\n\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\n\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\n\n### C4: Longer dt amplifies the problem\n\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\n\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\n\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\n\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\n\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\n\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\n\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\n\n原假设\"dt=1 imagination = practical mitigation\"被**否证**。跨 seed 数据：\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\n- **独立 seed 崩溃率: 1/2 (50%)**\n\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\n\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\n\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\n\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\n|------|---------------------|---------------------|\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\n\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\n\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \"seed 2 本身不稳定\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\n\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\n|------|-------------------|------------|------|\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\n\n**C6 最终状态: PARTIALLY FALSIFIED**\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\n- 崩溃是配置导致的，不是 seed 特异性\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\n\n**论文表述建议**: \"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\"\n\n| Evidence | Experiment | Key Metric |\n|----------|-----------|------------|\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\n\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\n\n---\n\n## Story Arc\n\n### 1. Introduction\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\n\n### 2. Background & Related Work\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\n- World-model RL (Dreamer family, IRIS, TWM)\n- Variable-rate planning in world models (few prior works, mostly positive framing)\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\n\n### 3. Methodology\n- DreamerV3 as base architecture\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\n\n### 4. Results\n- **Finding 1**: All dt>1 configurations degrade (C1)\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \"smoking gun\" comparison (008c vs 008d)\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\n- **Finding 4**: Longer dt amplifies (C4)\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\n\n### 5. Discussion\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\n\n### 6. Implications for Future Work\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\n- RSSM prediction quality must improve before variable-rate imagination is viable\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\n- Need for diagnostic methodology in temporal abstraction research\n\n---\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Limited to one environment / one base algorithm\"\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\n\n### R2: \"No proposed solution — what's the actionable takeaway?\"\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\n\n### R3: \"Value/eval ratio is a crude proxy for overestimation\"\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\n\n### R4: \"The factorial design is incomplete — missing cells in the grid\"\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\n\n### R5: \"Novelty concern — model exploitation / value overestimation in MBRL is well-known\"\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\n\n### R6: \"All results from a single seed — how robust are the conclusions?\"\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\n\n### R7: \"The factorial design confounds dt_embedding training with training data composition\"\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\n\n### R8: \"008f reward prediction degradation undermines the causal control\"\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\"去掉 dt_embedding → 不崩塌\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\n\n---\n\n## Experiment Coverage Assessment\n\n| Claim | Evidence Status | Gaps |\n|-------|----------------|------|\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\n\n### Priority Actions Before Submission\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \"multiple vulnerability pathways\" (CIVO Pathway A + non-CIVO Pathway B)\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\n\n---\n\n## Key Figures (Planned)\n\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "70337bf7-32ff-4b7f-9191-6ad35aaddee7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143dQ7xFHXE9fiZmnc8MQga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13207,
      "cache_read_input_tokens": 69603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13207
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

_source line 51 · 2026-05-15T23:41:13.341Z_

<details><summary>↩ Tool result · `toolu_01Hrfa7ECPzgLrUGHjzqoAHJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "4eefc850-9d59-4948-9cbd-0348c48259c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

D061 修正完成。修改摘要：

- **A. C2 证据表 016e 行**：从 "SGS delays onset / reward gradient is contributing factor" → "Reward SGS = no-op (reward gradient = 0 by architecture)，差异归因于随机变异"
- **B. Section 6 safeguard (a)**：从 "已实测否定，SGS 延迟崩溃" → "架构层面无效（reward gradient = 0 by design），真正干预目标是 observation decoder→dt_emb 梯度通路"
- **C. 全文残留清扫**：grep 确认无 "SGS delays"/"partially effective"/"贡献因素" 等残留
- **D. 新增梯度分解表**：RSSM Fidelity Table 之后插入 dt_emb Gradient Decomposition (D061) 段落，含 5 行梯度来源分布表 + 3 条推论
- **E. Priority Actions 6.5**：更新为 no-op 结论，删除旧的 "delays/contributing factor" 措辞
- **016e 实验数据保留**，仅修正归因解读

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "uuid": "aaf80489-6809-4d5d-8e61-60e2a709cd5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbUeE3FxBLhwWTdhTgGSjz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12482,
      "cache_read_input_tokens": 82810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12482
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

_source line 53_

D061 修正完成。修改摘要：

- **A. C2 证据表 016e 行**：从 "SGS delays onset / reward gradient is contributing factor" → "Reward SGS = no-op (reward gradient = 0 by architecture)，差异归因于随机变异"
- **B. Section 6 safeguard (a)**：从 "已实测否定，SGS 延迟崩溃" → "架构层面无效（reward gradient = 0 by design），真正干预目标是 observation decoder→dt_emb 梯度通路"
- **C. 全文残留清扫**：grep 确认无 "SGS delays"/"partially effective"/"贡献因素" 等残留
- **D. 新增梯度分解表**：RSSM Fidelity Table 之后插入 dt_emb Gradient Decomposition (D061) 段落，含 5 行梯度来源分布表 + 3 条推论
- **E. Priority Actions 6.5**：更新为 no-op 结论，删除旧的 "delays/contributing factor" 措辞
- **016e 实验数据保留**，仅修正归因解读

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 404952,
  "duration_api_ms": 404876,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "bf74a7e7-aa7c-47df-ac01-7a1f26b18fd8",
  "total_cost_usd": 1.44491675,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 83451,
    "cache_read_input_tokens": 960126,
    "output_tokens": 17637,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 83451,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 328,
        "cache_read_input_tokens": 82810,
        "cache_creation_input_tokens": 12482,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 12482
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2145,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002255,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 17637,
      "cacheReadInputTokens": 960126,
      "cacheCreationInputTokens": 83451,
      "webSearchRequests": 0,
      "costUSD": 1.4426617499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a79351ab-2d5b-4e5e-8e7d-5c9a2dfe062b"
}
```

</details>

---
