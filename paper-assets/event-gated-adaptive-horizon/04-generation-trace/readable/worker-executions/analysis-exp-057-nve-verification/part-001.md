# analysis exp 057 nve verification — Part 1 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[Transcript overview](../analysis-exp-057-nve-verification.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/81/81bcaa79d141b996d00f.json)

## Before a recorded user message

## Before a recorded user message

104 recorded events


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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
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
  "uuid": "069d6b61-a06e-4512-b2c0-a949d132f29c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779597600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2cb2fa6e-4ff8-44ca-be73-e0acf4ed09a1",
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task. I need to verify the NVE (Normalized Value Error) calculation for exp_057 and other Walker frozen experiments. Let me start by:

1. Reading project files for NVE definition
2. Checking the registry for baseline experiments
3. SSH to the server to search for NVE definition in paper files and extract metrics

Let me do multiple things in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "cdb56f57-6795-406d-85bd-36ddcc4abf21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKBo3vrEBiWyf45CifPMzF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12641,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12641
      },
      "output_tokens": 31,
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

开始验证 NVE 计算。先并行收集定义和数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "0664408f-ebb5-4d2a-bc4e-f0a3389215ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKBo3vrEBiWyf45CifPMzF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12641,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12641
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D1NrTBe5nLkUFt84Vt7cfF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "36ebfee5-5159-449f-b0f1-5303546c35e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKBo3vrEBiWyf45CifPMzF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12641,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12641
      },
      "output_tokens": 31,
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

_source line 7 · 2026-05-24T01:50:34.353Z_

<details><summary>↩ Tool result · `toolu_01D1NrTBe5nLkUFt84Vt7cfF`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "f5a9c6e2-8416-4933-a77b-94e27686217b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LdHmQfKizmXQE2pvDs8QKD`</summary>

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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "37ed3176-ceda-4704-ab4b-53797c350a25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133ShyuDamDTCz81dSiVeX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1435
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


### Tool result

_source line 9 · 2026-05-24T01:50:37.323Z_

<details><summary>↩ Tool result · `toolu_01LdHmQfKizmXQE2pvDs8QKD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**⚠️ 修正：reward head 贡献最大梯度（49%@55K），obs decoder 仅 16.3%。但 reward-only SGS 仍失败——梯度大小与因果重要性解耦。** |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**dt_emb Gradient Decomposition (D061) — ⚠️ 已修正**\\n\\n梯度验证（torch.autograd.grad analysis, correct config gate_fixed_dt=2）揭示 dt_emb.weight 的梯度来源分布：\\n\\n| Source | 55K (%) | 112K (%) |\\n|--------|---------|----------|\\n| Reward head | 49.0 | 38.1 |\\n| KL dynamics | 34.7 | 40.4 |\\n| Observation decoders | 16.3 | 21.5 |\\n| Cont head | ~0 | ~0 |\\n\\n⚠️ **之前的 93% obs / 0% reward 数据不可复现**（见 gradient_decomposition_008d_corrected.json）。正确结论：reward head 贡献最大梯度（38-49%），但 reward-only SGS (016e) 仍然失败（NVE=10.42×）；obs decoder 通路（16-22%）虽贡献最小，但携带关键的 Δt-specific 空间信息驱动 RSSM fidelity gap。**梯度大小与因果重要性解耦**是核心发现。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\n\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\n\\n原假设\\\"dt=1 imagination = practical mitigation\\\"被**否证**。跨 seed 数据：\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\n- **独立 seed 崩溃率: 1/2 (50%)**\\n\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\n\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\n\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\n\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\n|------|---------------------|---------------------|\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\n\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\n\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\"seed 2 本身不稳定\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\n\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\n|------|-------------------|------------|------|\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\n\\n**C6 最终状态: PARTIALLY FALSIFIED**\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\n- 崩溃是配置导致的，不是 seed 特异性\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\n\\n**论文表述建议**: \\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\"\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\n\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\n\\n### C7: Gradient-level interventions fail to eliminate CIVO — gradient magnitude decoupled from causal importance\\n\\n**⚠️ D107: SGS 全面失败，梯度干预不是正确的干预层级**\\n\\nAll three SGS variants fail to eliminate CIVO:\\n- **Reward-only SGS** (016e): 0/2, NVE=10.42× — paradoxically worse than untreated\\n- **Full-pathway SGS** (018+021): 0/3 across two environments — blocks all non-KL gradients, still fails\\n- **Obs-decoder-only SGS** (025+026): 1/6 across two environments — the identified causal channel, still fails\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Reward-only SGS 反效果 | exp_016e | NVE=10.42×, collapse to eval 31.7. 阻断 reward 梯度迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差 |\\n| Full SGS 0/3 | exp_018 (Walker 2 seeds) + exp_021 (Cheetah 1 seed) | s1: eval 448.3, NVE 1.66× (CIVO+); s2: collapse 40.8; Cheetah: transient NVE 9.94×→0.34× (not SGS effect) |\\n| Obs-decoder SGS 1/6 | exp_025 (Walker 4 seeds) + exp_026 (Cheetah 2 seeds) | Walker: 1/4 (s1 survived, s2-s4 collapsed); Cheetah: 0/2, NVE 21.9×-30.2× (2.6-3.6× worse than untreated 8.3×) |\\n| Compensatory amplification (Cheetah) | exp_026 vs exp_010b | Obs-decoder SGS NVE 21.9-30.2× vs untreated 8.3× — blocking obs-decoder shifts co-adaptation to reward head |\\n| Universal value collapse | exp_025 all seeds @215K | All 4 seeds terminal ve_ratio=0.056-0.14, including s1 \\\"success\\\" (eval 726, value 41) — critic underestimation as side effect |\\n| Fourth trajectory (s3) | exp_025_s3 | Healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery (590@215K) → persistent value collapse (ve_ratio 0.14) |\\n\\n**核心发现**：\\n1. **梯度量级与因果重要性脱耦**: Reward head 38-49% 梯度占比（最大），但 reward-only SGS 失败最惨；obs decoder 16-22%（最小非零），但 obs-decoder SGS 也失败。梯度分解成功作为**诊断工具**但失败作为**干预指南**。\\n2. **Backward-pass 是错误的干预层级**: Full SGS 阻断所有非 KL 梯度仍 0/3 → forward-pass representational damage 是不可约减的脆弱性底线。Temporal embedding 通过 forward pass 塑造潜在表示，无论哪些梯度更新它。\\n3. **补偿放大**: 阻断任一通道导致剩余通道放大 co-adaptation（Cheetah: 2.6-3.6× 放大）。\\n4. **SGS 副作用**: 即使\\\"成功\\\"的 seed 也遭受 critic 校准损坏（universal value collapse）。\\n\\n**Strength**: Strong. 17 seeds across 3 SGS variants and 2 environments. Only 1/17 avoids CIVO, and that seed still suffers value collapse. Embedding removal (008f+024b): 5/5 = 100% prevention. The contrast establishes gradient stopping as categorically insufficient.\\n\\n### C8: Forward-pass interventions — TCN and RAVE (🔄 验证中)\\n\\n**⚠️ D107/D108: 两种 forward-pass 干预方法并行验证**\\n\\nSGS 失败的根因是 backward-pass 干预无法消除 forward-pass representational damage。C8 提出绕过梯度冗余的 forward-pass 干预：\\n\\n**TCN (Temporal Conditioning Noise)**:\\n- 设计理念：imagination 时对 dt_embedding 输出加高斯噪声 $\\\\mathcal{N}(0, \\\\sigma^2)$，降低 conditioning 精度\\n- 机制假说：噪声阻止 RSSM 和 critic 对精确 dt 信号的过度 co-adaptation，同时保留粗粒度时间信息\\n- 与 SGS 的区别：在 forward pass 层面操作，不依赖梯度阻断\\n- 超参：σ=0.5×std（主实验）+ σ=0.2×std（替代超参）\\n- 实验：exp_027_tcn_walker_s0 (σ=0.5), exp_027_tcn_walker_s0_sigma02 (σ=0.2)\\n\\n**RAVE (Reality-Anchored Value Estimation)**:\\n- 设计理念：用 EMA 跟踪真实环境状态的值估计，当 imagined value 超过 EMA×ceiling 时截断\\n- 机制假说：直接限制 critic overestimation 的幅度，打断 CIVO 正反馈循环\\n- 与 SGS 的区别：不修改梯度流，而是在 value estimate 层面施加约束\\n- 超参：ceiling=2.0（主实验）+ ceiling=1.5（替代超参）\\n- 实验：exp_028_rave_walker_s0 (ceil=2.0), exp_028_rave_walker_s0_ceil15 (ceil=1.5)\\n\\n**D113 全面评估完成 (2026-05-20) — Scenario B 确认：Intervention Hierarchy 论文**\\n\\nTCN 跨环境 universal mitigation（Scenario A）已关闭。TCN 仅在 Walker σ=0.2 成功（2/8 configs），且 eval 保留高度不稳定（91%/45% across seeds）。论文核心转为 **Intervention Hierarchy**：三层干预（Gradient → Output → Representation）系统性评估，证明 CIVO fundamentally hard to mitigate。\\n\\n**TCN 全景表（D113 最终）：**\\n\\n| 环境 | σ | NVE_max | CIVO 阻止? | eval 保留 |\\n|------|---|---------|-----------|----------|\\n| Walker s0 | 0.1 | 1.02@95K | ⚠️ 边界（进行中） | TBD |\\n| Walker s0 | 0.2 | 0.91@95K | ✅ | 91% |\\n| Walker s1 | 0.2 | 0.64@55K | ✅ | **45%** |\\n| Walker s2 | 0.2 | **2.11@95K** | **❌ CIVO confirmed** | **5%** (eval 45, 持续崩溃) |\\n| Walker s3 | 0.2 | TBD | 🔄 5K | — |\\n| Walker s0 | 0.5 | 3.97 | ❌ oscillatory | ~40% |\\n| Walker s1 | 0.5 | 1.64 | ❌ oscillatory | ~40% |\\n| Cheetah s0 | 0.2 | 1.90@55K | ❌ dose insufficient | crashed |\\n| Cheetah s0 | 0.5 | **10.67@55K** | ❌ transient spike+recovery | 26% |\\n| PickCube s0 | 0.2 | **3.71@52.5K** | ❌ dose insufficient | failing |\\n\\n**关键发现**：\\n1. **TCN 成功率 2/10**（NVE<1.0× 标准）或 3/10（NVE<1.5×）：Walker σ=0.2 s2 NVE=2.11@95K（持续恶化），eval=45 (~5% baseline)，成功率从 2/2 降到 2/3。即使最优 dose + 最温和环境也不可靠\\n2. **Dose-environment dependency**：σ=0.2 在 Walker 有效但 Cheetah/PickCube 不足，σ=0.5 在 Walker 过量但 Cheetah 仍不足。不存在 universal effective dose\\n3. **防 CIVO ≠ 保性能**：s1 NVE_max=0.64（比 s0 的 0.91 更低），但 eval 仅 45%（比 s0 的 91% 差 2×）。噪声注入本身干扰学习\\n4. **Cheetah \\\"impossible dose\\\" 完整确认（exp_030c FINAL @224K）**：σ=1.0 全程 NVE≤0.30（CIVO 完全抑制），但 eval 从 peak 372@35K（116% baseline，初始学习不受影响！）→ 47@215K（15% baseline）。关键发现：(a) 噪声不阻止初始学习，而是**渐进腐蚀** policy（cumulative actor gradient interference）；(b) value 校准正常（value_mean=12.4, NVE=0.26@215K）→ policy degradation ≠ value corruption；(c) Cheetah 的 CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)，不存在 Goldilocks zone。这本身也是 CIVO 与标准 overestimation 不同的证据——标准 Double Q 不会有这种 dose-dependent policy erosion tradeoff\\n5. **Cheetah σ=0.5 失败模式**：NVE=10.67@55K（transient CIVO spike），但 >95K 恢复至 <0.3。eval 永久受损（peak 296@35K → 稳态 ~77）\\n6. **⚠️ \\\"90% baseline\\\" claim 已删除**：cross-seed 均值 (821+401)/2 = 611 ≈ 68%，不是 90%。论文改为 \\\"45%-91% across seeds (mean 68%)\\\"\\n7. **Seed 效应 > dose 效应**：Walker σ=0.2 跨 seed eval=45%-91%，而 σ=0.1→0.2 的 eval 差异（55% vs 68% mean）更小\\n\\n**RAVE 2 配置 ❌ — EMA anchor 自身污染**:\\n- ceil=2.0: negative\\n- ceil=1.5: negative\\n- 机制：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → anchor 被污染 → ceiling 无效\\n\\n**Intervention Hierarchy 总结（论文核心 Table）：**\\n\\n| 干预层级 | 方法 | 成功率 | 主要失败机制 |\\n|----------|------|--------|-------------|\\n| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage 不可逆 |\\n| Gradient (L1) | Obs-decoder SGS | 1/6 | 补偿放大 + critic 校准损坏 |\\n| Gradient (L1) | Reward SGS | 0/2 | No-op (梯度 ≠ 因果) |\\n| Output (L2) | RAVE ceil=2.0 | 0/1 | EMA anchor 污染 |\\n| Output (L2) | RAVE ceil=1.5 | 0/1 | EMA anchor 污染 |\\n| Representation (L3) | TCN σ=0.2 | 2/4 (Walker only) | ❌ s2 gradual onset NVE=2.77@105K; s3 sudden onset NVE=3.04@105K; Cheetah/PickCube dose insufficient |\\n| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose (Walker) / Still insufficient (Cheetah) |\\n| **Control** | **dt_emb removal** | **5/5** | **(not an intervention — removes the feature)** |\\n\\n**叙事方向（D116 最终版，Reviewer 三问审查后）**：TCN 是 **diagnostic probe**，不是 deployable mitigation。\\n最终 claim 措辞（确认 2/4）：\\\"TCN is the only tested intervention that achieves complete CIVO suppression in any configuration (2 of 4 Walker seeds at σ=0.2), but exhibits high seed sensitivity (50% failure rate) and fails to transfer across environments—positioning it as a diagnostic probe rather than a deployable mitigation.\\\"\\n\\n**Binary protection 假说（确认 + 扩展）**：s2 渐进上升（0.58→1.01→1.65→2.77@105K），s3 表面回落后突崩（0.855→0.666→3.042@105K）。两种不同的 CIVO onset 动态，但结果相同：runaway NVE>2.5 + eval 崩溃。结论：(1) TCN operates as an all-or-nothing gate — 2/4 success, 2/4 complete failure, no intermediate; (2) CIVO onset 有至少两种模式（gradual escalation vs apparent-recovery-then-sudden-collapse）; (3) NVE 短期回落不能预测保护成功（phase transition 特性）。作为 1-2 句观察写入 + appendix 详细分析，非独立贡献。\\n\\n**Dose-response 定位**：不升级为独立贡献（n 太小，seed variance > dose variance），但作为 Section 3.6 key observations：(1) \\\"Effective dose scales with CIVO severity; tolerable dose does not\\\" — observation; (2) \\\"Impossible dose on Cheetah\\\" — 最有力单点; (3) \\\"Seed variance exceeds dose variance\\\"。\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| TCN σ=0.5 s0 | exp_027_tcn_walker_s0 | ❌ NVE peak 4.0, eval peak 366 (40% baseline), oscillatory CIVO |\\n| TCN σ=0.5 s1 | exp_027_tcn_walker_s1 | ❌ NVE peak 1.637, eval peak 365, oscillatory CIVO |\\n| TCN σ=0.2 s0 | exp_027_tcn_walker_s0_sigma02 | ✅ NVE < 1.0× throughout (peak 0.908@95K), eval peak 821 (91% baseline) |\\n| TCN σ=0.2 s1 | exp_029a_tcn_walker_s1_sigma02 | ✅ NVE < 1.0× (peak 0.643@55K), eval peak 401 (**45% baseline**) |\\n| RAVE ceiling=2.0 | exp_028_rave_walker_s0 | ❌ negative, EMA anchor polluted |\\n| RAVE ceiling=1.5 | exp_028_rave_walker_s0_ceil15 | ❌ negative, same mechanism |\\n| Cheetah TCN σ=0.2 | exp_030a_tcn_cheetah_s0_sigma02 | ❌ NVE=1.903@55K, dose insufficient |\\n| Cheetah TCN σ=0.5 | exp_030b_tcn_cheetah_s0_sigma05 | ❌ NVE=10.67@55K, transient spike, eval=77 (26% baseline) |\\n| PickCube TCN σ=0.2 | exp_031_tcn_pickcube_s0_sigma02 | ❌ NVE=3.71@52.5K, dose insufficient |\\n| Cheetah TCN σ=1.0 (FINAL) | exp_030c @224K | ✅ CIVO prevented (NVE≤0.30 全程) but ❌ eval=372 peak@35K (116% baseline!) → 47@215K (15% baseline). **\\\"Impossible dose\\\" 完整确认**: initial learning unaffected, gradual policy erosion from cumulative noise. Value calibration normal (value_mean=12.4, NVE=0.26@215K) — policy degradation ≠ value corruption |\\n| Walker TCN σ=0.1 | exp_029c (running) | 🔄 边界剂量响应 |\\n\\n**D113**: Scenario A closed → Scenario B confirmed. 论文 = Intervention Hierarchy paper with Walker TCN as existence proof.\\n\\n**Strength**: Moderate. TCN 的 2/8 成功率 + high eval variance 反而是 diagnostic paper 的强证据——证明 CIVO 在所有三个干预层级都难以可靠缓解。Intervention Hierarchy 框架（7+ methods, 3 levels, 3 environments）是系统性贡献。\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x)\\n- **D040: Multiple vulnerability pathways**: Pathway A (CIVO, value-driven) + Pathway B (non-CIVO policy instability, eval-driven)\\n- **D107: Gradient-level interventions fail entirely**: SGS 0/3 (full) + 1/6 (obs-decoder) + 0/2 (reward-only) = backward-pass is categorically insufficient. Gradient magnitude ≠ causal importance (reward 38-49% but reward-only SGS fails worst; obs-decoder 16-22% but targeted SGS also fails). Forward-pass representational damage is the irreducible floor.\\n- **Compensatory amplification**: Blocking obs-decoder on Cheetah → 2.6-3.6× NVE amplification vs untreated. Blocking reward → obs-decoder reliance increases → spatial bias reinforced.\\n- **Universal value collapse**: Obs-decoder SGS degrades all seeds' critic calibration (ve_ratio 0.056-0.14 @215K), including CIVO-free seeds. \\\"Protection\\\" = trading overestimation for underestimation.\\n- **Fourth CIVO trajectory (s3)**: Latent onset → delayed collapse → policy recovery → persistent value collapse. CIVO-induced critic damage may be irreversible.\\n- MPC vs imagination: TAWM succeeds because MPC re-plans from real states; imagination-based critic bootstrapping creates the positive feedback loop\\n- **D032: Value self-correction mechanism (009b)**: Transient vs sustained nve>1.5x determines outcome. Early stochasticity (initialization, data sampling) is the gate.\\n\\n### 6. Implications for Future Work\\n- **D113: Intervention Hierarchy — all three levels fail or partially fail**: Gradient (SGS 1/17), Output (RAVE 0/2), Representation (TCN 2/8 with high variance). dt_embedding removal 5/5 but removes the feature entirely.\\n- TCN existence proof (Walker σ=0.2) shows mitigation is *possible in principle* but fragile — narrow dose window, environment-dependent, high seed variance in eval retention\\n- **Dose-environment dependency**: No universal σ exists; Walker-effective dose (σ=0.2) underdoses Cheetah/PickCube, Walker-overdose (σ=0.5) still underdoses Cheetah\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Hierarchical temporal abstraction (THICK, Hieros) may avoid flat-conditioning failure by maintaining separate dynamics per temporal scale\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. Beyond diagnosis, we provide a **systematic Intervention Hierarchy** evaluating 7+ methods across 3 levels (gradient/output/representation) and 3 environments. This is the most comprehensive evaluation of CIVO interventions to date. The key finding: even the most promising intervention (TCN, representation-level) succeeds only under narrow conditions (Walker σ=0.2, 2/8 configs, 45-91% eval retention). The actionable takeaway is that CIVO requires fundamental architectural solutions (hierarchical temporal abstraction per THICK/Hieros), not post-hoc interventions.\\n**Mitigation**: The Intervention Hierarchy table (7 methods × 3 levels) is a standalone contribution — it saves future researchers from re-exploring these dead ends and provides a systematic framework for evaluating future interventions.\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but three elements are genuinely novel: (a) **MPC vs imagination architectural boundary** — first empirical evidence that dt-conditioning succeeds in MPC (TAWM) but fails in imagination-based AC, localizing vulnerability to critic bootstrapping architecture; (b) **gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but is causally irrelevant, obs-decoder carries 16-22% but is causally critical (broader methodological insight for multi-head MBRL debugging); (c) **systematic three-level intervention hierarchy** — not a single failure report but a complete taxonomy of 7 methods × 3 levels with structured negative evidence.\\n**Mitigation**: Expand Related Work to engage deeply with MBPO framework, explicitly articulate what CIVO reveals that MBPO does not predict (the specific *trigger* through temporal conditioning, the MPC/imagination divergence, the gradient-causality dissociation).\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n### R9: \\\"Why not test standard overestimation countermeasures (Double Q, ensemble critics)?\\\" [Dream D1 — 三档一致 #1 弱点] → **已实验回答 (D118-D123)**\\n\\n**实验结果（D118-D124 dual-critic + mechanism ablation 系列）**：\\n\\n**1. Dual-critic 跨环境结果（D128 更新）**：\\n- Walker wide dual-critic: **3/3 CIVO prevented**（s0 eval 739.7, s1 551.8, s2 ~121）。NVE 全程 < 1.5\\n  - ⚠️ **s2 非 CIVO 崩溃**：NVE 正常但 eval 354→121，actor entropy 急升(-3.59→-0.45)。可能是 policy exploration failure。**必须区分 \\\"CIVO prevention\\\"(3/3) vs \\\"performance stability\\\"(2/3)**\\n- Walker narrow dual-critic: 1/1 CIVO occurred (NVE 2.75) → full recovery eval 697.8\\n- Cheetah dual-critic: CIVO 发生(NVE 1.75) → 部分恢复 eval 97.5 (31%, 晚期下降)\\n- Cheetah wide single: CIVO 发生(NVE 3.59) → 自修复 eval 146 (晚期下降)。Wide > dual in Cheetah (146 vs 97.5)\\n- PickCube dual-critic: NVE 短暂升至 2.3 后自行修正，**PickCube 不触发持续性 CIVO**（任务动态不同）。eval 27.7 的低性能源于 gate 配置本身对 manipulation 任务有害（vanilla baseline 58.6 → 加 subsample+dt_emb 后 26.6），非 CIVO 导致。PickCube 作为 scope limitation 讨论，跨环境 CIVO 叙事聚焦 locomotion (Walker/Cheetah)\\n- **v1≈v2 across all environments and all configs**（ρ>0.999 Walker; exact match Cheetah/PickCube）\\n\\n**2. v1≈v2 核心发现**：Double Q 的 pessimism 机制在 pure-imagination MBRL 中失效。两个 critic 共享相同 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值的 3-4%（ρ>0.998）。\\n\\n**3. 2×2 Mechanism Factorial（D126 — 全部 4 格填满）**：\\n| | Single critic | Dual critic (min) |\\n|--|--------------|-------------------|\\n| ~1.05-1.2M params | baseline (**CIVO → 永久崩溃**) | **exp_035 narrow: CIVO(NVE 2.75) → 恢复中 → eval 149+** |\\n| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → 自修复 → eval 408** | **exp_032: CIVO 预防(NVE≤1.1) → eval 670-788** |\\n\\n**4. 双维度发现（D127 最终修正 — 论文最核心新发现）**：\\n\\n**Recovery 维度（min 是主导因素）**：\\n| 配置 | CIVO 发生? | NVE peak | eval final | 恢复能力 |\\n|------|-----------|----------|------------|---------|\\n| Baseline (single+normal) | ✓ | ~2-4 | collapsed | 无 |\\n| exp_033 (single+wide) | ✓ | 4.75 | 408 | 部分(capacity) |\\n| **exp_035 (dual+narrow)** | **✓** | **2.75** | **697.8** | **完全(min)** |\\n| exp_032 (dual+wide) | ✗ | ≤1.1 | 670-788 | 无需恢复 |\\n\\n- **Min 的核心价值是 recovery 而非 prevention**：exp_035 eval 697.8 ≈ exp_032 670-788，尽管经历了 CIVO\\n- **Min >> Capacity for recovery**：697.8 vs 408。min 实现完全恢复，capacity 仅部分恢复\\n- **Min 同时降低 CIVO 严重度**：exp_035 NVE 2.75 < exp_033 NVE 4.75\\n\\n**Prevention 维度（需 min+capacity 协同）**：\\n- 只有 exp_032 (min+capacity) 从未触发 CIVO（NVE≤1.1）\\n- Prevention 优势不是最终性能（≈recovery-with-min），而是**训练效率**（节省 ~40K steps 恢复期）\\n- v1≈v2 在所有 dual-critic 中成立（包括 exp_032）→ 协同效应是经验事实，机制为 hypothesis\\n\\n**跨环境 caveat**：Walker 上 recovery 充分(697.8)，但 Cheetah 上 recovery 不充分(97.5, 31%)。环境越难，recovery 越不可靠 → prevention 在难环境中价值更大。\\n\\n**⚠️ 机制为 open hypothesis**：v1≈v2 在所有 dual-critic 中成立。可能的解释：(a) min 在训练早期(v1≠v2 时)建立了稳定学习轨迹 (b) min-target coupling 在 wider network 的 smoother loss landscape 上更有效 (c) capacity 提升 value calibration 质量而非多样性。论文中诚实报告经验事实，机制标注为 hypothesis。\\n\\n**论文 narrative（D127 最终版）**：双维度报告——(a) Prevention: min+capacity 协同预防 CIVO（训练效率优势）(b) Recovery: min 是 CIVO 后恢复的主导因素（被低估的特性）(c) 跨环境：难环境中 recovery 不充分，凸显 prevention 的必要性 (d) v1≈v2: pessimism 机制失效但 min 通过其他通路起效（open question）\\n\\n**5. 环境依赖性（D125 — exp_034 完成）**：\\n- **Walker（中等 CIVO，untreated NVE 2-4）**：min 操作完全预防 CIVO（2/2 seeds）\\n- **Cheetah（高强度 CIVO，untreated NVE 8.27-70.64，seed 间高方差）**：min 操作将 NVE peak 从 baseline 8.27-70.64 降至 1.75（≥4× reduction），但仍超 1.5 阈值，不能完全预防。双倍参数(2.36M)实现部分恢复(eval 97.5)但仅达 pre-CIVO 峰值的 31% 且晚期下降。对比 Walker wide-critic(exp_033) 恢复到 408(>pre-CIVO)，说明**环境动力学复杂度是恢复质量的决定性因素**。（来源：exp_010b s0 NVE_final=70.64, s1 NVE_peak=8.27。论文中须报告两个 seed 并使用保守 claim \\\"≥4× NVE reduction\\\"，不用 40×）\\n- **论文 claim 限定**：\\\"min=prevention\\\" 必须加 \\\"in moderate-CIVO environments\\\" 限定，否则审稿人拿 Cheetah 数据直接攻击。这反而强化 intervention hierarchy 叙事——即使 architecture-level 干预也有 CIVO 严重度边界\\n\\n**论文 narrative（D126 修正）**：从\\\"为什么不测标准对策\\\"转为\\\"我们测了——(a) pessimism 机制失效（v1≈v2 across all configs），(b) min alone 和 capacity alone 都不能预防 CIVO，(c) 两者协同（min+capacity）才能预防，(d) 机制：capacity 提供函数多样性 + min 约束 overestimation 反馈环，(e) prevention >> recovery\\\"。2×2 factorial 的**交互效应**比任何单因素更有方法论启示——对 ML 社区的 critic 设计指导价值更高。\\n\\n### R10: \\\"NVE threshold is calibrated and validated in-sample\\\" [Dream D8 — 三档一致]\\n**Pre-emption**: 承认 1.5× threshold 在同一 29 个数据点上 calibrate 和 validate。但 (a) Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×，不是事后拟合；(b) 4 环境 × 多种 configs 提供 reasonable diversity；(c) ground truth labeling 基于 mechanism identification（CIVO vs non-CIVO dynamics），不是简单的 performance threshold。\\n**Mitigation**: 明确承认 limitation，建议 held-out validation（不同架构或环境）作为 future work。讨论 NVE 在不同 reward scale 下的 generalization boundary。\\n\\n### R11: \\\"Pixel observations would change the gradient decomposition\\\" [Dream D9 — 三档一致]\\n**Pre-emption**: 正确——pixel 下 obs-decoder channel（本文识别为 16-22% 梯度但因果关键）会承载更多信息和更大梯度。CIVO 动态可能更强（更多空间信息可利用）或更弱（decoder 正则化效应更强）。这是一个重要的泛化性边界。\\n**Mitigation**: 在 limitations 中明确讨论，定位为 future work。强调本文在 proprioceptive setting 的发现建立了 CIVO 的基础机制理论，pixel 扩展需要后续工作。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations + 2 environments | None |\\n| C2 (CIVO trigger) | ✅ Strong — nve≥1.5× threshold 15/16, AUROC=0.969 (2 envs) | None |\\n| C3 (untrained emb protection) | ✅ Strong — 008a + cross-env replication | None |\\n| C4 (dt amplification) | ✅ Moderate — dt=1 > dt=2 > dt=4 monotonic | Only 2 dt values |\\n| C5 (horizon/subsample secondary) | ✅ Moderate | None blocking |\\n| C6 (dt=1 imag partial) | ✅ 4 seeds — 2/4 collapse via distinct pathways (CIVO + IRD) | None |\\n| C7 (SGS failure / gradient decoupling) | ✅ Strong — 17 seeds, 3 variants, 2 envs. 1/17 CIVO-free (with value collapse side effect). Embedding removal 5/5. | None |\\n| C8 (Intervention Hierarchy) | ✅ D113 确认 — TCN 2/8, RAVE 0/2, SGS 1/17. Hierarchy 本身是贡献 | Cheetah σ=1.0 + PickCube σ=0.5 pending (extra data points) |\\n\\n### Priority Actions Before Submission (updated 2026-05-20 D116 — Dream修复)\\n1. ~~C1-C7 实验~~ — ✅ 全部完成\\n2. ~~TCN/RAVE 评估~~ — ✅ D113 Scenario B 确认\\n3. ~~论文 TCN 文本修正~~ — ✅ cross-seed 报告 + narrative reframe\\n4. **🔄 [P0] 标准过估值对策讨论** — Paper Agent 执行中 (Dream R9)\\n5. **🔄 [P0] 参考文献扩展至 40+** — Paper Agent 执行中 (Dream D7)\\n6. **🔄 [P1] 新颖性锐化 + NVE 讨论 + pixel obs + CoRL 相关性** — Paper Agent 队列 (Dream D3/D8/D9/D2)\\n7. **🔄 [P1] Cheetah σ=1.0 + PickCube σ=0.5** — 运行中，Hierarchy 额外数据\\n8. **Re-dream 验证** — Paper Agent 结构性修复完成后\\n9. **论文收尾** — Reviewer 审查 + provenance + 三件套 + 5/25 数据锁定\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\n\", \"total_chars\": 46244, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "ab7f909b-3a95-4e76-ae41-2a549dca501d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\\\n\\\\n## Title Candidates\\\\n\\\\n1. **\\\\\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\\\\\"**\\\\n2. ~~**\\\\\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\\\\\"**~~ (deprecated — \\\\\\\"delusional critic\\\\\\\" conflicts with Lu et al. 2018)\\\\n3. **\\\\\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\\\\\"** ← preferred after D037 terminology decision\\\\n4. **\\\\\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\\\\\"**\\\\n\\\\n**⚠️ D037 术语决定**: \\\\\\\"delusional critic\\\\\\\" → **\\\\\\\"conditioning-induced value overestimation\\\\\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\\\\\"delusional critic\\\\\\\" → \\\\\\\"conditioning-induced value overestimation\\\\\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\\\n\\\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\\\\\"known failure class 的 specific instance\\\\\\\" 升级为 \\\\\\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\\\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\\\n\\\\n## Venue\\\\n\\\\n**CoRL 2026** — Deadline: 2026-05-29\\\\n\\\\n## Narrative Positioning\\\\n\\\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\\\n\\\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\\\n\\\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\\\n\\\\n---\\\\n\\\\n## Core Claims\\\\n\\\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\\\n\\\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\\\n\\\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\\\n\\\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\\\n\\\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\\\n\\\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\\\n\\\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\\\n\\\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\\\n\\\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\\\\\"point of no return\\\\\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\\\n\\\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\\\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**⚠️ 修正：reward head 贡献最大梯度（49%@55K），obs decoder 仅 16.3%。但 reward-only SGS 仍失败——梯度大小与因果重要性解耦。** |\\\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\\\n\\\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\\\\\"eliminates\\\\\\\" 改为 \\\\\\\"significantly delays and reduces\\\\\\\"。推荐方案仍是 008e_v3（C6）**。\\\\n\\\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\\\n\\\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\\\n|-------|------------|------------|---------|---------------|---------------|------------|\\\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\\\n\\\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\\\n\\\\n**dt_emb Gradient Decomposition (D061) — ⚠️ 已修正**\\\\n\\\\n梯度验证（torch.autograd.grad analysis, correct config gate_fixed_dt=2）揭示 dt_emb.weight 的梯度来源分布：\\\\n\\\\n| Source | 55K (%) | 112K (%) |\\\\n|--------|---------|----------|\\\\n| Reward head | 49.0 | 38.1 |\\\\n| KL dynamics | 34.7 | 40.4 |\\\\n| Observation decoders | 16.3 | 21.5 |\\\\n| Cont head | ~0 | ~0 |\\\\n\\\\n⚠️ **之前的 93% obs / 0% reward 数据不可复现**（见 gradient_decomposition_008d_corrected.json）。正确结论：reward head 贡献最大梯度（38-49%），但 reward-only SGS (016e) 仍然失败（NVE=10.42×）；obs decoder 通路（16-22%）虽贡献最小，但携带关键的 Δt-specific 空间信息驱动 RSSM fidelity gap。**梯度大小与因果重要性解耦**是核心发现。\\\\n\\\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\\\n\\\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\\\n\\\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\\\n\\\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\\\n\\\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\\\n\\\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\\\n\\\\n### C4: Longer dt amplifies the problem\\\\n\\\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\\\n\\\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\\\n\\\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\\\n\\\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\\\n\\\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\\\n\\\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\\\n\\\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\\\n\\\\n原假设\\\\\\\"dt=1 imagination = practical mitigation\\\\\\\"被**否证**。跨 seed 数据：\\\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\\\n- **独立 seed 崩溃率: 1/2 (50%)**\\\\n\\\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\\\n\\\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\\\n\\\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\\\n\\\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\\\n|------|---------------------|---------------------|\\\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\\\n\\\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\\\n\\\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\\\\\"seed 2 本身不稳定\\\\\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\\\n\\\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\\\n|------|-------------------|------------|------|\\\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\\\n\\\\n**C6 最终状态: PARTIALLY FALSIFIED**\\\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\\\n- 崩溃是配置导致的，不是 seed 特异性\\\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\\\n\\\\n**论文表述建议**: \\\\\\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\\\\\"\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\\\n\\\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\\\n\\\\n### C7: Gradient-level interventions fail to eliminate CIVO — gradient magnitude decoupled from causal importance\\\\n\\\\n**⚠️ D107: SGS 全面失败，梯度干预不是正确的干预层级**\\\\n\\\\nAll three SGS variants fail to eliminate CIVO:\\\\n- **Reward-only SGS** (016e): 0/2, NVE=10.42× — paradoxically worse than untreated\\\\n- **Full-pathway SGS** (018+021): 0/3 across two environments — blocks all non-KL gradients, still fails\\\\n- **Obs-decoder-only SGS** (025+026): 1/6 across two environments — the identified causal channel, still fails\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Reward-only SGS 反效果 | exp_016e | NVE=10.42×, collapse to eval 31.7. 阻断 reward 梯度迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差 |\\\\n| Full SGS 0/3 | exp_018 (Walker 2 seeds) + exp_021 (Cheetah 1 seed) | s1: eval 448.3, NVE 1.66× (CIVO+); s2: collapse 40.8; Cheetah: transient NVE 9.94×→0.34× (not SGS effect) |\\\\n| Obs-decoder SGS 1/6 | exp_025 (Walker 4 seeds) + exp_026 (Cheetah 2 seeds) | Walker: 1/4 (s1 survived, s2-s4 collapsed); Cheetah: 0/2, NVE 21.9×-30.2× (2.6-3.6× worse than untreated 8.3×) |\\\\n| Compensatory amplification (Cheetah) | exp_026 vs exp_010b | Obs-decoder SGS NVE 21.9-30.2× vs untreated 8.3× — blocking obs-decoder shifts co-adaptation to reward head |\\\\n| Universal value collapse | exp_025 all seeds @215K | All 4 seeds terminal ve_ratio=0.056-0.14, including s1 \\\\\\\"success\\\\\\\" (eval 726, value 41) — critic underestimation as side effect |\\\\n| Fourth trajectory (s3) | exp_025_s3 | Healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery (590@215K) → persistent value collapse (ve_ratio 0.14) |\\\\n\\\\n**核心发现**：\\\\n1. **梯度量级与因果重要性脱耦**: Reward head 38-49% 梯度占比（最大），但 reward-only SGS 失败最惨；obs decoder 16-22%（最小非零），但 obs-decoder SGS 也失败。梯度分解成功作为**诊断工具**但失败作为**干预指南**。\\\\n2. **Backward-pass 是错误的干预层级**: Full SGS 阻断所有非 KL 梯度仍 0/3 → forward-pass representational damage 是不可约减的脆弱性底线。Temporal embedding 通过 forward pass 塑造潜在表示，无论哪些梯度更新它。\\\\n3. **补偿放大**: 阻断任一通道导致剩余通道放大 co-adaptation（Cheetah: 2.6-3.6× 放大）。\\\\n4. **SGS 副作用**: 即使\\\\\\\"成功\\\\\\\"的 seed 也遭受 critic 校准损坏（universal value collapse）。\\\\n\\\\n**Strength**: Strong. 17 seeds across 3 SGS variants and 2 environments. Only 1/17 avoids CIVO, and that seed still suffers value collapse. Embedding removal (008f+024b): 5/5 = 100% prevention. The contrast establishes gradient stopping as categorically insufficient.\\\\n\\\\n### C8: Forward-pass interventions — TCN and RAVE (🔄 验证中)\\\\n\\\\n**⚠️ D107/D108: 两种 forward-pass 干预方法并行验证**\\\\n\\\\nSGS 失败的根因是 backward-pass 干预无法消除 forward-pass representational damage。C8 提出绕过梯度冗余的 forward-pass 干预：\\\\n\\\\n**TCN (Temporal Conditioning Noise)**:\\\\n- 设计理念：imagination 时对 dt_embedding 输出加高斯噪声 $\\\\\\\\mathcal{N}(0, \\\\\\\\sigma^2)$，降低 conditioning 精度\\\\n- 机制假说：噪声阻止 RSSM 和 critic 对精确 dt 信号的过度 co-adaptation，同时保留粗粒度时间信息\\\\n- 与 SGS 的区别：在 forward pass 层面操作，不依赖梯度阻断\\\\n- 超参：σ=0.5×std（主实验）+ σ=0.2×std（替代超参）\\\\n- 实验：exp_027_tcn_walker_s0 (σ=0.5), exp_027_tcn_walker_s0_sigma02 (σ=0.2)\\\\n\\\\n**RAVE (Reality-Anchored Value Estimation)**:\\\\n- 设计理念：用 EMA 跟踪真实环境状态的值估计，当 imagined value 超过 EMA×ceiling 时截断\\\\n- 机制假说：直接限制 critic overestimation 的幅度，打断 CIVO 正反馈循环\\\\n- 与 SGS 的区别：不修改梯度流，而是在 value estimate 层面施加约束\\\\n- 超参：ceiling=2.0（主实验）+ ceiling=1.5（替代超参）\\\\n- 实验：exp_028_rave_walker_s0 (ceil=2.0), exp_028_rave_walker_s0_ceil15 (ceil=1.5)\\\\n\\\\n**D113 全面评估完成 (2026-05-20) — Scenario B 确认：Intervention Hierarchy 论文**\\\\n\\\\nTCN 跨环境 universal mitigation（Scenario A）已关闭。TCN 仅在 Walker σ=0.2 成功（2/8 configs），且 eval 保留高度不稳定（91%/45% across seeds）。论文核心转为 **Intervention Hierarchy**：三层干预（Gradient → Output → Representation）系统性评估，证明 CIVO fundamentally hard to mitigate。\\\\n\\\\n**TCN 全景表（D113 最终）：**\\\\n\\\\n| 环境 | σ | NVE_max | CIVO 阻止? | eval 保留 |\\\\n|------|---|---------|-----------|----------|\\\\n| Walker s0 | 0.1 | 1.02@95K | ⚠️ 边界（进行中） | TBD |\\\\n| Walker s0 | 0.2 | 0.91@95K | ✅ | 91% |\\\\n| Walker s1 | 0.2 | 0.64@55K | ✅ | **45%** |\\\\n| Walker s2 | 0.2 | **2.11@95K** | **❌ CIVO confirmed** | **5%** (eval 45, 持续崩溃) |\\\\n| Walker s3 | 0.2 | TBD | 🔄 5K | — |\\\\n| Walker s0 | 0.5 | 3.97 | ❌ oscillatory | ~40% |\\\\n| Walker s1 | 0.5 | 1.64 | ❌ oscillatory | ~40% |\\\\n| Cheetah s0 | 0.2 | 1.90@55K | ❌ dose insufficient | crashed |\\\\n| Cheetah s0 | 0.5 | **10.67@55K** | ❌ transient spike+recovery | 26% |\\\\n| PickCube s0 | 0.2 | **3.71@52.5K** | ❌ dose insufficient | failing |\\\\n\\\\n**关键发现**：\\\\n1. **TCN 成功率 2/10**（NVE<1.0× 标准）或 3/10（NVE<1.5×）：Walker σ=0.2 s2 NVE=2.11@95K（持续恶化），eval=45 (~5% baseline)，成功率从 2/2 降到 2/3。即使最优 dose + 最温和环境也不可靠\\\\n2. **Dose-environment dependency**：σ=0.2 在 Walker 有效但 Cheetah/PickCube 不足，σ=0.5 在 Walker 过量但 Cheetah 仍不足。不存在 universal effective dose\\\\n3. **防 CIVO ≠ 保性能**：s1 NVE_max=0.64（比 s0 的 0.91 更低），但 eval 仅 45%（比 s0 的 91% 差 2×）。噪声注入本身干扰学习\\\\n4. **Cheetah \\\\\\\"impossible dose\\\\\\\" 完整确认（exp_030c FINAL @224K）**：σ=1.0 全程 NVE≤0.30（CIVO 完全抑制），但 eval 从 peak 372@35K（116% baseline，初始学习不受影响！）→ 47@215K（15% baseline）。关键发现：(a) 噪声不阻止初始学习，而是**渐进腐蚀** policy（cumulative actor gradient interference）；(b) value 校准正常（value_mean=12.4, NVE=0.26@215K）→ policy degradation ≠ value corruption；(c) Cheetah 的 CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)，不存在 Goldilocks zone。这本身也是 CIVO 与标准 overestimation 不同的证据——标准 Double Q 不会有这种 dose-dependent policy erosion tradeoff\\\\n5. **Cheetah σ=0.5 失败模式**：NVE=10.67@55K（transient CIVO spike），但 >95K 恢复至 <0.3。eval 永久受损（peak 296@35K → 稳态 ~77）\\\\n6. **⚠️ \\\\\\\"90% baseline\\\\\\\" claim 已删除**：cross-seed 均值 (821+401)/2 = 611 ≈ 68%，不是 90%。论文改为 \\\\\\\"45%-91% across seeds (mean 68%)\\\\\\\"\\\\n7. **Seed 效应 > dose 效应**：Walker σ=0.2 跨 seed eval=45%-91%，而 σ=0.1→0.2 的 eval 差异（55% vs 68% mean）更小\\\\n\\\\n**RAVE 2 配置 ❌ — EMA anchor 自身污染**:\\\\n- ceil=2.0: negative\\\\n- ceil=1.5: negative\\\\n- 机制：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → anchor 被污染 → ceiling 无效\\\\n\\\\n**Intervention Hierarchy 总结（论文核心 Table）：**\\\\n\\\\n| 干预层级 | 方法 | 成功率 | 主要失败机制 |\\\\n|----------|------|--------|-------------|\\\\n| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage 不可逆 |\\\\n| Gradient (L1) | Obs-decoder SGS | 1/6 | 补偿放大 + critic 校准损坏 |\\\\n| Gradient (L1) | Reward SGS | 0/2 | No-op (梯度 ≠ 因果) |\\\\n| Output (L2) | RAVE ceil=2.0 | 0/1 | EMA anchor 污染 |\\\\n| Output (L2) | RAVE ceil=1.5 | 0/1 | EMA anchor 污染 |\\\\n| Representation (L3) | TCN σ=0.2 | 2/4 (Walker only) | ❌ s2 gradual onset NVE=2.77@105K; s3 sudden onset NVE=3.04@105K; Cheetah/PickCube dose insufficient |\\\\n| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose (Walker) / Still insufficient (Cheetah) |\\\\n| **Control** | **dt_emb removal** | **5/5** | **(not an intervention — removes the feature)** |\\\\n\\\\n**叙事方向（D116 最终版，Reviewer 三问审查后）**：TCN 是 **diagnostic probe**，不是 deployable mitigation。\\\\n最终 claim 措辞（确认 2/4）：\\\\\\\"TCN is the only tested intervention that achieves complete CIVO suppression in any configuration (2 of 4 Walker seeds at σ=0.2), but exhibits high seed sensitivity (50% failure rate) and fails to transfer across environments—positioning it as a diagnostic probe rather than a deployable mitigation.\\\\\\\"\\\\n\\\\n**Binary protection 假说（确认 + 扩展）**：s2 渐进上升（0.58→1.01→1.65→2.77@105K），s3 表面回落后突崩（0.855→0.666→3.042@105K）。两种不同的 CIVO onset 动态，但结果相同：runaway NVE>2.5 + eval 崩溃。结论：(1) TCN operates as an all-or-nothing gate — 2/4 success, 2/4 complete failure, no intermediate; (2) CIVO onset 有至少两种模式（gradual escalation vs apparent-recovery-then-sudden-collapse）; (3) NVE 短期回落不能预测保护成功（phase transition 特性）。作为 1-2 句观察写入 + appendix 详细分析，非独立贡献。\\\\n\\\\n**Dose-response 定位**：不升级为独立贡献（n 太小，seed variance > dose variance），但作为 Section 3.6 key observations：(1) \\\\\\\"Effective dose scales with CIVO severity; tolerable dose does not\\\\\\\" — observation; (2) \\\\\\\"Impossible dose on Cheetah\\\\\\\" — 最有力单点; (3) \\\\\\\"Seed variance exceeds dose variance\\\\\\\"。\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| TCN σ=0.5 s0 | exp_027_tcn_walker_s0 | ❌ NVE peak 4.0, eval peak 366 (40% baseline), oscillatory CIVO |\\\\n| TCN σ=0.5 s1 | exp_027_tcn_walker_s1 | ❌ NVE peak 1.637, eval peak 365, oscillatory CIVO |\\\\n| TCN σ=0.2 s0 | exp_027_tcn_walker_s0_sigma02 | ✅ NVE < 1.0× throughout (peak 0.908@95K), eval peak 821 (91% baseline) |\\\\n| TCN σ=0.2 s1 | exp_029a_tcn_walker_s1_sigma02 | ✅ NVE < 1.0× (peak 0.643@55K), eval peak 401 (**45% baseline**) |\\\\n| RAVE ceiling=2.0 | exp_028_rave_walker_s0 | ❌ negative, EMA anchor polluted |\\\\n| RAVE ceiling=1.5 | exp_028_rave_walker_s0_ceil15 | ❌ negative, same mechanism |\\\\n| Cheetah TCN σ=0.2 | exp_030a_tcn_cheetah_s0_sigma02 | ❌ NVE=1.903@55K, dose insufficient |\\\\n| Cheetah TCN σ=0.5 | exp_030b_tcn_cheetah_s0_sigma05 | ❌ NVE=10.67@55K, transient spike, eval=77 (26% baseline) |\\\\n| PickCube TCN σ=0.2 | exp_031_tcn_pickcube_s0_sigma02 | ❌ NVE=3.71@52.5K, dose insufficient |\\\\n| Cheetah TCN σ=1.0 (FINAL) | exp_030c @224K | ✅ CIVO prevented (NVE≤0.30 全程) but ❌ eval=372 peak@35K (116% baseline!) → 47@215K (15% baseline). **\\\\\\\"Impossible dose\\\\\\\" 完整确认**: initial learning unaffected, gradual policy erosion from cumulative noise. Value calibration normal (value_mean=12.4, NVE=0.26@215K) — policy degradation ≠ value corruption |\\\\n| Walker TCN σ=0.1 | exp_029c (running) | 🔄 边界剂量响应 |\\\\n\\\\n**D113**: Scenario A closed → Scenario B confirmed. 论文 = Intervention Hierarchy paper with Walker TCN as existence proof.\\\\n\\\\n**Strength**: Moderate. TCN 的 2/8 成功率 + high eval variance 反而是 diagnostic paper 的强证据——证明 CIVO 在所有三个干预层级都难以可靠缓解。Intervention Hierarchy 框架（7+ methods, 3 levels, 3 environments）是系统性贡献。\\\\n\\\\n---\\\\n\\\\n## Story Arc\\\\n\\\\n### 1. Introduction\\\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\\\n\\\\n### 2. Background & Related Work\\\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\\\n- World-model RL (Dreamer family, IRIS, TWM)\\\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\\\n\\\\n### 3. Methodology\\\\n- DreamerV3 as base architecture\\\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\\\n\\\\n### 4. Results\\\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\\\\\"smoking gun\\\\\\\" comparison (008c vs 008d)\\\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\\\n- **Finding 4**: Longer dt amplifies (C4)\\\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\\\n\\\\n### 5. Discussion\\\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x)\\\\n- **D040: Multiple vulnerability pathways**: Pathway A (CIVO, value-driven) + Pathway B (non-CIVO policy instability, eval-driven)\\\\n- **D107: Gradient-level interventions fail entirely**: SGS 0/3 (full) + 1/6 (obs-decoder) + 0/2 (reward-only) = backward-pass is categorically insufficient. Gradient magnitude ≠ causal importance (reward 38-49% but reward-only SGS fails worst; obs-decoder 16-22% but targeted SGS also fails). Forward-pass representational damage is the irreducible floor.\\\\n- **Compensatory amplification**: Blocking obs-decoder on Cheetah → 2.6-3.6× NVE amplification vs untreated. Blocking reward → obs-decoder reliance increases → spatial bias reinforced.\\\\n- **Universal value collapse**: Obs-decoder SGS degrades all seeds' critic calibration (ve_ratio 0.056-0.14 @215K), including CIVO-free seeds. \\\\\\\"Protection\\\\\\\" = trading overestimation for underestimation.\\\\n- **Fourth CIVO trajectory (s3)**: Latent onset → delayed collapse → policy recovery → persistent value collapse. CIVO-induced critic damage may be irreversible.\\\\n- MPC vs imagination: TAWM succeeds because MPC re-plans from real states; imagination-based critic bootstrapping creates the positive feedback loop\\\\n- **D032: Value self-correction mechanism (009b)**: Transient vs sustained nve>1.5x determines outcome. Early stochasticity (initialization, data sampling) is the gate.\\\\n\\\\n### 6. Implications for Future Work\\\\n- **D113: Intervention Hierarchy — all three levels fail or partially fail**: Gradient (SGS 1/17), Output (RAVE 0/2), Representation (TCN 2/8 with high variance). dt_embedding removal 5/5 but removes the feature entirely.\\\\n- TCN existence proof (Walker σ=0.2) shows mitigation is *possible in principle* but fragile — narrow dose window, environment-dependent, high seed variance in eval retention\\\\n- **Dose-environment dependency**: No universal σ exists; Walker-effective dose (σ=0.2) underdoses Cheetah/PickCube, Walker-overdose (σ=0.5) still underdoses Cheetah\\\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\\\n- Hierarchical temporal abstraction (THICK, Hieros) may avoid flat-conditioning failure by maintaining separate dynamics per temporal scale\\\\n- Need for diagnostic methodology in temporal abstraction research\\\\n\\\\n---\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1: \\\\\\\"Limited to one environment / one base algorithm\\\\\\\"\\\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\\\n\\\\n### R2: \\\\\\\"No proposed solution — what's the actionable takeaway?\\\\\\\"\\\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. Beyond diagnosis, we provide a **systematic Intervention Hierarchy** evaluating 7+ methods across 3 levels (gradient/output/representation) and 3 environments. This is the most comprehensive evaluation of CIVO interventions to date. The key finding: even the most promising intervention (TCN, representation-level) succeeds only under narrow conditions (Walker σ=0.2, 2/8 configs, 45-91% eval retention). The actionable takeaway is that CIVO requires fundamental architectural solutions (hierarchical temporal abstraction per THICK/Hieros), not post-hoc interventions.\\\\n**Mitigation**: The Intervention Hierarchy table (7 methods × 3 levels) is a standalone contribution — it saves future researchers from re-exploring these dead ends and provides a systematic framework for evaluating future interventions.\\\\n\\\\n### R3: \\\\\\\"Value/eval ratio is a crude proxy for overestimation\\\\\\\"\\\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\\\n\\\\n### R4: \\\\\\\"The factorial design is incomplete — missing cells in the grid\\\\\\\"\\\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\\\n\\\\n### R5: \\\\\\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\\\\\"\\\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but three elements are genuinely novel: (a) **MPC vs imagination architectural boundary** — first empirical evidence that dt-conditioning succeeds in MPC (TAWM) but fails in imagination-based AC, localizing vulnerability to critic bootstrapping architecture; (b) **gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but is causally irrelevant, obs-decoder carries 16-22% but is causally critical (broader methodological insight for multi-head MBRL debugging); (c) **systematic three-level intervention hierarchy** — not a single failure report but a complete taxonomy of 7 methods × 3 levels with structured negative evidence.\\\\n**Mitigation**: Expand Related Work to engage deeply with MBPO framework, explicitly articulate what CIVO reveals that MBPO does not predict (the specific *trigger* through temporal conditioning, the MPC/imagination divergence, the gradient-causality dissociation).\\\\n\\\\n### R6: \\\\\\\"All results from a single seed — how robust are the conclusions?\\\\\\\"\\\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\\\n\\\\n### R7: \\\\\\\"The factorial design confounds dt_embedding training with training data composition\\\\\\\"\\\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\\\n\\\\n### R8: \\\\\\\"008f reward prediction degradation undermines the causal control\\\\\\\"\\\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\\\\\"去掉 dt_embedding → 不崩塌\\\\\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\\\n\\\\n### R9: \\\\\\\"Why not test standard overestimation countermeasures (Double Q, ensemble critics)?\\\\\\\" [Dream D1 — 三档一致 #1 弱点] → **已实验回答 (D118-D123)**\\\\n\\\\n**实验结果（D118-D124 dual-critic + mechanism ablation 系列）**：\\\\n\\\\n**1. Dual-critic 跨环境结果（D128 更新）**：\\\\n- Walker wide dual-critic: **3/3 CIVO prevented**（s0 eval 739.7, s1 551.8, s2 ~121）。NVE 全程 < 1.5\\\\n  - ⚠️ **s2 非 CIVO 崩溃**：NVE 正常但 eval 354→121，actor entropy 急升(-3.59→-0.45)。可能是 policy exploration failure。**必须区分 \\\\\\\"CIVO prevention\\\\\\\"(3/3) vs \\\\\\\"performance stability\\\\\\\"(2/3)**\\\\n- Walker narrow dual-critic: 1/1 CIVO occurred (NVE 2.75) → full recovery eval 697.8\\\\n- Cheetah dual-critic: CIVO 发生(NVE 1.75) → 部分恢复 eval 97.5 (31%, 晚期下降)\\\\n- Cheetah wide single: CIVO 发生(NVE 3.59) → 自修复 eval 146 (晚期下降)。Wide > dual in Cheetah (146 vs 97.5)\\\\n- PickCube dual-critic: NVE 短暂升至 2.3 后自行修正，**PickCube 不触发持续性 CIVO**（任务动态不同）。eval 27.7 的低性能源于 gate 配置本身对 manipulation 任务有害（vanilla baseline 58.6 → 加 subsample+dt_emb 后 26.6），非 CIVO 导致。PickCube 作为 scope limitation 讨论，跨环境 CIVO 叙事聚焦 locomotion (Walker/Cheetah)\\\\n- **v1≈v2 across all environments and all configs**（ρ>0.999 Walker; exact match Cheetah/PickCube）\\\\n\\\\n**2. v1≈v2 核心发现**：Double Q 的 pessimism 机制在 pure-imagination MBRL 中失效。两个 critic 共享相同 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值的 3-4%（ρ>0.998）。\\\\n\\\\n**3. 2×2 Mechanism Factorial（D126 — 全部 4 格填满）**：\\\\n| | Single critic | Dual critic (min) |\\\\n|--|--------------|-------------------|\\\\n| ~1.05-1.2M params | baseline (**CIVO → 永久崩溃**) | **exp_035 narrow: CIVO(NVE 2.75) → 恢复中 → eval 149+** |\\\\n| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → 自修复 → eval 408** | **exp_032: CIVO 预防(NVE≤1.1) → eval 670-788** |\\\\n\\\\n**4. 双维度发现（D127 最终修正 — 论文最核心新发现）**：\\\\n\\\\n**Recovery 维度（min 是主导因素）**：\\\\n| 配置 | CIVO 发生? | NVE peak | eval final | 恢复能力 |\\\\n|------|-----------|----------|------------|---------|\\\\n| Baseline (single+normal) | ✓ | ~2-4 | collapsed | 无 |\\\\n| exp_033 (single+wide) | ✓ | 4.75 | 408 | 部分(capacity) |\\\\n| **exp_035 (dual+narrow)** | **✓** | **2.75** | **697.8** | **完全(min)** |\\\\n| exp_032 (dual+wide) | ✗ | ≤1.1 | 670-788 | 无需恢复 |\\\\n\\\\n- **Min 的核心价值是 recovery 而非 prevention**：exp_035 eval 697.8 ≈ exp_032 670-788，尽管经历了 CIVO\\\\n- **Min >> Capacity for recovery**：697.8 vs 408。min 实现完全恢复，capacity 仅部分恢复\\\\n- **Min 同时降低 CIVO 严重度**：exp_035 NVE 2.75 < exp_033 NVE 4.75\\\\n\\\\n**Prevention 维度（需 min+capacity 协同）**：\\\\n- 只有 exp_032 (min+capacity) 从未触发 CIVO（NVE≤1.1）\\\\n- Prevention 优势不是最终性能（≈recovery-with-min），而是**训练效率**（节省 ~40K steps 恢复期）\\\\n- v1≈v2 在所有 dual-critic 中成立（包括 exp_032）→ 协同效应是经验事实，机制为 hypothesis\\\\n\\\\n**跨环境 caveat**：Walker 上 recovery 充分(697.8)，但 Cheetah 上 recovery 不充分(97.5, 31%)。环境越难，recovery 越不可靠 → prevention 在难环境中价值更大。\\\\n\\\\n**⚠️ 机制为 open hypothesis**：v1≈v2 在所有 dual-critic 中成立。可能的解释：(a) min 在训练早期(v1≠v2 时)建立了稳定学习轨迹 (b) min-target coupling 在 wider network 的 smoother loss landscape 上更有效 (c) capacity 提升 value calibration 质量而非多样性。论文中诚实报告经验事实，机制标注为 hypothesis。\\\\n\\\\n**论文 narrative（D127 最终版）**：双维度报告——(a) Prevention: min+capacity 协同预防 CIVO（训练效率优势）(b) Recovery: min 是 CIVO 后恢复的主导因素（被低估的特性）(c) 跨环境：难环境中 recovery 不充分，凸显 prevention 的必要性 (d) v1≈v2: pessimism 机制失效但 min 通过其他通路起效（open question）\\\\n\\\\n**5. 环境依赖性（D125 — exp_034 完成）**：\\\\n- **Walker（中等 CIVO，untreated NVE 2-4）**：min 操作完全预防 CIVO（2/2 seeds）\\\\n- **Cheetah（高强度 CIVO，untreated NVE 8.27-70.64，seed 间高方差）**：min 操作将 NVE peak 从 baseline 8.27-70.64 降至 1.75（≥4× reduction），但仍超 1.5 阈值，不能完全预防。双倍参数(2.36M)实现部分恢复(eval 97.5)但仅达 pre-CIVO 峰值的 31% 且晚期下降。对比 Walker wide-critic(exp_033) 恢复到 408(>pre-CIVO)，说明**环境动力学复杂度是恢复质量的决定性因素**。（来源：exp_010b s0 NVE_final=70.64, s1 NVE_peak=8.27。论文中须报告两个 seed 并使用保守 claim \\\\\\\"≥4× NVE reduction\\\\\\\"，不用 40×）\\\\n- **论文 claim 限定**：\\\\\\\"min=prevention\\\\\\\" 必须加 \\\\\\\"in moderate-CIVO environments\\\\\\\" 限定，否则审稿人拿 Cheetah 数据直接攻击。这反而强化 intervention hierarchy 叙事——即使 architecture-level 干预也有 CIVO 严重度边界\\\\n\\\\n**论文 narrative（D126 修正）**：从\\\\\\\"为什么不测标准对策\\\\\\\"转为\\\\\\\"我们测了——(a) pessimism 机制失效（v1≈v2 across all configs），(b) min alone 和 capacity alone 都不能预防 CIVO，(c) 两者协同（min+capacity）才能预防，(d) 机制：capacity 提供函数多样性 + min 约束 overestimation 反馈环，(e) prevention >> recovery\\\\\\\"。2×2 factorial 的**交互效应**比任何单因素更有方法论启示——对 ML 社区的 critic 设计指导价值更高。\\\\n\\\\n### R10: \\\\\\\"NVE threshold is calibrated and validated in-sample\\\\\\\" [Dream D8 — 三档一致]\\\\n**Pre-emption**: 承认 1.5× threshold 在同一 29 个数据点上 calibrate 和 validate。但 (a) Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×，不是事后拟合；(b) 4 环境 × 多种 configs 提供 reasonable diversity；(c) ground truth labeling 基于 mechanism identification（CIVO vs non-CIVO dynamics），不是简单的 performance threshold。\\\\n**Mitigation**: 明确承认 limitation，建议 held-out validation（不同架构或环境）作为 future work。讨论 NVE 在不同 reward scale 下的 generalization boundary。\\\\n\\\\n### R11: \\\\\\\"Pixel observations would change the gradient decomposition\\\\\\\" [Dream D9 — 三档一致]\\\\n**Pre-emption**: 正确——pixel 下 obs-decoder channel（本文识别为 16-22% 梯度但因果关键）会承载更多信息和更大梯度。CIVO 动态可能更强（更多空间信息可利用）或更弱（decoder 正则化效应更强）。这是一个重要的泛化性边界。\\\\n**Mitigation**: 在 limitations 中明确讨论，定位为 future work。强调本文在 proprioceptive setting 的发现建立了 CIVO 的基础机制理论，pixel 扩展需要后续工作。\\\\n\\\\n---\\\\n\\\\n## Experiment Coverage Assessment\\\\n\\\\n| Claim | Evidence Status | Gaps |\\\\n|-------|----------------|------|\\\\n| C1 (degradation) | ✅ Strong — 3 configurations + 2 environments | None |\\\\n| C2 (CIVO trigger) | ✅ Strong — nve≥1.5× threshold 15/16, AUROC=0.969 (2 envs) | None |\\\\n| C3 (untrained emb protection) | ✅ Strong — 008a + cross-env replication | None |\\\\n| C4 (dt amplification) | ✅ Moderate — dt=1 > dt=2 > dt=4 monotonic | Only 2 dt values |\\\\n| C5 (horizon/subsample secondary) | ✅ Moderate | None blocking |\\\\n| C6 (dt=1 imag partial) | ✅ 4 seeds — 2/4 collapse via distinct pathways (CIVO + IRD) | None |\\\\n| C7 (SGS failure / gradient decoupling) | ✅ Strong — 17 seeds, 3 variants, 2 envs. 1/17 CIVO-free (with value collapse side effect). Embedding removal 5/5. | None |\\\\n| C8 (Intervention Hierarchy) | ✅ D113 确认 — TCN 2/8, RAVE 0/2, SGS 1/17. Hierarchy 本身是贡献 | Cheetah σ=1.0 + PickCube σ=0.5 pending (extra data points) |\\\\n\\\\n### Priority Actions Before Submission (updated 2026-05-20 D116 — Dream修复)\\\\n1. ~~C1-C7 实验~~ — ✅ 全部完成\\\\n2. ~~TCN/RAVE 评估~~ — ✅ D113 Scenario B 确认\\\\n3. ~~论文 TCN 文本修正~~ — ✅ cross-seed 报告 + narrative reframe\\\\n4. **🔄 [P0] 标准过估值对策讨论** — Paper Agent 执行中 (Dream R9)\\\\n5. **🔄 [P0] 参考文献扩展至 40+** — Paper Agent 执行中 (Dream D7)\\\\n6. **🔄 [P1] 新颖性锐化 + NVE 讨论 + pixel obs + CoRL 相关性** — Paper Agent 队列 (Dream D3/D8/D9/D2)\\\\n7. **🔄 [P1] Cheetah σ=1.0 + PickCube σ=0.5** — 运行中，Hierarchy 额外数据\\\\n8. **Re-dream 验证** — Paper Agent 结构性修复完成后\\\\n9. **论文收尾** — Reviewer 审查 + provenance + 三件套 + 5/25 数据锁定\\\\n\\\\n---\\\\n\\\\n## Key Figures (Planned)\\\\n\\\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\\\n\\\", \\\"total_chars\\\": 46244, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**⚠️ 修正：reward head 贡献最大梯度（49%@55K），obs decoder 仅 16.3%。但 reward-only SGS 仍失败——梯度大小与因果重要性解耦。** |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**dt_emb Gradient Decomposition (D061) — ⚠️ 已修正**\\n\\n梯度验证（torch.autograd.grad analysis, correct config gate_fixed_dt=2）揭示 dt_emb.weight 的梯度来源分布：\\n\\n| Source | 55K (%) | 112K (%) |\\n|--------|---------|----------|\\n| Reward head | 49.0 | 38.1 |\\n| KL dynamics | 34.7 | 40.4 |\\n| Observation decoders | 16.3 | 21.5 |\\n| Cont head | ~0 | ~0 |\\n\\n⚠️ **之前的 93% obs / 0% reward 数据不可复现**（见 gradient_decomposition_008d_corrected.json）。正确结论：reward head 贡献最大梯度（38-49%），但 reward-only SGS (016e) 仍然失败（NVE=10.42×）；obs decoder 通路（16-22%）虽贡献最小，但携带关键的 Δt-specific 空间信息驱动 RSSM fidelity gap。**梯度大小与因果重要性解耦**是核心发现。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\n\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\n\\n原假设\\\"dt=1 imagination = practical mitigation\\\"被**否证**。跨 seed 数据：\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\n- **独立 seed 崩溃率: 1/2 (50%)**\\n\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\n\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\n\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\n\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\n|------|---------------------|---------------------|\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\n\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\n\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\"seed 2 本身不稳定\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\n\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\n|------|-------------------|------------|------|\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\n\\n**C6 最终状态: PARTIALLY FALSIFIED**\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\n- 崩溃是配置导致的，不是 seed 特异性\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\n\\n**论文表述建议**: \\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\"\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\n\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\n\\n### C7: Gradient-level interventions fail to eliminate CIVO — gradient magnitude decoupled from causal importance\\n\\n**⚠️ D107: SGS 全面失败，梯度干预不是正确的干预层级**\\n\\nAll three SGS variants fail to eliminate CIVO:\\n- **Reward-only SGS** (016e): 0/2, NVE=10.42× — paradoxically worse than untreated\\n- **Full-pathway SGS** (018+021): 0/3 across two environments — blocks all non-KL gradients, still fails\\n- **Obs-decoder-only SGS** (025+026): 1/6 across two environments — the identified causal channel, still fails\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Reward-only SGS 反效果 | exp_016e | NVE=10.42×, collapse to eval 31.7. 阻断 reward 梯度迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差 |\\n| Full SGS 0/3 | exp_018 (Walker 2 seeds) + exp_021 (Cheetah 1 seed) | s1: eval 448.3, NVE 1.66× (CIVO+); s2: collapse 40.8; Cheetah: transient NVE 9.94×→0.34× (not SGS effect) |\\n| Obs-decoder SGS 1/6 | exp_025 (Walker 4 seeds) + exp_026 (Cheetah 2 seeds) | Walker: 1/4 (s1 survived, s2-s4 collapsed); Cheetah: 0/2, NVE 21.9×-30.2× (2.6-3.6× worse than untreated 8.3×) |\\n| Compensatory amplification (Cheetah) | exp_026 vs exp_010b | Obs-decoder SGS NVE 21.9-30.2× vs untreated 8.3× — blocking obs-decoder shifts co-adaptation to reward head |\\n| Universal value collapse | exp_025 all seeds @215K | All 4 seeds terminal ve_ratio=0.056-0.14, including s1 \\\"success\\\" (eval 726, value 41) — critic underestimation as side effect |\\n| Fourth trajectory (s3) | exp_025_s3 | Healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery (590@215K) → persistent value collapse (ve_ratio 0.14) |\\n\\n**核心发现**：\\n1. **梯度量级与因果重要性脱耦**: Reward head 38-49% 梯度占比（最大），但 reward-only SGS 失败最惨；obs decoder 16-22%（最小非零），但 obs-decoder SGS 也失败。梯度分解成功作为**诊断工具**但失败作为**干预指南**。\\n2. **Backward-pass 是错误的干预层级**: Full SGS 阻断所有非 KL 梯度仍 0/3 → forward-pass representational damage 是不可约减的脆弱性底线。Temporal embedding 通过 forward pass 塑造潜在表示，无论哪些梯度更新它。\\n3. **补偿放大**: 阻断任一通道导致剩余通道放大 co-adaptation（Cheetah: 2.6-3.6× 放大）。\\n4. **SGS 副作用**: 即使\\\"成功\\\"的 seed 也遭受 critic 校准损坏（universal value collapse）。\\n\\n**Strength**: Strong. 17 seeds across 3 SGS variants and 2 environments. Only 1/17 avoids CIVO, and that seed still suffers value collapse. Embedding removal (008f+024b): 5/5 = 100% prevention. The contrast establishes gradient stopping as categorically insufficient.\\n\\n### C8: Forward-pass interventions — TCN and RAVE (🔄 验证中)\\n\\n**⚠️ D107/D108: 两种 forward-pass 干预方法并行验证**\\n\\nSGS 失败的根因是 backward-pass 干预无法消除 forward-pass representational damage。C8 提出绕过梯度冗余的 forward-pass 干预：\\n\\n**TCN (Temporal Conditioning Noise)**:\\n- 设计理念：imagination 时对 dt_embedding 输出加高斯噪声 $\\\\mathcal{N}(0, \\\\sigma^2)$，降低 conditioning 精度\\n- 机制假说：噪声阻止 RSSM 和 critic 对精确 dt 信号的过度 co-adaptation，同时保留粗粒度时间信息\\n- 与 SGS 的区别：在 forward pass 层面操作，不依赖梯度阻断\\n- 超参：σ=0.5×std（主实验）+ σ=0.2×std（替代超参）\\n- 实验：exp_027_tcn_walker_s0 (σ=0.5), exp_027_tcn_walker_s0_sigma02 (σ=0.2)\\n\\n**RAVE (Reality-Anchored Value Estimation)**:\\n- 设计理念：用 EMA 跟踪真实环境状态的值估计，当 imagined value 超过 EMA×ceiling 时截断\\n- 机制假说：直接限制 critic overestimation 的幅度，打断 CIVO 正反馈循环\\n- 与 SGS 的区别：不修改梯度流，而是在 value estimate 层面施加约束\\n- 超参：ceiling=2.0（主实验）+ ceiling=1.5（替代超参）\\n- 实验：exp_028_rave_walker_s0 (ceil=2.0), exp_028_rave_walker_s0_ceil15 (ceil=1.5)\\n\\n**D113 全面评估完成 (2026-05-20) — Scenario B 确认：Intervention Hierarchy 论文**\\n\\nTCN 跨环境 universal mitigation（Scenario A）已关闭。TCN 仅在 Walker σ=0.2 成功（2/8 configs），且 eval 保留高度不稳定（91%/45% across seeds）。论文核心转为 **Intervention Hierarchy**：三层干预（Gradient → Output → Representation）系统性评估，证明 CIVO fundamentally hard to mitigate。\\n\\n**TCN 全景表（D113 最终）：**\\n\\n| 环境 | σ | NVE_max | CIVO 阻止? | eval 保留 |\\n|------|---|---------|-----------|----------|\\n| Walker s0 | 0.1 | 1.02@95K | ⚠️ 边界（进行中） | TBD |\\n| Walker s0 | 0.2 | 0.91@95K | ✅ | 91% |\\n| Walker s1 | 0.2 | 0.64@55K | ✅ | **45%** |\\n| Walker s2 | 0.2 | **2.11@95K** | **❌ CIVO confirmed** | **5%** (eval 45, 持续崩溃) |\\n| Walker s3 | 0.2 | TBD | 🔄 5K | — |\\n| Walker s0 | 0.5 | 3.97 | ❌ oscillatory | ~40% |\\n| Walker s1 | 0.5 | 1.64 | ❌ oscillatory | ~40% |\\n| Cheetah s0 | 0.2 | 1.90@55K | ❌ dose insufficient | crashed |\\n| Cheetah s0 | 0.5 | **10.67@55K** | ❌ transient spike+recovery | 26% |\\n| PickCube s0 | 0.2 | **3.71@52.5K** | ❌ dose insufficient | failing |\\n\\n**关键发现**：\\n1. **TCN 成功率 2/10**（NVE<1.0× 标准）或 3/10（NVE<1.5×）：Walker σ=0.2 s2 NVE=2.11@95K（持续恶化），eval=45 (~5% baseline)，成功率从 2/2 降到 2/3。即使最优 dose + 最温和环境也不可靠\\n2. **Dose-environment dependency**：σ=0.2 在 Walker 有效但 Cheetah/PickCube 不足，σ=0.5 在 Walker 过量但 Cheetah 仍不足。不存在 universal effective dose\\n3. **防 CIVO ≠ 保性能**：s1 NVE_max=0.64（比 s0 的 0.91 更低），但 eval 仅 45%（比 s0 的 91% 差 2×）。噪声注入本身干扰学习\\n4. **Cheetah \\\"impossible dose\\\" 完整确认（exp_030c FINAL @224K）**：σ=1.0 全程 NVE≤0.30（CIVO 完全抑制），但 eval 从 peak 372@35K（116% baseline，初始学习不受影响！）→ 47@215K（15% baseline）。关键发现：(a) 噪声不阻止初始学习，而是**渐进腐蚀** policy（cumulative actor gradient interference）；(b) value 校准正常（value_mean=12.4, NVE=0.26@215K）→ policy degradation ≠ value corruption；(c) Cheetah 的 CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)，不存在 Goldilocks zone。这本身也是 CIVO 与标准 overestimation 不同的证据——标准 Double Q 不会有这种 dose-dependent policy erosion tradeoff\\n5. **Cheetah σ=0.5 失败模式**：NVE=10.67@55K（transient CIVO spike），但 >95K 恢复至 <0.3。eval 永久受损（peak 296@35K → 稳态 ~77）\\n6. **⚠️ \\\"90% baseline\\\" claim 已删除**：cross-seed 均值 (821+401)/2 = 611 ≈ 68%，不是 90%。论文改为 \\\"45%-91% across seeds (mean 68%)\\\"\\n7. **Seed 效应 > dose 效应**：Walker σ=0.2 跨 seed eval=45%-91%，而 σ=0.1→0.2 的 eval 差异（55% vs 68% mean）更小\\n\\n**RAVE 2 配置 ❌ — EMA anchor 自身污染**:\\n- ceil=2.0: negative\\n- ceil=1.5: negative\\n- 机制：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → anchor 被污染 → ceiling 无效\\n\\n**Intervention Hierarchy 总结（论文核心 Table）：**\\n\\n| 干预层级 | 方法 | 成功率 | 主要失败机制 |\\n|----------|------|--------|-------------|\\n| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage 不可逆 |\\n| Gradient (L1) | Obs-decoder SGS | 1/6 | 补偿放大 + critic 校准损坏 |\\n| Gradient (L1) | Reward SGS | 0/2 | No-op (梯度 ≠ 因果) |\\n| Output (L2) | RAVE ceil=2.0 | 0/1 | EMA anchor 污染 |\\n| Output (L2) | RAVE ceil=1.5 | 0/1 | EMA anchor 污染 |\\n| Representation (L3) | TCN σ=0.2 | 2/4 (Walker only) | ❌ s2 gradual onset NVE=2.77@105K; s3 sudden onset NVE=3.04@105K; Cheetah/PickCube dose insufficient |\\n| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose (Walker) / Still insufficient (Cheetah) |\\n| **Control** | **dt_emb removal** | **5/5** | **(not an intervention — removes the feature)** |\\n\\n**叙事方向（D116 最终版，Reviewer 三问审查后）**：TCN 是 **diagnostic probe**，不是 deployable mitigation。\\n最终 claim 措辞（确认 2/4）：\\\"TCN is the only tested intervention that achieves complete CIVO suppression in any configuration (2 of 4 Walker seeds at σ=0.2), but exhibits high seed sensitivity (50% failure rate) and fails to transfer across environments—positioning it as a diagnostic probe rather than a deployable mitigation.\\\"\\n\\n**Binary protection 假说（确认 + 扩展）**：s2 渐进上升（0.58→1.01→1.65→2.77@105K），s3 表面回落后突崩（0.855→0.666→3.042@105K）。两种不同的 CIVO onset 动态，但结果相同：runaway NVE>2.5 + eval 崩溃。结论：(1) TCN operates as an all-or-nothing gate — 2/4 success, 2/4 complete failure, no intermediate; (2) CIVO onset 有至少两种模式（gradual escalation vs apparent-recovery-then-sudden-collapse）; (3) NVE 短期回落不能预测保护成功（phase transition 特性）。作为 1-2 句观察写入 + appendix 详细分析，非独立贡献。\\n\\n**Dose-response 定位**：不升级为独立贡献（n 太小，seed variance > dose variance），但作为 Section 3.6 key observations：(1) \\\"Effective dose scales with CIVO severity; tolerable dose does not\\\" — observation; (2) \\\"Impossible dose on Cheetah\\\" — 最有力单点; (3) \\\"Seed variance exceeds dose variance\\\"。\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| TCN σ=0.5 s0 | exp_027_tcn_walker_s0 | ❌ NVE peak 4.0, eval peak 366 (40% baseline), oscillatory CIVO |\\n| TCN σ=0.5 s1 | exp_027_tcn_walker_s1 | ❌ NVE peak 1.637, eval peak 365, oscillatory CIVO |\\n| TCN σ=0.2 s0 | exp_027_tcn_walker_s0_sigma02 | ✅ NVE < 1.0× throughout (peak 0.908@95K), eval peak 821 (91% baseline) |\\n| TCN σ=0.2 s1 | exp_029a_tcn_walker_s1_sigma02 | ✅ NVE < 1.0× (peak 0.643@55K), eval peak 401 (**45% baseline**) |\\n| RAVE ceiling=2.0 | exp_028_rave_walker_s0 | ❌ negative, EMA anchor polluted |\\n| RAVE ceiling=1.5 | exp_028_rave_walker_s0_ceil15 | ❌ negative, same mechanism |\\n| Cheetah TCN σ=0.2 | exp_030a_tcn_cheetah_s0_sigma02 | ❌ NVE=1.903@55K, dose insufficient |\\n| Cheetah TCN σ=0.5 | exp_030b_tcn_cheetah_s0_sigma05 | ❌ NVE=10.67@55K, transient spike, eval=77 (26% baseline) |\\n| PickCube TCN σ=0.2 | exp_031_tcn_pickcube_s0_sigma02 | ❌ NVE=3.71@52.5K, dose insufficient |\\n| Cheetah TCN σ=1.0 (FINAL) | exp_030c @224K | ✅ CIVO prevented (NVE≤0.30 全程) but ❌ eval=372 peak@35K (116% baseline!) → 47@215K (15% baseline). **\\\"Impossible dose\\\" 完整确认**: initial learning unaffected, gradual policy erosion from cumulative noise. Value calibration normal (value_mean=12.4, NVE=0.26@215K) — policy degradation ≠ value corruption |\\n| Walker TCN σ=0.1 | exp_029c (running) | 🔄 边界剂量响应 |\\n\\n**D113**: Scenario A closed → Scenario B confirmed. 论文 = Intervention Hierarchy paper with Walker TCN as existence proof.\\n\\n**Strength**: Moderate. TCN 的 2/8 成功率 + high eval variance 反而是 diagnostic paper 的强证据——证明 CIVO 在所有三个干预层级都难以可靠缓解。Intervention Hierarchy 框架（7+ methods, 3 levels, 3 environments）是系统性贡献。\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x)\\n- **D040: Multiple vulnerability pathways**: Pathway A (CIVO, value-driven) + Pathway B (non-CIVO policy instability, eval-driven)\\n- **D107: Gradient-level interventions fail entirely**: SGS 0/3 (full) + 1/6 (obs-decoder) + 0/2 (reward-only) = backward-pass is categorically insufficient. Gradient magnitude ≠ causal importance (reward 38-49% but reward-only SGS fails worst; obs-decoder 16-22% but targeted SGS also fails). Forward-pass representational damage is the irreducible floor.\\n- **Compensatory amplification**: Blocking obs-decoder on Cheetah → 2.6-3.6× NVE amplification vs untreated. Blocking reward → obs-decoder reliance increases → spatial bias reinforced.\\n- **Universal value collapse**: Obs-decoder SGS degrades all seeds' critic calibration (ve_ratio 0.056-0.14 @215K), including CIVO-free seeds. \\\"Protection\\\" = trading overestimation for underestimation.\\n- **Fourth CIVO trajectory (s3)**: Latent onset → delayed collapse → policy recovery → persistent value collapse. CIVO-induced critic damage may be irreversible.\\n- MPC vs imagination: TAWM succeeds because MPC re-plans from real states; imagination-based critic bootstrapping creates the positive feedback loop\\n- **D032: Value self-correction mechanism (009b)**: Transient vs sustained nve>1.5x determines outcome. Early stochasticity (initialization, data sampling) is the gate.\\n\\n### 6. Implications for Future Work\\n- **D113: Intervention Hierarchy — all three levels fail or partially fail**: Gradient (SGS 1/17), Output (RAVE 0/2), Representation (TCN 2/8 with high variance). dt_embedding removal 5/5 but removes the feature entirely.\\n- TCN existence proof (Walker σ=0.2) shows mitigation is *possible in principle* but fragile — narrow dose window, environment-dependent, high seed variance in eval retention\\n- **Dose-environment dependency**: No universal σ exists; Walker-effective dose (σ=0.2) underdoses Cheetah/PickCube, Walker-overdose (σ=0.5) still underdoses Cheetah\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Hierarchical temporal abstraction (THICK, Hieros) may avoid flat-conditioning failure by maintaining separate dynamics per temporal scale\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. Beyond diagnosis, we provide a **systematic Intervention Hierarchy** evaluating 7+ methods across 3 levels (gradient/output/representation) and 3 environments. This is the most comprehensive evaluation of CIVO interventions to date. The key finding: even the most promising intervention (TCN, representation-level) succeeds only under narrow conditions (Walker σ=0.2, 2/8 configs, 45-91% eval retention). The actionable takeaway is that CIVO requires fundamental architectural solutions (hierarchical temporal abstraction per THICK/Hieros), not post-hoc interventions.\\n**Mitigation**: The Intervention Hierarchy table (7 methods × 3 levels) is a standalone contribution — it saves future researchers from re-exploring these dead ends and provides a systematic framework for evaluating future interventions.\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but three elements are genuinely novel: (a) **MPC vs imagination architectural boundary** — first empirical evidence that dt-conditioning succeeds in MPC (TAWM) but fails in imagination-based AC, localizing vulnerability to critic bootstrapping architecture; (b) **gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but is causally irrelevant, obs-decoder carries 16-22% but is causally critical (broader methodological insight for multi-head MBRL debugging); (c) **systematic three-level intervention hierarchy** — not a single failure report but a complete taxonomy of 7 methods × 3 levels with structured negative evidence.\\n**Mitigation**: Expand Related Work to engage deeply with MBPO framework, explicitly articulate what CIVO reveals that MBPO does not predict (the specific *trigger* through temporal conditioning, the MPC/imagination divergence, the gradient-causality dissociation).\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n### R9: \\\"Why not test standard overestimation countermeasures (Double Q, ensemble critics)?\\\" [Dream D1 — 三档一致 #1 弱点] → **已实验回答 (D118-D123)**\\n\\n**实验结果（D118-D124 dual-critic + mechanism ablation 系列）**：\\n\\n**1. Dual-critic 跨环境结果（D128 更新）**：\\n- Walker wide dual-critic: **3/3 CIVO prevented**（s0 eval 739.7, s1 551.8, s2 ~121）。NVE 全程 < 1.5\\n  - ⚠️ **s2 非 CIVO 崩溃**：NVE 正常但 eval 354→121，actor entropy 急升(-3.59→-0.45)。可能是 policy exploration failure。**必须区分 \\\"CIVO prevention\\\"(3/3) vs \\\"performance stability\\\"(2/3)**\\n- Walker narrow dual-critic: 1/1 CIVO occurred (NVE 2.75) → full recovery eval 697.8\\n- Cheetah dual-critic: CIVO 发生(NVE 1.75) → 部分恢复 eval 97.5 (31%, 晚期下降)\\n- Cheetah wide single: CIVO 发生(NVE 3.59) → 自修复 eval 146 (晚期下降)。Wide > dual in Cheetah (146 vs 97.5)\\n- PickCube dual-critic: NVE 短暂升至 2.3 后自行修正，**PickCube 不触发持续性 CIVO**（任务动态不同）。eval 27.7 的低性能源于 gate 配置本身对 manipulation 任务有害（vanilla baseline 58.6 → 加 subsample+dt_emb 后 26.6），非 CIVO 导致。PickCube 作为 scope limitation 讨论，跨环境 CIVO 叙事聚焦 locomotion (Walker/Cheetah)\\n- **v1≈v2 across all environments and all configs**（ρ>0.999 Walker; exact match Cheetah/PickCube）\\n\\n**2. v1≈v2 核心发现**：Double Q 的 pessimism 机制在 pure-imagination MBRL 中失效。两个 critic 共享相同 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值的 3-4%（ρ>0.998）。\\n\\n**3. 2×2 Mechanism Factorial（D126 — 全部 4 格填满）**：\\n| | Single critic | Dual critic (min) |\\n|--|--------------|-------------------|\\n| ~1.05-1.2M params | baseline (**CIVO → 永久崩溃**) | **exp_035 narrow: CIVO(NVE 2.75) → 恢复中 → eval 149+** |\\n| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → 自修复 → eval 408** | **exp_032: CIVO 预防(NVE≤1.1) → eval 670-788** |\\n\\n**4. 双维度发现（D127 最终修正 — 论文最核心新发现）**：\\n\\n**Recovery 维度（min 是主导因素）**：\\n| 配置 | CIVO 发生? | NVE peak | eval final | 恢复能力 |\\n|------|-----------|----------|------------|---------|\\n| Baseline (single+normal) | ✓ | ~2-4 | collapsed | 无 |\\n| exp_033 (single+wide) | ✓ | 4.75 | 408 | 部分(capacity) |\\n| **exp_035 (dual+narrow)** | **✓** | **2.75** | **697.8** | **完全(min)** |\\n| exp_032 (dual+wide) | ✗ | ≤1.1 | 670-788 | 无需恢复 |\\n\\n- **Min 的核心价值是 recovery 而非 prevention**：exp_035 eval 697.8 ≈ exp_032 670-788，尽管经历了 CIVO\\n- **Min >> Capacity for recovery**：697.8 vs 408。min 实现完全恢复，capacity 仅部分恢复\\n- **Min 同时降低 CIVO 严重度**：exp_035 NVE 2.75 < exp_033 NVE 4.75\\n\\n**Prevention 维度（需 min+capacity 协同）**：\\n- 只有 exp_032 (min+capacity) 从未触发 CIVO（NVE≤1.1）\\n- Prevention 优势不是最终性能（≈recovery-with-min），而是**训练效率**（节省 ~40K steps 恢复期）\\n- v1≈v2 在所有 dual-critic 中成立（包括 exp_032）→ 协同效应是经验事实，机制为 hypothesis\\n\\n**跨环境 caveat**：Walker 上 recovery 充分(697.8)，但 Cheetah 上 recovery 不充分(97.5, 31%)。环境越难，recovery 越不可靠 → prevention 在难环境中价值更大。\\n\\n**⚠️ 机制为 open hypothesis**：v1≈v2 在所有 dual-critic 中成立。可能的解释：(a) min 在训练早期(v1≠v2 时)建立了稳定学习轨迹 (b) min-target coupling 在 wider network 的 smoother loss landscape 上更有效 (c) capacity 提升 value calibration 质量而非多样性。论文中诚实报告经验事实，机制标注为 hypothesis。\\n\\n**论文 narrative（D127 最终版）**：双维度报告——(a) Prevention: min+capacity 协同预防 CIVO（训练效率优势）(b) Recovery: min 是 CIVO 后恢复的主导因素（被低估的特性）(c) 跨环境：难环境中 recovery 不充分，凸显 prevention 的必要性 (d) v1≈v2: pessimism 机制失效但 min 通过其他通路起效（open question）\\n\\n**5. 环境依赖性（D125 — exp_034 完成）**：\\n- **Walker（中等 CIVO，untreated NVE 2-4）**：min 操作完全预防 CIVO（2/2 seeds）\\n- **Cheetah（高强度 CIVO，untreated NVE 8.27-70.64，seed 间高方差）**：min 操作将 NVE peak 从 baseline 8.27-70.64 降至 1.75（≥4× reduction），但仍超 1.5 阈值，不能完全预防。双倍参数(2.36M)实现部分恢复(eval 97.5)但仅达 pre-CIVO 峰值的 31% 且晚期下降。对比 Walker wide-critic(exp_033) 恢复到 408(>pre-CIVO)，说明**环境动力学复杂度是恢复质量的决定性因素**。（来源：exp_010b s0 NVE_final=70.64, s1 NVE_peak=8.27。论文中须报告两个 seed 并使用保守 claim \\\"≥4× NVE reduction\\\"，不用 40×）\\n- **论文 claim 限定**：\\\"min=prevention\\\" 必须加 \\\"in moderate-CIVO environments\\\" 限定，否则审稿人拿 Cheetah 数据直接攻击。这反而强化 intervention hierarchy 叙事——即使 architecture-level 干预也有 CIVO 严重度边界\\n\\n**论文 narrative（D126 修正）**：从\\\"为什么不测标准对策\\\"转为\\\"我们测了——(a) pessimism 机制失效（v1≈v2 across all configs），(b) min alone 和 capacity alone 都不能预防 CIVO，(c) 两者协同（min+capacity）才能预防，(d) 机制：capacity 提供函数多样性 + min 约束 overestimation 反馈环，(e) prevention >> recovery\\\"。2×2 factorial 的**交互效应**比任何单因素更有方法论启示——对 ML 社区的 critic 设计指导价值更高。\\n\\n### R10: \\\"NVE threshold is calibrated and validated in-sample\\\" [Dream D8 — 三档一致]\\n**Pre-emption**: 承认 1.5× threshold 在同一 29 个数据点上 calibrate 和 validate。但 (a) Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×，不是事后拟合；(b) 4 环境 × 多种 configs 提供 reasonable diversity；(c) ground truth labeling 基于 mechanism identification（CIVO vs non-CIVO dynamics），不是简单的 performance threshold。\\n**Mitigation**: 明确承认 limitation，建议 held-out validation（不同架构或环境）作为 future work。讨论 NVE 在不同 reward scale 下的 generalization boundary。\\n\\n### R11: \\\"Pixel observations would change the gradient decomposition\\\" [Dream D9 — 三档一致]\\n**Pre-emption**: 正确——pixel 下 obs-decoder channel（本文识别为 16-22% 梯度但因果关键）会承载更多信息和更大梯度。CIVO 动态可能更强（更多空间信息可利用）或更弱（decoder 正则化效应更强）。这是一个重要的泛化性边界。\\n**Mitigation**: 在 limitations 中明确讨论，定位为 future work。强调本文在 proprioceptive setting 的发现建立了 CIVO 的基础机制理论，pixel 扩展需要后续工作。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations + 2 environments | None |\\n| C2 (CIVO trigger) | ✅ Strong — nve≥1.5× threshold 15/16, AUROC=0.969 (2 envs) | None |\\n| C3 (untrained emb protection) | ✅ Strong — 008a + cross-env replication | None |\\n| C4 (dt amplification) | ✅ Moderate — dt=1 > dt=2 > dt=4 monotonic | Only 2 dt values |\\n| C5 (horizon/subsample secondary) | ✅ Moderate | None blocking |\\n| C6 (dt=1 imag partial) | ✅ 4 seeds — 2/4 collapse via distinct pathways (CIVO + IRD) | None |\\n| C7 (SGS failure / gradient decoupling) | ✅ Strong — 17 seeds, 3 variants, 2 envs. 1/17 CIVO-free (with value collapse side effect). Embedding removal 5/5. | None |\\n| C8 (Intervention Hierarchy) | ✅ D113 确认 — TCN 2/8, RAVE 0/2, SGS 1/17. Hierarchy 本身是贡献 | Cheetah σ=1.0 + PickCube σ=0.5 pending (extra data points) |\\n\\n### Priority Actions Before Submission (updated 2026-05-20 D116 — Dream修复)\\n1. ~~C1-C7 实验~~ — ✅ 全部完成\\n2. ~~TCN/RAVE 评估~~ — ✅ D113 Scenario B 确认\\n3. ~~论文 TCN 文本修正~~ — ✅ cross-seed 报告 + narrative reframe\\n4. **🔄 [P0] 标准过估值对策讨论** — Paper Agent 执行中 (Dream R9)\\n5. **🔄 [P0] 参考文献扩展至 40+** — Paper Agent 执行中 (Dream D7)\\n6. **🔄 [P1] 新颖性锐化 + NVE 讨论 + pixel obs + CoRL 相关性** — Paper Agent 队列 (Dream D3/D8/D9/D2)\\n7. **🔄 [P1] Cheetah σ=1.0 + PickCube σ=0.5** — 运行中，Hierarchy 额外数据\\n8. **Re-dream 验证** — Paper Agent 结构性修复完成后\\n9. **论文收尾** — Reviewer 审查 + provenance + 三件套 + 5/25 数据锁定\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\n\", \"total_chars\": 46244, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017UXxfaFCG7ErJNwXzoCW36`</summary>

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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "5c199433-508f-419a-a2a4-4878b92d2ac7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133ShyuDamDTCz81dSiVeX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1435
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


### Tool result

_source line 11 · 2026-05-24T01:50:37.836Z_

<details><summary>↩ Tool result · `toolu_017UXxfaFCG7ErJNwXzoCW36`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n> 不可从 registry/代码派生的决策原因、约束、经验教训。\\n\\n## 竞品实验参考\\n（待补充）\\n\\n## 经验教训\\n\\n### CIVO Severity Threshold 发现 (2026-05-22)\\n- **核心发现**：CIVO 可恢复性取决于严重程度，存在 severity threshold\\n- Walker (NVE~5, exp_045): 完全自修复 — ve_ratio 4.91→0.05 (99%), eval 35→868, 170K 步\\n- Cheetah (NVE~70, exp_048): 部分修复但不可逆损伤 — ve_ratio 46.3→1.80 (96%), eval 23.4 (远低于正常), gate 永久坍塌\\n- **二次爆发**：Cheetah 在 152K-162K 出现 ve_ratio 回弹到 24.1 (NVE 36.8)，即使一度下降到 2.9 → 极端 CIVO 有\\\"记忆\\\"可导致复发\\n- **Paper framing**：轻度 CIVO 是可逆暂态，极端 CIVO 造成永久损伤 → frozen dt_emb 等预防措施是必要的\\n\\n### Gradient Stopping 加速自修复 (2026-05-22)\\n- exp_044: reward_dt_emb_detach 不阻止 CIVO 触发（ve_ratio peak=4.4）但加速自修复\\n- 修复速度：40K 步 (exp_044 with detach) vs 170K 步 (exp_045 without)\\n- 支撑 Intervention Hierarchy：gradient-level 最弱（不预防但加速恢复）, frozen dt_emb 最强（完全预防）\\n\\n### Frozen dt_emb 跨环境验证 (2026-05-22)\\n- Walker: exp_042 NVE=0.19 (s0), exp_015b NVE=0.47 (s1), exp_047 NVE=1.71 transient→0.56 (s1) — 3/3 无持续 CIVO\\n- Cheetah: exp_046 NVE=1.35 (s0) — 1/1 无 CIVO（即便 trained dt_emb 时 NVE=70.64）\\n- 三向因果（Walker）: trained 4/4 CIVO, frozen 0/2, removed 0/4 (Fisher p=0.003)\\n\\n### CIVO Self-Correction 发现 (2026-05-22)\\n- exp_045 (008d s3 从 112K 恢复到 300K): CIVO 不是永久崩溃，而是暂态不稳定\\n- 时间线：ve_ratio 4.91@132K → 0.43@142K（30K steps 内急剧自纠正）→ 0.05@302K\\n- eval: 35@132K → 350@142K → 868@302K（接近 baseline ~920）\\n- 与 exp_009b (s2, NVE 2.05→0.38@105K) 一致：self-correction 在多个 seed 中出现\\n- **论文 framing 影响**：CIVO 在标准评估窗口（105K）看起来是 collapse，但 extended training 显示 agent 能自我修正。真正的代价是 convergence delay（额外 ~130K steps 才接近 baseline）\\n- **决策约束**：需要 Director 决定是否调整 framing（\\\"catastrophic collapse\\\" → \\\"transient instability with convergence delay\\\"）\\n\\n### Dual-Critic 机制发现 (2026-05-21)\\n- exp_032/032b Walker dual-critic: v1≈v2 (gap <0.5), min 无 pessimism 效果，但 CIVO 仍被抑制 → 机制是 implicit regularization，不是传统 Double-Q pessimism\\n- exp_033 wide-critic (2.89M params, 2.44× normal): CIVO 仍触发 (NVE 4.7) → 参数量本身不能防 CIVO\\n- exp_034 Cheetah dual-critic: NVE 1.8 (vs baseline 70.64, 降 40×) 但仍超 1.5 阈值 → 部分抑制但不完全。Dual-wave CIVO pattern\\n\\n### 2×2 Factorial 完成 (2026-05-21)\\n- {single, dual} × {normal ~1.2M, scaled ~2.4-2.9M}:\\n  - single + normal = baseline (CIVO → collapse)\\n  - single + scaled = exp_033 (CIVO NVE 4.7 → partial recovery, eval 408)\\n  - dual + normal = exp_035 (CIVO NVE 2.75 → full recovery, eval 697.8) — Director override success\\n  - dual + scaled = exp_032 (CIVO prevented, NVE ≤1.1, eval 787.7)\\n- **双维度 insight**: Prevention = min+capacity synergy; Recovery = min 主导 (697.8 vs 408)\\n\\n### Cross-Environment 完整结果 (2026-05-21 更新)\\n- **Walker**: dual-critic 2/2 CIVO prevented (s0=787.7, s1=551.8)，但 s2 (exp_038) 出现 non-CIVO collapse (peak 354→120, NVE≤0.3)。Narrow dual s0 recovery 697.8, s1 (exp_039) collapsing\\n- **Cheetah**: dual-critic negative (NVE 1.8, eval 97.5); wide single negative (peak 350→146 decay)。两种干预都不够\\n- **PickCube**: CIVO 根本不发生（NVE 自行修正至 0.2）。subsample+dt_emb 配置本身损害性能（vanilla 58.6→config 26.6）。Dual-critic 无关（v1=v2）\\n- **结论**: 干预在 locomotion 中部分有效（Walker > Cheetah），manipulation 域 CIVO 不触发 → scope limitation\\n\\n### Non-CIVO Collapse 发现 (2026-05-21)\\n- exp_038 Walker dual s2: eval 崩溃但 NVE≤0.3 → 存在独立于 CIVO 的崩溃机制\\n- Dual-critic 专门解决 value overestimation cascade，不是万能防崩溃方案\\n- 论文需区分 \\\"CIVO prevention\\\" vs \\\"general stability\\\"\\n\\n### TCN 全景 (2026-05-21)\\n- Walker: σ=0.2 部分有效 (2/4 seeds), σ=0.1 和 σ=0.5 失败\\n- Cheetah: 全部失败 (σ=0.2/0.5/1.0)\\n- PickCube: 全部失败 (σ=0.2/0.5)\\n- 结论：TCN 窗口极窄，仅 Walker σ=0.2 部分 work\\n\\n### NVE 诊断经验 (2026-05-21)\\n- Late-stage NVE 下降需区分 genuine CIVO recovery vs floor effect\\n- 关键判据：eval 是否同步恢复。Eval 恢复 → genuine；eval 平坦 → floor effect\\n- exp_031b 教训：NVE 3.3→0.2 看似恢复，但 eval 25-29 平坦 → floor effect / negative\\n\\n### Registry 工具问题 (2026-05-21 更新 2026-05-22)\\n- read_registry 工具有时只返回部分实验（11/101），直接读 YAML 更可靠\\n- update_registry 工具有时创建内存条目但不持久化到 YAML（exp_045/046/047/048 案例）\\n- 状态转换有限制（如 PREPARING 只能 → PENDING/QUEUED，不能直接 → RUNNING）\\n- 有 parent 字段的实验被当 eval 实验，需要额外提供 checkpoint_source/eval_data\\n- **教训**：重要实验注册后必须 grep YAML 验证实际写入，完成后必须手动编辑 YAML 确保持久化\\n\\n### exp_040 诊断 (2026-05-22)\\n- Cheetah dual-critic (含 wide variant) 无效。宽 critic 不解决 Cheetah CIVO。\\n\", \"total_chars\": 4056, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "b9d92d1b-4af9-4dda-9046-2a4a1dd755e3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\\\", \\\"content\\\": \\\"# Memory — event-gated-adaptive-horizon\\\\n\\\\n> 不可从 registry/代码派生的决策原因、约束、经验教训。\\\\n\\\\n## 竞品实验参考\\\\n（待补充）\\\\n\\\\n## 经验教训\\\\n\\\\n### CIVO Severity Threshold 发现 (2026-05-22)\\\\n- **核心发现**：CIVO 可恢复性取决于严重程度，存在 severity threshold\\\\n- Walker (NVE~5, exp_045): 完全自修复 — ve_ratio 4.91→0.05 (99%), eval 35→868, 170K 步\\\\n- Cheetah (NVE~70, exp_048): 部分修复但不可逆损伤 — ve_ratio 46.3→1.80 (96%), eval 23.4 (远低于正常), gate 永久坍塌\\\\n- **二次爆发**：Cheetah 在 152K-162K 出现 ve_ratio 回弹到 24.1 (NVE 36.8)，即使一度下降到 2.9 → 极端 CIVO 有\\\\\\\"记忆\\\\\\\"可导致复发\\\\n- **Paper framing**：轻度 CIVO 是可逆暂态，极端 CIVO 造成永久损伤 → frozen dt_emb 等预防措施是必要的\\\\n\\\\n### Gradient Stopping 加速自修复 (2026-05-22)\\\\n- exp_044: reward_dt_emb_detach 不阻止 CIVO 触发（ve_ratio peak=4.4）但加速自修复\\\\n- 修复速度：40K 步 (exp_044 with detach) vs 170K 步 (exp_045 without)\\\\n- 支撑 Intervention Hierarchy：gradient-level 最弱（不预防但加速恢复）, frozen dt_emb 最强（完全预防）\\\\n\\\\n### Frozen dt_emb 跨环境验证 (2026-05-22)\\\\n- Walker: exp_042 NVE=0.19 (s0), exp_015b NVE=0.47 (s1), exp_047 NVE=1.71 transient→0.56 (s1) — 3/3 无持续 CIVO\\\\n- Cheetah: exp_046 NVE=1.35 (s0) — 1/1 无 CIVO（即便 trained dt_emb 时 NVE=70.64）\\\\n- 三向因果（Walker）: trained 4/4 CIVO, frozen 0/2, removed 0/4 (Fisher p=0.003)\\\\n\\\\n### CIVO Self-Correction 发现 (2026-05-22)\\\\n- exp_045 (008d s3 从 112K 恢复到 300K): CIVO 不是永久崩溃，而是暂态不稳定\\\\n- 时间线：ve_ratio 4.91@132K → 0.43@142K（30K steps 内急剧自纠正）→ 0.05@302K\\\\n- eval: 35@132K → 350@142K → 868@302K（接近 baseline ~920）\\\\n- 与 exp_009b (s2, NVE 2.05→0.38@105K) 一致：self-correction 在多个 seed 中出现\\\\n- **论文 framing 影响**：CIVO 在标准评估窗口（105K）看起来是 collapse，但 extended training 显示 agent 能自我修正。真正的代价是 convergence delay（额外 ~130K steps 才接近 baseline）\\\\n- **决策约束**：需要 Director 决定是否调整 framing（\\\\\\\"catastrophic collapse\\\\\\\" → \\\\\\\"transient instability with convergence delay\\\\\\\"）\\\\n\\\\n### Dual-Critic 机制发现 (2026-05-21)\\\\n- exp_032/032b Walker dual-critic: v1≈v2 (gap <0.5), min 无 pessimism 效果，但 CIVO 仍被抑制 → 机制是 implicit regularization，不是传统 Double-Q pessimism\\\\n- exp_033 wide-critic (2.89M params, 2.44× normal): CIVO 仍触发 (NVE 4.7) → 参数量本身不能防 CIVO\\\\n- exp_034 Cheetah dual-critic: NVE 1.8 (vs baseline 70.64, 降 40×) 但仍超 1.5 阈值 → 部分抑制但不完全。Dual-wave CIVO pattern\\\\n\\\\n### 2×2 Factorial 完成 (2026-05-21)\\\\n- {single, dual} × {normal ~1.2M, scaled ~2.4-2.9M}:\\\\n  - single + normal = baseline (CIVO → collapse)\\\\n  - single + scaled = exp_033 (CIVO NVE 4.7 → partial recovery, eval 408)\\\\n  - dual + normal = exp_035 (CIVO NVE 2.75 → full recovery, eval 697.8) — Director override success\\\\n  - dual + scaled = exp_032 (CIVO prevented, NVE ≤1.1, eval 787.7)\\\\n- **双维度 insight**: Prevention = min+capacity synergy; Recovery = min 主导 (697.8 vs 408)\\\\n\\\\n### Cross-Environment 完整结果 (2026-05-21 更新)\\\\n- **Walker**: dual-critic 2/2 CIVO prevented (s0=787.7, s1=551.8)，但 s2 (exp_038) 出现 non-CIVO collapse (peak 354→120, NVE≤0.3)。Narrow dual s0 recovery 697.8, s1 (exp_039) collapsing\\\\n- **Cheetah**: dual-critic negative (NVE 1.8, eval 97.5); wide single negative (peak 350→146 decay)。两种干预都不够\\\\n- **PickCube**: CIVO 根本不发生（NVE 自行修正至 0.2）。subsample+dt_emb 配置本身损害性能（vanilla 58.6→config 26.6）。Dual-critic 无关（v1=v2）\\\\n- **结论**: 干预在 locomotion 中部分有效（Walker > Cheetah），manipulation 域 CIVO 不触发 → scope limitation\\\\n\\\\n### Non-CIVO Collapse 发现 (2026-05-21)\\\\n- exp_038 Walker dual s2: eval 崩溃但 NVE≤0.3 → 存在独立于 CIVO 的崩溃机制\\\\n- Dual-critic 专门解决 value overestimation cascade，不是万能防崩溃方案\\\\n- 论文需区分 \\\\\\\"CIVO prevention\\\\\\\" vs \\\\\\\"general stability\\\\\\\"\\\\n\\\\n### TCN 全景 (2026-05-21)\\\\n- Walker: σ=0.2 部分有效 (2/4 seeds), σ=0.1 和 σ=0.5 失败\\\\n- Cheetah: 全部失败 (σ=0.2/0.5/1.0)\\\\n- PickCube: 全部失败 (σ=0.2/0.5)\\\\n- 结论：TCN 窗口极窄，仅 Walker σ=0.2 部分 work\\\\n\\\\n### NVE 诊断经验 (2026-05-21)\\\\n- Late-stage NVE 下降需区分 genuine CIVO recovery vs floor effect\\\\n- 关键判据：eval 是否同步恢复。Eval 恢复 → genuine；eval 平坦 → floor effect\\\\n- exp_031b 教训：NVE 3.3→0.2 看似恢复，但 eval 25-29 平坦 → floor effect / negative\\\\n\\\\n### Registry 工具问题 (2026-05-21 更新 2026-05-22)\\\\n- read_registry 工具有时只返回部分实验（11/101），直接读 YAML 更可靠\\\\n- update_registry 工具有时创建内存条目但不持久化到 YAML（exp_045/046/047/048 案例）\\\\n- 状态转换有限制（如 PREPARING 只能 → PENDING/QUEUED，不能直接 → RUNNING）\\\\n- 有 parent 字段的实验被当 eval 实验，需要额外提供 checkpoint_source/eval_data\\\\n- **教训**：重要实验注册后必须 grep YAML 验证实际写入，完成后必须手动编辑 YAML 确保持久化\\\\n\\\\n### exp_040 诊断 (2026-05-22)\\\\n- Cheetah dual-critic (含 wide variant) 无效。宽 critic 不解决 Cheetah CIVO。\\\\n\\\", \\\"total_chars\\\": 4056, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n> 不可从 registry/代码派生的决策原因、约束、经验教训。\\n\\n## 竞品实验参考\\n（待补充）\\n\\n## 经验教训\\n\\n### CIVO Severity Threshold 发现 (2026-05-22)\\n- **核心发现**：CIVO 可恢复性取决于严重程度，存在 severity threshold\\n- Walker (NVE~5, exp_045): 完全自修复 — ve_ratio 4.91→0.05 (99%), eval 35→868, 170K 步\\n- Cheetah (NVE~70, exp_048): 部分修复但不可逆损伤 — ve_ratio 46.3→1.80 (96%), eval 23.4 (远低于正常), gate 永久坍塌\\n- **二次爆发**：Cheetah 在 152K-162K 出现 ve_ratio 回弹到 24.1 (NVE 36.8)，即使一度下降到 2.9 → 极端 CIVO 有\\\"记忆\\\"可导致复发\\n- **Paper framing**：轻度 CIVO 是可逆暂态，极端 CIVO 造成永久损伤 → frozen dt_emb 等预防措施是必要的\\n\\n### Gradient Stopping 加速自修复 (2026-05-22)\\n- exp_044: reward_dt_emb_detach 不阻止 CIVO 触发（ve_ratio peak=4.4）但加速自修复\\n- 修复速度：40K 步 (exp_044 with detach) vs 170K 步 (exp_045 without)\\n- 支撑 Intervention Hierarchy：gradient-level 最弱（不预防但加速恢复）, frozen dt_emb 最强（完全预防）\\n\\n### Frozen dt_emb 跨环境验证 (2026-05-22)\\n- Walker: exp_042 NVE=0.19 (s0), exp_015b NVE=0.47 (s1), exp_047 NVE=1.71 transient→0.56 (s1) — 3/3 无持续 CIVO\\n- Cheetah: exp_046 NVE=1.35 (s0) — 1/1 无 CIVO（即便 trained dt_emb 时 NVE=70.64）\\n- 三向因果（Walker）: trained 4/4 CIVO, frozen 0/2, removed 0/4 (Fisher p=0.003)\\n\\n### CIVO Self-Correction 发现 (2026-05-22)\\n- exp_045 (008d s3 从 112K 恢复到 300K): CIVO 不是永久崩溃，而是暂态不稳定\\n- 时间线：ve_ratio 4.91@132K → 0.43@142K（30K steps 内急剧自纠正）→ 0.05@302K\\n- eval: 35@132K → 350@142K → 868@302K（接近 baseline ~920）\\n- 与 exp_009b (s2, NVE 2.05→0.38@105K) 一致：self-correction 在多个 seed 中出现\\n- **论文 framing 影响**：CIVO 在标准评估窗口（105K）看起来是 collapse，但 extended training 显示 agent 能自我修正。真正的代价是 convergence delay（额外 ~130K steps 才接近 baseline）\\n- **决策约束**：需要 Director 决定是否调整 framing（\\\"catastrophic collapse\\\" → \\\"transient instability with convergence delay\\\"）\\n\\n### Dual-Critic 机制发现 (2026-05-21)\\n- exp_032/032b Walker dual-critic: v1≈v2 (gap <0.5), min 无 pessimism 效果，但 CIVO 仍被抑制 → 机制是 implicit regularization，不是传统 Double-Q pessimism\\n- exp_033 wide-critic (2.89M params, 2.44× normal): CIVO 仍触发 (NVE 4.7) → 参数量本身不能防 CIVO\\n- exp_034 Cheetah dual-critic: NVE 1.8 (vs baseline 70.64, 降 40×) 但仍超 1.5 阈值 → 部分抑制但不完全。Dual-wave CIVO pattern\\n\\n### 2×2 Factorial 完成 (2026-05-21)\\n- {single, dual} × {normal ~1.2M, scaled ~2.4-2.9M}:\\n  - single + normal = baseline (CIVO → collapse)\\n  - single + scaled = exp_033 (CIVO NVE 4.7 → partial recovery, eval 408)\\n  - dual + normal = exp_035 (CIVO NVE 2.75 → full recovery, eval 697.8) — Director override success\\n  - dual + scaled = exp_032 (CIVO prevented, NVE ≤1.1, eval 787.7)\\n- **双维度 insight**: Prevention = min+capacity synergy; Recovery = min 主导 (697.8 vs 408)\\n\\n### Cross-Environment 完整结果 (2026-05-21 更新)\\n- **Walker**: dual-critic 2/2 CIVO prevented (s0=787.7, s1=551.8)，但 s2 (exp_038) 出现 non-CIVO collapse (peak 354→120, NVE≤0.3)。Narrow dual s0 recovery 697.8, s1 (exp_039) collapsing\\n- **Cheetah**: dual-critic negative (NVE 1.8, eval 97.5); wide single negative (peak 350→146 decay)。两种干预都不够\\n- **PickCube**: CIVO 根本不发生（NVE 自行修正至 0.2）。subsample+dt_emb 配置本身损害性能（vanilla 58.6→config 26.6）。Dual-critic 无关（v1=v2）\\n- **结论**: 干预在 locomotion 中部分有效（Walker > Cheetah），manipulation 域 CIVO 不触发 → scope limitation\\n\\n### Non-CIVO Collapse 发现 (2026-05-21)\\n- exp_038 Walker dual s2: eval 崩溃但 NVE≤0.3 → 存在独立于 CIVO 的崩溃机制\\n- Dual-critic 专门解决 value overestimation cascade，不是万能防崩溃方案\\n- 论文需区分 \\\"CIVO prevention\\\" vs \\\"general stability\\\"\\n\\n### TCN 全景 (2026-05-21)\\n- Walker: σ=0.2 部分有效 (2/4 seeds), σ=0.1 和 σ=0.5 失败\\n- Cheetah: 全部失败 (σ=0.2/0.5/1.0)\\n- PickCube: 全部失败 (σ=0.2/0.5)\\n- 结论：TCN 窗口极窄，仅 Walker σ=0.2 部分 work\\n\\n### NVE 诊断经验 (2026-05-21)\\n- Late-stage NVE 下降需区分 genuine CIVO recovery vs floor effect\\n- 关键判据：eval 是否同步恢复。Eval 恢复 → genuine；eval 平坦 → floor effect\\n- exp_031b 教训：NVE 3.3→0.2 看似恢复，但 eval 25-29 平坦 → floor effect / negative\\n\\n### Registry 工具问题 (2026-05-21 更新 2026-05-22)\\n- read_registry 工具有时只返回部分实验（11/101），直接读 YAML 更可靠\\n- update_registry 工具有时创建内存条目但不持久化到 YAML（exp_045/046/047/048 案例）\\n- 状态转换有限制（如 PREPARING 只能 → PENDING/QUEUED，不能直接 → RUNNING）\\n- 有 parent 字段的实验被当 eval 实验，需要额外提供 checkpoint_source/eval_data\\n- **教训**：重要实验注册后必须 grep YAML 验证实际写入，完成后必须手动编辑 YAML 确保持久化\\n\\n### exp_040 诊断 (2026-05-22)\\n- Cheetah dual-critic (含 wide variant) 无效。宽 critic 不解决 Cheetah CIVO。\\n\", \"total_chars\": 4056, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015R3w4yhfbUPQ8puhXG2HvF`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "47a10c8f-0112-4ab7-95bd-149fb43a0a9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133ShyuDamDTCz81dSiVeX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1435
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


### Tool result

_source line 13 · 2026-05-24T01:50:40.100Z_

<details><summary>↩ Tool result · `toolu_015R3w4yhfbUPQ8puhXG2HvF`</summary>

```text
Error: result (297,856 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "2b4e1737-0be1-489d-8591-b17bb9c2c44d",
  "tool_use_result": {
    "content": "Error: result (297,856 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:30:00.000Z\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. ve_ratio 全程极低 (peak 0.231). Cheetah frozen n=2: s0=1.35, s1=0.23 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:02:23.683Z\", \"updated_at\": \"2026-05-24T00:00:00.000Z\", \"hypothesis\": \"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\", \"parent\": \"exp_053_peginsertion_frozen_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:00:00.000Z\", \"metrics\": {\"total_steps\": 222500, \"ve_ratio_peak\": 11.321, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 1.193, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 4.37, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.42, \"eval_return_peak_step\": 132500, \"nve_classification\": \"burst\", \"note\": \"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\", \"ve_ratio_trajectory\": {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:50:00.000Z\", \"updated_at\": \"2026-05-23T23:38:30.000Z\", \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}, \"ve_ratio_peak\": \"3.08@92500\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:38:25.428Z\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_peak\": 3.08, \"ve_ratio_peak_step\": 92500, \"ve_ratio_final\": 0.498, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 11.44, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.05, \"eval_return_peak_step\": 112500, \"nve_classification\": \"transient\", \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"note\": \"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\", \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}}, \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/checkpoint_222500.pt\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:25:00.000Z\", \"updated_at\": \"2026-05-23T23:30:00.000Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}, \"completed_at\": \"2026-05-23T23:30:00.000Z\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_classification\": \"no_civo\", \"note\": \"Walker frozen s2. Peak transient at 115K, self-corrected. Walker frozen n=3 complete: s0=0.19, s1=1.71, s2=1.28 — all clean/transient.\"}}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:24.310Z\", \"updated_at\": \"2026-05-23T18:08:00.000Z\", \"hypothesis\": \"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.81@62500\", \"eval_final\": 10.26, \"eval_final_step\": 212500, \"ve_ratio_final\": 0.583, \"ve_ratio_final_step\": 212500}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:23:10.381Z\", \"updated_at\": \"2026-05-23T15:00:00.000Z\", \"hypothesis\": \"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.10@52500\", \"eval_final\": 5.89, \"ve_ratio_final\": 0.202, \"ve_ratio_final_step\": 212500}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:38:33.441Z\", \"updated_at\": \"2026-05-23T08:51:11.592Z\", \"hypothesis\": \"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\", \"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}, \"metrics\": {\"ve_ratio_peak\": 10.05, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 0.379, \"ve_ratio_final_step\": 212500, \"civo_self_corrected\": true, \"civo_correction_delay_steps\": 130000, \"eval_final\": 20.86, \"eval_final_step\": 212500, \"eval_peak\": 20.86, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:30:00.000Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:30:00.000Z\", \"updated_at\": \"2026-05-23T08:48:40.404Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}, \"metrics\": {\"ve_ratio_peak\": 4.3, \"ve_ratio_peak_step\": 42500, \"ve_ratio_final\": 0.122, \"ve_ratio_final_step\": 212500, \"eval_final\": 45.31, \"eval_final_step\": 212500, \"eval_peak\": 45.31, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:48:40.404Z\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-23T07:45:47.966Z\", \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}, \"metrics\": {\"eval_final\": 29.458, \"eval_final_step\": 212500, \"eval_peak\": 39.873, \"eval_peak_step\": 162500, \"ve_ratio_final\": 0.133, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.67, \"ve_ratio_peak_step\": 52500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/checkpoint_202500.pt\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/metrics.jsonl\", \"completed_at\": \"2026-05-23T07:45:47.966Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-23T04:23:01.339Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}, \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.05, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222500, \"total_episodes\": 1112}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/checkpoint_202500.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/metrics.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:23:01.339Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:18:00.000Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.4, \"eval_final_step\": 302000, \"eval_peak\": 32.8, \"eval_peak_step\": 252000, \"ve_ratio_initial\": 46.3, \"ve_ratio_peak\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_initial\": 70.64, \"nve_peak_secondary\": 36.76, \"nve_final\": 2.75, \"total_steps\": 312000, \"civo_self_corrected\": false, \"civo_correction_pct\": 96, \"secondary_burst_step\": 152000, \"secondary_burst_nve\": 36.47, \"gate_collapsed\": true}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/checkpoint_300000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:18:00.000Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:03:31.428Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T18:56:07.648Z\"}, \"metrics\": {\"eval_final\": 144.22, \"eval_final_step\": 215000, \"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T19:01:30.894Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:41:53.934Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-22T10:42:06.985Z\", \"finished_at\": \"2026-05-22T18:27:00.000Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_044_gradient_stop_walker\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:03:45.656Z\", \"updated_at\": \"2026-05-22T16:08:22.684Z\", \"hypothesis\": \"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:04:32.082Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:04:36.793540+00:00\"}]}, \"metrics\": {\"eval_final\": 538.6, \"eval_peak\": 561.2, \"eval_peak_step\": 185000, \"eval_civo_trough\": 44.3, \"eval_civo_trough_step\": 95000, \"ve_ratio_peak\": 4.4, \"ve_ratio_peak_step\": 95000, \"ve_ratio_final\": 0.1, \"civo_onset_step\": 85000, \"civo_resolved_step\": 125000, \"civo_duration_steps\": 40000, \"total_steps\": 224000, \"pre_civo_peak\": 545.6, \"pre_civo_peak_step\": 75000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_044_gradient_stop_walker/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:08:22.684Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:41:43.036Z\", \"status\": \"DONE\", \"retry_count\": 0, \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"nve_peak\": 4.91, \"nve_peak_step\": 132000, \"nve_final\": 0.052, \"ve_ratio_final\": 0.052, \"total_steps\": 312000, \"civo_alerts\": 0, \"civo_self_corrected\": true, \"civo_correction_step\": 142000, \"eval_trajectory\": {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}, \"ve_ratio_trajectory\": {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/train.log\", \"completed_at\": \"2026-05-22T15:41:43.036Z\"}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:38:36.474Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"metrics\": {\"eval_final\": 673.73, \"eval_peak\": 673.73, \"eval_peak_step\": 215000, \"nve_peak\": 0.808, \"nve_peak_step\": 105000, \"nve_final\": 0.123, \"civo_alert\": false, \"total_steps\": 224000, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"note\": \"No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:38:36.474Z\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:29:26.337Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 612.45, \"eval_peak\": 682.38, \"eval_peak_step\": 205000, \"nve_peak\": 0.194, \"nve_final\": 0.051, \"civo_alert\": false, \"total_steps\": 224000, \"total_train_episodes\": 224}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:29:26.337Z\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:37:44.547Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:35:07.693Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:35:10.404Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:35:14.583680+00:00\"}]}}, \"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:04:44.715Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:00:53.721Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:00:58.393731+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_peak\": 761.1, \"eval_return_final\": 544, \"eval_return_peak_step\": 165000, \"nve_peak\": 1.5, \"nve_final\": 0.1, \"civo_prevented\": true, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": false, \"steps\": 215000, \"note\": \"CIVO prevented (NVE≤1.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2).\"}, \"completed_at\": \"2026-05-22T09:03:32.751Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"completed_at\": \"2026-05-22T02:35:33.617Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"completed_at\": \"2026-05-22T02:11:36.842Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.177Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"completed_at\": \"2026-05-21T19:45:52.311Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"completed_at\": \"2026-05-21T19:45:31.290Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T19:38:29.196731+00:00\"}]}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:38:24.346Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T16:11:39.130025+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T16:08:03.906985+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:07:58.973Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T07:48:17.595Z\", \"training_hours\": 8.33}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/\", \"completed_at\": \"2026-05-21T12:18:09.552Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"retry_count\": 0, \"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah\", \"completed_at\": \"2026-05-21T12:14:19.189109+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:46.032647+00:00\"}]}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:37.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"logdir/exp_033_wide_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T12:08:15.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:31.184962+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:26.400Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T03:46:14.882Z\", \"training_hours\": 8.27}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031b_tcn_pickcube_s0_sigma05/latest.pt\", \"completed_at\": \"2026-05-21T08:43:18.481253+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T08:41:51.310620+00:00\"}]}, \"failure_reason\": \"NVE late-stage decline is floor effect (value signal collapse), not CIVO recovery. Eval flat 25-29 throughout — agent never learned meaningful manipulation. Confirmed by Reviewer. TCN PickCube: 0/2 (σ=0.2 and σ=0.5 both failed).\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:41:45.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T07:47:55.131382+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T07:45:13.742811+00:00\"}]}, \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:45:08.395Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt\", \"completed_at\": \"2026-05-21T05:50:59.612299+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T05:48:16.069863+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"pid\": \"973387\", \"reproduce\": {\"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032b_dual_critic_walker_s1\\\"\", \"finished_at\": \"2026-05-21T05:48:11.173Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-20T23:22:55.338Z\", \"training_hours\": 6.42}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"completed_at\": \"2026-05-21T03:39:24.356918+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T03:32:52.751412+00:00\"}]}, \"failure_reason\": \"Sudden CIVO blowup: NVE appeared healthy at 95K (0.666, declining from 0.855@85K), then catastrophic spike to 3.0@105K. Eval collapsed 349.6→71.8. Late-stage NVE recovery to 0.4@215K = value adaptation (eval stayed at 104.5, never recovered). TCN σ=0.2 Walker: 2/4 seeds CIVO failure (s2: NVE 2.77, s3: NVE 3.0).\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T03:32:47.021Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031_tcn_pickcube_s0_sigma02\", \"completed_at\": \"2026-05-20T23:52:48.308Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T23:50:00.801433+00:00\"}]}, \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"reproduce\": {\"finished_at\": \"2026-05-20T23:49:56.649Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"completed_at\": \"2026-05-20T22:58:31.008151+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"failure_reason\": \"CIVO confirmed: NVE accelerated 1.01→1.65→2.77@105K (008d-like pattern), eval collapsed 177.7→32.0. Late-stage NVE decline to 1.06@155K = value adaptation to collapsed policy, NOT CIVO self-recovery (eval remained at 56.5, never recovered). Killed at 156K to free GPU for dual-critic experiment.\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"completed_at\": \"2026-05-20T22:34:07.916411+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T22:28:30.207347+00:00\"}]}, \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:28:26.022Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T19:30:34.687287+00:00\"}]}, \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T19:30:28.923Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"completed_at\": \"2026-05-20T16:47:18.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"completed_at\": \"2026-05-20T16:49:02.778Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"completed_at\": \"2026-05-20T12:38:02.085Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:19:31.331Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:10:00.827Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"completed_at\": \"2026-05-20T09:24:09.016Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"completed_at\": \"2026-05-20T08:31:12.389Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"completed_at\": \"2026-05-20T06:14:31.720Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"completed_at\": \"2026-05-20T03:14:06.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"completed_at\": \"2026-05-20T03:02:46.556Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"completed_at\": \"2026-05-20T03:02:43.170Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"completed_at\": \"2026-05-20T03:02:39.948Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"completed_at\": \"2026-05-20T03:02:36.670Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"completed_at\": \"2026-05-20T03:02:32.583Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T23:06:42.122Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"completed_at\": \"2026-05-19T21:23:44.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"completed_at\": \"2026-05-19T17:44:27.212Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T09:02:40.466Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"completed_at\": \"2026-05-19T09:00:10.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"completed_at\": \"2026-05-19T06:26:03.295Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:47.459Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:45.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"completed_at\": \"2026-05-19T00:13:55.909Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"completed_at\": \"2026-05-18T23:18:51.672Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"completed_at\": \"2026-05-18T21:40:10.763Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"completed_at\": \"2026-05-18T21:40:09.329Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"completed_at\": \"2026-05-18T18:41:05.369Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"completed_at\": \"2026-05-18T18:20:00.278Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"completed_at\": \"2026-05-18T18:19:58.491Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"completed_at\": \"2026-05-18T17:12:05.307Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"completed_at\": \"2026-05-18T11:33:57.033Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:31:45.212576+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:31:41.800Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"completed_at\": \"2026-05-18T11:24:41.197Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:20:58.896484+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:20:55.020Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/latest.pt\", \"completed_at\": \"2026-05-18T08:16:42.716Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:12:12.866455+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:12:09.402Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt\", \"completed_at\": \"2026-05-18T08:10:06.059Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008d_civo_trigger_s4\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/latest.pt\", \"completed_at\": \"2026-05-18T05:17:45.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/metrics.jsonl\", \"metrics\": {\"civo_alert_105K\": 1, \"civo_confirmed\": true, \"delta_ve_105K\": 2.05, \"eval_return_trajectory\": {\"105K\": 63.6, \"15K\": 171.4, \"25K\": 189.5, \"35K\": 153.8, \"45K\": 158.2, \"55K\": 229.3, \"5K\": 30.9, \"65K\": 333.6, \"75K\": 302.4, \"85K\": 383.3, \"95K\": 240.3}, \"final_eval_return_105K\": 63.6, \"final_step\": 112000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 383.3, \"peak_eval_step\": 85000, \"target_step\": 105000, \"value_mean_105K\": 192.65, \"value_mean_95K\": 235.42, \"ve_ratio_105K\": 3.03}, \"parent\": \"exp_008d_civo_trigger_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:17:45.132Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"completed_at\": \"2026-05-18T05:11:15.900Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/metrics.jsonl\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"completed_at\": \"2026-05-18T02:00:15.236Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-18T01:56:17.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:52:09.175571+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"pid\": \"706158\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-18T01:52:05.296Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T20:35:13.253Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T20:35:16.021173+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T22:57:54.400584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:57:48.608Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T22:49:15.021Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T22:45:35.442053+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"pid\": \"696201\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:45:32.093Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T19:28:08.484Z\", \"training_hours\": 3.29}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"completed_at\": \"2026-05-17T20:34:04.841Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T20:31:37.915652+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:31:34.777Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"completed_at\": \"2026-05-16T16:16:00.478Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T16:11:35.101384+00:00\"}]}, \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:11:32.766Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"completed_at\": \"2026-05-17T19:29:52.643Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T19:25:39.255677+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:25:34.295Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo_trigger/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:35:47.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"error_summary\": \"KeyError in dreamer.py:421 — configs[\\\"maniskill\\\"] not found. Config block missing from dreamer.py.\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T03:35:50.727034+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:49:42.379952+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17 04:01: Registry shows DONE(failed) from first attempt (KeyError transient). Actual state: RUNNING (PID 646809, step 8400+, started 11:39 UTC). Cron monitoring via submit_on_allocated tmux session. Will need manual status correction when cron detects completion.\"}}, \"failure_reason\": \"Traceback → Traceback (most recent call last): File \\\"/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\", line 421, in &lt;module> recursive_update(defaults, configs[name]) ~~~~~~~^^^^^^ KeyError: 'maniskill'\", \"gpu\": \"cuda:0\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019b_pickcube_civo_trigger.log\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger\\\"\", \"finished_at\": \"2026-05-17T14:49:39.328Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T03:25:03.091Z\", \"training_hours\": 11.41}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T14:01:23.413Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:56:29.726988+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"pid\": \"670554\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"finished_at\": \"2026-05-17T13:56:27.483Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"completed_at\": \"2026-05-17T07:44:38.596Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:44:42.334281+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T10:47:17.307752+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Config error: used --configs dmc_vision (CNN+image, wrong modality) instead of dmc_proprio, and --compile True (torch.compile inductor crash). Killed and resubmitting with correct config.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:47:12.534Z\"}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"completed_at\": \"2026-05-16T21:07:12.193Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"account\": \"root\", \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"completed_at\": \"2026-05-14T04:09:46.829Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"completed_at\": \"2026-05-13T09:58:31.673Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"completed_at\": \"2026-05-13T15:23:26.384Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_15K\": 153.86, \"fps\": 8.1, \"gate_dt_mean_15K\": 1, \"gate_scale_15K\": 0, \"step\": 20000}}}, \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"latest_metrics\": {\"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"checked_at\": \"2026-05-13\", \"eval_return\": 465.67, \"eval_return_trajectory\": {\"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"5K\": 31, \"65K\": 465.7}, \"fps\": 6.69, \"gap_vs_baseline\": -150.2, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_bonus\": 0.0865, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_scale\": 0.10004, \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"pid\": 51721, \"prev_eval_return\": 541.18, \"process_status\": \"running\", \"step\": 65000, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"uptime\": \"2h31m\"}, \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s3/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:24:26.004Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T03:18:40.430236+00:00\"}]}, \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:18:37.221Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018v2_full_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-16T17:24:44.481Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T17:17:46.576638+00:00\"}]}, \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:17:44.050Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_008d_subsample_on_h8\": {\"completed_at\": \"2026-05-14T04:50:52.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:04.661Z\"}, \"exp_018_full_sgs_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt\", \"completed_at\": \"2026-05-16T23:47:49.458Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"pid\": \"612876\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_009b_008d_walker_s2\": {\"account\": \"root\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 0 sustained nve>1.5x across 4 consecutive checkpoints and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 39.27, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0, \"ve_ratio\": 0}, {\"baseline_ve\": null, \"eval_return\": 144.31, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 4.47, \"ve_ratio\": 0.031}, {\"baseline_ve\": 0.087, \"eval_return\": 141.12, \"normalized_ve\": 2.05, \"step\": 25000, \"value_mean\": 25.14, \"ve_ratio\": 0.178}, {\"baseline_ve\": 0.241, \"eval_return\": 164.14, \"normalized_ve\": 1.24, \"step\": 35000, \"value_mean\": 49.02, \"ve_ratio\": 0.299}, {\"baseline_ve\": 0.331, \"eval_return\": 141.04, \"normalized_ve\": 1.62, \"step\": 45000, \"value_mean\": 75.59, \"ve_ratio\": 0.536}, {\"baseline_ve\": 0.404, \"eval_return\": 172.33, \"normalized_ve\": 1.41, \"step\": 55000, \"value_mean\": 98.28, \"ve_ratio\": 0.57}, {\"baseline_ve\": 0.563, \"eval_return\": 209.16, \"normalized_ve\": 0.94, \"step\": 65000, \"value_mean\": 110.91, \"ve_ratio\": 0.53}, {\"baseline_ve\": 0.719, \"eval_return\": 197.46, \"normalized_ve\": 0.66, \"step\": 75000, \"value_mean\": 93.49, \"ve_ratio\": 0.474}, {\"baseline_ve\": 0.701, \"eval_return\": 236.49, \"normalized_ve\": 0.51, \"step\": 85000, \"value_mean\": 83.86, \"ve_ratio\": 0.355}, {\"baseline_ve\": 0.632, \"eval_return\": 278.54, \"normalized_ve\": 0.43, \"step\": 95000, \"value_mean\": 75.72, \"ve_ratio\": 0.272}, {\"baseline_ve\": 0.656, \"eval_return\": 267.93, \"normalized_ve\": 0.38, \"step\": 105000, \"value_mean\": 67.27, \"ve_ratio\": 0.251}], \"target_steps\": 105000, \"trend\": \"Eval rising throughout: 39→144→141→164→141→172→209→197→236→279→268. Value peaks at 110.91@65K then self-corrects downward to 67.27@105K. v/e ratio peaks 0.57@55K then monotonically declines to 0.25@105K. NO delusional critic collapse — value self-corrects while eval improves.\", \"verdict\": \"NEGATIVE — hypothesis was to replicate collapse, collapse NOT reproduced. However, pathological nve>1.5x episode confirmed (2.05x@25K, 1.62x@45K), consistent with trained dt_emb inducing pathological overestimation. Self-correction to 0.38x@105K distinguishes from seed 0's sustained overestimation → collapse.\", \"vs_baseline_105K\": \"-70.8%\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"887053\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:34.989Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"completed_at\": \"2026-05-15T19:35:10.508Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"failure_reason\": \"Same hang as 016c — SummaryWriter.flush() deadlock after add_video with moviepy 2.x. try/except insufficient because flush() blocks on incomplete async video encode. Fix: Logger.video() → no-op.\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"completed_at\": \"2026-05-13T15:23:24.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"fps\": 8.3, \"step\": 245000, \"train_return_244K\": \"935-976\"}}}, \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"latest_metrics\": {\"checked_at\": \"2026-05-13\", \"eta_hours\": 1.8, \"eval_return\": 953.37, \"eval_step\": 445000, \"fps\": 7.29, \"pid\": 9409, \"prev_eval_return\": 964.96, \"process_status\": \"running\", \"step\": 452000, \"steps_remaining\": 48000, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"uptime\": \"16h35m\"}, \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"completed_at\": \"2026-05-17T00:24:10.180Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_s3_no_dt_embed_walker/checkpoint.ckpt\", \"completed_at\": \"2026-05-16T20:09:51.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"601233\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"completed_at\": \"2026-05-16T19:43:57.604Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T19:40:49.938571+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"pid\": \"596344\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-16T19:40:47.795Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T13:43:00.745Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"pid\": \"586751\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T12:00:04.473Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T12:43:09.226Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T12:40:17.132664+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_walker_s1.log\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"pid\": \"577467\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_018_full_sgs_walker_s1 --steps 105000 --full_sgs True --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T12:40:14.687Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T09:50:18.238Z\", \"training_hours\": 2.83}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"pid\": \"536890\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"training_hours\": 13.18}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T12:10:01.788Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:10:04.203907+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:24:17.652463+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T09:48:44.475703+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T09:48:42.388Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T12:06:19.592Z\", \"training_hours\": 21.71}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"completed_at\": \"2026-05-16T04:46:30.361Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"completed_at\": \"2026-05-16T01:39:17.916Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T22:31:16.457Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:26:05.863Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer). EGL fix confirmed working: eval at step 5000 completed successfully (eval_return=31.0). OOM occurred during training loop startup after eval. Likely system RAM OOM (replay buffer + model + eval concurrent memory peak).\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:08:12.013Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:08:15.731787+00:00\"}]}, \"failure_reason\": \"误杀: Director 基于 Reviewer 错误诊断下令 kill（认为 zombie PID 522009 导致 eval deadlock），但日志证明 EGL fix (MUJOCO_EGL_DEVICE_ID=1) 已生效，eval 正常运行中 (iter=500, t=95.9s)。EGL fix 确认有效。\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009h_008f_walker_s0.log\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"522450\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T19:08:09.836Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:10:52.235Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:10:53.928926+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 524244, \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T19:10:51.013Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:59:55.315Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:59:59.820061+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM). Root cause: MUJOCO_GL=egl defaults to EGL device 0 while CUDA_VISIBLE_DEVICES=1 binds CUDA to GPU 1, causing cross-GPU context conflict and eval deadlock at step 5000.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009g_008f_walker_s0.log\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"517413\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:59:53.840Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_009f_008f_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:46:03.293Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:46:05.155411+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:52:15.790170+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Seed duplication: 009f used seed=1 same as parent 008f, producing deterministic repeat (prefill returns identical). Killed by Director order.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"516110\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:52:12.322Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T18:44:58.143Z\", \"training_hours\": 0.12}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:54:04.806Z\"}, \"exp_016_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:43:52.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:43:57.605618+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"514417\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T18:43:51.025Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"completed_at\": \"2026-05-15T12:12:25.846Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T18:27:09.189680+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次提交。首次失败原因: --device cuda:1 但 CUDA_VISIBLE_DEVICES=1 后进程内只有 cuda:0。已修正为 --device cuda:0。PID 144831, 从头开始 (step=0)。预计 ~5h 完成 105K steps。\"}}, \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:27:07.138Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"completed_at\": \"2026-05-15T11:54:55.153Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"pid\": 122271, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009e_008d_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T11:26:52.478Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 1 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/metrics.jsonl\", \"metrics\": {\"actor_loss_sign_flip\": 85000, \"baseline_105K\": 915.67, \"collapse_rate_note\": \"Independent rate = 1/2 (seed 1 collapsed, seed 2 self-corrected). 008d and 009e share seed=1, count as one independent observation.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0, \"ve_ratio\": 0}, {\"eval_return\": 153.7, \"step\": 15000, \"value_mean\": 3.4, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 167.2, \"normalized_ve\": 1.78, \"step\": 25000, \"value_mean\": 25.9, \"ve_ratio\": 0.155}, {\"baseline_ve\": 0.241, \"eval_return\": 146.3, \"normalized_ve\": 1.71, \"step\": 35000, \"value_mean\": 60.2, \"ve_ratio\": 0.411}, {\"baseline_ve\": 0.331, \"eval_return\": 140.8, \"normalized_ve\": 2.09, \"step\": 45000, \"value_mean\": 97.5, \"ve_ratio\": 0.693}, {\"baseline_ve\": 0.404, \"eval_return\": 82.7, \"normalized_ve\": 4.12, \"step\": 55000, \"value_mean\": 137.9, \"ve_ratio\": 1.666}, {\"baseline_ve\": 0.563, \"eval_return\": 250, \"normalized_ve\": 1.23, \"step\": 65000, \"value_mean\": 173.8, \"ve_ratio\": 0.695}, {\"baseline_ve\": 0.719, \"eval_return\": 178.1, \"normalized_ve\": 1.48, \"step\": 75000, \"value_mean\": 189.9, \"ve_ratio\": 1.066}, {\"baseline_ve\": 0.701, \"eval_return\": 201.93, \"normalized_ve\": 1.15, \"step\": 85000, \"value_mean\": 163.08, \"ve_ratio\": 0.808}, {\"baseline_ve\": 0.632, \"eval_return\": 132.79, \"normalized_ve\": 1.73, \"step\": 95000, \"value_mean\": 144.82, \"ve_ratio\": 1.091}, {\"baseline_ve\": 0.656, \"eval_return\": 131.08, \"normalized_ve\": 1.57, \"step\": 105000, \"value_mean\": 135.37, \"ve_ratio\": 1.033}], \"final_eval_return\": 131.08, \"final_nve\": 1.57, \"final_value_mean\": 135.37, \"final_ve_ratio\": 1.033, \"peak_nve\": 4.12, \"peak_nve_step\": 55000, \"target_steps\": 105000, \"vs_baseline_105K\": \"-85.7%\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 119108, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:31:04.722Z\"}, \"exp_009a_baseline_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:33:12.892Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"pid\": \"142508\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:08.969Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:00:20.816Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"43437\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"898127\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"140980\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"training_hours\": 6.95}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"account\": \"root\", \"completed_at\": \"2026-05-14T01:13:11.533Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"extra\": {\"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\", \"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\"}, \"gpu\": \"cuda:0\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"latest_metrics\": {\"checked_at\": \"2026-05-14\", \"eval_return\": 485.3, \"eval_return_trajectory\": {\"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3, \"5K\": 31}, \"eval_step\": 35000, \"fps\": 6.6, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"pid\": 85029, \"prev_eval_return\": 321.4, \"process_status\": \"running\", \"step\": 36000}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"pid\": \"85029\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-13T22:12:00.446Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"completed_at\": \"2026-05-13T04:50:14.987Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\", \"retry_count\": 0, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 132, \"total\": 132, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8963}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0154i1YWWtDkVqEnubiGGejZ`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"NVE\\|Normalized Value Error\\|normalized.*value.*error\\|ve_ratio.*baseline\\|baseline.*ve_ratio\\|NVE.*=\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d9e4e9fd-416d-4cc3-b947-262f9f5891fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133ShyuDamDTCz81dSiVeX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1435
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


### Tool result

_source line 15 · 2026-05-24T01:50:41.178Z_

<details><summary>↩ Tool result · `toolu_0154i1YWWtDkVqEnubiGGejZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "7c3b5e37-d405-4cc6-ab88-39a7382bbd8c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
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
The SSH command was blocked because of the pipe character. Let me also search the registry for Walker baseline experiments. Let me also search on the server for NVE definition without pipe characters. Let me also search for exp_057 and exp_042, exp_047 in the registry.

Let me first look at the paper_framing.md content I got. I can see that NVE is defined as the "normalized v/e" or "v/e overshoot ratio" = experiment v/e / baseline v/e at same training step. The threshold is 1.5x.
 
Now I understand the NVE calculation from the paper framing—it's the ratio of experiment v/e to baseline v/e at the same training step, with anything above 1.5x flagged as pathological. I need to find the baseline Walker experiments and pull their v/e ratios at the specific checkpoints for each experiment, then locate the details for exp_057, exp_042, and exp_047 in the registry.

The registry search is too broad, so I'm narrowing down to specific experiments. Looking at the memory notes, I can see the frozen dt_emb experiments are already documented: exp_042 has a v/e peak of 0.19, exp_047 shows 1.71 at 95K steps (transient, dropping to 0.56), and exp_057 peaks at 1.283 at 115K steps. These NVE values in memory.md appear to be the actual diagnostic metrics I need to verify.

Now I'm checking whether the NVE values recorded in memory match what the user is reporting as ve_ratio_peak. The user lists exp_042 with ve_ratio_peak = 0.19, which matches the NVE=0.19 in memory, but I need to clarify if these are the same metric or if NVE is a normalized version of ve_ratio that depends on a baseline ratio at that timestep.

Looking at the concrete examples in paper_framing.md, I can see how NVE is calculated: it's the experiment's v/e ratio divided by the baseline v/e ratio at the same evaluation count. For exp_008a at 55K, the v/e of 37.6% divided by the baseline's 40.4% gives 0.93x, which matches the recorded NVE. So now I need to figure out what the baseline ve_ratio was for exp_057 to properly interpret the reported values.

The reviewer indicates the baseline ve_ratio at 115K is around 0.65, which would make exp_057's NVE approximately 1.97 given its peak of 1.283. But I notice exp_057 isn't listed in memory.md alongside the other Walker frozen experiments like exp_042, exp_015b, and exp_047, so I'm trying to determine whether this is a new experiment or if there's something I'm missing about how the NVE values were originally calculated.

Looking at exp_047 as a reference point—memory shows NVE=1.71 and the user mentions ve_ratio_peak=1.71 at 95K, which suggests these might be the same metric rather than NVE being a normalized ratio. But that doesn't quite align with the formula NVE = ve_ratio / baseline_ve_ratio unless the baseline happens to be 1.0, which seems unlikely given the baseline data showing values like 40.4% at 55K and 65.6% at 105K.

Now looking at exp_057 where the user says ve_ratio_peak = 1.283@115K—if this were a percentage like the paper's format, 1.283% wouldn't make sense, so maybe ve_ratio is actually being expressed as a decimal ratio rather than a percentage, which would explain why the values don't match my percentage-based calculations. I'm realizing the ve_ratio values in the experiments might be a completely different metric than what I'm calculating from the paper framing. Rather than keep guessing at the definitions, I should pull the actual experimental data from the registry to see what these numbers really represent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "4829bbf9-e08b-412e-8166-17fbfa280800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrigbxvSan2iYAPNuMzjgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23829,
      "cache_read_input_tokens": 25523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23829
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

_source line 17_

Registry 太大了，让我搜索关键实验。同时在服务器上搜索 NVE 定义和提取数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "679c6d6b-8e9f-4291-9732-2d25392862c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrigbxvSan2iYAPNuMzjgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23829,
      "cache_read_input_tokens": 25523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23829
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_016uE2BFCMqB6UrPYiMq1M7x`</summary>

```json
{
  "command": "grep -n \"exp_057\\|exp_042\\|exp_047\\|exp_009a\\|exp_001\" /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt | head -50",
  "description": "Search registry output for relevant experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "a7cabde3-065f-4062-b05b-969f83ecf979",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrigbxvSan2iYAPNuMzjgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23829,
      "cache_read_input_tokens": 25523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23829
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

_source line 19 · 2026-05-24T01:51:29.075Z_

<details><summary>↩ Tool result · `toolu_016uE2BFCMqB6UrPYiMq1M7x`</summary>

```text
&lt;persisted-output>
Output too large (297.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/bpu5q1n3u.txt

Preview (first 2KB):
1:{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:30:00.000Z\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. ve_ratio 全程极低 (peak 0.231). Cheetah frozen n=2: s0=1.35, s1=0.23 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DO
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "b0e11388-b3db-4108-87b5-e7a61c8d4cce",
  "tool_use_result": {
    "stdout": "1:{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_058_frozen_dt_emb_cheetah_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T18:10:49.773Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:30:00.000Z\\\", \\\"hypothesis\\\": \\\"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\\\", \\\"parent\\\": \\\"exp_046_frozen_dt_emb_cheetah\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 164830, \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Cheetah s1)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T00:30:00.000Z\\\", \\\"metrics\\\": {\\\"total_steps\\\": 224000, \\\"ve_ratio_peak\\\": 0.231, \\\"ve_ratio_peak_step\\\": 45000, \\\"ve_ratio_final\\\": 0.107, \\\"ve_ratio_final_step\\\": 215000, \\\"eval_return_final\\\": 80.46, \\\"eval_return_final_step\\\": 215000, \\\"eval_return_peak\\\": 191.74, \\\"eval_return_peak_step\\\": 25000, \\\"nve_classification\\\": \\\"no_civo\\\", \\\"note\\\": \\\"Cheetah frozen s1. ve_ratio 全程极低 (peak 0.231). Cheetah frozen n=2: s0=1.35, s1=0.23 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\\\"}}, \\\"exp_056_peginsertion_frozen_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T09:02:23.683Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:00:00.000Z\\\", \\\"hypothesis\\\": \\\"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\\\", \\\"parent\\\": \\\"exp_053_peginsertion_frozen_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 346430, \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_056_peginsertion_frozen_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-24T00:00:00.000Z\\\", \\\"metrics\\\": {\\\"total_steps\\\": 222500, \\\"ve_ratio_peak\\\": 11.321, \\\"ve_ratio_peak_step\\\": 82500, \\\"ve_ratio_final\\\": 1.193, \\\"ve_ratio_final_step\\\": 212500, \\\"eval_return_final\\\": 4.37, \\\"eval_return_final_step\\\": 212500, \\\"eval_return_peak\\\": 24.42, \\\"eval_return_peak_step\\\": 132500, \\\"nve_classification\\\": \\\"burst\\\", \\\"note\\\": \\\"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\\\", \\\"ve_ratio_trajectory\\\": {\\\"12500\\\": 0.316, \\\"22500\\\": 0.975, \\\"32500\\\": 1.839, \\\"42500\\\": 1.966, \\\"52500\\\": 5.422, \\\"62500\\\": 4.047, \\\"72500\\\": 8.408, \\\"82500\\\": 11.321, \\\"92500\\\": 3.724, \\\"102500\\\": 3.034, \\\"112500\\\": 2.204, \\\"122500\\\": 2.425, \\\"132500\\\": 0.842, \\\"142500\\\": 2.194, \\\"152500\\\": 2.203, \\\"162500\\\": 0.651, \\\"172500\\\": 1.085, \\\"182500\\\": 1.07, \\\"192500\\\": 0.467, \\\"202500\\\": 0.708, \\\"212500\\\": 1.193}}}, \\\"exp_055_peginsertion_civo_trigger_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T08:50:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:38:30.000Z\\\", \\\"hypothesis\\\": \\\"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\\\", \\\"parent\\\": \\\"exp_050_peginsertion_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 345223, \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\\\"}, \\\"ve_ratio_peak\\\": \\\"3.08@92500\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T23:38:25.428Z\\\", \\\"metrics\\\": {\\\"total_steps\\\": 222400, \\\"ve_ratio_peak\\\": 3.08, \\\"ve_ratio_peak_step\\\": 92500, \\\"ve_ratio_final\\\": 0.498, \\\"ve_ratio_final_step\\\": 212500, \\\"eval_return_final\\\": 11.44, \\\"eval_return_final_step\\\": 212500, \\\"eval_return_peak\\\": 24.05, \\\"eval_return_peak_step\\\": 112500, \\\"nve_classification\\\": \\\"transient\\\", \\\"civo_triggered\\\": true, \\\"civo_self_corrected\\\": \\\"partial\\\", \\\"note\\\": \\\"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\\\", \\\"ve_ratio_trajectory\\\": {\\\"12500\\\": 0.19, \\\"22500\\\": 0.81, \\\"32500\\\": 1.35, \\\"42500\\\": 2.0, \\\"52500\\\": 2.39, \\\"62500\\\": 2.85, \\\"72500\\\": 2.28, \\\"82500\\\": 2.48, \\\"92500\\\": 3.08, \\\"102500\\\": 2.51, \\\"112500\\\": 0.91, \\\"122500\\\": 1.21, \\\"132500\\\": 1.36, \\\"142500\\\": 0.75, \\\"152500\\\": 0.55, \\\"162500\\\": 1.17, \\\"172500\\\": 0.96, \\\"182500\\\": 0.94, \\\"192500\\\": 0.9, \\\"202500\\\": 0.73, \\\"212500\\\": 0.5}}, \\\"checkpoint_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1/checkpoint_222500.pt\\\"}, \\\"exp_057_frozen_dt_emb_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T15:25:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:30:00.000Z\\\", \\\"hypothesis\\\": \\\"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 157775, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Walker s2)\\\", \\\"seed\\\": 2, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\\\"}, \\\"completed_at\\\": \\\"2026-05-23T23:30:00.000Z\\\", \\\"metrics\\\": {\\\"total_steps\\\": 225000, \\\"ve_ratio_peak\\\": 1.283, \\\"ve_ratio_peak_step\\\": 115000, \\\"ve_ratio_final\\\": 0.177, \\\"ve_ratio_final_step\\\": 215000, \\\"nve_classification\\\": \\\"no_civo\\\", \\\"note\\\": \\\"Walker frozen s2. Peak transient at 115K, self-corrected. Walker frozen n=3 complete: s0=0.19, s1=1.71, s2=1.28 — all clean/transient.\\\"}}, \\\"exp_054_pickcube_frozen_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T07:47:24.310Z\\\", \\\"updated_at\\\": \\\"2026-05-23T18:08:00.000Z\\\", \\\"hypothesis\\\": \\\"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 133956, \\\"data_path\\\": \\\"ManiSkill PickCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PickCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\\\"}, \\\"ve_ratio_peak\\\": \\\"8.81@62500\\\", \\\"eval_final\\\": 10.26, \\\"eval_final_step\\\": 212500, \\\"ve_ratio_final\\\": 0.583, \\\"ve_ratio_final_step\\\": 212500}, \\\"exp_053_peginsertion_frozen_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T04:23:10.381Z\\\", \\\"updated_at\\\": \\\"2026-05-23T15:00:00.000Z\\\", \\\"hypothesis\\\": \\\"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\\\", \\\"parent\\\": \\\"exp_050_peginsertion_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 123495, \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\\\"}, \\\"ve_ratio_peak\\\": \\\"8.10@52500\\\", \\\"eval_final\\\": 5.89, \\\"ve_ratio_final\\\": 0.202, \\\"ve_ratio_final_step\\\": 212500}, \\\"exp_050_peginsertion_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T18:38:33.441Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:51:11.592Z\\\", \\\"hypothesis\\\": \\\"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\\\", \\\"spec\\\": {\\\"command\\\": \\\"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\\\", \\\"seed\\\": 0, \\\"pid\\\": 304736, \\\"gpu_ids\\\": [0], \\\"log_path\\\": \\\"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_050_peginsertion_civo_trigger_s0\\\"}, \\\"metrics\\\": {\\\"ve_ratio_peak\\\": 10.05, \\\"ve_ratio_peak_step\\\": 82500, \\\"ve_ratio_final\\\": 0.379, \\\"ve_ratio_final_step\\\": 212500, \\\"civo_self_corrected\\\": true, \\\"civo_correction_delay_steps\\\": 130000, \\\"eval_final\\\": 20.86, \\\"eval_final_step\\\": 212500, \\\"eval_peak\\\": 20.86, \\\"eval_peak_step\\\": 212500, \\\"total_steps\\\": 222400}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T08:30:00.000Z\\\"}, \\\"exp_051_stackcube_frozen_dt_emb_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T19:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-23T08:48:40.404Z\\\", \\\"hypothesis\\\": \\\"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\\\", \\\"parent\\\": \\\"exp_049_stackcube_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 305974, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\\\"}, \\\"metrics\\\": {\\\"ve_ratio_peak\\\": 4.3, \\\"ve_ratio_peak_step\\\": 42500, \\\"ve_ratio_final\\\": 0.122, \\\"ve_ratio_final_step\\\": 212500, \\\"eval_final\\\": 45.31, \\\"eval_final_step\\\": 212500, \\\"eval_peak\\\": 45.31, \\\"eval_peak_step\\\": 212500, \\\"total_steps\\\": 222400}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T08:48:40.404Z\\\"}, \\\"exp_052_stackcube_civo_trigger_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T21:26:49.825Z\\\", \\\"updated_at\\\": \\\"2026-05-23T07:45:47.966Z\\\", \\\"hypothesis\\\": \\\"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\\\", \\\"parent\\\": \\\"exp_049_stackcube_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 103781, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_052_stackcube_civo_trigger_s1/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 29.458, \\\"eval_final_step\\\": 212500, \\\"eval_peak\\\": 39.873, \\\"eval_peak_step\\\": 162500, \\\"ve_ratio_final\\\": 0.133, \\\"ve_ratio_final_step\\\": 212500, \\\"ve_ratio_peak\\\": 4.67, \\\"ve_ratio_peak_step\\\": 52500, \\\"total_steps\\\": 222400}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_052_stackcube_civo_trigger_s1/checkpoint_202500.pt\\\", \\\"log_path\\\": \\\"logdir/exp_052_stackcube_civo_trigger_s1/metrics.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-23T07:45:47.966Z\\\"}, \\\"exp_049_stackcube_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T17:14:38.578Z\\\", \\\"updated_at\\\": \\\"2026-05-23T04:23:01.339Z\\\", \\\"hypothesis\\\": \\\"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\\\", \\\"parent\\\": \\\"exp_048_stackcube_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 91395, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_049_stackcube_civo_trigger_s0/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 34.88, \\\"eval_final_step\\\": 212500, \\\"eval_peak\\\": 35.89, \\\"eval_peak_step\\\": 182500, \\\"ve_ratio_final\\\": 0.186, \\\"ve_ratio_final_step\\\": 212500, \\\"ve_ratio_peak\\\": 5.05, \\\"ve_ratio_peak_step\\\": 42500, \\\"total_steps\\\": 222500, \\\"total_episodes\\\": 1112}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/checkpoint_202500.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/metrics.jsonl\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T04:23:01.339Z\\\"}, \\\"exp_048_cheetah_civo_extension\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:30:40.050Z\\\", \\\"updated_at\\\": \\\"2026-05-22T21:18:00.000Z\\\", \\\"hypothesis\\\": \\\"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger_s0\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 88654, \\\"data_path\\\": \\\"dmc_cheetah_run (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/train.log\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 23.4, \\\"eval_final_step\\\": 302000, \\\"eval_peak\\\": 32.8, \\\"eval_peak_step\\\": 252000, \\\"ve_ratio_initial\\\": 46.3, \\\"ve_ratio_peak\\\": 24.112, \\\"ve_ratio_peak_step\\\": 162000, \\\"ve_ratio_final\\\": 1.803, \\\"nve_initial\\\": 70.64, \\\"nve_peak_secondary\\\": 36.76, \\\"nve_final\\\": 2.75, \\\"total_steps\\\": 312000, \\\"civo_self_corrected\\\": false, \\\"civo_correction_pct\\\": 96, \\\"secondary_burst_step\\\": 152000, \\\"secondary_burst_nve\\\": 36.47, \\\"gate_collapsed\\\": true}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/checkpoint_300000.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T21:18:00.000Z\\\"}, \\\"exp_047_frozen_dt_emb_walker_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T11:03:31.428Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:01:30.894Z\\\", \\\"hypothesis\\\": \\\"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"dreamer_gated_frozen_dt_emb\\\", \\\"seed\\\": 1, \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T18:56:07.648Z\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 144.22, \\\"eval_final_step\\\": 215000, \\\"eval_peak\\\": 408.79, \\\"eval_peak_step\\\": 125000, \\\"ve_ratio_peak\\\": 1.099, \\\"ve_ratio_peak_step\\\": 75000, \\\"ve_ratio_final\\\": 0.277, \\\"nve_peak\\\": 1.71, \\\"nve_peak_step\\\": 95000, \\\"nve_final_105k\\\": 0.56, \\\"total_steps\\\": 225000}, \\\"checkpoint_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\\\", \\\"log_path\\\": \\\"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T19:01:30.894Z\\\"}, \\\"exp_046_frozen_dt_emb_cheetah\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:41:53.934Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:32:34.105Z\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"hypothesis\\\": \\\"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\\\", \\\"parent\\\": \\\"exp_042_frozen_dt_emb_walker\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-22T10:42:06.985Z\\\", \\\"finished_at\\\": \\\"2026-05-22T18:27:00.000Z\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"seed\\\": 0, \\\"model_name\\\": \\\"dreamerv3-cheetah-frozen-dt-emb\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 210000, \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\"}, \\\"metrics\\\": {\\\"eval_final\\\": 150.5, \\\"eval_peak\\\": 207.4, \\\"eval_peak_step\\\": 145000, \\\"ve_ratio_peak\\\": 0.4, \\\"ve_ratio_final\\\": 0.1, \\\"nve_peak\\\": 1.35, \\\"nve_peak_step\\\": 45000, \\\"nve_final\\\": 0.17, \\\"total_steps\\\": 224000, \\\"civo_alert_count\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T18:31:00.933Z\\\"}, \\\"exp_044_gradient_stop_walker\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T09:03:45.656Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:08:22.684Z\\\", \\\"hypothesis\\\": \\\"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"68371\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T09:08:10.295Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"DMC Walker Walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 + reward_dt_emb_detach\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\", \\\"wall_clock_seconds\\\": 25212.4, \\\"gpu_hours\\\": 7.0}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T16:04:32.082Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T16:04:36.793540+00:00\\\"}]}, \\\"metrics\\\": {\\\"eval_final\\\": 538.6, \\\"eval_peak\\\": 561.2, \\\"eval_peak_step\\\": 185000, \\\"eval_civo_trough\\\": 44.3, \\\"eval_civo_trough_step\\\": 95000, \\\"ve_ratio_peak\\\": 4.4, \\\"ve_ratio_peak_step\\\": 95000, \\\"ve_ratio_final\\\": 0.1, \\\"civo_onset_step\\\": 85000, \\\"civo_resolved_step\\\": 125000, \\\"civo_duration_steps\\\": 40000, \\\"total_steps\\\": 224000, \\\"pre_civo_peak\\\": 545.6, \\\"pre_civo_peak_step\\\": 75000}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_044_gradient_stop_walker/latest.pt\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T16:08:22.684Z\\\"}, \\\"exp_045_treatment_extension_008d_s3\\\": {\\\"created_at\\\": \\\"2026-05-22T09:40:52.894Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:41:43.036Z\\\", \\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"hypothesis\\\": \\\"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\\\", \\\"parent\\\": \\\"exp_008d_civo_trigger_s3\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": \\\"70945\\\", \\\"data_path\\\": \\\"dmc_walker_walk (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config)\\\", \\\"seed\\\": 3, \\\"checkpoint_source\\\": \\\"exp_008d_civo_trigger_s3/latest.pt (step 112K)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval, same as training env)\\\", \\\"log_path\\\": \\\"logdir/exp_045_treatment_extension_008d_s3/train.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_final\\\": 867.6, \\\"eval_peak\\\": 869.7, \\\"eval_peak_step\\\": 242000, \\\"nve_peak\\\": 4.91, \\\"nve_peak_step\\\": 132000, \\\"nve_final\\\": 0.052, \\\"ve_ratio_final\\\": 0.052, \\\"total_steps\\\": 312000, \\\"civo_alerts\\\": 0, \\\"civo_self_corrected\\\": true, \\\"civo_correction_step\\\": 142000, \\\"eval_trajectory\\\": {\\\"112000\\\": 58.5, \\\"122000\\\": 41.8, \\\"132000\\\": 35.1, \\\"142000\\\": 350.2, \\\"152000\\\": 646.4, \\\"162000\\\": 482.3, \\\"172000\\\": 600.4, \\\"182000\\\": 600.5, \\\"192000\\\": 699.5, \\\"202000\\\": 684.3, \\\"212000\\\": 758.6, \\\"222000\\\": 744.6, \\\"232000\\\": 745.4, \\\"242000\\\": 869.7, \\\"252000\\\": 721.6, \\\"262000\\\": 820.6, \\\"272000\\\": 716.2, \\\"282000\\\": 755.6, \\\"292000\\\": 843, \\\"302",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/bpu5q1n3u.txt",
    "persistedOutputSize": 304826
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015zegQrYurSWS5eLcncZJi8`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"NVE\\|Normalized Value Error\\|normalized.*value.*error\\|ve_ratio.*baseline\\|nve\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "9cc3b7e7-21be-41ee-bd4f-45fdd4fdea23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrigbxvSan2iYAPNuMzjgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23829,
      "cache_read_input_tokens": 25523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23829
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

_source line 21 · 2026-05-24T01:51:31.488Z_

<details><summary>↩ Tool result · `toolu_015zegQrYurSWS5eLcncZJi8`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "4b68f611-9b4d-49ab-b5bb-8523077fb74d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DdS9ENMTXC2KTt8xoj2tNk`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls -d /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057* /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042* /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_047* /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a* /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "7bbd912a-3dd3-46a6-a66f-5b83e24bd149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrigbxvSan2iYAPNuMzjgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23829,
      "cache_read_input_tokens": 25523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23829
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

_source line 23 · 2026-05-24T01:51:34.021Z_

<details><summary>↩ Tool result · `toolu_01DdS9ENMTXC2KTt8xoj2tNk`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3.log\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4.log\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042*': No such file or directory\\nls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_047*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.15}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "07591e4a-cec3-4cfa-8fff-d0a0b5679994",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3.log\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4.log\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2\\\\n\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042*': No such file or directory\\\\nls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_047*': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.15}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3.log\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4.log\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042*': No such file or directory\\nls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_047*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.15}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Good. I found the directories:
- exp_057_frozen_dt_emb_walker_s2
- exp_009a_baseline_walker_s2
- exp_001_baseline_s2, s3, s4

exp_042 and exp_047 are not on the server. Let me now:

1. Search for NVE definition in paper tex files (need to fix the grep without pipe)
2. Extract ve_ratio data from exp_057 and baseline at relevant timesteps
3. Search the registry for exp_057, exp_042, exp_047 details

Let me also search the registry output file for these experiment IDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "21c0eb50-1033-484c-b2df-b228f29e80b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbAW4NoNEt1Q9cGTygyqEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4275
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01XTxAAaoj6RAvu2RciZooPZ`</summary>

```json
{
  "command": "grep -o '\"exp_057[^\"]*\"' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt | head -5",
  "description": "Find exp_057 entry in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "a72a1699-31b1-46aa-854b-ca5af8df26f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbAW4NoNEt1Q9cGTygyqEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4275
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

_source line 26 · 2026-05-24T01:51:44.075Z_

<details><summary>↩ Tool result · `toolu_01XTxAAaoj6RAvu2RciZooPZ`</summary>

```text
"exp_057_frozen_dt_emb_walker_s2\"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "39a6e462-0419-47a8-951d-41b8de13acfa",
  "tool_use_result": {
    "stdout": "\"exp_057_frozen_dt_emb_walker_s2\\\"",
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_0153uNfKEZuZi31xhZL4nxmX`</summary>

```json
{
  "command": "grep -A 100 '\"exp_057_frozen_dt_emb_walker_s2\"' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt | head -60",
  "description": "Get exp_057 registry details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "eb427d59-60e1-49f5-8695-43ba2b9c8e2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbAW4NoNEt1Q9cGTygyqEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4275
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

_source line 28 · 2026-05-24T01:51:45.449Z_

<details><summary>↩ Tool result · `toolu_0153uNfKEZuZi31xhZL4nxmX`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "f188159f-274e-47f0-82a8-cab58e50fe44",
  "tool_use_result": {
    "stdout": "",
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01UdX4vvA4YTg1qhmjZHw4kJ`</summary>

```json
{
  "command": "grep -A 80 '\"exp_042_frozen_dt_emb_walker_s0\"' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt | head -60",
  "description": "Get exp_042 registry details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "2370ff95-e3b4-479e-a267-95dbc93dfb7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbAW4NoNEt1Q9cGTygyqEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4275
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

_source line 30 · 2026-05-24T01:51:47.479Z_

<details><summary>↩ Tool result · `toolu_01UdX4vvA4YTg1qhmjZHw4kJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "e4888a04-4143-4962-b621-a02678d1d8ba",
  "tool_use_result": {
    "stdout": "",
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_019tjA6sTRrrcxgvtwKrvtKu`</summary>

```json
{
  "command": "grep -A 80 '\"exp_047_frozen_dt_emb_walker_s1\"' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt | head -60",
  "description": "Get exp_047 registry details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "3c1a5bb3-2cc9-4055-8a8a-b27ce5b91167",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbAW4NoNEt1Q9cGTygyqEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4275
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

_source line 32 · 2026-05-24T01:51:48.787Z_

<details><summary>↩ Tool result · `toolu_019tjA6sTRrrcxgvtwKrvtKu`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "13137005-c18f-4523-bfd8-c7c6194a3885",
  "tool_use_result": {
    "stdout": "",
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

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The grep -A approach didn't work because the file is a single JSON line. Let me use jq or python to parse it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "4e4683d4-d75e-4148-84b0-735ddaa27952",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ls55u35v72WGxfFveLRXKh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 53627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

<details open><summary>🔧 Tool call — Bash · `toolu_01U7WDpBKcn3iX7PB7vfaz5U`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/mcp-agent-ml-research-read_registry-1779587440084.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nfor eid in ['exp_057_frozen_dt_emb_walker_s2', 'exp_042_frozen_dt_emb_walker_s0', 'exp_047_frozen_dt_emb_walker_s1', 'exp_009a_baseline_walker_s2', 'exp_001_baseline']:\n    matches = [k for k in exps if k.startswith(eid.split('_')[0] + '_' + eid.split('_')[1]) or k == eid]\n    for m in matches:\n        if m in exps:\n            e = exps[m]\n            print(f'=== {m} ===')\n            print(json.dumps(e.get('metrics', {}), indent=2))\n            print()\n\n# Also search for any baseline walker experiments\nfor k in exps:\n    if 'baseline' in k.lower() and 'walker' in k.lower():\n        print(f'=== {k} ===')\n        print(json.dumps(exps[k].get('metrics', {}), indent=2))\n        print()\n    elif k.startswith('exp_001'):\n        print(f'=== {k} (status={exps[k][\\\"status\\\"]}) ===')\n        if exps[k].get('metrics'):\n            print(json.dumps(exps[k].get('metrics', {}), indent=2))\n        print()\n\"\n",
  "description": "Parse registry JSON for relevant experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "0f756aa9-3044-4a21-8ff3-e28c32c8e1b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ls55u35v72WGxfFveLRXKh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 53627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 35 · 2026-05-24T01:51:58.004Z_

<details><summary>↩ Tool result · `toolu_01U7WDpBKcn3iX7PB7vfaz5U`</summary>

```text
=== exp_057_frozen_dt_emb_walker_s2 ===
{
  "total_steps": 225000,
  "ve_ratio_peak": 1.283,
  "ve_ratio_peak_step": 115000,
  "ve_ratio_final": 0.177,
  "ve_ratio_final_step": 215000,
  "nve_classification": "no_civo",
  "note": "Walker frozen s2. Peak transient at 115K, self-corrected. Walker frozen n=3 complete: s0=0.19, s1=1.71, s2=1.28 \u2014 all clean/transient."
}

=== exp_042_frozen_dt_emb_walker ===
{
  "eval_final": 612.45,
  "eval_peak": 682.38,
  "eval_peak_step": 205000,
  "nve_peak": 0.194,
  "nve_final": 0.051,
  "civo_alert": false,
  "total_steps": 224000,
  "total_train_episodes": 224
}

=== exp_047_frozen_dt_emb_walker_s1 ===
{
  "eval_final": 144.22,
  "eval_final_step": 215000,
  "eval_peak": 408.79,
  "eval_peak_step": 125000,
  "ve_ratio_peak": 1.099,
  "ve_ratio_peak_step": 75000,
  "ve_ratio_final": 0.277,
  "nve_peak": 1.71,
  "nve_peak_step": 95000,
  "nve_final_105k": 0.56,
  "total_steps": 225000
}

=== exp_009a_baseline_walker_s2 ===
{
  "cross_seed_ve_stable": "seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72",
  "eval_return_peak": 966.94,
  "eval_return_peak_step": 395000,
  "eval_trajectory": [
    {
      "eval_return": 41.21,
      "step": 5000
    },
    {
      "eval_return": 106.01,
      "step": 15000
    },
    {
      "eval_return": 325.33,
      "step": 25000
    },
    {
      "eval_return": 354.49,
      "step": 35000
    },
    {
      "eval_return": 498.01,
      "step": 45000
    },
    {
      "eval_return": 534.13,
      "step": 55000
    },
    {
      "eval_return": 688.87,
      "step": 65000
    },
    {
      "eval_return": 656.85,
      "step": 75000
    },
    {
      "eval_return": 618.73,
      "step": 85000
    },
    {
      "eval_return": 596.24,
      "step": 95000
    },
    {
      "eval_return": 836.51,
      "step": 105000
    },
    {
      "eval_return": 804.79,
      "step": 115000
    },
    {
      "eval_return": 865.48,
      "step": 125000
    },
    {
      "eval_return": 876.08,
      "step": 135000
    },
    {
      "eval_return": 869.18,
      "step": 145000
    },
    {
      "eval_return": 778.99,
      "step": 155000
    },
    {
      "eval_return": 864.03,
      "step": 165000
    },
    {
      "eval_return": 850.53,
      "step": 175000
    },
    {
      "eval_return": 907.31,
      "step": 185000
    },
    {
      "eval_return": 873.49,
      "step": 195000
    },
    {
      "eval_return": 887.02,
      "step": 205000
    },
    {
      "eval_return": 956.04,
      "step": 215000
    },
    {
      "eval_return": 892.09,
      "step": 225000
    },
    {
      "eval_return": 914.78,
      "step": 235000
    },
    {
      "eval_return": 950.32,
      "step": 245000
    },
    {
      "eval_return": 936.9,
      "step": 255000
    },
    {
      "eval_return": 937.27,
      "step": 265000
    },
    {
      "eval_return": 934.78,
      "step": 275000
    },
    {
      "eval_return": 960.2,
      "step": 285000
    },
    {
      "eval_return": 947.46,
      "step": 295000
    },
    {
      "eval_return": 937.8,
      "step": 305000
    },
    {
      "eval_return": 948.66,
      "step": 315000
    },
    {
      "eval_return": 930.61,
      "step": 325000
    },
    {
      "eval_return": 919.23,
      "step": 335000
    },
    {
      "eval_return": 816.18,
      "step": 345000
    },
    {
      "eval_return": 932.45,
      "step": 355000
    },
    {
      "eval_return": 943.13,
      "step": 365000
    },
    {
      "eval_return": 952.86,
      "step": 375000
    },
    {
      "eval_return": 942.31,
      "step": 385000
    },
    {
      "eval_return": 966.94,
      "step": 395000
    },
    {
      "eval_return": 948.01,
      "step": 405000
    },
    {
      "eval_return": 957.06,
      "step": 415000
    },
    {
      "eval_return": 939.37,
      "step": 425000
    },
    {
      "eval_return": 963.65,
      "step": 435000
    },
    {
      "eval_return": 948.42,
      "step": 445000
    },
    {
      "eval_return": 937.72,
      "step": 455000
    },
    {
      "eval_return": 939.54,
      "step": 465000
    },
    {
      "eval_return": 965.94,
      "step": 475000
    },
    {
      "eval_return": 916.74,
      "step": 485000
    },
    {
      "eval_return": 945.58,
      "step": 495000
    },
    {
      "eval_return": 957.87,
      "step": 505000
    }
  ],
  "final_eval_return": 957.87,
  "final_eval_step": 505000,
  "final_value_mean": 665.17,
  "final_ve_ratio": 0.694,
  "last10_mean": 947.19,
  "n_evals": 51,
  "total_steps": 505000,
  "value_trajectory": [
    {
      "step": 5000,
      "value_mean": 0
    },
    {
      "step": 25000,
      "value_mean": 45.78
    },
    {
      "step": 55000,
      "value_mean": 253.49
    },
    {
      "step": 105000,
      "value_mean": 539.34
    },
    {
      "step": 155000,
      "value_mean": 633.42
    },
    {
      "step": 205000,
      "value_mean": 658.92
    },
    {
      "step": 255000,
      "value_mean": 663.87
    },
    {
      "step": 305000,
      "value_mean": 663.86
    },
    {
      "step": 355000,
      "value_mean": 663.78
    },
    {
      "step": 405000,
      "value_mean": 663.95
    },
    {
      "step": 455000,
      "value_mean": 664.42
    },
    {
      "step": 505000,
      "value_mean": 665.17
    }
  ],
  "ve_ratio_trajectory": [
    {
      "step": 25000,
      "ve": 0.141
    },
    {
      "step": 55000,
      "ve": 0.475
    },
    {
      "step": 105000,
      "ve": 0.645
    },
    {
      "step": 155000,
      "ve": 0.813
    },
    {
      "step": 205000,
      "ve": 0.743
    },
    {
      "step": 255000,
      "ve": 0.709
    },
    {
      "step": 305000,
      "ve": 0.708
    },
    {
      "step": 355000,
      "ve": 0.712
    },
    {
      "step": 405000,
      "ve": 0.7
    },
    {
      "step": 455000,
      "ve": 0.709
    },
    {
      "step": 505000,
      "ve": 0.694
    }
  ],
  "ve_stable_range": "0.69-0.72 from 235K+",
  "vs_exp001_105K": "836.51 vs 915.67 (-8.6%)",
  "vs_exp001_final": "957.87 vs 970.41 (-1.3%)",
  "vs_exp001_last10": "947.19 vs 950.90 (-0.4%)",
  "vs_exp001_peak": "966.94 vs 970.41 (-0.4%)"
}

=== exp_001_baseline_s4_extended ===
{
  "convergence_mean_250k_plus": 935,
  "final_eval_return": 938.86,
  "final_step": 520000,
  "peak_eval_return": 960.6
}

=== exp_001_baseline_s3_extended ===
{
  "eval_profile": {
    "102000": 869.03,
    "112000": 898.89,
    "120000": 898.38,
    "130000": 837.74,
    "140000": 876.64,
    "15000": 224.27,
    "150000": 899.47,
    "160000": 922.77,
    "170000": 925.77,
    "180000": 912.89,
    "190000": 915.07,
    "200000": 894.77,
    "210000": 899.79,
    "220000": 951.18,
    "230000": 930.56,
    "240000": 910.47,
    "25000": 329.99,
    "250000": 914.02,
    "260000": 931.33,
    "270000": 954.65,
    "280000": 928.01,
    "290000": 947.4,
    "300000": 853.32,
    "310000": 906.35,
    "320000": 847.16,
    "330000": 934.78,
    "340000": 921.08,
    "35000": 413.12,
    "350000": 922.63,
    "360000": 844.99,
    "370000": 911.36,
    "380000": 917.73,
    "390000": 937.21,
    "400000": 928,
    "410000": 945.88,
    "420000": 897.2,
    "430000": 949.45,
    "440000": 937.28,
    "45000": 332.69,
    "450000": 924.24,
    "460000": 967.25,
    "470000": 940.55,
    "480000": 936.24,
    "490000": 944.67,
    "5000": 42.15,
    "500000": 957.09,
    "510000": 947.68,
    "55000": 519.91,
    "65000": 667.42,
    "72000": 771.33,
    "82000": 772.88,
    "92000": 854.6
  },
  "final_eval_return": 947.68,
  "final_step": 520000,
  "final_train_return_avg": 945.4
}

=== exp_001_baseline_s2_extended ===
{
  "eval_return_at_105K": 443.5,
  "eval_return_final": 945.7,
  "eval_return_peak": 962.6,
  "total_steps": 512000,
  "value_mean_at_105K": 329.16,
  "value_mean_plateau": 665,
  "ve_ratio_at_105K": 0.7422,
  "ve_ratio_converged_range": "0.69-0.77"
}

=== exp_001_baseline_s4 ===
{
  "current_step": 112000,
  "eval_return_105k": 922.8,
  "peak_eval": 922.8,
  "peak_eval_step": 105000,
  "target_steps": 105000,
  "value_mean_final": 576.1,
  "ve_ratio_105k": 0.624
}

=== exp_001_baseline_s3 ===
{
  "current_step": 120000,
  "eval_return_102k": 869.03,
  "peak_eval": 898.89,
  "peak_eval_step": 112000,
  "target_steps": 105000,
  "value_mean_final": 622.2,
  "ve_ratio_final": 0.692
}

=== exp_001_baseline_s2 ===
{
  "current_step": 112000,
  "eval_return_105k": 443.46,
  "target_steps": 105000,
  "value_mean_105k": 329.16,
  "ve_ratio_105k": 0.742
}

=== exp_001_baseline ===
{
  "data_source_ve": "from training logs metrics.jsonl",
  "eval_return_last10_mean": 950.9,
  "eval_return_peak": 970.41,
  "eval_return_peak_step": 505000,
  "eval_trajectory": {
    "105K": 915.67,
    "115K": 919.81,
    "125K": 921.37,
    "135K": 900,
    "145K": 932.16,
    "155K": 933.34,
    "15K": 206.61,
    "165K": 907.98,
    "175K": 918.87,
    "185K": 954.69,
    "195K": 936.09,
    "205K": 949.24,
    "215K": 913.4,
    "225K": 962.44,
    "235K": 937.24,
    "245K": 934.42,
    "255K": 948.45,
    "25K": 395.27,
    "265K": 925.09,
    "275K": 931.51,
    "285K": 925.75,
    "295K": 936.3,
    "305K": 939.33,
    "315K": 948.42,
    "325K": 967.75,
    "335K": 942.41,
    "345K": 969.83,
    "355K": 941.11,
    "35K": 388.47,
    "365K": 935.76,
    "375K": 918.24,
    "385K": 937.98,
    "395K": 955.38,
    "405K": 937.83,
    "415K": 948.99,
    "425K": 954.64,
    "435K": 964.96,
    "445K": 953.37,
    "455K": 945.84,
    "45K": 513.77,
    "465K": 947.81,
    "475K": 947.66,
    "485K": 930.6,
    "495K": 944.73,
    "505K": 970.41,
    "55K": 625.73,
    "5K": 31.77,
    "65K": 615.86,
    "75K": 596.28,
    "85K": 713.93,
    "95K": 871.06
  },
  "final": true,
  "step": 512000,
  "value_eval_ratio_105K": 0.656,
  "value_eval_ratio_25K": 0.087,
  "value_eval_ratio_35K": 0.241,
  "value_eval_ratio_45K": 0.331,
  "value_eval_ratio_55K": 0.404,
  "value_eval_ratio_65K": 0.563,
  "value_eval_ratio_75K": 0.719,
  "value_eval_ratio_85K": 0.701,
  "value_eval_ratio_95K": 0.632,
  "value_eval_ratio_stable": "~69-72% from 135K+"
}

=== exp_001_baseline_s4_extended (status=DONE) ===
{
  "convergence_mean_250k_plus": 935,
  "final_eval_return": 938.86,
  "final_step": 520000,
  "peak_eval_return": 960.6
}

=== exp_001_baseline_s3_extended (status=DONE) ===
{
  "eval_profile": {
    "102000": 869.03,
    "112000": 898.89,
    "120000": 898.38,
    "130000": 837.74,
    "140000": 876.64,
    "15000": 224.27,
    "150000": 899.47,
    "160000": 922.77,
    "170000": 925.77,
    "180000": 912.89,
    "190000": 915.07,
    "200000": 894.77,
    "210000": 899.79,
    "220000": 951.18,
    "230000": 930.56,
    "240000": 910.47,
    "25000": 329.99,
    "250000": 914.02,
    "260000": 931.33,
    "270000": 954.65,
    "280000": 928.01,
    "290000": 947.4,
    "300000": 853.32,
    "310000": 906.35,
    "320000": 847.16,
    "330000": 934.78,
    "340000": 921.08,
    "35000": 413.12,
    "350000": 922.63,
    "360000": 844.99,
    "370000": 911.36,
    "380000": 917.73,
    "390000": 937.21,
    "400000": 928,
    "410000": 945.88,
    "420000": 897.2,
    "430000": 949.45,
    "440000": 937.28,
    "45000": 332.69,
    "450000": 924.24,
    "460000": 967.25,
    "470000": 940.55,
    "480000": 936.24,
    "490000": 944.67,
    "5000": 42.15,
    "500000": 957.09,
    "510000": 947.68,
    "55000": 519.91,
    "65000": 667.42,
    "72000": 771.33,
    "82000": 772.88,
    "92000": 854.6
  },
  "final_eval_return": 947.68,
  "final_step": 520000,
  "final_train_return_avg": 945.4
}

=== exp_001_baseline_s2_extended (status=DONE) ===
{
  "eval_return_at_105K": 443.5,
  "eval_return_final": 945.7,
  "eval_return_peak": 962.6,
  "total_steps": 512000,
  "value_mean_at_105K": 329.16,
  "value_mean_plateau": 665,
  "ve_ratio_at_105K": 0.7422,
  "ve_ratio_converged_range": "0.69-0.77"
}

=== exp_001_baseline_s4 (status=DONE) ===
{
  "current_step": 112000,
  "eval_return_105k": 922.8,
  "peak_eval": 922.8,
  "peak_eval_step": 105000,
  "target_steps": 105000,
  "value_mean_final": 576.1,
  "ve_ratio_105k": 0.624
}

=== exp_001_baseline_s3 (status=DONE) ===
{
  "current_step": 120000,
  "eval_return_102k": 869.03,
  "peak_eval": 898.89,
  "peak_eval_step": 112000,
  "target_steps": 105000,
  "value_mean_final": 622.2,
  "ve_ratio_final": 0.692
}

=== exp_001_baseline_s2 (status=DONE) ===
{
  "current_step": 112000,
  "eval_return_105k": 443.46,
  "target_steps": 105000,
  "value_mean_105k": 329.16,
  "ve_ratio_105k": 0.742
}

=== exp_001_baseline (status=DONE) ===
{
  "data_source_ve": "from training logs metrics.jsonl",
  "eval_return_last10_mean": 950.9,
  "eval_return_peak": 970.41,
  "eval_return_peak_step": 505000,
  "eval_trajectory": {
    "105K": 915.67,
    "115K": 919.81,
    "125K": 921.37,
    "135K": 900,
    "145K": 932.16,
    "155K": 933.34,
    "15K": 206.61,
    "165K": 907.98,
    "175K": 918.87,
    "185K": 954.69,
    "195K": 936.09,
    "205K": 949.24,
    "215K": 913.4,
    "225K": 962.44,
    "235K": 937.24,
    "245K": 934.42,
    "255K": 948.45,
    "25K": 395.27,
    "265K": 925.09,
    "275K": 931.51,
    "285K": 925.75,
    "295K": 936.3,
    "305K": 939.33,
    "315K": 948.42,
    "325K": 967.75,
    "335K": 942.41,
    "345K": 969.83,
    "355K": 941.11,
    "35K": 388.47,
    "365K": 935.76,
    "375K": 918.24,
    "385K": 937.98,
    "395K": 955.38,
    "405K": 937.83,
    "415K": 948.99,
    "425K": 954.64,
    "435K": 964.96,
    "445K": 953.37,
    "455K": 945.84,
    "45K": 513.77,
    "465K": 947.81,
    "475K": 947.66,
    "485K": 930.6,
    "495K": 944.73,
    "505K": 970.41,
    "55K": 625.73,
    "5K": 31.77,
    "65K": 615.86,
    "75K": 596.28,
    "85K": 713.93,
    "95K": 871.06
  },
  "final": true,
  "step": 512000,
  "value_eval_ratio_105K": 0.656,
  "value_eval_ratio_25K": 0.087,
  "value_eval_ratio_35K": 0.241,
  "value_eval_ratio_45K": 0.331,
  "value_eval_ratio_55K": 0.404,
  "value_eval_ratio_65K": 0.563,
  "value_eval_ratio_75K": 0.719,
  "value_eval_ratio_85K": 0.701,
  "value_eval_ratio_95K": 0.632,
  "value_eval_ratio_stable": "~69-72% from 135K+"
}

=== exp_009d_baseline_walker_s0 ===
{
  "eval_return": 927.6,
  "eval_return_at_508K": 927.6,
  "eval_return_peak": 950.96,
  "eval_return_peak_step": 398000,
  "note": "COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K",
  "step": 508000
}

=== exp_009d_baseline_walker_s1 ===
{}

=== exp_009a_baseline_walker_s2 ===
{
  "cross_seed_ve_stable": "seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72",
  "eval_return_peak": 966.94,
  "eval_return_peak_step": 395000,
  "eval_trajectory": [
    {
      "eval_return": 41.21,
      "step": 5000
    },
    {
      "eval_return": 106.01,
      "step": 15000
    },
    {
      "eval_return": 325.33,
      "step": 25000
    },
    {
      "eval_return": 354.49,
      "step": 35000
    },
    {
      "eval_return": 498.01,
      "step": 45000
    },
    {
      "eval_return": 534.13,
      "step": 55000
    },
    {
      "eval_return": 688.87,
      "step": 65000
    },
    {
      "eval_return": 656.85,
      "step": 75000
    },
    {
      "eval_return": 618.73,
      "step": 85000
    },
    {
      "eval_return": 596.24,
      "step": 95000
    },
    {
      "eval_return": 836.51,
      "step": 105000
    },
    {
      "eval_return": 804.79,
      "step": 115000
    },
    {
      "eval_return": 865.48,
      "step": 125000
    },
    {
      "eval_return": 876.08,
      "step": 135000
    },
    {
      "eval_return": 869.18,
      "step": 145000
    },
    {
      "eval_return": 778.99,
      "step": 155000
    },
    {
      "eval_return": 864.03,
      "step": 165000
    },
    {
      "eval_return": 850.53,
      "step": 175000
    },
    {
      "eval_return": 907.31,
      "step": 185000
    },
    {
      "eval_return": 873.49,
      "step": 195000
    },
    {
      "eval_return": 887.02,
      "step": 205000
    },
    {
      "eval_return": 956.04,
      "step": 215000
    },
    {
      "eval_return": 892.09,
      "step": 225000
    },
    {
      "eval_return": 914.78,
      "step": 235000
    },
    {
      "eval_return": 950.32,
      "step": 245000
    },
    {
      "eval_return": 936.9,
      "step": 255000
    },
    {
      "eval_return": 937.27,
      "step": 265000
    },
    {
      "eval_return": 934.78,
      "step": 275000
    },
    {
      "eval_return": 960.2,
      "step": 285000
    },
    {
      "eval_return": 947.46,
      "step": 295000
    },
    {
      "eval_return": 937.8,
      "step": 305000
    },
    {
      "eval_return": 948.66,
      "step": 315000
    },
    {
      "eval_return": 930.61,
      "step": 325000
    },
    {
      "eval_return": 919.23,
      "step": 335000
    },
    {
      "eval_return": 816.18,
      "step": 345000
    },
    {
      "eval_return": 932.45,
      "step": 355000
    },
    {
      "eval_return": 943.13,
      "step": 365000
    },
    {
      "eval_return": 952.86,
      "step": 375000
    },
    {
      "eval_return": 942.31,
      "step": 385000
    },
    {
      "eval_return": 966.94,
      "step": 395000
    },
    {
      "eval_return": 948.01,
      "step": 405000
    },
    {
      "eval_return": 957.06,
      "step": 415000
    },
    {
      "eval_return": 939.37,
      "step": 425000
    },
    {
      "eval_return": 963.65,
      "step": 435000
    },
    {
      "eval_return": 948.42,
      "step": 445000
    },
    {
      "eval_return": 937.72,
      "step": 455000
    },
    {
      "eval_return": 939.54,
      "step": 465000
    },
    {
      "eval_return": 965.94,
      "step": 475000
    },
    {
      "eval_return": 916.74,
      "step": 485000
    },
    {
      "eval_return": 945.58,
      "step": 495000
    },
    {
      "eval_return": 957.87,
      "step": 505000
    }
  ],
  "final_eval_return": 957.87,
  "final_eval_step": 505000,
  "final_value_mean": 665.17,
  "final_ve_ratio": 0.694,
  "last10_mean": 947.19,
  "n_evals": 51,
  "total_steps": 505000,
  "value_trajectory": [
    {
      "step": 5000,
      "value_mean": 0
    },
    {
      "step": 25000,
      "value_mean": 45.78
    },
    {
      "step": 55000,
      "value_mean": 253.49
    },
    {
      "step": 105000,
      "value_mean": 539.34
    },
    {
      "step": 155000,
      "value_mean": 633.42
    },
    {
      "step": 205000,
      "value_mean": 658.92
    },
    {
      "step": 255000,
      "value_mean": 663.87
    },
    {
      "step": 305000,
      "value_mean": 663.86
    },
    {
      "step": 355000,
      "value_mean": 663.78
    },
    {
      "step": 405000,
      "value_mean": 663.95
    },
    {
      "step": 455000,
      "value_mean": 664.42
    },
    {
      "step": 505000,
      "value_mean": 665.17
    }
  ],
  "ve_ratio_trajectory": [
    {
      "step": 25000,
      "ve": 0.141
    },
    {
      "step": 55000,
      "ve": 0.475
    },
    {
      "step": 105000,
      "ve": 0.645
    },
    {
      "step": 155000,
      "ve": 0.813
    },
    {
      "step": 205000,
      "ve": 0.743
    },
    {
      "step": 255000,
      "ve": 0.709
    },
    {
      "step": 305000,
      "ve": 0.708
    },
    {
      "step": 355000,
      "ve": 0.712
    },
    {
      "step": 405000,
      "ve": 0.7
    },
    {
      "step": 455000,
      "ve": 0.709
    },
    {
      "step": 505000,
      "ve": 0.694
    }
  ],
  "ve_stable_range": "0.69-0.72 from 235K+",
  "vs_exp001_105K": "836.51 vs 915.67 (-8.6%)",
  "vs_exp001_final": "957.87 vs 970.41 (-1.3%)",
  "vs_exp001_last10": "947.19 vs 950.90 (-0.4%)",
  "vs_exp001_peak": "966.94 vs 970.41 (-0.4%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "c8c339fd-579e-4f68-b220-6cd459a47156",
  "tool_use_result": {
    "stdout": "=== exp_057_frozen_dt_emb_walker_s2 ===\n{\n  \"total_steps\": 225000,\n  \"ve_ratio_peak\": 1.283,\n  \"ve_ratio_peak_step\": 115000,\n  \"ve_ratio_final\": 0.177,\n  \"ve_ratio_final_step\": 215000,\n  \"nve_classification\": \"no_civo\",\n  \"note\": \"Walker frozen s2. Peak transient at 115K, self-corrected. Walker frozen n=3 complete: s0=0.19, s1=1.71, s2=1.28 \\u2014 all clean/transient.\"\n}\n\n=== exp_042_frozen_dt_emb_walker ===\n{\n  \"eval_final\": 612.45,\n  \"eval_peak\": 682.38,\n  \"eval_peak_step\": 205000,\n  \"nve_peak\": 0.194,\n  \"nve_final\": 0.051,\n  \"civo_alert\": false,\n  \"total_steps\": 224000,\n  \"total_train_episodes\": 224\n}\n\n=== exp_047_frozen_dt_emb_walker_s1 ===\n{\n  \"eval_final\": 144.22,\n  \"eval_final_step\": 215000,\n  \"eval_peak\": 408.79,\n  \"eval_peak_step\": 125000,\n  \"ve_ratio_peak\": 1.099,\n  \"ve_ratio_peak_step\": 75000,\n  \"ve_ratio_final\": 0.277,\n  \"nve_peak\": 1.71,\n  \"nve_peak_step\": 95000,\n  \"nve_final_105k\": 0.56,\n  \"total_steps\": 225000\n}\n\n=== exp_009a_baseline_walker_s2 ===\n{\n  \"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\",\n  \"eval_return_peak\": 966.94,\n  \"eval_return_peak_step\": 395000,\n  \"eval_trajectory\": [\n    {\n      \"eval_return\": 41.21,\n      \"step\": 5000\n    },\n    {\n      \"eval_return\": 106.01,\n      \"step\": 15000\n    },\n    {\n      \"eval_return\": 325.33,\n      \"step\": 25000\n    },\n    {\n      \"eval_return\": 354.49,\n      \"step\": 35000\n    },\n    {\n      \"eval_return\": 498.01,\n      \"step\": 45000\n    },\n    {\n      \"eval_return\": 534.13,\n      \"step\": 55000\n    },\n    {\n      \"eval_return\": 688.87,\n      \"step\": 65000\n    },\n    {\n      \"eval_return\": 656.85,\n      \"step\": 75000\n    },\n    {\n      \"eval_return\": 618.73,\n      \"step\": 85000\n    },\n    {\n      \"eval_return\": 596.24,\n      \"step\": 95000\n    },\n    {\n      \"eval_return\": 836.51,\n      \"step\": 105000\n    },\n    {\n      \"eval_return\": 804.79,\n      \"step\": 115000\n    },\n    {\n      \"eval_return\": 865.48,\n      \"step\": 125000\n    },\n    {\n      \"eval_return\": 876.08,\n      \"step\": 135000\n    },\n    {\n      \"eval_return\": 869.18,\n      \"step\": 145000\n    },\n    {\n      \"eval_return\": 778.99,\n      \"step\": 155000\n    },\n    {\n      \"eval_return\": 864.03,\n      \"step\": 165000\n    },\n    {\n      \"eval_return\": 850.53,\n      \"step\": 175000\n    },\n    {\n      \"eval_return\": 907.31,\n      \"step\": 185000\n    },\n    {\n      \"eval_return\": 873.49,\n      \"step\": 195000\n    },\n    {\n      \"eval_return\": 887.02,\n      \"step\": 205000\n    },\n    {\n      \"eval_return\": 956.04,\n      \"step\": 215000\n    },\n    {\n      \"eval_return\": 892.09,\n      \"step\": 225000\n    },\n    {\n      \"eval_return\": 914.78,\n      \"step\": 235000\n    },\n    {\n      \"eval_return\": 950.32,\n      \"step\": 245000\n    },\n    {\n      \"eval_return\": 936.9,\n      \"step\": 255000\n    },\n    {\n      \"eval_return\": 937.27,\n      \"step\": 265000\n    },\n    {\n      \"eval_return\": 934.78,\n      \"step\": 275000\n    },\n    {\n      \"eval_return\": 960.2,\n      \"step\": 285000\n    },\n    {\n      \"eval_return\": 947.46,\n      \"step\": 295000\n    },\n    {\n      \"eval_return\": 937.8,\n      \"step\": 305000\n    },\n    {\n      \"eval_return\": 948.66,\n      \"step\": 315000\n    },\n    {\n      \"eval_return\": 930.61,\n      \"step\": 325000\n    },\n    {\n      \"eval_return\": 919.23,\n      \"step\": 335000\n    },\n    {\n      \"eval_return\": 816.18,\n      \"step\": 345000\n    },\n    {\n      \"eval_return\": 932.45,\n      \"step\": 355000\n    },\n    {\n      \"eval_return\": 943.13,\n      \"step\": 365000\n    },\n    {\n      \"eval_return\": 952.86,\n      \"step\": 375000\n    },\n    {\n      \"eval_return\": 942.31,\n      \"step\": 385000\n    },\n    {\n      \"eval_return\": 966.94,\n      \"step\": 395000\n    },\n    {\n      \"eval_return\": 948.01,\n      \"step\": 405000\n    },\n    {\n      \"eval_return\": 957.06,\n      \"step\": 415000\n    },\n    {\n      \"eval_return\": 939.37,\n      \"step\": 425000\n    },\n    {\n      \"eval_return\": 963.65,\n      \"step\": 435000\n    },\n    {\n      \"eval_return\": 948.42,\n      \"step\": 445000\n    },\n    {\n      \"eval_return\": 937.72,\n      \"step\": 455000\n    },\n    {\n      \"eval_return\": 939.54,\n      \"step\": 465000\n    },\n    {\n      \"eval_return\": 965.94,\n      \"step\": 475000\n    },\n    {\n      \"eval_return\": 916.74,\n      \"step\": 485000\n    },\n    {\n      \"eval_return\": 945.58,\n      \"step\": 495000\n    },\n    {\n      \"eval_return\": 957.87,\n      \"step\": 505000\n    }\n  ],\n  \"final_eval_return\": 957.87,\n  \"final_eval_step\": 505000,\n  \"final_value_mean\": 665.17,\n  \"final_ve_ratio\": 0.694,\n  \"last10_mean\": 947.19,\n  \"n_evals\": 51,\n  \"total_steps\": 505000,\n  \"value_trajectory\": [\n    {\n      \"step\": 5000,\n      \"value_mean\": 0\n    },\n    {\n      \"step\": 25000,\n      \"value_mean\": 45.78\n    },\n    {\n      \"step\": 55000,\n      \"value_mean\": 253.49\n    },\n    {\n      \"step\": 105000,\n      \"value_mean\": 539.34\n    },\n    {\n      \"step\": 155000,\n      \"value_mean\": 633.42\n    },\n    {\n      \"step\": 205000,\n      \"value_mean\": 658.92\n    },\n    {\n      \"step\": 255000,\n      \"value_mean\": 663.87\n    },\n    {\n      \"step\": 305000,\n      \"value_mean\": 663.86\n    },\n    {\n      \"step\": 355000,\n      \"value_mean\": 663.78\n    },\n    {\n      \"step\": 405000,\n      \"value_mean\": 663.95\n    },\n    {\n      \"step\": 455000,\n      \"value_mean\": 664.42\n    },\n    {\n      \"step\": 505000,\n      \"value_mean\": 665.17\n    }\n  ],\n  \"ve_ratio_trajectory\": [\n    {\n      \"step\": 25000,\n      \"ve\": 0.141\n    },\n    {\n      \"step\": 55000,\n      \"ve\": 0.475\n    },\n    {\n      \"step\": 105000,\n      \"ve\": 0.645\n    },\n    {\n      \"step\": 155000,\n      \"ve\": 0.813\n    },\n    {\n      \"step\": 205000,\n      \"ve\": 0.743\n    },\n    {\n      \"step\": 255000,\n      \"ve\": 0.709\n    },\n    {\n      \"step\": 305000,\n      \"ve\": 0.708\n    },\n    {\n      \"step\": 355000,\n      \"ve\": 0.712\n    },\n    {\n      \"step\": 405000,\n      \"ve\": 0.7\n    },\n    {\n      \"step\": 455000,\n      \"ve\": 0.709\n    },\n    {\n      \"step\": 505000,\n      \"ve\": 0.694\n    }\n  ],\n  \"ve_stable_range\": \"0.69-0.72 from 235K+\",\n  \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\",\n  \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\",\n  \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\",\n  \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"\n}\n\n=== exp_001_baseline_s4_extended ===\n{\n  \"convergence_mean_250k_plus\": 935,\n  \"final_eval_return\": 938.86,\n  \"final_step\": 520000,\n  \"peak_eval_return\": 960.6\n}\n\n=== exp_001_baseline_s3_extended ===\n{\n  \"eval_profile\": {\n    \"102000\": 869.03,\n    \"112000\": 898.89,\n    \"120000\": 898.38,\n    \"130000\": 837.74,\n    \"140000\": 876.64,\n    \"15000\": 224.27,\n    \"150000\": 899.47,\n    \"160000\": 922.77,\n    \"170000\": 925.77,\n    \"180000\": 912.89,\n    \"190000\": 915.07,\n    \"200000\": 894.77,\n    \"210000\": 899.79,\n    \"220000\": 951.18,\n    \"230000\": 930.56,\n    \"240000\": 910.47,\n    \"25000\": 329.99,\n    \"250000\": 914.02,\n    \"260000\": 931.33,\n    \"270000\": 954.65,\n    \"280000\": 928.01,\n    \"290000\": 947.4,\n    \"300000\": 853.32,\n    \"310000\": 906.35,\n    \"320000\": 847.16,\n    \"330000\": 934.78,\n    \"340000\": 921.08,\n    \"35000\": 413.12,\n    \"350000\": 922.63,\n    \"360000\": 844.99,\n    \"370000\": 911.36,\n    \"380000\": 917.73,\n    \"390000\": 937.21,\n    \"400000\": 928,\n    \"410000\": 945.88,\n    \"420000\": 897.2,\n    \"430000\": 949.45,\n    \"440000\": 937.28,\n    \"45000\": 332.69,\n    \"450000\": 924.24,\n    \"460000\": 967.25,\n    \"470000\": 940.55,\n    \"480000\": 936.24,\n    \"490000\": 944.67,\n    \"5000\": 42.15,\n    \"500000\": 957.09,\n    \"510000\": 947.68,\n    \"55000\": 519.91,\n    \"65000\": 667.42,\n    \"72000\": 771.33,\n    \"82000\": 772.88,\n    \"92000\": 854.6\n  },\n  \"final_eval_return\": 947.68,\n  \"final_step\": 520000,\n  \"final_train_return_avg\": 945.4\n}\n\n=== exp_001_baseline_s2_extended ===\n{\n  \"eval_return_at_105K\": 443.5,\n  \"eval_return_final\": 945.7,\n  \"eval_return_peak\": 962.6,\n  \"total_steps\": 512000,\n  \"value_mean_at_105K\": 329.16,\n  \"value_mean_plateau\": 665,\n  \"ve_ratio_at_105K\": 0.7422,\n  \"ve_ratio_converged_range\": \"0.69-0.77\"\n}\n\n=== exp_001_baseline_s4 ===\n{\n  \"current_step\": 112000,\n  \"eval_return_105k\": 922.8,\n  \"peak_eval\": 922.8,\n  \"peak_eval_step\": 105000,\n  \"target_steps\": 105000,\n  \"value_mean_final\": 576.1,\n  \"ve_ratio_105k\": 0.624\n}\n\n=== exp_001_baseline_s3 ===\n{\n  \"current_step\": 120000,\n  \"eval_return_102k\": 869.03,\n  \"peak_eval\": 898.89,\n  \"peak_eval_step\": 112000,\n  \"target_steps\": 105000,\n  \"value_mean_final\": 622.2,\n  \"ve_ratio_final\": 0.692\n}\n\n=== exp_001_baseline_s2 ===\n{\n  \"current_step\": 112000,\n  \"eval_return_105k\": 443.46,\n  \"target_steps\": 105000,\n  \"value_mean_105k\": 329.16,\n  \"ve_ratio_105k\": 0.742\n}\n\n=== exp_001_baseline ===\n{\n  \"data_source_ve\": \"from training logs metrics.jsonl\",\n  \"eval_return_last10_mean\": 950.9,\n  \"eval_return_peak\": 970.41,\n  \"eval_return_peak_step\": 505000,\n  \"eval_trajectory\": {\n    \"105K\": 915.67,\n    \"115K\": 919.81,\n    \"125K\": 921.37,\n    \"135K\": 900,\n    \"145K\": 932.16,\n    \"155K\": 933.34,\n    \"15K\": 206.61,\n    \"165K\": 907.98,\n    \"175K\": 918.87,\n    \"185K\": 954.69,\n    \"195K\": 936.09,\n    \"205K\": 949.24,\n    \"215K\": 913.4,\n    \"225K\": 962.44,\n    \"235K\": 937.24,\n    \"245K\": 934.42,\n    \"255K\": 948.45,\n    \"25K\": 395.27,\n    \"265K\": 925.09,\n    \"275K\": 931.51,\n    \"285K\": 925.75,\n    \"295K\": 936.3,\n    \"305K\": 939.33,\n    \"315K\": 948.42,\n    \"325K\": 967.75,\n    \"335K\": 942.41,\n    \"345K\": 969.83,\n    \"355K\": 941.11,\n    \"35K\": 388.47,\n    \"365K\": 935.76,\n    \"375K\": 918.24,\n    \"385K\": 937.98,\n    \"395K\": 955.38,\n    \"405K\": 937.83,\n    \"415K\": 948.99,\n    \"425K\": 954.64,\n    \"435K\": 964.96,\n    \"445K\": 953.37,\n    \"455K\": 945.84,\n    \"45K\": 513.77,\n    \"465K\": 947.81,\n    \"475K\": 947.66,\n    \"485K\": 930.6,\n    \"495K\": 944.73,\n    \"505K\": 970.41,\n    \"55K\": 625.73,\n    \"5K\": 31.77,\n    \"65K\": 615.86,\n    \"75K\": 596.28,\n    \"85K\": 713.93,\n    \"95K\": 871.06\n  },\n  \"final\": true,\n  \"step\": 512000,\n  \"value_eval_ratio_105K\": 0.656,\n  \"value_eval_ratio_25K\": 0.087,\n  \"value_eval_ratio_35K\": 0.241,\n  \"value_eval_ratio_45K\": 0.331,\n  \"value_eval_ratio_55K\": 0.404,\n  \"value_eval_ratio_65K\": 0.563,\n  \"value_eval_ratio_75K\": 0.719,\n  \"value_eval_ratio_85K\": 0.701,\n  \"value_eval_ratio_95K\": 0.632,\n  \"value_eval_ratio_stable\": \"~69-72% from 135K+\"\n}\n\n=== exp_001_baseline_s4_extended (status=DONE) ===\n{\n  \"convergence_mean_250k_plus\": 935,\n  \"final_eval_return\": 938.86,\n  \"final_step\": 520000,\n  \"peak_eval_return\": 960.6\n}\n\n=== exp_001_baseline_s3_extended (status=DONE) ===\n{\n  \"eval_profile\": {\n    \"102000\": 869.03,\n    \"112000\": 898.89,\n    \"120000\": 898.38,\n    \"130000\": 837.74,\n    \"140000\": 876.64,\n    \"15000\": 224.27,\n    \"150000\": 899.47,\n    \"160000\": 922.77,\n    \"170000\": 925.77,\n    \"180000\": 912.89,\n    \"190000\": 915.07,\n    \"200000\": 894.77,\n    \"210000\": 899.79,\n    \"220000\": 951.18,\n    \"230000\": 930.56,\n    \"240000\": 910.47,\n    \"25000\": 329.99,\n    \"250000\": 914.02,\n    \"260000\": 931.33,\n    \"270000\": 954.65,\n    \"280000\": 928.01,\n    \"290000\": 947.4,\n    \"300000\": 853.32,\n    \"310000\": 906.35,\n    \"320000\": 847.16,\n    \"330000\": 934.78,\n    \"340000\": 921.08,\n    \"35000\": 413.12,\n    \"350000\": 922.63,\n    \"360000\": 844.99,\n    \"370000\": 911.36,\n    \"380000\": 917.73,\n    \"390000\": 937.21,\n    \"400000\": 928,\n    \"410000\": 945.88,\n    \"420000\": 897.2,\n    \"430000\": 949.45,\n    \"440000\": 937.28,\n    \"45000\": 332.69,\n    \"450000\": 924.24,\n    \"460000\": 967.25,\n    \"470000\": 940.55,\n    \"480000\": 936.24,\n    \"490000\": 944.67,\n    \"5000\": 42.15,\n    \"500000\": 957.09,\n    \"510000\": 947.68,\n    \"55000\": 519.91,\n    \"65000\": 667.42,\n    \"72000\": 771.33,\n    \"82000\": 772.88,\n    \"92000\": 854.6\n  },\n  \"final_eval_return\": 947.68,\n  \"final_step\": 520000,\n  \"final_train_return_avg\": 945.4\n}\n\n=== exp_001_baseline_s2_extended (status=DONE) ===\n{\n  \"eval_return_at_105K\": 443.5,\n  \"eval_return_final\": 945.7,\n  \"eval_return_peak\": 962.6,\n  \"total_steps\": 512000,\n  \"value_mean_at_105K\": 329.16,\n  \"value_mean_plateau\": 665,\n  \"ve_ratio_at_105K\": 0.7422,\n  \"ve_ratio_converged_range\": \"0.69-0.77\"\n}\n\n=== exp_001_baseline_s4 (status=DONE) ===\n{\n  \"current_step\": 112000,\n  \"eval_return_105k\": 922.8,\n  \"peak_eval\": 922.8,\n  \"peak_eval_step\": 105000,\n  \"target_steps\": 105000,\n  \"value_mean_final\": 576.1,\n  \"ve_ratio_105k\": 0.624\n}\n\n=== exp_001_baseline_s3 (status=DONE) ===\n{\n  \"current_step\": 120000,\n  \"eval_return_102k\": 869.03,\n  \"peak_eval\": 898.89,\n  \"peak_eval_step\": 112000,\n  \"target_steps\": 105000,\n  \"value_mean_final\": 622.2,\n  \"ve_ratio_final\": 0.692\n}\n\n=== exp_001_baseline_s2 (status=DONE) ===\n{\n  \"current_step\": 112000,\n  \"eval_return_105k\": 443.46,\n  \"target_steps\": 105000,\n  \"value_mean_105k\": 329.16,\n  \"ve_ratio_105k\": 0.742\n}\n\n=== exp_001_baseline (status=DONE) ===\n{\n  \"data_source_ve\": \"from training logs metrics.jsonl\",\n  \"eval_return_last10_mean\": 950.9,\n  \"eval_return_peak\": 970.41,\n  \"eval_return_peak_step\": 505000,\n  \"eval_trajectory\": {\n    \"105K\": 915.67,\n    \"115K\": 919.81,\n    \"125K\": 921.37,\n    \"135K\": 900,\n    \"145K\": 932.16,\n    \"155K\": 933.34,\n    \"15K\": 206.61,\n    \"165K\": 907.98,\n    \"175K\": 918.87,\n    \"185K\": 954.69,\n    \"195K\": 936.09,\n    \"205K\": 949.24,\n    \"215K\": 913.4,\n    \"225K\": 962.44,\n    \"235K\": 937.24,\n    \"245K\": 934.42,\n    \"255K\": 948.45,\n    \"25K\": 395.27,\n    \"265K\": 925.09,\n    \"275K\": 931.51,\n    \"285K\": 925.75,\n    \"295K\": 936.3,\n    \"305K\": 939.33,\n    \"315K\": 948.42,\n    \"325K\": 967.75,\n    \"335K\": 942.41,\n    \"345K\": 969.83,\n    \"355K\": 941.11,\n    \"35K\": 388.47,\n    \"365K\": 935.76,\n    \"375K\": 918.24,\n    \"385K\": 937.98,\n    \"395K\": 955.38,\n    \"405K\": 937.83,\n    \"415K\": 948.99,\n    \"425K\": 954.64,\n    \"435K\": 964.96,\n    \"445K\": 953.37,\n    \"455K\": 945.84,\n    \"45K\": 513.77,\n    \"465K\": 947.81,\n    \"475K\": 947.66,\n    \"485K\": 930.6,\n    \"495K\": 944.73,\n    \"505K\": 970.41,\n    \"55K\": 625.73,\n    \"5K\": 31.77,\n    \"65K\": 615.86,\n    \"75K\": 596.28,\n    \"85K\": 713.93,\n    \"95K\": 871.06\n  },\n  \"final\": true,\n  \"step\": 512000,\n  \"value_eval_ratio_105K\": 0.656,\n  \"value_eval_ratio_25K\": 0.087,\n  \"value_eval_ratio_35K\": 0.241,\n  \"value_eval_ratio_45K\": 0.331,\n  \"value_eval_ratio_55K\": 0.404,\n  \"value_eval_ratio_65K\": 0.563,\n  \"value_eval_ratio_75K\": 0.719,\n  \"value_eval_ratio_85K\": 0.701,\n  \"value_eval_ratio_95K\": 0.632,\n  \"value_eval_ratio_stable\": \"~69-72% from 135K+\"\n}\n\n=== exp_009d_baseline_walker_s0 ===\n{\n  \"eval_return\": 927.6,\n  \"eval_return_at_508K\": 927.6,\n  \"eval_return_peak\": 950.96,\n  \"eval_return_peak_step\": 398000,\n  \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\",\n  \"step\": 508000\n}\n\n=== exp_009d_baseline_walker_s1 ===\n{}\n\n=== exp_009a_baseline_walker_s2 ===\n{\n  \"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\",\n  \"eval_return_peak\": 966.94,\n  \"eval_return_peak_step\": 395000,\n  \"eval_trajectory\": [\n    {\n      \"eval_return\": 41.21,\n      \"step\": 5000\n    },\n    {\n      \"eval_return\": 106.01,\n      \"step\": 15000\n    },\n    {\n      \"eval_return\": 325.33,\n      \"step\": 25000\n    },\n    {\n      \"eval_return\": 354.49,\n      \"step\": 35000\n    },\n    {\n      \"eval_return\": 498.01,\n      \"step\": 45000\n    },\n    {\n      \"eval_return\": 534.13,\n      \"step\": 55000\n    },\n    {\n      \"eval_return\": 688.87,\n      \"step\": 65000\n    },\n    {\n      \"eval_return\": 656.85,\n      \"step\": 75000\n    },\n    {\n      \"eval_return\": 618.73,\n      \"step\": 85000\n    },\n    {\n      \"eval_return\": 596.24,\n      \"step\": 95000\n    },\n    {\n      \"eval_return\": 836.51,\n      \"step\": 105000\n    },\n    {\n      \"eval_return\": 804.79,\n      \"step\": 115000\n    },\n    {\n      \"eval_return\": 865.48,\n      \"step\": 125000\n    },\n    {\n      \"eval_return\": 876.08,\n      \"step\": 135000\n    },\n    {\n      \"eval_return\": 869.18,\n      \"step\": 145000\n    },\n    {\n      \"eval_return\": 778.99,\n      \"step\": 155000\n    },\n    {\n      \"eval_return\": 864.03,\n      \"step\": 165000\n    },\n    {\n      \"eval_return\": 850.53,\n      \"step\": 175000\n    },\n    {\n      \"eval_return\": 907.31,\n      \"step\": 185000\n    },\n    {\n      \"eval_return\": 873.49,\n      \"step\": 195000\n    },\n    {\n      \"eval_return\": 887.02,\n      \"step\": 205000\n    },\n    {\n      \"eval_return\": 956.04,\n      \"step\": 215000\n    },\n    {\n      \"eval_return\": 892.09,\n      \"step\": 225000\n    },\n    {\n      \"eval_return\": 914.78,\n      \"step\": 235000\n    },\n    {\n      \"eval_return\": 950.32,\n      \"step\": 245000\n    },\n    {\n      \"eval_return\": 936.9,\n      \"step\": 255000\n    },\n    {\n      \"eval_return\": 937.27,\n      \"step\": 265000\n    },\n    {\n      \"eval_return\": 934.78,\n      \"step\": 275000\n    },\n    {\n      \"eval_return\": 960.2,\n      \"step\": 285000\n    },\n    {\n      \"eval_return\": 947.46,\n      \"step\": 295000\n    },\n    {\n      \"eval_return\": 937.8,\n      \"step\": 305000\n    },\n    {\n      \"eval_return\": 948.66,\n      \"step\": 315000\n    },\n    {\n      \"eval_return\": 930.61,\n      \"step\": 325000\n    },\n    {\n      \"eval_return\": 919.23,\n      \"step\": 335000\n    },\n    {\n      \"eval_return\": 816.18,\n      \"step\": 345000\n    },\n    {\n      \"eval_return\": 932.45,\n      \"step\": 355000\n    },\n    {\n      \"eval_return\": 943.13,\n      \"step\": 365000\n    },\n    {\n      \"eval_return\": 952.86,\n      \"step\": 375000\n    },\n    {\n      \"eval_return\": 942.31,\n      \"step\": 385000\n    },\n    {\n      \"eval_return\": 966.94,\n      \"step\": 395000\n    },\n    {\n      \"eval_return\": 948.01,\n      \"step\": 405000\n    },\n    {\n      \"eval_return\": 957.06,\n      \"step\": 415000\n    },\n    {\n      \"eval_return\": 939.37,\n      \"step\": 425000\n    },\n    {\n      \"eval_return\": 963.65,\n      \"step\": 435000\n    },\n    {\n      \"eval_return\": 948.42,\n      \"step\": 445000\n    },\n    {\n      \"eval_return\": 937.72,\n      \"step\": 455000\n    },\n    {\n      \"eval_return\": 939.54,\n      \"step\": 465000\n    },\n    {\n      \"eval_return\": 965.94,\n      \"step\": 475000\n    },\n    {\n      \"eval_return\": 916.74,\n      \"step\": 485000\n    },\n    {\n      \"eval_return\": 945.58,\n      \"step\": 495000\n    },\n    {\n      \"eval_return\": 957.87,\n      \"step\": 505000\n    }\n  ],\n  \"final_eval_return\": 957.87,\n  \"final_eval_step\": 505000,\n  \"final_value_mean\": 665.17,\n  \"final_ve_ratio\": 0.694,\n  \"last10_mean\": 947.19,\n  \"n_evals\": 51,\n  \"total_steps\": 505000,\n  \"value_trajectory\": [\n    {\n      \"step\": 5000,\n      \"value_mean\": 0\n    },\n    {\n      \"step\": 25000,\n      \"value_mean\": 45.78\n    },\n    {\n      \"step\": 55000,\n      \"value_mean\": 253.49\n    },\n    {\n      \"step\": 105000,\n      \"value_mean\": 539.34\n    },\n    {\n      \"step\": 155000,\n      \"value_mean\": 633.42\n    },\n    {\n      \"step\": 205000,\n      \"value_mean\": 658.92\n    },\n    {\n      \"step\": 255000,\n      \"value_mean\": 663.87\n    },\n    {\n      \"step\": 305000,\n      \"value_mean\": 663.86\n    },\n    {\n      \"step\": 355000,\n      \"value_mean\": 663.78\n    },\n    {\n      \"step\": 405000,\n      \"value_mean\": 663.95\n    },\n    {\n      \"step\": 455000,\n      \"value_mean\": 664.42\n    },\n    {\n      \"step\": 505000,\n      \"value_mean\": 665.17\n    }\n  ],\n  \"ve_ratio_trajectory\": [\n    {\n      \"step\": 25000,\n      \"ve\": 0.141\n    },\n    {\n      \"step\": 55000,\n      \"ve\": 0.475\n    },\n    {\n      \"step\": 105000,\n      \"ve\": 0.645\n    },\n    {\n      \"step\": 155000,\n      \"ve\": 0.813\n    },\n    {\n      \"step\": 205000,\n      \"ve\": 0.743\n    },\n    {\n      \"step\": 255000,\n      \"ve\": 0.709\n    },\n    {\n      \"step\": 305000,\n      \"ve\": 0.708\n    },\n    {\n      \"step\": 355000,\n      \"ve\": 0.712\n    },\n    {\n      \"step\": 405000,\n      \"ve\": 0.7\n    },\n    {\n      \"step\": 455000,\n      \"ve\": 0.709\n    },\n    {\n      \"step\": 505000,\n      \"ve\": 0.694\n    }\n  ],\n  \"ve_stable_range\": \"0.69-0.72 from 235K+\",\n  \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\",\n  \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\",\n  \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\",\n  \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"\n}",
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

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me analyze.

**NVE Definition** from paper_framing.md:
"Diagnostic metric: v/e overshoot ratio = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning."

So NVE = experiment_ve_ratio / baseline_ve_ratio at the same step.

**Key issue**: The registry stores two different things:
- For exp_057: `ve_ratio_peak = 1.283` — this is the raw v/e ratio (value_mean / eval_return)


- For exp_042: `nve_peak = 0.194` — this is already NVE (normalized)
- For exp_047: both metrics exist at different timesteps, with `ve_ratio_peak = 1.099` at 75K and `nve_peak = 1.71` at 95K

So for exp_057, I need to calculate NVE by comparing its v/e ratio against the baseline's v/e ratio at the same training step.

Looking at the baseline data, exp_001_baseline has sparse v/e ratio measurements — 0.656 at 105K and 0.632 at 95K, but no explicit 115K value. For exp_009a_baseline_walker_s2, the same-seed baseline for exp_057, the v/e ratio trajectory also doesn't have a 115K data point.

The reviewer's estimate of 0.65 at 115K seems reasonable as an interpolation from exp_009a's 0.645 at 105K, but I need to check if the server's metrics.jsonl has finer-grained data to get the precise value. There's also a critical issue: exp_057's registry records a v/e ratio peak of 1.283 but doesn't include the normalized v/e peak value.

Looking at the classification note, whoever registered exp_057 listed the v/e ratio values for the Walker frozen variants (0.19, 1.71, 1.28) and marked them as "all clean/transient" with a "no_civo" classification, but this seems inconsistent with how normalized v/e should be calculated—dividing each v/e ratio by the baseline v/e ratio of around 0.65 would give different normalized values than what's implied by the classification.

Now I'm checking exp_047 more carefully: the registry shows nve_peak = 1.71 at 95K, but the v/e_ratio_peak is only 1.099 at 75K, which means the NVE peak isn't simply the v/e ratio peak. Working backward from the baseline v/e ratio at 95K (0.632), if NVE = 1.71, then the actual v/e ratio at that temperature would be around 1.08, not the 1.099 peak observed at a different temperature.

The same issue appears with exp_057: its v/e_ratio_peak of 1.283 at 115K would give an NVE of roughly 1.97 when divided by the baseline ratio at that temperature, yet it's marked as "no_civo" in the registry. I need to figure out which baseline is being used for these calculations—there are multiple options like exp_001 and exp_009a with different seeds.

For exp_047 specifically, if I use exp_001's baseline v/e_ratio of 0.632 at 95K and multiply by the reported NVE of 1.71, I get a v/e_ratio of about 1.08, but the peak recorded is 1.099 at 75K, so the values at different timesteps don't quite line up. I should pull the actual v/e_ratio values from the metrics files on the server rather than relying on the sparse registry data. I'm also wondering whether "NVE" for these frozen experiments might just be the raw v/e_ratio rather than a normalized version.

Looking at exp_042, the memory notes say NVE=0.19 while the registry shows nve_peak=0.194—these match closely, suggesting they're the same metric. But if NVE were truly normalized (v/e_ratio divided by baseline), then a raw v/e_ratio of 0.19 with a baseline around 0.65 would give NVE≈0.29, not 0.194. This makes me think there's some inconsistency in how different experiments calculated or labeled their NVE values.

Checking the registry more carefully, I see exp_042 stores nve_peak and nve_final as computed NVE values, exp_047 stores both ve_ratio_peak and nve_peak, but exp_057 only has ve_ratio_peak=1.283 with no nve_peak at all. So exp_057 was likely classified as "no_civo" based on the raw ve_ratio rather than a normalized NVE. If I compute NVE for exp_057 using that ve_ratio divided by a baseline of ~0.65, I get roughly 1.97, which exceeds the 1.5x threshold the reviewer mentioned.

Now I need to pull the actual metrics from the server to verify the baseline ve_ratio at 115K and check the exact values for exp_057 at its peak timestep, since the experiment directories for exp_042 and exp_047 are no longer available on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "38e808c7-1727-4f7e-990c-cacef61825cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoV6tbTWwsucp1FK8J2HaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9747,
      "cache_read_input_tokens": 54657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9747
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

关键发现：exp_057 只存了 `ve_ratio_peak=1.283`，没有计算 NVE。需要从服务器提取精确的 baseline ve_ratio。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "e820f135-7d77-4aeb-879f-88697196293c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoV6tbTWwsucp1FK8J2HaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9747,
      "cache_read_input_tokens": 54657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9747
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015CPufA4GUZUqWdTLSuM24B`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "find /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2 -name \"metrics.jsonl\" -o -name \"*.jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "7fc37512-a90b-4a9c-8432-089507940434",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoV6tbTWwsucp1FK8J2HaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9747,
      "cache_read_input_tokens": 54657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9747
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

_source line 39 · 2026-05-24T01:52:50.519Z_

<details><summary>↩ Tool result · `toolu_015CPufA4GUZUqWdTLSuM24B`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "e2693d98-24d3-49d5-8391-956e1cb97388",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01M2G76tGo7vbVq2YvJQETeH`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "find /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2 -name \"metrics.jsonl\" -o -name \"*.jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "633eec81-8019-496c-809a-b0af6b77ef70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoV6tbTWwsucp1FK8J2HaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9747,
      "cache_read_input_tokens": 54657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9747
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

_source line 41 · 2026-05-24T01:52:51.489Z_

<details><summary>↩ Tool result · `toolu_01M2G76tGo7vbVq2YvJQETeH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/metrics.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "55b8bd8c-9686-42f8-90fe-e3219a588270",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/metrics.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/metrics.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UnbBTfQaLh7sTiQMpwSvW7`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_057_frozen_dt_emb_walker_s2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "5fade8cd-1d30-452d-8073-dcb260e57d9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoV6tbTWwsucp1FK8J2HaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9747,
      "cache_read_input_tokens": 54657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9747
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

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AGY74mDwQu75PxsLF8ioJr`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "850d3ab4-746b-47cc-995d-f55617551b81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RoV6tbTWwsucp1FK8J2HaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9747,
      "cache_read_input_tokens": 54657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9747
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

_source line 44 · 2026-05-24T01:52:52.829Z_

<details><summary>↩ Tool result · `toolu_01UnbBTfQaLh7sTiQMpwSvW7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoint_125000.pt\\ncheckpoint_175000.pt\\ncheckpoint_225000.pt\\ncheckpoint_25000.pt\\ncheckpoint_75000.pt\\neval_eps\\nevents.out.tfevents.1779549904.autodl-container-k9z16fn7md-3a522761.157775.0\\nlatest.pt\\nmetrics.jsonl\\ntrain.log\\ntrain_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d0d1f3ea-6ab5-4a84-b796-cac72a4fc38b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"checkpoint_125000.pt\\\\ncheckpoint_175000.pt\\\\ncheckpoint_225000.pt\\\\ncheckpoint_25000.pt\\\\ncheckpoint_75000.pt\\\\neval_eps\\\\nevents.out.tfevents.1779549904.autodl-container-k9z16fn7md-3a522761.157775.0\\\\nlatest.pt\\\\nmetrics.jsonl\\\\ntrain.log\\\\ntrain_eps\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"checkpoint_125000.pt\\ncheckpoint_175000.pt\\ncheckpoint_225000.pt\\ncheckpoint_25000.pt\\ncheckpoint_75000.pt\\neval_eps\\nevents.out.tfevents.1779549904.autodl-container-k9z16fn7md-3a522761.157775.0\\nlatest.pt\\nmetrics.jsonl\\ntrain.log\\ntrain_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-24T01:52:53.256Z_

<details><summary>↩ Tool result · `toolu_01AGY74mDwQu75PxsLF8ioJr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_eps\\nevents.out.tfevents.1778751180.autodl-container-k9z16fn7md-3a522761.142513.0\\nlatest.pt\\nmetrics.jsonl\\ntrain_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "591b029e-95d9-4e73-9dbd-b65e34496ff4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_eps\\\\nevents.out.tfevents.1778751180.autodl-container-k9z16fn7md-3a522761.142513.0\\\\nlatest.pt\\\\nmetrics.jsonl\\\\ntrain_eps\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_eps\\nevents.out.tfevents.1778751180.autodl-container-k9z16fn7md-3a522761.142513.0\\nlatest.pt\\nmetrics.jsonl\\ntrain_eps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Good, both have metrics.jsonl files. Now I need to extract ve_ratio data at specific timesteps. Since ssh_read_only blocks pipe characters, I need to use python3 -c with a print-only script.

Let me write a python script to extract the relevant data from both experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "24a40197-4022-4783-92db-87c05e66456d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLT4GhBfTMX86wA4JU9ij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 64404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3506
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

_source line 47_

Now extracting ve_ratio at specific timesteps from both experiments via python3 -c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "4e474427-30ae-4dcf-8586-040982409811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLT4GhBfTMX86wA4JU9ij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 64404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3506
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

_source line 48_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NhQHkiz2JGVU5t56TqkRwm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "8d399a6d-757a-4f67-b2e7-6cd133c09e82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLT4GhBfTMX86wA4JU9ij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 64404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3506
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

_source line 49 · 2026-05-24T01:53:01.185Z_

<details><summary>↩ Tool result · `toolu_01NhQHkiz2JGVU5t56TqkRwm`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d0617cf7-c3d4-4121-ace7-113a2825be84",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01BKWAuhH2e8V5Xdqs2vvBL5`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cd /root/autodl-tmp/event-gated-adaptive-horizon && python3 -c \"\nimport json\n\n# === exp_057 (frozen s2) ===\nprint('=== exp_057_frozen_dt_emb_walker_s2 ===')\nwith open('logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl') as f:\n    for line in f:\n        m = json.loads(line)\n        step = m.get('step', 0)\n        if 85000 <= step <= 225000:\n            ve = m.get('ve_ratio', None)\n            val = m.get('value_mean', None)\n            ev = m.get('eval_return', None)\n            if ve is not None or val is not None:\n                print(f'  step={step}, ve_ratio={ve}, value_mean={val}, eval_return={ev}')\n\nprint()\n\n# === exp_009a baseline s2 ===\nprint('=== exp_009a_baseline_walker_s2 ===')\nwith open('logdir/exp_009a_baseline_walker_s2/metrics.jsonl') as f:\n    for line in f:\n        m = json.loads(line)\n        step = m.get('step', 0)\n        if 85000 <= step <= 225000:\n            ve = m.get('ve_ratio', None)\n            val = m.get('value_mean', None)\n            ev = m.get('eval_return', None)\n            if ve is not None or val is not None:\n                print(f'  step={step}, ve_ratio={ve}, value_mean={val}, eval_return={ev}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "05504194-5371-4eb3-8217-c267ebccb8b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gp1PK66QDYN56pMnVB5S3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 67910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 51 · 2026-05-24T01:53:08.565Z_

<details><summary>↩ Tool result · `toolu_01BKWAuhH2e8V5Xdqs2vvBL5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== exp_057_frozen_dt_emb_walker_s2 ===\\n  step=85000, ve_ratio=None, value_mean=50.74726867675781, eval_return=None\\n  step=95000, ve_ratio=None, value_mean=48.0203742980957, eval_return=None\\n  step=105000, ve_ratio=None, value_mean=44.49610137939453, eval_return=None\\n  step=115000, ve_ratio=None, value_mean=40.47226333618164, eval_return=None\\n  step=125000, ve_ratio=None, value_mean=37.486839294433594, eval_return=None\\n  step=135000, ve_ratio=None, value_mean=34.92658615112305, eval_return=None\\n  step=145000, ve_ratio=None, value_mean=32.9945068359375, eval_return=None\\n  step=155000, ve_ratio=None, value_mean=32.51809310913086, eval_return=None\\n  step=165000, ve_ratio=None, value_mean=31.254331588745117, eval_return=None\\n  step=175000, ve_ratio=None, value_mean=27.76986312866211, eval_return=None\\n  step=185000, ve_ratio=None, value_mean=25.062862396240234, eval_return=None\\n  step=195000, ve_ratio=None, value_mean=24.05299949645996, eval_return=None\\n  step=205000, ve_ratio=None, value_mean=23.082571029663086, eval_return=None\\n  step=215000, ve_ratio=None, value_mean=21.988418579101562, eval_return=None\\n\\n=== exp_009a_baseline_walker_s2 ===\\n  step=85000, ve_ratio=None, value_mean=450.5047912597656, eval_return=None\\n  step=95000, ve_ratio=None, value_mean=503.7415466308594, eval_return=None\\n  step=105000, ve_ratio=None, value_mean=539.3400268554688, eval_return=None\\n  step=115000, ve_ratio=None, value_mean=574.9320068359375, eval_return=None\\n  step=125000, ve_ratio=None, value_mean=612.47802734375, eval_return=None\\n  step=135000, ve_ratio=None, value_mean=628.1507568359375, eval_return=None\\n  step=145000, ve_ratio=None, value_mean=629.357177734375, eval_return=None\\n  step=155000, ve_ratio=None, value_mean=633.4157104492188, eval_return=None\\n  step=165000, ve_ratio=None, value_mean=641.3565063476562, eval_return=None\\n  step=175000, ve_ratio=None, value_mean=647.7266845703125, eval_return=None\\n  step=185000, ve_ratio=None, value_mean=653.0147705078125, eval_return=None\\n  step=195000, ve_ratio=None, value_mean=656.4356079101562, eval_return=None\\n  step=205000, ve_ratio=None, value_mean=658.9210815429688, eval_return=None\\n  step=215000, ve_ratio=None, value_mean=661.174560546875, eval_return=None\\n  step=225000, ve_ratio=None, value_mean=662.2446899414062, eval_return=None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "3ef17558-353c-4053-93ed-81bb9ff39804",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== exp_057_frozen_dt_emb_walker_s2 ===\\\\n  step=85000, ve_ratio=None, value_mean=50.74726867675781, eval_return=None\\\\n  step=95000, ve_ratio=None, value_mean=48.0203742980957, eval_return=None\\\\n  step=105000, ve_ratio=None, value_mean=44.49610137939453, eval_return=None\\\\n  step=115000, ve_ratio=None, value_mean=40.47226333618164, eval_return=None\\\\n  step=125000, ve_ratio=None, value_mean=37.486839294433594, eval_return=None\\\\n  step=135000, ve_ratio=None, value_mean=34.92658615112305, eval_return=None\\\\n  step=145000, ve_ratio=None, value_mean=32.9945068359375, eval_return=None\\\\n  step=155000, ve_ratio=None, value_mean=32.51809310913086, eval_return=None\\\\n  step=165000, ve_ratio=None, value_mean=31.254331588745117, eval_return=None\\\\n  step=175000, ve_ratio=None, value_mean=27.76986312866211, eval_return=None\\\\n  step=185000, ve_ratio=None, value_mean=25.062862396240234, eval_return=None\\\\n  step=195000, ve_ratio=None, value_mean=24.05299949645996, eval_return=None\\\\n  step=205000, ve_ratio=None, value_mean=23.082571029663086, eval_return=None\\\\n  step=215000, ve_ratio=None, value_mean=21.988418579101562, eval_return=None\\\\n\\\\n=== exp_009a_baseline_walker_s2 ===\\\\n  step=85000, ve_ratio=None, value_mean=450.5047912597656, eval_return=None\\\\n  step=95000, ve_ratio=None, value_mean=503.7415466308594, eval_return=None\\\\n  step=105000, ve_ratio=None, value_mean=539.3400268554688, eval_return=None\\\\n  step=115000, ve_ratio=None, value_mean=574.9320068359375, eval_return=None\\\\n  step=125000, ve_ratio=None, value_mean=612.47802734375, eval_return=None\\\\n  step=135000, ve_ratio=None, value_mean=628.1507568359375, eval_return=None\\\\n  step=145000, ve_ratio=None, value_mean=629.357177734375, eval_return=None\\\\n  step=155000, ve_ratio=None, value_mean=633.4157104492188, eval_return=None\\\\n  step=165000, ve_ratio=None, value_mean=641.3565063476562, eval_return=None\\\\n  step=175000, ve_ratio=None, value_mean=647.7266845703125, eval_return=None\\\\n  step=185000, ve_ratio=None, value_mean=653.0147705078125, eval_return=None\\\\n  step=195000, ve_ratio=None, value_mean=656.4356079101562, eval_return=None\\\\n  step=205000, ve_ratio=None, value_mean=658.9210815429688, eval_return=None\\\\n  step=215000, ve_ratio=None, value_mean=661.174560546875, eval_return=None\\\\n  step=225000, ve_ratio=None, value_mean=662.2446899414062, eval_return=None\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== exp_057_frozen_dt_emb_walker_s2 ===\\n  step=85000, ve_ratio=None, value_mean=50.74726867675781, eval_return=None\\n  step=95000, ve_ratio=None, value_mean=48.0203742980957, eval_return=None\\n  step=105000, ve_ratio=None, value_mean=44.49610137939453, eval_return=None\\n  step=115000, ve_ratio=None, value_mean=40.47226333618164, eval_return=None\\n  step=125000, ve_ratio=None, value_mean=37.486839294433594, eval_return=None\\n  step=135000, ve_ratio=None, value_mean=34.92658615112305, eval_return=None\\n  step=145000, ve_ratio=None, value_mean=32.9945068359375, eval_return=None\\n  step=155000, ve_ratio=None, value_mean=32.51809310913086, eval_return=None\\n  step=165000, ve_ratio=None, value_mean=31.254331588745117, eval_return=None\\n  step=175000, ve_ratio=None, value_mean=27.76986312866211, eval_return=None\\n  step=185000, ve_ratio=None, value_mean=25.062862396240234, eval_return=None\\n  step=195000, ve_ratio=None, value_mean=24.05299949645996, eval_return=None\\n  step=205000, ve_ratio=None, value_mean=23.082571029663086, eval_return=None\\n  step=215000, ve_ratio=None, value_mean=21.988418579101562, eval_return=None\\n\\n=== exp_009a_baseline_walker_s2 ===\\n  step=85000, ve_ratio=None, value_mean=450.5047912597656, eval_return=None\\n  step=95000, ve_ratio=None, value_mean=503.7415466308594, eval_return=None\\n  step=105000, ve_ratio=None, value_mean=539.3400268554688, eval_return=None\\n  step=115000, ve_ratio=None, value_mean=574.9320068359375, eval_return=None\\n  step=125000, ve_ratio=None, value_mean=612.47802734375, eval_return=None\\n  step=135000, ve_ratio=None, value_mean=628.1507568359375, eval_return=None\\n  step=145000, ve_ratio=None, value_mean=629.357177734375, eval_return=None\\n  step=155000, ve_ratio=None, value_mean=633.4157104492188, eval_return=None\\n  step=165000, ve_ratio=None, value_mean=641.3565063476562, eval_return=None\\n  step=175000, ve_ratio=None, value_mean=647.7266845703125, eval_return=None\\n  step=185000, ve_ratio=None, value_mean=653.0147705078125, eval_return=None\\n  step=195000, ve_ratio=None, value_mean=656.4356079101562, eval_return=None\\n  step=205000, ve_ratio=None, value_mean=658.9210815429688, eval_return=None\\n  step=215000, ve_ratio=None, value_mean=661.174560546875, eval_return=None\\n  step=225000, ve_ratio=None, value_mean=662.2446899414062, eval_return=None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
`ve_ratio` and `eval_return` are not in the metrics.jsonl. Only `value_mean` is logged at these steps. The ve_ratio must be computed from value_mean and eval_return, but eval_return is logged at different steps (eval episodes).

Let me check what keys are available in the metrics.jsonl to find where eval_return is logged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "609eaac0-787f-4627-bc68-1842fef62483",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE8se4py2yQ91Udcz7Qbtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 68356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1534
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

_source line 53_

ve_ratio 和 eval_return 不在这些行里。让我检查 metrics.jsonl 的完整字段结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "180c5f4b-9565-48b2-a672-e3fbb96794ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE8se4py2yQ91Udcz7Qbtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 68356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1534
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

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016nKx4jycT9nmBdtjYKFqjG`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cd /root/autodl-tmp/event-gated-adaptive-horizon && python3 -c \"\nimport json\n\n# Check what keys exist in exp_057 metrics\nprint('=== exp_057 keys sample ===')\nwith open('logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl') as f:\n    lines = f.readlines()\n    # Print keys from a few lines with different step values\n    seen_keys = set()\n    for line in lines:\n        m = json.loads(line)\n        keys = set(m.keys())\n        if keys != seen_keys:\n            step = m.get('step', 'N/A')\n            print(f'step={step}: {sorted(m.keys())}')\n            seen_keys = keys\n            # Print full content for a line that has eval info\n            if 'eval' in str(keys).lower() or 'return' in str(keys).lower():\n                print(f'  FULL: {json.dumps(m)}')\n\nprint()\nprint('=== exp_057: lines with eval/return ===')\nwith open('logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl') as f:\n    for line in f:\n        m = json.loads(line)\n        if any('eval' in k.lower() or 'return' in k.lower() or 've_ratio' in k.lower() for k in m.keys()):\n            step = m.get('step', 'N/A')\n            print(f'  step={step}: {json.dumps({k:v for k,v in m.items() if \\\"eval\\\" in k.lower() or \\\"return\\\" in k.lower() or \\\"ve_ratio\\\" in k.lower() or k==\\\"step\\\"})}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "56c958ef-4500-4051-b0f8-2ad718f86a40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE8se4py2yQ91Udcz7Qbtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 68356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1534
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

_source line 55 · 2026-05-24T01:53:24.611Z_

<details><summary>↩ Tool result · `toolu_016nKx4jycT9nmBdtjYKFqjG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== exp_057 keys sample ===\\nstep=0: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\n  FULL: {\\\"step\\\": 0, \\\"dataset_size\\\": 2000.0, \\\"train_return\\\": 62.74878692626953, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 4.0}\\nstep=5000: ['step']\\nstep=5000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\n  FULL: {\\\"step\\\": 5000, \\\"eval_return\\\": 39.26672782897949, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\nstep=5000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', 'orientations_loss', 'post_ent', 'prior_ent', 'rep_loss', 'rep_scale', 'reward_loss', 'step', 'target_max', 'target_mean', 'target_min', 'target_std', 'update_count', 'value_grad_norm', 'value_loss', 'value_max', 'value_mean', 'value_min', 'value_std', 'velocity_loss']\\nstep=8000: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\n  FULL: {\\\"step\\\": 8000, \\\"dataset_size\\\": 4000.0, \\\"train_return\\\": 39.657447814941406, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 8.0}\\nstep=15000: ['step']\\nstep=15000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\n  FULL: {\\\"step\\\": 15000, \\\"eval_return\\\": 181.96920776367188, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\nstep=15000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'civo/alert', 'civo/delta_ve', 'civo/ve_ratio', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', 'orientations_loss', 'post_ent', 'prior_ent', 'rep_loss', 'rep_scale', 'reward_loss', 'step', 'target_max', 'target_mean', 'target_min', 'target_std', 'update_count', 'value_grad_norm', 'value_loss', 'value_max', 'value_mean', 'value_min', 'value_std', 'velocity_loss']\\nstep=16000: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\n  FULL: {\\\"step\\\": 16000, \\\"dataset_size\\\": 8000.0, \\\"train_return\\\": 152.9766845703125, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 16.0}\\nstep=25000: ['step']\\nstep=25000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\n  FULL: {\\\"step\\\": 25000, \\\"eval_return\\\": 184.06726837158203, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\nstep=25000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'civo/alert', 'civo/delta_ve', 'civo/ve_ratio', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', '\\n\\n... [截断: 输出过长，省略 42575 字符] ...\\n\\nstep\\\": 176000, \\\"train_return\\\": 61.60499572753906}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 72.96839904785156}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 203.7918701171875}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 187.43519592285156}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 74.25837707519531}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 79.65927124023438}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 229.9039764404297}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 285.094970703125}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 60.712371826171875}\\n  step=185000: {\\\"step\\\": 185000, \\\"eval_return\\\": 208.4181335449219, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=185000: {\\\"step\\\": 185000, \\\"civo/ve_ratio\\\": 0.12025161113375325}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 81.25110626220703}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 185.87765502929688}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 276.7749328613281}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 138.64089965820312}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 79.8086929321289}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 290.1952209472656}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 89.81228637695312}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 56.90764617919922}\\n  step=195000: {\\\"step\\\": 195000, \\\"eval_return\\\": 221.71768188476562, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=195000: {\\\"step\\\": 195000, \\\"civo/ve_ratio\\\": 0.1084899494098272}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 229.42941284179688}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 207.6281280517578}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 67.41763305664062}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 122.93838500976562}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 61.20667266845703}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 165.01318359375}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 106.95035552978516}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 58.140647888183594}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 68.50728607177734}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 70.99976348876953}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 95.0828857421875}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 64.14974975585938}\\n  step=205000: {\\\"step\\\": 205000, \\\"eval_return\\\": 215.62352905273437, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=205000: {\\\"step\\\": 205000, \\\"civo/ve_ratio\\\": 0.10706286945628224}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 55.24531173706055}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 118.64993286132812}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 119.94863891601562}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 175.5042266845703}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 68.51705932617188}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 172.4085235595703}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 55.939247131347656}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 221.85865783691406}\\n  step=215000: {\\\"step\\\": 215000, \\\"eval_return\\\": 123.9377670288086, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=215000: {\\\"step\\\": 215000, \\\"civo/ve_ratio\\\": 0.17742178390818805}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 129.0413818359375}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 112.13914489746094}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 115.97281646728516}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 69.46036529541016}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 204.3446502685547}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 171.500244140625}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 73.99068450927734}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 112.25099182128906}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 67.41929626464844}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 67.7218017578125}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 75.39198303222656}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 114.04935455322266}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "da19ac34-9438-4f47-9117-3a0858dcd9ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== exp_057 keys sample ===\\\\nstep=0: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\\\n  FULL: {\\\\\\\"step\\\\\\\": 0, \\\\\\\"dataset_size\\\\\\\": 2000.0, \\\\\\\"train_return\\\\\\\": 62.74878692626953, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 4.0}\\\\nstep=5000: ['step']\\\\nstep=5000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\\\n  FULL: {\\\\\\\"step\\\\\\\": 5000, \\\\\\\"eval_return\\\\\\\": 39.26672782897949, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\nstep=5000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', 'orientations_loss', 'post_ent', 'prior_ent', 'rep_loss', 'rep_scale', 'reward_loss', 'step', 'target_max', 'target_mean', 'target_min', 'target_std', 'update_count', 'value_grad_norm', 'value_loss', 'value_max', 'value_mean', 'value_min', 'value_std', 'velocity_loss']\\\\nstep=8000: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\\\n  FULL: {\\\\\\\"step\\\\\\\": 8000, \\\\\\\"dataset_size\\\\\\\": 4000.0, \\\\\\\"train_return\\\\\\\": 39.657447814941406, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 8.0}\\\\nstep=15000: ['step']\\\\nstep=15000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\\\n  FULL: {\\\\\\\"step\\\\\\\": 15000, \\\\\\\"eval_return\\\\\\\": 181.96920776367188, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\nstep=15000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'civo/alert', 'civo/delta_ve', 'civo/ve_ratio', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', 'orientations_loss', 'post_ent', 'prior_ent', 'rep_loss', 'rep_scale', 'reward_loss', 'step', 'target_max', 'target_mean', 'target_min', 'target_std', 'update_count', 'value_grad_norm', 'value_loss', 'value_max', 'value_mean', 'value_min', 'value_std', 'velocity_loss']\\\\nstep=16000: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\\\n  FULL: {\\\\\\\"step\\\\\\\": 16000, \\\\\\\"dataset_size\\\\\\\": 8000.0, \\\\\\\"train_return\\\\\\\": 152.9766845703125, \\\\\\\"train_length\\\\\\\": 500.0, \\\\\\\"train_episodes\\\\\\\": 16.0}\\\\nstep=25000: ['step']\\\\nstep=25000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\\\n  FULL: {\\\\\\\"step\\\\\\\": 25000, \\\\\\\"eval_return\\\\\\\": 184.06726837158203, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\nstep=25000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'civo/alert', 'civo/delta_ve', 'civo/ve_ratio', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', '\\\\n\\\\n... [截断: 输出过长，省略 42575 字符] ...\\\\n\\\\nstep\\\\\\\": 176000, \\\\\\\"train_return\\\\\\\": 61.60499572753906}\\\\n  step=180000: {\\\\\\\"step\\\\\\\": 180000, \\\\\\\"train_return\\\\\\\": 72.96839904785156}\\\\n  step=180000: {\\\\\\\"step\\\\\\\": 180000, \\\\\\\"train_return\\\\\\\": 203.7918701171875}\\\\n  step=180000: {\\\\\\\"step\\\\\\\": 180000, \\\\\\\"train_return\\\\\\\": 187.43519592285156}\\\\n  step=180000: {\\\\\\\"step\\\\\\\": 180000, \\\\\\\"train_return\\\\\\\": 74.25837707519531}\\\\n  step=184000: {\\\\\\\"step\\\\\\\": 184000, \\\\\\\"train_return\\\\\\\": 79.65927124023438}\\\\n  step=184000: {\\\\\\\"step\\\\\\\": 184000, \\\\\\\"train_return\\\\\\\": 229.9039764404297}\\\\n  step=184000: {\\\\\\\"step\\\\\\\": 184000, \\\\\\\"train_return\\\\\\\": 285.094970703125}\\\\n  step=184000: {\\\\\\\"step\\\\\\\": 184000, \\\\\\\"train_return\\\\\\\": 60.712371826171875}\\\\n  step=185000: {\\\\\\\"step\\\\\\\": 185000, \\\\\\\"eval_return\\\\\\\": 208.4181335449219, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\n  step=185000: {\\\\\\\"step\\\\\\\": 185000, \\\\\\\"civo/ve_ratio\\\\\\\": 0.12025161113375325}\\\\n  step=188000: {\\\\\\\"step\\\\\\\": 188000, \\\\\\\"train_return\\\\\\\": 81.25110626220703}\\\\n  step=188000: {\\\\\\\"step\\\\\\\": 188000, \\\\\\\"train_return\\\\\\\": 185.87765502929688}\\\\n  step=188000: {\\\\\\\"step\\\\\\\": 188000, \\\\\\\"train_return\\\\\\\": 276.7749328613281}\\\\n  step=188000: {\\\\\\\"step\\\\\\\": 188000, \\\\\\\"train_return\\\\\\\": 138.64089965820312}\\\\n  step=192000: {\\\\\\\"step\\\\\\\": 192000, \\\\\\\"train_return\\\\\\\": 79.8086929321289}\\\\n  step=192000: {\\\\\\\"step\\\\\\\": 192000, \\\\\\\"train_return\\\\\\\": 290.1952209472656}\\\\n  step=192000: {\\\\\\\"step\\\\\\\": 192000, \\\\\\\"train_return\\\\\\\": 89.81228637695312}\\\\n  step=192000: {\\\\\\\"step\\\\\\\": 192000, \\\\\\\"train_return\\\\\\\": 56.90764617919922}\\\\n  step=195000: {\\\\\\\"step\\\\\\\": 195000, \\\\\\\"eval_return\\\\\\\": 221.71768188476562, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\n  step=195000: {\\\\\\\"step\\\\\\\": 195000, \\\\\\\"civo/ve_ratio\\\\\\\": 0.1084899494098272}\\\\n  step=196000: {\\\\\\\"step\\\\\\\": 196000, \\\\\\\"train_return\\\\\\\": 229.42941284179688}\\\\n  step=196000: {\\\\\\\"step\\\\\\\": 196000, \\\\\\\"train_return\\\\\\\": 207.6281280517578}\\\\n  step=196000: {\\\\\\\"step\\\\\\\": 196000, \\\\\\\"train_return\\\\\\\": 67.41763305664062}\\\\n  step=196000: {\\\\\\\"step\\\\\\\": 196000, \\\\\\\"train_return\\\\\\\": 122.93838500976562}\\\\n  step=200000: {\\\\\\\"step\\\\\\\": 200000, \\\\\\\"train_return\\\\\\\": 61.20667266845703}\\\\n  step=200000: {\\\\\\\"step\\\\\\\": 200000, \\\\\\\"train_return\\\\\\\": 165.01318359375}\\\\n  step=200000: {\\\\\\\"step\\\\\\\": 200000, \\\\\\\"train_return\\\\\\\": 106.95035552978516}\\\\n  step=200000: {\\\\\\\"step\\\\\\\": 200000, \\\\\\\"train_return\\\\\\\": 58.140647888183594}\\\\n  step=204000: {\\\\\\\"step\\\\\\\": 204000, \\\\\\\"train_return\\\\\\\": 68.50728607177734}\\\\n  step=204000: {\\\\\\\"step\\\\\\\": 204000, \\\\\\\"train_return\\\\\\\": 70.99976348876953}\\\\n  step=204000: {\\\\\\\"step\\\\\\\": 204000, \\\\\\\"train_return\\\\\\\": 95.0828857421875}\\\\n  step=204000: {\\\\\\\"step\\\\\\\": 204000, \\\\\\\"train_return\\\\\\\": 64.14974975585938}\\\\n  step=205000: {\\\\\\\"step\\\\\\\": 205000, \\\\\\\"eval_return\\\\\\\": 215.62352905273437, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\n  step=205000: {\\\\\\\"step\\\\\\\": 205000, \\\\\\\"civo/ve_ratio\\\\\\\": 0.10706286945628224}\\\\n  step=208000: {\\\\\\\"step\\\\\\\": 208000, \\\\\\\"train_return\\\\\\\": 55.24531173706055}\\\\n  step=208000: {\\\\\\\"step\\\\\\\": 208000, \\\\\\\"train_return\\\\\\\": 118.64993286132812}\\\\n  step=208000: {\\\\\\\"step\\\\\\\": 208000, \\\\\\\"train_return\\\\\\\": 119.94863891601562}\\\\n  step=208000: {\\\\\\\"step\\\\\\\": 208000, \\\\\\\"train_return\\\\\\\": 175.5042266845703}\\\\n  step=212000: {\\\\\\\"step\\\\\\\": 212000, \\\\\\\"train_return\\\\\\\": 68.51705932617188}\\\\n  step=212000: {\\\\\\\"step\\\\\\\": 212000, \\\\\\\"train_return\\\\\\\": 172.4085235595703}\\\\n  step=212000: {\\\\\\\"step\\\\\\\": 212000, \\\\\\\"train_return\\\\\\\": 55.939247131347656}\\\\n  step=212000: {\\\\\\\"step\\\\\\\": 212000, \\\\\\\"train_return\\\\\\\": 221.85865783691406}\\\\n  step=215000: {\\\\\\\"step\\\\\\\": 215000, \\\\\\\"eval_return\\\\\\\": 123.9377670288086, \\\\\\\"eval_length\\\\\\\": 500.0, \\\\\\\"eval_episodes\\\\\\\": 10.0}\\\\n  step=215000: {\\\\\\\"step\\\\\\\": 215000, \\\\\\\"civo/ve_ratio\\\\\\\": 0.17742178390818805}\\\\n  step=216000: {\\\\\\\"step\\\\\\\": 216000, \\\\\\\"train_return\\\\\\\": 129.0413818359375}\\\\n  step=216000: {\\\\\\\"step\\\\\\\": 216000, \\\\\\\"train_return\\\\\\\": 112.13914489746094}\\\\n  step=216000: {\\\\\\\"step\\\\\\\": 216000, \\\\\\\"train_return\\\\\\\": 115.97281646728516}\\\\n  step=216000: {\\\\\\\"step\\\\\\\": 216000, \\\\\\\"train_return\\\\\\\": 69.46036529541016}\\\\n  step=220000: {\\\\\\\"step\\\\\\\": 220000, \\\\\\\"train_return\\\\\\\": 204.3446502685547}\\\\n  step=220000: {\\\\\\\"step\\\\\\\": 220000, \\\\\\\"train_return\\\\\\\": 171.500244140625}\\\\n  step=220000: {\\\\\\\"step\\\\\\\": 220000, \\\\\\\"train_return\\\\\\\": 73.99068450927734}\\\\n  step=220000: {\\\\\\\"step\\\\\\\": 220000, \\\\\\\"train_return\\\\\\\": 112.25099182128906}\\\\n  step=224000: {\\\\\\\"step\\\\\\\": 224000, \\\\\\\"train_return\\\\\\\": 67.41929626464844}\\\\n  step=224000: {\\\\\\\"step\\\\\\\": 224000, \\\\\\\"train_return\\\\\\\": 67.7218017578125}\\\\n  step=224000: {\\\\\\\"step\\\\\\\": 224000, \\\\\\\"train_return\\\\\\\": 75.39198303222656}\\\\n  step=224000: {\\\\\\\"step\\\\\\\": 224000, \\\\\\\"train_return\\\\\\\": 114.04935455322266}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== exp_057 keys sample ===\\nstep=0: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\n  FULL: {\\\"step\\\": 0, \\\"dataset_size\\\": 2000.0, \\\"train_return\\\": 62.74878692626953, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 4.0}\\nstep=5000: ['step']\\nstep=5000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\n  FULL: {\\\"step\\\": 5000, \\\"eval_return\\\": 39.26672782897949, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\nstep=5000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', 'orientations_loss', 'post_ent', 'prior_ent', 'rep_loss', 'rep_scale', 'reward_loss', 'step', 'target_max', 'target_mean', 'target_min', 'target_std', 'update_count', 'value_grad_norm', 'value_loss', 'value_max', 'value_mean', 'value_min', 'value_std', 'velocity_loss']\\nstep=8000: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\n  FULL: {\\\"step\\\": 8000, \\\"dataset_size\\\": 4000.0, \\\"train_return\\\": 39.657447814941406, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 8.0}\\nstep=15000: ['step']\\nstep=15000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\n  FULL: {\\\"step\\\": 15000, \\\"eval_return\\\": 181.96920776367188, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\nstep=15000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'civo/alert', 'civo/delta_ve', 'civo/ve_ratio', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', 'orientations_loss', 'post_ent', 'prior_ent', 'rep_loss', 'rep_scale', 'reward_loss', 'step', 'target_max', 'target_mean', 'target_min', 'target_std', 'update_count', 'value_grad_norm', 'value_loss', 'value_max', 'value_mean', 'value_min', 'value_std', 'velocity_loss']\\nstep=16000: ['dataset_size', 'step', 'train_episodes', 'train_length', 'train_return']\\n  FULL: {\\\"step\\\": 16000, \\\"dataset_size\\\": 8000.0, \\\"train_return\\\": 152.9766845703125, \\\"train_length\\\": 500.0, \\\"train_episodes\\\": 16.0}\\nstep=25000: ['step']\\nstep=25000: ['eval_episodes', 'eval_length', 'eval_return', 'step']\\n  FULL: {\\\"step\\\": 25000, \\\"eval_return\\\": 184.06726837158203, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\nstep=25000: ['EMA_005', 'EMA_095', 'actor_entropy', 'actor_grad_norm', 'actor_loss', 'civo/alert', 'civo/delta_ve', 'civo/ve_ratio', 'cont_loss', 'dyn_loss', 'dyn_scale', 'fps', 'gate_dt_1_frac', 'gate_dt_2_frac', 'gate_dt_3_frac', 'gate_dt_4_frac', 'gate_dt_5_frac', 'gate_dt_6_frac', 'gate_dt_7_frac', 'gate_dt_8_frac', 'gate_dt_autocorr', 'gate_dt_max', 'gate_dt_mean', 'gate_dt_min', 'gate_dt_std', 'gate_empirical_entropy', 'gate_entropy_ratio', 'height_loss', 'imag_action_max', 'imag_action_mean', 'imag_action_min', 'imag_action_std', 'imag_reward_max', 'imag_reward_mean', 'imag_reward_min', 'imag_reward_std', 'kl', 'kl_free', 'model_grad_norm', 'model_loss', 'normed_target_max', 'normed_target_mean', 'normed_target_min', 'normed_target_std', '\\n\\n... [截断: 输出过长，省略 42575 字符] ...\\n\\nstep\\\": 176000, \\\"train_return\\\": 61.60499572753906}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 72.96839904785156}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 203.7918701171875}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 187.43519592285156}\\n  step=180000: {\\\"step\\\": 180000, \\\"train_return\\\": 74.25837707519531}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 79.65927124023438}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 229.9039764404297}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 285.094970703125}\\n  step=184000: {\\\"step\\\": 184000, \\\"train_return\\\": 60.712371826171875}\\n  step=185000: {\\\"step\\\": 185000, \\\"eval_return\\\": 208.4181335449219, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=185000: {\\\"step\\\": 185000, \\\"civo/ve_ratio\\\": 0.12025161113375325}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 81.25110626220703}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 185.87765502929688}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 276.7749328613281}\\n  step=188000: {\\\"step\\\": 188000, \\\"train_return\\\": 138.64089965820312}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 79.8086929321289}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 290.1952209472656}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 89.81228637695312}\\n  step=192000: {\\\"step\\\": 192000, \\\"train_return\\\": 56.90764617919922}\\n  step=195000: {\\\"step\\\": 195000, \\\"eval_return\\\": 221.71768188476562, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=195000: {\\\"step\\\": 195000, \\\"civo/ve_ratio\\\": 0.1084899494098272}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 229.42941284179688}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 207.6281280517578}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 67.41763305664062}\\n  step=196000: {\\\"step\\\": 196000, \\\"train_return\\\": 122.93838500976562}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 61.20667266845703}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 165.01318359375}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 106.95035552978516}\\n  step=200000: {\\\"step\\\": 200000, \\\"train_return\\\": 58.140647888183594}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 68.50728607177734}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 70.99976348876953}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 95.0828857421875}\\n  step=204000: {\\\"step\\\": 204000, \\\"train_return\\\": 64.14974975585938}\\n  step=205000: {\\\"step\\\": 205000, \\\"eval_return\\\": 215.62352905273437, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=205000: {\\\"step\\\": 205000, \\\"civo/ve_ratio\\\": 0.10706286945628224}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 55.24531173706055}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 118.64993286132812}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 119.94863891601562}\\n  step=208000: {\\\"step\\\": 208000, \\\"train_return\\\": 175.5042266845703}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 68.51705932617188}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 172.4085235595703}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 55.939247131347656}\\n  step=212000: {\\\"step\\\": 212000, \\\"train_return\\\": 221.85865783691406}\\n  step=215000: {\\\"step\\\": 215000, \\\"eval_return\\\": 123.9377670288086, \\\"eval_length\\\": 500.0, \\\"eval_episodes\\\": 10.0}\\n  step=215000: {\\\"step\\\": 215000, \\\"civo/ve_ratio\\\": 0.17742178390818805}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 129.0413818359375}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 112.13914489746094}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 115.97281646728516}\\n  step=216000: {\\\"step\\\": 216000, \\\"train_return\\\": 69.46036529541016}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 204.3446502685547}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 171.500244140625}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 73.99068450927734}\\n  step=220000: {\\\"step\\\": 220000, \\\"train_return\\\": 112.25099182128906}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 67.41929626464844}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 67.7218017578125}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 75.39198303222656}\\n  step=224000: {\\\"step\\\": 224000, \\\"train_return\\\": 114.04935455322266}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
I can see that `civo/ve_ratio` is the field name in the metrics, not just `ve_ratio`. And it's logged at eval checkpoints (every 10K). Now let me extract the civo/ve_ratio values for exp_057 and the baseline at the relevant timesteps. Let me also check what the baseline logs as civo/ve_ratio — wait, the baseline wouldn't have civo/ve_ratio because civo monitoring is only added for the gate experiments.

For the baseline, I need to compute ve_ratio = value_mean / eval_return manually.


Extracting the data now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "7f18b749-a2b4-444f-8ab6-4b8a9b7db686",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cf6FQJGJ9KRZWcWHXqSCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5003,
      "cache_read_input_tokens": 69890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5003
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

_source line 57_

字段名是 `civo/ve_ratio`。现在提取两个实验的精确数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "583d0449-3c7c-4c57-a58c-213d5d884991",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cf6FQJGJ9KRZWcWHXqSCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5003,
      "cache_read_input_tokens": 69890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5003
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01FqG7mU5qmXJdsJ31PCnmFM`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cd /root/autodl-tmp/event-gated-adaptive-horizon && python3 -c \"\nimport json\n\n# === exp_057: extract civo/ve_ratio and eval_return ===\nprint('=== exp_057 civo/ve_ratio + eval_return ===')\nwith open('logdir/exp_057_frozen_dt_emb_walker_s2/metrics.jsonl') as f:\n    for line in f:\n        m = json.loads(line)\n        step = m.get('step', 0)\n        if 'civo/ve_ratio' in m:\n            print(f'  step={step}, civo/ve_ratio={m[\\\"civo/ve_ratio\\\"]:.6f}')\n        elif 'eval_return' in m and step >= 5000:\n            print(f'  step={step}, eval_return={m[\\\"eval_return\\\"]:.2f}')\n\nprint()\n\n# === exp_009a baseline s2: compute ve_ratio = value_mean / eval_return ===\nprint('=== exp_009a baseline s2: value_mean + eval_return ===')\neval_returns = {}\nvalue_means = {}\nwith open('logdir/exp_009a_baseline_walker_s2/metrics.jsonl') as f:\n    for line in f:\n        m = json.loads(line)\n        step = m.get('step', 0)\n        if 'eval_return' in m:\n            eval_returns[step] = m['eval_return']\n        if 'value_mean' in m:\n            value_means[step] = m['value_mean']\n\n# Compute ve_ratio at eval steps\nfor step in sorted(eval_returns.keys()):\n    if step >= 5000:\n        ev = eval_returns[step]\n        # Find closest value_mean\n        vm = value_means.get(step, None)\n        if vm is None:\n            # Try nearby steps\n            for delta in [0, 5000, -5000, 10000, -10000]:\n                if step + delta in value_means:\n                    vm = value_means[step + delta]\n                    break\n        if vm is not None and ev > 0:\n            ve = vm / ev\n            print(f'  step={step}, eval_return={ev:.2f}, value_mean={vm:.2f}, ve_ratio={ve:.4f}')\n        else:\n            print(f'  step={step}, eval_return={ev:.2f}, value_mean=N/A')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "ac5a7528-d270-4bd5-9840-535f7ab6ca6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cf6FQJGJ9KRZWcWHXqSCV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5003,
      "cache_read_input_tokens": 69890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5003
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

_source line 59 · 2026-05-24T01:53:42.050Z_

<details><summary>↩ Tool result · `toolu_01FqG7mU5qmXJdsJ31PCnmFM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== exp_057 civo/ve_ratio + eval_return ===\\n  step=5000, eval_return=39.27\\n  step=15000, eval_return=181.97\\n  step=15000, civo/ve_ratio=0.020433\\n  step=25000, eval_return=184.07\\n  step=25000, civo/ve_ratio=0.136940\\n  step=35000, eval_return=94.98\\n  step=35000, civo/ve_ratio=0.494518\\n  step=45000, eval_return=106.39\\n  step=45000, civo/ve_ratio=0.614521\\n  step=55000, eval_return=110.73\\n  step=55000, civo/ve_ratio=0.746827\\n  step=65000, eval_return=103.36\\n  step=65000, civo/ve_ratio=0.715091\\n  step=75000, eval_return=93.78\\n  step=75000, civo/ve_ratio=0.619483\\n  step=85000, eval_return=83.76\\n  step=85000, civo/ve_ratio=0.605900\\n  step=95000, eval_return=75.52\\n  step=95000, civo/ve_ratio=0.635865\\n  step=105000, eval_return=81.85\\n  step=105000, civo/ve_ratio=0.543658\\n  step=115000, eval_return=31.56\\n  step=115000, civo/ve_ratio=1.282565\\n  step=125000, eval_return=51.25\\n  step=125000, civo/ve_ratio=0.731515\\n  step=135000, eval_return=32.68\\n  step=135000, civo/ve_ratio=1.068784\\n  step=145000, eval_return=28.36\\n  step=145000, civo/ve_ratio=1.163372\\n  step=155000, eval_return=71.94\\n  step=155000, civo/ve_ratio=0.451984\\n  step=165000, eval_return=115.12\\n  step=165000, civo/ve_ratio=0.271504\\n  step=175000, eval_return=190.16\\n  step=175000, civo/ve_ratio=0.146028\\n  step=185000, eval_return=208.42\\n  step=185000, civo/ve_ratio=0.120252\\n  step=195000, eval_return=221.72\\n  step=195000, civo/ve_ratio=0.108490\\n  step=205000, eval_return=215.62\\n  step=205000, civo/ve_ratio=0.107063\\n  step=215000, eval_return=123.94\\n  step=215000, civo/ve_ratio=0.177422\\n\\n=== exp_009a baseline s2: value_mean + eval_return ===\\n  step=5000, eval_return=41.21, value_mean=0.00, ve_ratio=0.0000\\n  step=15000, eval_return=106.01, value_mean=7.34, ve_ratio=0.0693\\n  step=25000, eval_return=325.33, value_mean=45.78, ve_ratio=0.1407\\n  step=35000, eval_return=354.49, value_mean=108.32, ve_ratio=0.3056\\n  step=45000, eval_return=498.01, value_mean=180.74, ve_ratio=0.3629\\n  step=55000, eval_return=534.13, value_mean=253.49, ve_ratio=0.4746\\n  step=65000, eval_return=688.87, value_mean=326.34, ve_ratio=0.4737\\n  step=75000, eval_return=656.85, value_mean=392.43, ve_ratio=0.5974\\n  step=85000, eval_return=618.73, value_mean=450.50, ve_ratio=0.7281\\n  step=95000, eval_return=596.24, value_mean=503.74, ve_ratio=0.8449\\n  step=105000, eval_return=836.51, value_mean=539.34, ve_ratio=0.6447\\n  step=115000, eval_return=804.79, value_mean=574.93, ve_ratio=0.7144\\n  step=125000, eval_return=865.48, value_mean=612.48, ve_ratio=0.7077\\n  step=135000, eval_return=876.08, value_mean=628.15, ve_ratio=0.7170\\n  step=145000, eval_return=869.18, value_mean=629.36, ve_ratio=0.7241\\n  step=155000, eval_return=778.99, value_mean=633.42, ve_ratio=0.8131\\n  step=165000, eval_return=864.03, value_mean=641.36, ve_ratio=0.7423\\n  step=175000, eval_return=850.53, value_mean=647.73, ve_ratio=0.7616\\n  step=185000, eval_return=907.31, value_mean=653.01, ve_ratio=0.7197\\n  step=195000, eval_return=873.49, value_mean=656.44, ve_ratio=0.7515\\n  step=205000, eval_return=887.02, value_mean=658.92, ve_ratio=0.7428\\n  step=215000, eval_return=956.04, value_mean=661.17, ve_ratio=0.6916\\n  step=225000, eval_return=892.09, value_mean=662.24, ve_ratio=0.7423\\n  step=235000, eval_return=914.78, value_mean=663.00, ve_ratio=0.7248\\n  step=245000, eval_return=950.32, value_mean=663.83, ve_ratio=0.6985\\n  step=255000, eval_return=936.90, value_mean=663.87, ve_ratio=0.7086\\n  step=265000, eval_return=937.27, value_mean=663.68, ve_ratio=0.7081\\n  step=275000, eval_return=934.78, value_mean=663.68, ve_ratio=0.7100\\n  step=285000, eval_return=960.20, value_mean=664.02, ve_ratio=0.6915\\n  step=295000, eval_return=947.46, value_mean=664.07, ve_ratio=0.7009\\n  step=305000, eval_return=937.80, value_mean=663.86, ve_ratio=0.7079\\n  step=315000, eval_return=948.66, value_mean=663.27, ve_ratio=0.6992\\n  step=325000, eval_return=930.61, value_mean=663.37, ve_ratio=0.7128\\n  step=335000, eval_return=919.23, value_mean=663.36, ve_ratio=0.7216\\n  step=345000, eval_return=816.18, value_mean=663.60, ve_ratio=0.8131\\n  step=355000, eval_return=932.45, value_mean=663.78, ve_ratio=0.7119\\n  step=365000, eval_return=943.13, value_mean=664.18, ve_ratio=0.7042\\n  step=375000, eval_return=952.86, value_mean=663.90, ve_ratio=0.6967\\n  step=385000, eval_return=942.31, value_mean=663.41, ve_ratio=0.7040\\n  step=395000, eval_return=966.94, value_mean=663.50, ve_ratio=0.6862\\n  step=405000, eval_return=948.01, value_mean=663.95, ve_ratio=0.7004\\n  step=415000, eval_return=957.06, value_mean=664.26, ve_ratio=0.6941\\n  step=425000, eval_return=939.37, value_mean=664.27, ve_ratio=0.7071\\n  step=435000, eval_return=963.65, value_mean=664.53, ve_ratio=0.6896\\n  step=445000, eval_return=948.42, value_mean=664.44, ve_ratio=0.7006\\n  step=455000, eval_return=937.72, value_mean=664.42, ve_ratio=0.7086\\n  step=465000, eval_return=939.54, value_mean=664.44, ve_ratio=0.7072\\n  step=475000, eval_return=965.94, value_mean=664.68, ve_ratio=0.6881\\n  step=485000, eval_return=916.74, value_mean=664.98, ve_ratio=0.7254\\n  step=495000, eval_return=945.58, value_mean=665.07, ve_ratio=0.7033\\n  step=505000, eval_return=957.87, value_mean=665.17, ve_ratio=0.6944\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "4bfb9982-3932-42c2-a099-d98156212328",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== exp_057 civo/ve_ratio + eval_return ===\\\\n  step=5000, eval_return=39.27\\\\n  step=15000, eval_return=181.97\\\\n  step=15000, civo/ve_ratio=0.020433\\\\n  step=25000, eval_return=184.07\\\\n  step=25000, civo/ve_ratio=0.136940\\\\n  step=35000, eval_return=94.98\\\\n  step=35000, civo/ve_ratio=0.494518\\\\n  step=45000, eval_return=106.39\\\\n  step=45000, civo/ve_ratio=0.614521\\\\n  step=55000, eval_return=110.73\\\\n  step=55000, civo/ve_ratio=0.746827\\\\n  step=65000, eval_return=103.36\\\\n  step=65000, civo/ve_ratio=0.715091\\\\n  step=75000, eval_return=93.78\\\\n  step=75000, civo/ve_ratio=0.619483\\\\n  step=85000, eval_return=83.76\\\\n  step=85000, civo/ve_ratio=0.605900\\\\n  step=95000, eval_return=75.52\\\\n  step=95000, civo/ve_ratio=0.635865\\\\n  step=105000, eval_return=81.85\\\\n  step=105000, civo/ve_ratio=0.543658\\\\n  step=115000, eval_return=31.56\\\\n  step=115000, civo/ve_ratio=1.282565\\\\n  step=125000, eval_return=51.25\\\\n  step=125000, civo/ve_ratio=0.731515\\\\n  step=135000, eval_return=32.68\\\\n  step=135000, civo/ve_ratio=1.068784\\\\n  step=145000, eval_return=28.36\\\\n  step=145000, civo/ve_ratio=1.163372\\\\n  step=155000, eval_return=71.94\\\\n  step=155000, civo/ve_ratio=0.451984\\\\n  step=165000, eval_return=115.12\\\\n  step=165000, civo/ve_ratio=0.271504\\\\n  step=175000, eval_return=190.16\\\\n  step=175000, civo/ve_ratio=0.146028\\\\n  step=185000, eval_return=208.42\\\\n  step=185000, civo/ve_ratio=0.120252\\\\n  step=195000, eval_return=221.72\\\\n  step=195000, civo/ve_ratio=0.108490\\\\n  step=205000, eval_return=215.62\\\\n  step=205000, civo/ve_ratio=0.107063\\\\n  step=215000, eval_return=123.94\\\\n  step=215000, civo/ve_ratio=0.177422\\\\n\\\\n=== exp_009a baseline s2: value_mean + eval_return ===\\\\n  step=5000, eval_return=41.21, value_mean=0.00, ve_ratio=0.0000\\\\n  step=15000, eval_return=106.01, value_mean=7.34, ve_ratio=0.0693\\\\n  step=25000, eval_return=325.33, value_mean=45.78, ve_ratio=0.1407\\\\n  step=35000, eval_return=354.49, value_mean=108.32, ve_ratio=0.3056\\\\n  step=45000, eval_return=498.01, value_mean=180.74, ve_ratio=0.3629\\\\n  step=55000, eval_return=534.13, value_mean=253.49, ve_ratio=0.4746\\\\n  step=65000, eval_return=688.87, value_mean=326.34, ve_ratio=0.4737\\\\n  step=75000, eval_return=656.85, value_mean=392.43, ve_ratio=0.5974\\\\n  step=85000, eval_return=618.73, value_mean=450.50, ve_ratio=0.7281\\\\n  step=95000, eval_return=596.24, value_mean=503.74, ve_ratio=0.8449\\\\n  step=105000, eval_return=836.51, value_mean=539.34, ve_ratio=0.6447\\\\n  step=115000, eval_return=804.79, value_mean=574.93, ve_ratio=0.7144\\\\n  step=125000, eval_return=865.48, value_mean=612.48, ve_ratio=0.7077\\\\n  step=135000, eval_return=876.08, value_mean=628.15, ve_ratio=0.7170\\\\n  step=145000, eval_return=869.18, value_mean=629.36, ve_ratio=0.7241\\\\n  step=155000, eval_return=778.99, value_mean=633.42, ve_ratio=0.8131\\\\n  step=165000, eval_return=864.03, value_mean=641.36, ve_ratio=0.7423\\\\n  step=175000, eval_return=850.53, value_mean=647.73, ve_ratio=0.7616\\\\n  step=185000, eval_return=907.31, value_mean=653.01, ve_ratio=0.7197\\\\n  step=195000, eval_return=873.49, value_mean=656.44, ve_ratio=0.7515\\\\n  step=205000, eval_return=887.02, value_mean=658.92, ve_ratio=0.7428\\\\n  step=215000, eval_return=956.04, value_mean=661.17, ve_ratio=0.6916\\\\n  step=225000, eval_return=892.09, value_mean=662.24, ve_ratio=0.7423\\\\n  step=235000, eval_return=914.78, value_mean=663.00, ve_ratio=0.7248\\\\n  step=245000, eval_return=950.32, value_mean=663.83, ve_ratio=0.6985\\\\n  step=255000, eval_return=936.90, value_mean=663.87, ve_ratio=0.7086\\\\n  step=265000, eval_return=937.27, value_mean=663.68, ve_ratio=0.7081\\\\n  step=275000, eval_return=934.78, value_mean=663.68, ve_ratio=0.7100\\\\n  step=285000, eval_return=960.20, value_mean=664.02, ve_ratio=0.6915\\\\n  step=295000, eval_return=947.46, value_mean=664.07, ve_ratio=0.7009\\\\n  step=305000, eval_return=937.80, value_mean=663.86, ve_ratio=0.7079\\\\n  step=315000, eval_return=948.66, value_mean=663.27, ve_ratio=0.6992\\\\n  step=325000, eval_return=930.61, value_mean=663.37, ve_ratio=0.7128\\\\n  step=335000, eval_return=919.23, value_mean=663.36, ve_ratio=0.7216\\\\n  step=345000, eval_return=816.18, value_mean=663.60, ve_ratio=0.8131\\\\n  step=355000, eval_return=932.45, value_mean=663.78, ve_ratio=0.7119\\\\n  step=365000, eval_return=943.13, value_mean=664.18, ve_ratio=0.7042\\\\n  step=375000, eval_return=952.86, value_mean=663.90, ve_ratio=0.6967\\\\n  step=385000, eval_return=942.31, value_mean=663.41, ve_ratio=0.7040\\\\n  step=395000, eval_return=966.94, value_mean=663.50, ve_ratio=0.6862\\\\n  step=405000, eval_return=948.01, value_mean=663.95, ve_ratio=0.7004\\\\n  step=415000, eval_return=957.06, value_mean=664.26, ve_ratio=0.6941\\\\n  step=425000, eval_return=939.37, value_mean=664.27, ve_ratio=0.7071\\\\n  step=435000, eval_return=963.65, value_mean=664.53, ve_ratio=0.6896\\\\n  step=445000, eval_return=948.42, value_mean=664.44, ve_ratio=0.7006\\\\n  step=455000, eval_return=937.72, value_mean=664.42, ve_ratio=0.7086\\\\n  step=465000, eval_return=939.54, value_mean=664.44, ve_ratio=0.7072\\\\n  step=475000, eval_return=965.94, value_mean=664.68, ve_ratio=0.6881\\\\n  step=485000, eval_return=916.74, value_mean=664.98, ve_ratio=0.7254\\\\n  step=495000, eval_return=945.58, value_mean=665.07, ve_ratio=0.7033\\\\n  step=505000, eval_return=957.87, value_mean=665.17, ve_ratio=0.6944\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== exp_057 civo/ve_ratio + eval_return ===\\n  step=5000, eval_return=39.27\\n  step=15000, eval_return=181.97\\n  step=15000, civo/ve_ratio=0.020433\\n  step=25000, eval_return=184.07\\n  step=25000, civo/ve_ratio=0.136940\\n  step=35000, eval_return=94.98\\n  step=35000, civo/ve_ratio=0.494518\\n  step=45000, eval_return=106.39\\n  step=45000, civo/ve_ratio=0.614521\\n  step=55000, eval_return=110.73\\n  step=55000, civo/ve_ratio=0.746827\\n  step=65000, eval_return=103.36\\n  step=65000, civo/ve_ratio=0.715091\\n  step=75000, eval_return=93.78\\n  step=75000, civo/ve_ratio=0.619483\\n  step=85000, eval_return=83.76\\n  step=85000, civo/ve_ratio=0.605900\\n  step=95000, eval_return=75.52\\n  step=95000, civo/ve_ratio=0.635865\\n  step=105000, eval_return=81.85\\n  step=105000, civo/ve_ratio=0.543658\\n  step=115000, eval_return=31.56\\n  step=115000, civo/ve_ratio=1.282565\\n  step=125000, eval_return=51.25\\n  step=125000, civo/ve_ratio=0.731515\\n  step=135000, eval_return=32.68\\n  step=135000, civo/ve_ratio=1.068784\\n  step=145000, eval_return=28.36\\n  step=145000, civo/ve_ratio=1.163372\\n  step=155000, eval_return=71.94\\n  step=155000, civo/ve_ratio=0.451984\\n  step=165000, eval_return=115.12\\n  step=165000, civo/ve_ratio=0.271504\\n  step=175000, eval_return=190.16\\n  step=175000, civo/ve_ratio=0.146028\\n  step=185000, eval_return=208.42\\n  step=185000, civo/ve_ratio=0.120252\\n  step=195000, eval_return=221.72\\n  step=195000, civo/ve_ratio=0.108490\\n  step=205000, eval_return=215.62\\n  step=205000, civo/ve_ratio=0.107063\\n  step=215000, eval_return=123.94\\n  step=215000, civo/ve_ratio=0.177422\\n\\n=== exp_009a baseline s2: value_mean + eval_return ===\\n  step=5000, eval_return=41.21, value_mean=0.00, ve_ratio=0.0000\\n  step=15000, eval_return=106.01, value_mean=7.34, ve_ratio=0.0693\\n  step=25000, eval_return=325.33, value_mean=45.78, ve_ratio=0.1407\\n  step=35000, eval_return=354.49, value_mean=108.32, ve_ratio=0.3056\\n  step=45000, eval_return=498.01, value_mean=180.74, ve_ratio=0.3629\\n  step=55000, eval_return=534.13, value_mean=253.49, ve_ratio=0.4746\\n  step=65000, eval_return=688.87, value_mean=326.34, ve_ratio=0.4737\\n  step=75000, eval_return=656.85, value_mean=392.43, ve_ratio=0.5974\\n  step=85000, eval_return=618.73, value_mean=450.50, ve_ratio=0.7281\\n  step=95000, eval_return=596.24, value_mean=503.74, ve_ratio=0.8449\\n  step=105000, eval_return=836.51, value_mean=539.34, ve_ratio=0.6447\\n  step=115000, eval_return=804.79, value_mean=574.93, ve_ratio=0.7144\\n  step=125000, eval_return=865.48, value_mean=612.48, ve_ratio=0.7077\\n  step=135000, eval_return=876.08, value_mean=628.15, ve_ratio=0.7170\\n  step=145000, eval_return=869.18, value_mean=629.36, ve_ratio=0.7241\\n  step=155000, eval_return=778.99, value_mean=633.42, ve_ratio=0.8131\\n  step=165000, eval_return=864.03, value_mean=641.36, ve_ratio=0.7423\\n  step=175000, eval_return=850.53, value_mean=647.73, ve_ratio=0.7616\\n  step=185000, eval_return=907.31, value_mean=653.01, ve_ratio=0.7197\\n  step=195000, eval_return=873.49, value_mean=656.44, ve_ratio=0.7515\\n  step=205000, eval_return=887.02, value_mean=658.92, ve_ratio=0.7428\\n  step=215000, eval_return=956.04, value_mean=661.17, ve_ratio=0.6916\\n  step=225000, eval_return=892.09, value_mean=662.24, ve_ratio=0.7423\\n  step=235000, eval_return=914.78, value_mean=663.00, ve_ratio=0.7248\\n  step=245000, eval_return=950.32, value_mean=663.83, ve_ratio=0.6985\\n  step=255000, eval_return=936.90, value_mean=663.87, ve_ratio=0.7086\\n  step=265000, eval_return=937.27, value_mean=663.68, ve_ratio=0.7081\\n  step=275000, eval_return=934.78, value_mean=663.68, ve_ratio=0.7100\\n  step=285000, eval_return=960.20, value_mean=664.02, ve_ratio=0.6915\\n  step=295000, eval_return=947.46, value_mean=664.07, ve_ratio=0.7009\\n  step=305000, eval_return=937.80, value_mean=663.86, ve_ratio=0.7079\\n  step=315000, eval_return=948.66, value_mean=663.27, ve_ratio=0.6992\\n  step=325000, eval_return=930.61, value_mean=663.37, ve_ratio=0.7128\\n  step=335000, eval_return=919.23, value_mean=663.36, ve_ratio=0.7216\\n  step=345000, eval_return=816.18, value_mean=663.60, ve_ratio=0.8131\\n  step=355000, eval_return=932.45, value_mean=663.78, ve_ratio=0.7119\\n  step=365000, eval_return=943.13, value_mean=664.18, ve_ratio=0.7042\\n  step=375000, eval_return=952.86, value_mean=663.90, ve_ratio=0.6967\\n  step=385000, eval_return=942.31, value_mean=663.41, ve_ratio=0.7040\\n  step=395000, eval_return=966.94, value_mean=663.50, ve_ratio=0.6862\\n  step=405000, eval_return=948.01, value_mean=663.95, ve_ratio=0.7004\\n  step=415000, eval_return=957.06, value_mean=664.26, ve_ratio=0.6941\\n  step=425000, eval_return=939.37, value_mean=664.27, ve_ratio=0.7071\\n  step=435000, eval_return=963.65, value_mean=664.53, ve_ratio=0.6896\\n  step=445000, eval_return=948.42, value_mean=664.44, ve_ratio=0.7006\\n  step=455000, eval_return=937.72, value_mean=664.42, ve_ratio=0.7086\\n  step=465000, eval_return=939.54, value_mean=664.44, ve_ratio=0.7072\\n  step=475000, eval_return=965.94, value_mean=664.68, ve_ratio=0.6881\\n  step=485000, eval_return=916.74, value_mean=664.98, ve_ratio=0.7254\\n  step=495000, eval_return=945.58, value_mean=665.07, ve_ratio=0.7033\\n  step=505000, eval_return=957.87, value_mean=665.17, ve_ratio=0.6944\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Now I have the precise data. Let me compute the NVE values.

**exp_057 at 115K:**
- civo/ve_ratio = 1.282565
- eval_return = 31.56

**exp_009a baseline s2 at 115K:**
- ve_ratio = 0.7144 (value_mean=574.93, eval_return=804.79)

**NVE(exp_057@115K) = 1.282565 / 0.7144 = 1.7953**

This exceeds 1.5x! The reviewer is correct, and the "no_civo" classification is wrong.


I'm verifying the NVE definition against the paper — it's the ratio of the experiment's v/e ratio to the baseline's v/e ratio at the same training step. My calculation confirms NVE = 1.795, which is well above the 1.5x threshold.

Now I need to determine whether `civo/ve_ratio` in the data is already the normalized ratio or the raw v/e value. Looking at the registry entries and how they're referenced in the paper framing, `civo/ve_ratio` appears to be the raw v/e ratio, not the normalized version.

To compute the actual NVE, I divide the raw v/e ratio by the baseline v/e ratio — so for exp_057 at 115K, that's 1.2826 divided by 0.7144, giving me 1.795. But I need to confirm which baseline experiment the paper uses for all these calculations, since it might not be the seed-matched one.

Looking at the paper's baseline calibration data, exp_001_baseline (seed 0) appears to be the reference point across all NVE computations. Now I'm trying to extract the v/e ratio for exp_001_baseline at 115K to use as my denominator, but the registry only has explicit values up to 105K, so I need to interpolate or find the 115K eval return and value mean from the trajectory data. I need to track down the exp_001 baseline data at 115K steps. Looking at the directory listing, I see exp_001_baseline exists for seeds 2, 3, and 4, but I'm comparing against exp_009a which is the baseline for seed 2. Let me check if I can pull the value_eval_ratio at 115K from the exp_001_baseline_s2 registry to make a proper comparison.

Actually, the paper uses exp_001_baseline (seed 0) as the standard reference, so I should use that for NVE normalization. From the data I have, exp_001 shows a ve_ratio of 0.656 at 105K, and extrapolating to 115K gives roughly 0.67. This puts the NVE at approximately 1.91 when dividing 1.2826 by 0.67, compared to 1.80 using exp_009a's 0.7144 ratio—both well above the 1.5x threshold.

Now checking the other seeds: exp_042 (seed 0) has an nve_peak of 0.194 from the registry, which is far below 1.5x. But exp_047 (seed 1) shows nve_peak = 1.71 at 95K, exceeding the threshold. This is puzzling since the paper marks exp_057 as "no_civo" but the records indicate exp_047 already crossed 1.5x—I need to understand how that was originally classified.

Looking back at the memory, exp_047 was marked as transient with NVE peaking at 1.71 but self-correcting down to 0.56, which explains why it was labeled as having no sustained CIVO despite the peak. For exp_057, the registry shows s0=0.19, s1=1.71, and s2=1.28, but I'm realizing the 1.28 is the ve_ratio_peak rather than the NVE itself, and it's being conflated with the other values.

The actual NVE for exp_057 should be around 1.80, not 1.28. Now I need to compute the NVE values for all three seeds to get consistent measurements—I have 0.194 for exp_042, 1.71 for exp_047, and for exp_057 I need to figure out which baseline was used to convert the ve_ratio_peak of 1.283 into the proper NVE.

Looking at exp_047 more carefully, the NVE peaks at 95K with a value of 1.71, but the ve_ratio peaks earlier at 75K with 1.099. If the baseline at 95K is 0.632, then the ve_ratio at that step would be 1.71 × 0.632 = 1.081, which makes sense as a slightly lower value than the earlier peak.

For exp_057 at 115K, I'm trying to determine the right baseline to use. The same-seed baseline (exp_009a for seed 2) gives ve_ratio@115K = 0.7144, which yields NVE = 1.2826 / 0.7144 = 1.795. I need to check whether the paper consistently uses exp_001 as the baseline or switches to same-seed baselines for different seeds.

Looking at exp_001's data, I have ve_ratio at 105K (0.656) but not at 115K. The registry doesn't contain the full value trajectory for exp_001 at that step, and I'm not sure if the baseline logs are available on the server to compute it directly.

Actually, I should just use the same baseline approach that was applied to exp_047 for consistency. But I think I have what I need: exp_057 at 115K gives me a civo/ve_ratio of 1.2826, and using the same-seed baseline (exp_009a) with ve_ratio of 0.7144 at 115K, I get an NVE of 1.795—which makes sense given the reviewer's 0.65 estimate was for a different seed.

So exp_042 shows a peak NVE of 0.194, well below the 1.5x threshold, while exp_047 hits 1.71 at 95K which exceeds it transiently. The key issue is that exp_057's classification as "no_civo" doesn't hold up—with an NVE of 1.795, it clearly exceeds 1.5x. I should double-check whether the paper's NVE definition might have shifted or if there's a different calculation being used for the frozen experiments, so let me search the tex files for how NVE is actually defined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "49fb3a3b-9252-4b55-847f-e113a884e0a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5M7hka7EKUgW7o8UFBmdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3380,
      "cache_read_input_tokens": 74893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3380
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

数据已提取。现在计算精确 NVE 值。同时搜索论文中的 NVE 定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "20b00acf-ed66-4a4a-b3ab-6c7616278f29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5M7hka7EKUgW7o8UFBmdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3380,
      "cache_read_input_tokens": 74893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3380
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

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FT2H2m81Q31TVXMSV1b3UE`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"nve\\|NVE\\|ve_ratio\\|overshoot\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "571f8fc2-da40-488e-bc3f-0b11e38138aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5M7hka7EKUgW7o8UFBmdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3380,
      "cache_read_input_tokens": 74893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3380
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

_source line 63 · 2026-05-24T01:54:55.426Z_

<details><summary>↩ Tool result · `toolu_01FT2H2m81Q31TVXMSV1b3UE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d0958dfa-7735-4a31-86bd-7bfcc4991b05",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01G8xTr135mmZBPHyQLjhQUj`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cd /root/autodl-tmp/event-gated-adaptive-horizon && python3 -c \"\n# Compute NVE for all three Walker frozen seeds\n# NVE = exp_ve_ratio / baseline_ve_ratio at same step\n\n# Baseline (exp_009a s2) ve_ratio trajectory\nbaseline_s2 = {\n    25: 0.1407, 35: 0.3056, 45: 0.3629, 55: 0.4746,\n    65: 0.4737, 75: 0.5974, 85: 0.7281, 95: 0.8449,\n    105: 0.6447, 115: 0.7144, 125: 0.7077, 135: 0.7170,\n    145: 0.7241, 155: 0.8131\n}\n\n# exp_001 baseline (s0) ve_ratio from registry\nbaseline_s0 = {\n    25: 0.087, 35: 0.241, 45: 0.331, 55: 0.404,\n    65: 0.563, 75: 0.719, 85: 0.701, 95: 0.632, 105: 0.656\n}\n\n# exp_057 (s2) civo/ve_ratio at all eval steps\nexp057 = {\n    15: 0.020433, 25: 0.136940, 35: 0.494518, 45: 0.614521,\n    55: 0.746827, 65: 0.715091, 75: 0.619483, 85: 0.605900,\n    95: 0.635865, 105: 0.543658, 115: 1.282565, 125: 0.731515,\n    135: 1.068784, 145: 1.163372, 155: 0.451984, 165: 0.271504,\n    175: 0.146028, 185: 0.120252, 195: 0.108490, 205: 0.107063,\n    215: 0.177422\n}\n\nprint('=== exp_057 NVE (using exp_009a s2 baseline) ===')\nfor step_k in sorted(exp057.keys()):\n    if step_k in baseline_s2:\n        nve = exp057[step_k] / baseline_s2[step_k]\n        marker = ' *** EXCEEDS 1.5x ***' if nve > 1.5 else ''\n        print(f'  step={step_k}K: exp_ve={exp057[step_k]:.4f}, baseline_ve={baseline_s2[step_k]:.4f}, NVE={nve:.3f}{marker}')\n\nprint()\nprint('=== exp_057 NVE (using exp_001 s0 baseline) ===')\nfor step_k in sorted(exp057.keys()):\n    if step_k in baseline_s0:\n        nve = exp057[step_k] / baseline_s0[step_k]\n        marker = ' *** EXCEEDS 1.5x ***' if nve > 1.5 else ''\n        print(f'  step={step_k}K: exp_ve={exp057[step_k]:.4f}, baseline_ve={baseline_s0[step_k]:.4f}, NVE={nve:.3f}{marker}')\n\nprint()\nprint('=== exp_047 (s1) verification ===')\n# exp_047: registry says nve_peak=1.71 at 95K, ve_ratio_peak=1.099 at 75K\n# If NVE@95K = 1.71 and baseline_s0@95K = 0.632, then exp_047 ve@95K = 1.71 * 0.632 = 1.081\n# If using baseline_s2@95K = 0.8449, then NVE = 1.081 / 0.8449 = 1.28\n# But registry says NVE = 1.71 using baseline_s0\nprint(f'  exp_047 NVE=1.71 at 95K. Using baseline_s0@95K={baseline_s0[95]:.3f}: implied exp_ve={1.71*baseline_s0[95]:.4f}')\nprint(f'  Using baseline_s2@95K={baseline_s2[95]:.3f}: would give NVE={1.71*baseline_s0[95]/baseline_s2[95]:.3f}')\n\nprint()\nprint('=== SUMMARY: All Walker frozen seeds NVE ===')\nprint(f'  exp_042 (s0): nve_peak = 0.194 (from registry, well below 1.5x)')\nprint(f'  exp_047 (s1): nve_peak = 1.71 at 95K (EXCEEDS 1.5x, transient → 0.56)')\n\n# For exp_057, compute NVE_peak using exp_001 baseline (consistent with other experiments)\n# At 115K, exp_001 baseline doesn't have explicit ve_ratio\n# Interpolate: @105K=0.656, converged ~0.69-0.72 by 135K\n# Linear interpolation: 0.656 + (115-105)/(135-105) * (0.70 - 0.656) = 0.656 + 0.333*0.044 = 0.671\nbaseline_s0_115k_interp = 0.656 + (10/30) * (0.70 - 0.656)  # conservative estimate\nnve_057_s0 = exp057[115] / baseline_s0_115k_interp\nprint(f'  exp_057 (s2): ve_ratio_peak = 1.283 at 115K')\nprint(f'    NVE (using exp_001 s0, interpolated@115K={baseline_s0_115k_interp:.3f}): {nve_057_s0:.3f} *** EXCEEDS 1.5x ***')\nprint(f'    NVE (using exp_009a s2, actual@115K=0.7144): {exp057[115]/0.7144:.3f} *** EXCEEDS 1.5x ***')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "7efac985-9e42-4c22-9826-8f6b7cfc731e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5M7hka7EKUgW7o8UFBmdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3380,
      "cache_read_input_tokens": 74893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3380
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

_source line 65 · 2026-05-24T01:55:19.649Z_

<details><summary>↩ Tool result · `toolu_01G8xTr135mmZBPHyQLjhQUj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== exp_057 NVE (using exp_009a s2 baseline) ===\\n  step=25K: exp_ve=0.1369, baseline_ve=0.1407, NVE=0.973\\n  step=35K: exp_ve=0.4945, baseline_ve=0.3056, NVE=1.618 *** EXCEEDS 1.5x ***\\n  step=45K: exp_ve=0.6145, baseline_ve=0.3629, NVE=1.693 *** EXCEEDS 1.5x ***\\n  step=55K: exp_ve=0.7468, baseline_ve=0.4746, NVE=1.574 *** EXCEEDS 1.5x ***\\n  step=65K: exp_ve=0.7151, baseline_ve=0.4737, NVE=1.510 *** EXCEEDS 1.5x ***\\n  step=75K: exp_ve=0.6195, baseline_ve=0.5974, NVE=1.037\\n  step=85K: exp_ve=0.6059, baseline_ve=0.7281, NVE=0.832\\n  step=95K: exp_ve=0.6359, baseline_ve=0.8449, NVE=0.753\\n  step=105K: exp_ve=0.5437, baseline_ve=0.6447, NVE=0.843\\n  step=115K: exp_ve=1.2826, baseline_ve=0.7144, NVE=1.795 *** EXCEEDS 1.5x ***\\n  step=125K: exp_ve=0.7315, baseline_ve=0.7077, NVE=1.034\\n  step=135K: exp_ve=1.0688, baseline_ve=0.7170, NVE=1.491\\n  step=145K: exp_ve=1.1634, baseline_ve=0.7241, NVE=1.607 *** EXCEEDS 1.5x ***\\n  step=155K: exp_ve=0.4520, baseline_ve=0.8131, NVE=0.556\\n\\n=== exp_057 NVE (using exp_001 s0 baseline) ===\\n  step=25K: exp_ve=0.1369, baseline_ve=0.0870, NVE=1.574 *** EXCEEDS 1.5x ***\\n  step=35K: exp_ve=0.4945, baseline_ve=0.2410, NVE=2.052 *** EXCEEDS 1.5x ***\\n  step=45K: exp_ve=0.6145, baseline_ve=0.3310, NVE=1.857 *** EXCEEDS 1.5x ***\\n  step=55K: exp_ve=0.7468, baseline_ve=0.4040, NVE=1.849 *** EXCEEDS 1.5x ***\\n  step=65K: exp_ve=0.7151, baseline_ve=0.5630, NVE=1.270\\n  step=75K: exp_ve=0.6195, baseline_ve=0.7190, NVE=0.862\\n  step=85K: exp_ve=0.6059, baseline_ve=0.7010, NVE=0.864\\n  step=95K: exp_ve=0.6359, baseline_ve=0.6320, NVE=1.006\\n  step=105K: exp_ve=0.5437, baseline_ve=0.6560, NVE=0.829\\n\\n=== exp_047 (s1) verification ===\\n  exp_047 NVE=1.71 at 95K. Using baseline_s0@95K=0.632: implied exp_ve=1.0807\\n  Using baseline_s2@95K=0.845: would give NVE=1.279\\n\\n=== SUMMARY: All Walker frozen seeds NVE ===\\n  exp_042 (s0): nve_peak = 0.194 (from registry, well below 1.5x)\\n  exp_047 (s1): nve_peak = 1.71 at 95K (EXCEEDS 1.5x, transient → 0.56)\\n  exp_057 (s2): ve_ratio_peak = 1.283 at 115K\\n    NVE (using exp_001 s0, interpolated@115K=0.671): 1.912 *** EXCEEDS 1.5x ***\\n    NVE (using exp_009a s2, actual@115K=0.7144): 1.795 *** EXCEEDS 1.5x ***\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "a7b5da40-2172-409c-80d7-020db6cbfaa1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== exp_057 NVE (using exp_009a s2 baseline) ===\\\\n  step=25K: exp_ve=0.1369, baseline_ve=0.1407, NVE=0.973\\\\n  step=35K: exp_ve=0.4945, baseline_ve=0.3056, NVE=1.618 *** EXCEEDS 1.5x ***\\\\n  step=45K: exp_ve=0.6145, baseline_ve=0.3629, NVE=1.693 *** EXCEEDS 1.5x ***\\\\n  step=55K: exp_ve=0.7468, baseline_ve=0.4746, NVE=1.574 *** EXCEEDS 1.5x ***\\\\n  step=65K: exp_ve=0.7151, baseline_ve=0.4737, NVE=1.510 *** EXCEEDS 1.5x ***\\\\n  step=75K: exp_ve=0.6195, baseline_ve=0.5974, NVE=1.037\\\\n  step=85K: exp_ve=0.6059, baseline_ve=0.7281, NVE=0.832\\\\n  step=95K: exp_ve=0.6359, baseline_ve=0.8449, NVE=0.753\\\\n  step=105K: exp_ve=0.5437, baseline_ve=0.6447, NVE=0.843\\\\n  step=115K: exp_ve=1.2826, baseline_ve=0.7144, NVE=1.795 *** EXCEEDS 1.5x ***\\\\n  step=125K: exp_ve=0.7315, baseline_ve=0.7077, NVE=1.034\\\\n  step=135K: exp_ve=1.0688, baseline_ve=0.7170, NVE=1.491\\\\n  step=145K: exp_ve=1.1634, baseline_ve=0.7241, NVE=1.607 *** EXCEEDS 1.5x ***\\\\n  step=155K: exp_ve=0.4520, baseline_ve=0.8131, NVE=0.556\\\\n\\\\n=== exp_057 NVE (using exp_001 s0 baseline) ===\\\\n  step=25K: exp_ve=0.1369, baseline_ve=0.0870, NVE=1.574 *** EXCEEDS 1.5x ***\\\\n  step=35K: exp_ve=0.4945, baseline_ve=0.2410, NVE=2.052 *** EXCEEDS 1.5x ***\\\\n  step=45K: exp_ve=0.6145, baseline_ve=0.3310, NVE=1.857 *** EXCEEDS 1.5x ***\\\\n  step=55K: exp_ve=0.7468, baseline_ve=0.4040, NVE=1.849 *** EXCEEDS 1.5x ***\\\\n  step=65K: exp_ve=0.7151, baseline_ve=0.5630, NVE=1.270\\\\n  step=75K: exp_ve=0.6195, baseline_ve=0.7190, NVE=0.862\\\\n  step=85K: exp_ve=0.6059, baseline_ve=0.7010, NVE=0.864\\\\n  step=95K: exp_ve=0.6359, baseline_ve=0.6320, NVE=1.006\\\\n  step=105K: exp_ve=0.5437, baseline_ve=0.6560, NVE=0.829\\\\n\\\\n=== exp_047 (s1) verification ===\\\\n  exp_047 NVE=1.71 at 95K. Using baseline_s0@95K=0.632: implied exp_ve=1.0807\\\\n  Using baseline_s2@95K=0.845: would give NVE=1.279\\\\n\\\\n=== SUMMARY: All Walker frozen seeds NVE ===\\\\n  exp_042 (s0): nve_peak = 0.194 (from registry, well below 1.5x)\\\\n  exp_047 (s1): nve_peak = 1.71 at 95K (EXCEEDS 1.5x, transient → 0.56)\\\\n  exp_057 (s2): ve_ratio_peak = 1.283 at 115K\\\\n    NVE (using exp_001 s0, interpolated@115K=0.671): 1.912 *** EXCEEDS 1.5x ***\\\\n    NVE (using exp_009a s2, actual@115K=0.7144): 1.795 *** EXCEEDS 1.5x ***\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== exp_057 NVE (using exp_009a s2 baseline) ===\\n  step=25K: exp_ve=0.1369, baseline_ve=0.1407, NVE=0.973\\n  step=35K: exp_ve=0.4945, baseline_ve=0.3056, NVE=1.618 *** EXCEEDS 1.5x ***\\n  step=45K: exp_ve=0.6145, baseline_ve=0.3629, NVE=1.693 *** EXCEEDS 1.5x ***\\n  step=55K: exp_ve=0.7468, baseline_ve=0.4746, NVE=1.574 *** EXCEEDS 1.5x ***\\n  step=65K: exp_ve=0.7151, baseline_ve=0.4737, NVE=1.510 *** EXCEEDS 1.5x ***\\n  step=75K: exp_ve=0.6195, baseline_ve=0.5974, NVE=1.037\\n  step=85K: exp_ve=0.6059, baseline_ve=0.7281, NVE=0.832\\n  step=95K: exp_ve=0.6359, baseline_ve=0.8449, NVE=0.753\\n  step=105K: exp_ve=0.5437, baseline_ve=0.6447, NVE=0.843\\n  step=115K: exp_ve=1.2826, baseline_ve=0.7144, NVE=1.795 *** EXCEEDS 1.5x ***\\n  step=125K: exp_ve=0.7315, baseline_ve=0.7077, NVE=1.034\\n  step=135K: exp_ve=1.0688, baseline_ve=0.7170, NVE=1.491\\n  step=145K: exp_ve=1.1634, baseline_ve=0.7241, NVE=1.607 *** EXCEEDS 1.5x ***\\n  step=155K: exp_ve=0.4520, baseline_ve=0.8131, NVE=0.556\\n\\n=== exp_057 NVE (using exp_001 s0 baseline) ===\\n  step=25K: exp_ve=0.1369, baseline_ve=0.0870, NVE=1.574 *** EXCEEDS 1.5x ***\\n  step=35K: exp_ve=0.4945, baseline_ve=0.2410, NVE=2.052 *** EXCEEDS 1.5x ***\\n  step=45K: exp_ve=0.6145, baseline_ve=0.3310, NVE=1.857 *** EXCEEDS 1.5x ***\\n  step=55K: exp_ve=0.7468, baseline_ve=0.4040, NVE=1.849 *** EXCEEDS 1.5x ***\\n  step=65K: exp_ve=0.7151, baseline_ve=0.5630, NVE=1.270\\n  step=75K: exp_ve=0.6195, baseline_ve=0.7190, NVE=0.862\\n  step=85K: exp_ve=0.6059, baseline_ve=0.7010, NVE=0.864\\n  step=95K: exp_ve=0.6359, baseline_ve=0.6320, NVE=1.006\\n  step=105K: exp_ve=0.5437, baseline_ve=0.6560, NVE=0.829\\n\\n=== exp_047 (s1) verification ===\\n  exp_047 NVE=1.71 at 95K. Using baseline_s0@95K=0.632: implied exp_ve=1.0807\\n  Using baseline_s2@95K=0.845: would give NVE=1.279\\n\\n=== SUMMARY: All Walker frozen seeds NVE ===\\n  exp_042 (s0): nve_peak = 0.194 (from registry, well below 1.5x)\\n  exp_047 (s1): nve_peak = 1.71 at 95K (EXCEEDS 1.5x, transient → 0.56)\\n  exp_057 (s2): ve_ratio_peak = 1.283 at 115K\\n    NVE (using exp_001 s0, interpolated@115K=0.671): 1.912 *** EXCEEDS 1.5x ***\\n    NVE (using exp_009a s2, actual@115K=0.7144): 1.795 *** EXCEEDS 1.5x ***\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also check the NVE definition in the paper tex files. The ssh_read_only command with grep got blocked because of a pipeline character that wasn't there... let me check — it was `--include="*.tex"`. Actually that should be fine. Let me try again without the `--include` syntax that might be causing issues.

Actually wait, the error says "Shell metacharacter '|' not allowed" but I didn't use a pipe. Let me look at the command more carefully: `grep -rn "nve\|NVE\|ve_ratio\|overshoot"` — the `\|` is being interpreted as a pipe. 

I should use the `-E` flag to enable extended regex so the pipe character works as an alternation operator, or I could quote the pattern differently to avoid the shell interpreting it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "66dd1138-4f5d-496f-845f-3406ee0996ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PD6xenLw1Zm3HTXcCNQLp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6740,
      "cache_read_input_tokens": 78273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6740
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

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01541Rz615D3PSLqLLLZtTnn`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rnE \"nve|NVE|overshoot.ratio|normalized.*value\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "8d1cf7e7-3da6-4745-a1af-467429dbdbf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PD6xenLw1Zm3HTXcCNQLp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6740,
      "cache_read_input_tokens": 78273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6740
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

_source line 68 · 2026-05-24T01:55:31.082Z_

<details><summary>↩ Tool result · `toolu_01541Rz615D3PSLqLLLZtTnn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "dfce05ec-d2d9-47b8-9a39-0e6603d975b4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UhSxXKePjC1e1LFLumzva7`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"NVE\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "3a5ecbff-3c6f-4053-a621-7bfea2409065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHdVbms1GxiMU72dbE2K35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 85013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 70 · 2026-05-24T01:55:34.816Z_

<details><summary>↩ Tool result · `toolu_01UhSxXKePjC1e1LFLumzva7`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "e69e83e8-fe8e-42dc-b2de-33eced822e69",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E5Ept3MJLWRTjxQaqWetG6`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"overshoot\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "f1e6de3c-eff5-4b22-81dd-1bcce27bbd02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHdVbms1GxiMU72dbE2K35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 85013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 72 · 2026-05-24T01:55:35.811Z_

<details><summary>↩ Tool result · `toolu_01E5Ept3MJLWRTjxQaqWetG6`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "72c578f5-5aed-44e1-b775-8aac8384aa10",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UtDMjSubhz8XhhHTUrnB8M`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"ve_ratio\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "75956d83-be35-4751-9cf4-66ba2d7532e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHdVbms1GxiMU72dbE2K35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 85013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 74 · 2026-05-24T01:55:36.756Z_

<details><summary>↩ Tool result · `toolu_01UtDMjSubhz8XhhHTUrnB8M`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "684cfc1e-0d66-4a6d-93b2-07b791b1e4c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XxP3QFDWDeMk6Amgc1DGEp`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -rn \"normalized\" /root/autodl-tmp/event-gated-adaptive-horizon/paper/ --include=\"*.tex\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "645cbbd3-4484-4435-bea3-ac00406a63d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHdVbms1GxiMU72dbE2K35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 85013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 76 · 2026-05-24T01:55:37.416Z_

<details><summary>↩ Tool result · `toolu_01XxP3QFDWDeMk6Amgc1DGEp`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "f2e442dd-0991-4432-9dc7-fa7d223624f8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/event-gated-adaptive-horizon/paper/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 77_

<details><summary>Logged reasoning block</summary>

```text
No paper/ directory on the server. Let me check the local project for the paper files or check the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d931460f-18be-4333-9e91-c22f91ded91c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPix4SFe7xzKpMBJwtnp8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 85449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1028
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

_source line 78_

Paper 目录不在服务器上。检查本地项目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "93a1633b-58c6-4e1c-8fc0-4ace61fb8986",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPix4SFe7xzKpMBJwtnp8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 85449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1028
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

_source line 79_

<details open><summary>🔧 Tool call — Glob · `toolu_013yeJz6ziWWZjxvPPJpeR9Z`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "f653bd8b-fcf2-4c91-b299-6ea081278bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPix4SFe7xzKpMBJwtnp8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 85449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1028
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

_source line 80 · 2026-05-24T01:55:42.441Z_

<details><summary>↩ Tool result · `toolu_013yeJz6ziWWZjxvPPJpeR9Z`</summary>

```text
docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
paper/tables/nve_sensitivity_table.tex
artifacts/dream_reports/dream_20260520T155150/best/paper.tex
artifacts/dream_reports/dream_20260520T155150/median/paper.tex
artifacts/dream_reports/dream_20260520T155150/worst/paper.tex
artifacts/dream_reports/dream_20260520T210241/best/paper.tex
artifacts/dream_reports/dream_20260520T210241/median/paper.tex
docs/paper/main.tex
docs/paper/sections/methodology.tex
docs/paper/sections/related_work.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
docs/paper/sections/appendix.tex
docs/paper/sections/results.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d0e3a050-4a75-4f0c-b7fe-83a40918d283",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_corl_template/corl_2026_template_submission/example.tex",
      "docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.tex",
      "artifacts/figures/archive/tab_rssm_fidelity.tex",
      "artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.tex",
      "artifacts/analysis/detector_table.tex",
      "artifacts/_project/paper/nve_sensitivity_table.tex",
      "paper/tables/nve_sensitivity_table.tex",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/abstract_body.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/results.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/analysis.tex"
    ],
    "durationMs": 16,
    "numFiles": 36,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Glob · `toolu_01KfJZPWoFenjnVbvAvzftX3`</summary>

```json
{
  "pattern": "artifacts/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "4838025c-39d3-4bb0-ac67-1b05a19402c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPix4SFe7xzKpMBJwtnp8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 85449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1028
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

_source line 82 · 2026-05-24T01:55:42.798Z_

<details><summary>↩ Tool result · `toolu_01KfJZPWoFenjnVbvAvzftX3`</summary>

```text
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
artifacts/dream_reports/dream_20260520T155150/best/paper.tex
artifacts/dream_reports/dream_20260520T155150/median/paper.tex
artifacts/dream_reports/dream_20260520T155150/worst/paper.tex
artifacts/dream_reports/dream_20260520T210241/best/paper.tex
artifacts/dream_reports/dream_20260520T210241/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "32b5e3dd-e49e-4935-91a1-2b0b43013bd6",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T062606/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.tex",
      "artifacts/figures/archive/tab_rssm_fidelity.tex",
      "artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.tex",
      "artifacts/analysis/detector_table.tex",
      "artifacts/_project/paper/nve_sensitivity_table.tex",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.tex"
    ],
    "durationMs": 13,
    "numFiles": 24,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Grep · `toolu_01Lu5N5ytCwP4oCX1SYASQDF`</summary>

```json
{
  "pattern": "NVE|nve|overshoot|\\\\\\\\text\\{NVE\\}|normalized.*value.*error",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "289444b7-3a4a-418d-bd0a-8a01604f0e28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F84jntVnSwPVG2YhKAAKGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 86477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1423
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

_source line 84 · 2026-05-24T01:55:47.693Z_

<details><summary>↩ Tool result · `toolu_01Lu5N5ytCwP4oCX1SYASQDF`</summary>

```text
&lt;persisted-output>
Output too large (31.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/9ea8f404-d312-4e9d-9b1c-5c24d8601855/tool-results/toolu_01Lu5N5ytCwP4oCX1SYASQDF.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-267-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-268-INPUT /usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmri8t.vf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-269-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmri8r.tfm
docs/paper/main.fls:270:INPUT ./figures/fig1_nve_trajectory.pdf
docs/paper/main.fls:271:INPUT ./figures/fig1_nve_trajectory.pdf
docs/paper/main.fls:272:INPUT ./figures/fig1_nve_trajectory.pdf
docs/paper/main.fls:273:INPUT ./figures/fig1_nve_trajectory.pdf
docs/paper/main.fls:274:INPUT ./figures/fig1_nve_trajectory.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-275-INPUT ./sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-276-INPUT ./sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-277-INPUT ./sections/analysis.tex
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-292-INPUT sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-293-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8t.tfm
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-294-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmri8t.tfm
docs/paper/main.fls:295:INPUT ../../artifacts/figures/nve_roc_curve.pdf
docs/paper/main.fls:296:INPUT ../../artifacts/figures/nve_roc_curve.pdf
docs/paper/main.fls:297:INPUT ../../artifacts/figures/nve_roc_curve.pdf
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
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "cd32cf45-8971-4246-b1f3-6639657dc566",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-267-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-268-INPUT /usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmri8t.vf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-269-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmri8r.tfm\ndocs/paper/main.fls:270:INPUT ./figures/fig1_nve_trajectory.pdf\ndocs/paper/main.fls:271:INPUT ./figures/fig1_nve_trajectory.pdf\ndocs/paper/main.fls:272:INPUT ./figures/fig1_nve_trajectory.pdf\ndocs/paper/main.fls:273:INPUT ./figures/fig1_nve_trajectory.pdf\ndocs/paper/main.fls:274:INPUT ./figures/fig1_nve_trajectory.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-275-INPUT ./sections/analysis.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-276-INPUT ./sections/analysis.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-277-INPUT ./sections/analysis.tex\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-292-INPUT sections/appendix.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-293-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8t.tfm\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-294-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmri8t.tfm\ndocs/paper/main.fls:295:INPUT ../../artifacts/figures/nve_roc_curve.pdf\ndocs/paper/main.fls:296:INPUT ../../artifacts/figures/nve_roc_curve.pdf\ndocs/paper/main.fls:297:INPUT ../../artifacts/figures/nve_roc_curve.pdf\ndocs/paper/main.fls:298:INPUT ../../artifacts/figures/nve_roc_curve.pdf\ndocs/paper/main.fls:299:INPUT ../../artifacts/figures/nve_roc_curve.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-300-INPUT ../../artifacts/figures/paper/fig3_factorial_grid.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-301-INPUT ../../artifacts/figures/paper/fig3_factorial_grid.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.fls-302-INPUT ../../artifacts/figures/paper/fig3_factorial_grid.pdf\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-2-\ndocs/paper/rebuttal_notes.md-3-## Q1: Limited Environment Generalization\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-4-\ndocs/paper/rebuttal_notes.md:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-6-\ndocs/paper/rebuttal_notes.md-7-## Q2: Threshold Circularity / Overfitting\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-8-\ndocs/paper/rebuttal_notes.md:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-10-\ndocs/paper/rebuttal_notes.md-11-## Q3: Architecture Generalization\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-12-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-18-\ndocs/paper/rebuttal_notes.md-19-## Q5: SGS Sample Size (n=2)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md-20-\ndocs/paper/rebuttal_notes.md:21:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-22-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-23-% Custom commands\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-24-\\newcommand{\\dt}{\\mathrm{dt}}\ndocs/paper/main.tex:25:\\newcommand{\\nve}{\\mathrm{nve}}\ndocs/paper/main.tex-26-% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-27-\\newcommand{\\sgseval}{448.3}\ndocs/paper/main.tex:28:\\newcommand{\\sgsnve}{1.66}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-29-\\newcommand{\\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-30-\\newcommand{\\ie}{\\textit{i.e.}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex-31-\\newcommand{\\eg}{\\textit{e.g.}}\n--\ndocs/paper/sections/analysis.tex-2-\\label{sec:discussion}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-3-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-4-\\paragraph{CIVO mechanism.}\ndocs/paper/sections/analysis.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-6-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-7-\\paragraph{Practitioner guidelines.}\ndocs/paper/sections/analysis.tex:8:Monitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.953$; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding reduces CIVO from sustained collapse (4/4 trained) to at most a transient spike (1/3 frozen Walker, 0/2 frozen Cheetah). Recovery is severity-dependent: moderate CIVO self-corrects; extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-9-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-10-\\paragraph{Implications for robot learning.}\ndocs/paper/sections/analysis.tex-11-No $\\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\\times$), but frozen controls show comparable or higher peaks (Table~\\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.\n--\ndocs/paper/sections/abstract_body.tex:1:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-145-\\c@section@level=\\count293\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-146-)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-147-(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty\ndocs/paper/main.log:148:Package: stringenc 2019/11/29 v1.12 Convert strings between diff. encodings (HO\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-149-)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-150-)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-151-\\@linkdim=\\dimen156\n--\ndocs/paper/main.log-479-LaTeX Font Info:    Checking defaults for PU/pdf/m/n on input line 42.\ndocs/paper/main.log-480-LaTeX Font Info:    ... okay on input line 42.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-481- (/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\ndocs/paper/main.log:482:[Loading MPS to PDF converter (version 2006.09.02).]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-483-\\scratchcounter=\\count339\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-484-\\scratchdimen=\\dimen260\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-485-\\scratchbox=\\box62\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-490-\\MPscratchDim=\\dimen261\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-491-\\MPnumerator=\\count343\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-492-\\makeMPintoPDFobject=\\count344\ndocs/paper/main.log:493:\\everyMPtoPDFconversion=\\toks35\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-494-) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\ndocs/paper/main.log-495-Package: epstopdf-base 2020-01-24 v2.11 Base part for package epstopdf\ndocs/paper/main.log-496-Package epstopdf-base Info: Redefining graphics rule for `.eps' on input line 4\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-616-  used on input line 60.\ndocs/paper/main.log-617-(pdftex.def)             Requested size: 258.36281pt x 168.47272pt.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-618- [5 <../../artifacts/figures/paper/fig1_learning_curves.pdf>]\ndocs/paper/main.log:619:&lt;figures/fig1_nve_trajectory.pdf, id=467, 353.95363pt x 240.60767pt>\ndocs/paper/main.log:620:File: figures/fig1_nve_trajectory.pdf Graphic file (type pdf)\ndocs/paper/main.log:621:&lt;use figures/fig1_nve_trajectory.pdf>\ndocs/paper/main.log:622:Package pdftex.def Info: figures/fig1_nve_trajectory.pdf  used on input line 76\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-623-.\ndocs/paper/main.log-624-(pdftex.def)             Requested size: 258.36281pt x 175.63478pt.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-625-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-626-Underfull \\vbox (badness 1584) has occurred while \\output is active []\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-627-\ndocs/paper/main.log:628: [6 <./figures/fig1_nve_trajectory.pdf>]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-629-Underfull \\hbox (badness 2351) in paragraph at lines 109--110\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-630- []\\T1/ptm/b/n/10 Targeted obs-decoder-only SGS con-firms path-way re-dun-dancy\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-631-.[] \\T1/ptm/m/n/10 Obs-decoder-only SGS\n--\ndocs/paper/main.log-641-LaTeX Warning: `h' float specifier changed to `ht'.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-642-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-643-[11]\ndocs/paper/main.log:644:<../../artifacts/figures/nve_roc_curve.pdf, id=605, 273.5pt x 280.09079pt>\ndocs/paper/main.log:645:File: ../../artifacts/figures/nve_roc_curve.pdf Graphic file (type pdf)\ndocs/paper/main.log:646:&lt;use ../../artifacts/figures/nve_roc_curve.pdf>\ndocs/paper/main.log:647:Package pdftex.def Info: ../../artifacts/figures/nve_roc_curve.pdf  used on inp\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-648-ut line 232.\ndocs/paper/main.log-649-(pdftex.def)             Requested size: 278.23827pt x 284.97507pt.\ndocs/paper/main.log:650: [12 <../../artifacts/figures/nve_roc_curve.pdf>]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-651-\ndocs/paper/main.log-652-LaTeX Warning: `h' float specifier changed to `ht'.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log-653-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex-5-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex-6-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex-7-\\paragraph{Value overestimation and model fidelity.}\ndocs/paper/sections/related_work.tex:8:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-1-\\section{Conclusion}\ndocs/paper/sections/conclusion.tex-2-\\label{sec:conclusion}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-3-\ndocs/paper/sections/conclusion.tex:4:We identify trained $\\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (26/29, AUROC${=}0.953$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the structural factor.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-5-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-6-\\paragraph{Limitations.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-7-Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-8-All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \\citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex-9-We characterize CIVO under fixed-$\\dt$ subsampling; learned temporal gates warrant separate study.\ndocs/paper/sections/conclusion.tex:10:Statistical power with 4 seeds per configuration is limited \\citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.981$) may require recalibration for different reward scales.\ndocs/paper/sections/conclusion.tex-11-Code: upon acceptance.\ndocs/paper/sections/conclusion.tex-12-\\label{sec:limitations}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-34-\\subsection{Diagnostic Metrics}\ndocs/paper/sections/methodology.tex-35-\\label{sec:metrics}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-36-\ndocs/paper/sections/methodology.tex:37:\\paragraph{Normalized value-to-eval ratio ($\\nve$).}\ndocs/paper/sections/methodology.tex:38:We define $\\nve_t = (v/e)_{\\text{config},t} / (v/e)_{\\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\\_001, seed~1, 505K steps). We restrict to a \\textbf{35K+ window} to avoid early-training inflation. The $\\nve \\geq 1.5\\times$ threshold achieves 26/29 accuracy (AUROC${=}0.953$, in-sample; LOEO cross-validated, mean AUROC${=}0.981$, Appendix~Table~\\ref{tab:nve_loeo}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-39-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-40-\\subsection{Selective Gradient Stopping}\ndocs/paper/sections/methodology.tex-41-\\label{sec:sgs_method}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-55-\\subsection{Environment and Training Details}\ndocs/paper/sections/methodology.tex-56-\\label{sec:env_details}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-57-\ndocs/paper/sections/methodology.tex:58:[Omitted long matching line]\n--\ndocs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty-10-%\t       Main changes:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty-11-%\t       - The abstract is more compact compared to NeurIPS/ICML\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty-12-%\t       - References are by default using natbib with squared numbers (e.g., [1])\ndocs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty:13:%\t       - DOI fields from the bibtex are automatically converted to hyperlinks \n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty-14-%\t       to the corresponding page\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty-15-%\t       - acknowledgments are now a command, and the corresponding subsubsection is\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty-16-%\t       automatically included only in the final version\n--\ndocs/paper/corl_2026.sty-10-%\t       Main changes:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty-11-%\t       - The abstract is more compact compared to NeurIPS/ICML\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty-12-%\t       - References are by default using natbib with squared numbers (e.g., [1])\ndocs/paper/corl_2026.sty:13:%\t       - DOI fields from the bibtex are automatically converted to hyperlinks \n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty-14-%\t       to the corresponding page\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty-15-%\t       - acknowledgments are now a command, and the corresponding subsubsection is\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty-16-%\t       automatically included only in the final version\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-7-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-8-\\begin{table*}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-9-\\centering\ndocs/paper/sections/appendix.tex:10:\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\ndocs/paper/sections/appendix.tex-11-\\label{tab:complete_results}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-12-\\scriptsize\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-13-\\setlength{\\tabcolsep}{3pt}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-14-\\begin{tabular}{llcccccl}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-15-\\toprule\ndocs/paper/sections/appendix.tex:16:\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-17-\\midrule\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-18-001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-19-001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-41-042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-42-057 & Frozen emb (s2) & frz$^b$ & ON & 8 & --- & 1.28$\\times$ & No CIVO \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-43-\\midrule\ndocs/paper/sections/appendix.tex:44:018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-45-\\rowcolor{gray!15}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-46-018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-47-008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-82-exp$^a$ = trained, subsample OFF;\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-83-frz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-84---- = removed ($d{=}0$).\\\\\ndocs/paper/sections/appendix.tex:85:$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-86-$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\ndocs/paper/sections/appendix.tex:87:$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\ndocs/paper/sections/appendix.tex:88:$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\ndocs/paper/sections/appendix.tex:89:$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\ndocs/paper/sections/appendix.tex-90-$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\ndocs/paper/sections/appendix.tex-91-$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\ndocs/paper/sections/appendix.tex-92-$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-101-\\toprule\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-102-\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-103-\\midrule\ndocs/paper/sections/appendix.tex:104:Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\\ndocs/paper/sections/appendix.tex:105:Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-106-Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-107-Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-108-Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-110-\\end{tabular}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-111-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-112-\ndocs/paper/sections/appendix.tex:113:\\section{NVE Threshold Sensitivity Analysis}\ndocs/paper/sections/appendix.tex-114-\\label{sec:appendix_sensitivity}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-115-\ndocs/paper/sections/appendix.tex:116:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-117-\ndocs/paper/sections/appendix.tex:118:\\subsection{Per-Experiment NVE Values}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-119-\ndocs/paper/sections/appendix.tex:120:Table~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-121-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-122-\\begin{table}[ht]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-123-\\centering\ndocs/paper/sections/appendix.tex:124:\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\ndocs/paper/sections/appendix.tex:125:\\label{tab:nve_raw}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-126-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-127-\\begin{tabular}{@{}lrccc@{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-128-\\toprule\ndocs/paper/sections/appendix.tex:129:Experiment & NVE & Mechanism & B1 & B2 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-130-\\midrule\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-131-006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-132-008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-144-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-145-\\subsection{Multi-Threshold Classification Performance}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-146-\ndocs/paper/sections/appendix.tex:147:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-148-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-149-\\begin{table*}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-150-\\centering\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-212-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-213-\\subsection{Threshold Recommendation}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-214-\ndocs/paper/sections/appendix.tex:215:For the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-216-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-217-\\begin{enumerate}[nosep,leftmargin=*]\ndocs/paper/sections/appendix.tex:218:\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.",
    "numLines": 250,
    "appliedLimit": 250
  }
}
```

</details>

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Grep · `toolu_01An7AufcGy9i3HPXa3f31dr`</summary>

```json
{
  "pattern": "NVE|nve|overshoot|normalized.*value",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": true,
  "context": 2,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ea8f404-d312-4e9d-9b1c-5c24d8601855",
  "uuid": "d7385da5-c150-46dd-9c8f-544a081e62af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xb2xsgjbWe8ovYWhdpau5y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 87900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
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
