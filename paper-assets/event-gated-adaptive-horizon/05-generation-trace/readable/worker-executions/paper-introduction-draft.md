# paper introduction draft

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_introduction-draft_20260516T200221.log`
- **Structured JSON:** [`012088b0a9b86fd0c761.json`](../../sessions/01/012088b0a9b86fd0c761.json)

## Before a recorded user message

25 recorded events

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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
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
  "uuid": "7619ee87-edb9-44f0-bf10-38215755091f",
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
    "resetsAt": 1778979000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6b998645-f7dd-48d2-b39d-fa7e2c693ff4",
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write an Introduction section draft for their paper about "Critic-Induced Value Overestimation" (CIVO) in world-model RL. Let me first read the relevant context files to understand the paper framing, existing drafts, and key findings before writing.

Let me read:
1. paper_framing.md for the claims and framing
2. The related work draft for context on how they position the paper
3. The results section for understanding the findings
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "b971a6fd-9088-4802-a0fb-63e2502123e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNekw8Hk9ZB19SdPrLUbhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11671,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11671
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

### Assistant

_source line 5_

Let me read the relevant files to get the full context before writing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "1e791d92-2864-4319-9d7a-3c3d74f94091",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNekw8Hk9ZB19SdPrLUbhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11671,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11671
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_018kCPq1XqEv2f4QpAjkHNpj`</summary>

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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "99f3d479-df8b-4ff8-98be-e7c9cdd64d33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNekw8Hk9ZB19SdPrLUbhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11671,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11671
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

_source line 7 · 2026-05-16T20:02:36.485Z_

<details><summary>↩ Tool result · `toolu_018kCPq1XqEv2f4QpAjkHNpj`</summary>

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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "55218ce1-4c8d-40a2-bff8-edfe2d23b3f5",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01GKBJn8JkBCPTrtUuxcPy83`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "7b211fa4-3edb-4d9e-84e5-39d4d4bdc87b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNekw8Hk9ZB19SdPrLUbhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11671,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11671
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

_source line 9 · 2026-05-16T20:02:36.725Z_

<details><summary>↩ Tool result · `toolu_01GKBJn8JkBCPTrtUuxcPy83`</summary>

```text
1	# Related Work — Draft
2	
3	## 2.1 World-Model Reinforcement Learning
4	
5	World-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.
6	
7	A well-known risk in model-based RL is \emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \citep{schrittwieser2020muzero} and EfficientZero \citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.
8	
9	## 2.2 Temporal Abstraction in Reinforcement Learning
10	
11	Temporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \citep{sharma2017figar} augments the action space with a discrete repeat count, \citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.
12	
13	Within world-model RL, temporal abstraction has been pursued primarily through \emph{hierarchical} architectures. Director \citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the CIVO phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.
14	
15	Most relevant to our work is TAWM \citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\Delta t$ and trains over diverse $\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\Delta t$ conditioning \emph{improves} performance and data efficiency—but critically, TAWM is a model-agnostic framework evaluated on TD-MPC2, which uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.
16	
17	The sensitivity of RL algorithms to time discretization has been studied theoretically: \citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\delta$ and propose architectural modifications for $\delta$-invariance. SAR \citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\delta\!=\!1$ degrade substantially at $dt\!>\!1$, and temporal conditioning amplifies rather than compensates for this degradation.
18	
19	## 2.3 Value Overestimation and Delusional Bias
20	
21	Value overestimation in deep RL was first identified by \citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.
22	
23	Distinct from general overestimation, \citet{lu2018nondelusional} formalize \emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \emph{CIVO} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\!>\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.
24	
25	Recent work has connected value overestimation to training dynamics in model-based settings. \citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our CIVO mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.
26	
27	## 2.4 Multi-Step Prediction and Compounding Error
28	
29	Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \citep{venkatraman2015improving, lambert2022investigating}. \citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.
30	
31	Our findings add a new dimension: when imagination operates at $dt\!>\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \emph{on top of} the standard compounding error problem.
32	
33	## 2.5 Diagnostic Methodology
34	
35	Our diagnostic methodology follows a tradition of systematic controlled experiments in RL. \citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.
36	
37	---
38	
39	**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\!=\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\% in initial seed) without any architectural modification.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "64f349b1-f65c-4ca7-afb3-d4dd8ddbca3c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
      "content": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the CIVO phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is a model-agnostic framework evaluated on TD-MPC2, which uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{CIVO} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our CIVO mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \\citep{venkatraman2015improving, lambert2022investigating}. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.\n\nOur findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n## 2.5 Diagnostic Methodology\n\nOur diagnostic methodology follows a tradition of systematic controlled experiments in RL. \\citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \\citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01Smkw7Rfpj4QpnY8d3LKGVs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/results_section_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "8b42e9cf-4e1c-4078-a86d-9d4d37f3765d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNekw8Hk9ZB19SdPrLUbhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11671,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11671
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

_source line 11 · 2026-05-16T20:02:37.252Z_

<details><summary>↩ Tool result · `toolu_01Smkw7Rfpj4QpnY8d3LKGVs`</summary>

```text
1	# Results Section Draft (LaTeX-ready)
2	
3	## 4. Results
4	
5	We organize our findings into seven progressively deeper diagnostics, moving from phenomenon characterization (F1--F2) through causal isolation (F3--F4) to mechanistic explanation (F5) and intervention (F6--F7).
6	
7	All experiments use DreamerV3 on DeepMind Control Suite unless stated otherwise. We report eval returns (mean over 10 episodes, every 5K steps) and the Normalized Value Excess (NVE), defined as the ratio of the critic's imagined value to the realized evaluation return. An NVE $>1.5\times$ sustained over $\geq$10K steps indicates pathological overestimation. Bootstrap 95\% confidence intervals (10,000 resamples) are reported where sample size permits ($n \geq 3$).
8	
9	### 4.1 Finding 1: Variable-Rate Imagination Universally Degrades Performance
10	
11	\textbf{Setup.} We augment DreamerV3 with a discrete duration token $d_t \in \{1,2,4\}$ appended to the imagination trajectory, comparing against vanilla DreamerV3 (exp\_001, eval 916@105K, 970@505K).
12	
13	\textbf{Results.} All variable-rate configurations collapse:
14	\begin{itemize}
15	  \item \textbf{exp\_005} (learned gating): peak 541@55K $\rightarrow$ 99@145K (10.4\% of baseline)
16	  \item \textbf{exp\_006} (fixed $d_t=2$): peak 485@35K $\rightarrow$ 133@65K; value/eval ratio inflates from 31\% to 272\%
17	  \item \textbf{exp\_007} (fixed $d_t=4$): peak 177@25K, never recovers (33\% of baseline at best)
18	\end{itemize}
19	
20	The severity scales with temporal skip: $d_t=2$ degrades performance by $\sim$85\% and $d_t=4$ by $\sim$81\% from peak, with larger skips producing earlier and more severe collapses. This establishes the core phenomenon: multi-step imagination in world-model RL induces a failure mode absent from standard single-step training.
21	
22	### 4.2 Finding 2: Conditioning-Induced Value Overestimation (CIVO) Is the Primary Failure Mode
23	
24	\textbf{Setup.} We isolate the role of the trained duration embedding (dt\_emb) by comparing configurations with and without it under matched architectures ($d_t=2$, $H=8$, subsample ON, Walker Walk).
25	
26	\textbf{Primary demonstration (exp\_008d).} With trained dt\_emb: eval 167@25K $\rightarrow$ 83@55K (collapse onset), NVE peaks at $4.12\times$@55K and remains $>1.5\times$ through 105K. The critic's imagined values inflate to 1.67$\times$ the realized return at collapse, and actor loss flips positive by 85K---indicating the critic actively drives policy toward worse actions.
27	
28	\textbf{Statistical separation.} Across conditions:
29	\begin{itemize}
30	  \item \textbf{Trained dt\_emb} ($n=3$): NVE peak mean $3.43\times$ [95\% CI: 2.05, 4.12]; collapse rate 0.667
31	  \item \textbf{No dt\_emb} ($n=2$): NVE peak mean $1.14\times$ [95\% CI: 1.02, 1.26]; collapse rate 0.000
32	  \item \textbf{Effect size}: $\Delta$ NVE peak $= +2.29$ [95\% CI: +0.91, +3.10]; CI excludes zero
33	\end{itemize}
34	
35	The NVE $>1.5\times$ threshold achieves perfect binary classification: all trained dt\_emb runs (3/3) exceed it; no baseline runs (0/2) do. The stochastic nature of collapse (2/3 seeds collapse fully) is consistent with a necessary-but-not-sufficient trigger: the trained dt\_emb creates vulnerability, but whether it manifests depends on the training trajectory.
36	
37	\textbf{Variant behavior (exp\_009b, seed 2).} NVE peaks at $2.04\times$@25K but self-corrects to $0.38\times$@105K (eval 278, stable). This transient CIVO confirms that trained dt\_emb reliably triggers overestimation, though collapse is not deterministic---reinforcing the diagnostic framing over a guaranteed failure claim.
38	
39	### 4.3 Finding 3: Causal Ablation Confirms dt\_emb as Necessary Condition
40	
41	\textbf{Ablation 1: Remove dt\_emb entirely (exp\_008f).} Configuration identical to exp\_008d except dt\_emb is replaced with a zero vector. Result: eval stable at 503@105K (no collapse), NVE peaks at $0.97\times$ (never exceeds $1.5\times$). Performance is lower than vanilla DreamerV3 due to the multi-step imagination overhead, but critically, no pathological overestimation emerges.
42	
43	\textbf{Ablation 2: Freeze dt\_emb (exp\_015b).} The duration embedding is initialized randomly and frozen (no gradient updates). Result: NVE peaks at $1.45\times$@55K (briefly, stays below $1.5\times$ threshold), with partial recovery to eval 204@105K. The degradation reflects gradient starvation (the model cannot leverage duration information) rather than CIVO---the failure mode is qualitatively different (no sustained value inflation).
44	
45	\textbf{Ablation 3: Vanilla DreamerV3 without any gating (exp\_020).} Seed 2, $H=15$, no dt\_emb, no gate, no subsample. Result: stable 837@105K with no collapse. A 75K--95K dip (689$\rightarrow$596) represents normal variance with full recovery to 837. Compared against exp\_008e\_v3\_s2 (same seed, same hyperparameters, but WITH trained dt\_emb): that run collapses 715$\rightarrow$137@105K (NVE $3.78\times$).
46	
47	\textbf{Interpretation.} The conjunction of these three ablations establishes trained dt\_emb as a necessary condition for both CIVO (Pathway A) and the secondary instability mode (Pathway B, \S4.7). The embedding itself is not toxic---it must be trained, receiving gradient updates that create the pathological feedback loop.
48	
49	### 4.4 Finding 4: Cross-Environment Generalization (Cheetah Run)
50	
51	\textbf{Setup.} To address whether CIVO is specific to the Walker Walk morphology, we replicate the diagnostic configuration (trained dt\_emb, subsample ON, $d_t=2$, $H=8$) on Cheetah Run (exp\_010b, seed 1).
52	
53	\textbf{Result.} NVE reaches $8.63\times$ (sustained average; raw peak $14.59\times$), with eval collapsing from 287@45K $\rightarrow$ 45@105K. All 5 CIVO diagnostic criteria are met:
54	\begin{enumerate}
55	  \item NVE $> 1.5\times$ sustained $\checkmark$ ($8.63\times$)
56	  \item Monotonic eval decline post-peak $\checkmark$ (287$\rightarrow$45)
57	  \item Value inflation precedes eval collapse $\checkmark$
58	  \item Entropy reduction (policy lock-in) $\checkmark$
59	  \item Positive actor loss (critic drives degradation) $\checkmark$
60	\end{enumerate}
61	
62	\textbf{Comparison.} The Cheetah baseline (exp\_010a, same config without trained dt\_emb) reaches stable 654@105K. The CIVO effect is more severe in Cheetah (NVE $8.63\times$ vs Walker's $4.12\times$), possibly because the faster dynamics amplify multi-step prediction errors.
63	
64	\textbf{Implication.} CIVO is environment-general. It emerges from the interaction between trained temporal embeddings and the world-model training objective, not from specific kinematic properties of Walker Walk.
65	
66	### 4.5 Finding 5: Gradient Decomposition Reveals Observation Decoder Dominance
67	
68	\textbf{Setup.} We decompose gradients flowing through dt\_emb by source component using per-loss backward passes at multiple checkpoints during exp\_008d training (methodology in Appendix~\ref{app:gradient}).
69	
70	\textbf{Gradient composition evolves during training:}
71	\begin{itemize}
72	  \item \textbf{Step 55K} (pre-collapse): obs decoders 25.8\%, reward head 23.5\%, KL dynamics 50.7\%
73	  \item \textbf{Step 105K} (post-collapse): obs decoders \textbf{93\%}, reward head \textbf{0\%}, KL dynamics 7\%
74	\end{itemize}
75	
76	The observation decoder gradient norm grows from 0.601 to 1.505 while total gradient norm \emph{decreases} (2.33$\rightarrow$1.62), indicating that other components' gradients collapse as the obs decoder dominates. This constitutes a positive feedback loop: obs decoder gradients reshape dt\_emb $\rightarrow$ dt\_emb misrepresents temporal context $\rightarrow$ critic overestimates $\rightarrow$ policy degrades $\rightarrow$ obs decoder receives higher loss $\rightarrow$ obs decoder gradients grow further.
77	
78	\textbf{Counterfactual: reward-only SGS (exp\_016e).} Blocking only the reward head gradient from dt\_emb is a no-op, since reward contributes 0\% by the time collapse occurs. In fact, this intervention \emph{worsens} outcomes: NVE reaches $10.42\times$@95K with eval collapsing to 32 (vs 008d's 131@105K). This confirms that the CIVO mechanism is driven by observation reconstruction, not reward prediction.
79	
80	### 4.6 Finding 6: Full Selective Gradient Stopping Eliminates CIVO
81	
82	\textbf{Setup (exp\_018v2).} We apply Full-SGS: detaching the observation decoder's gradient path from dt\_emb while preserving all other gradient flows. Configuration otherwise identical to exp\_008d (trained dt\_emb, subsample ON, $d_t=2$, $H=8$, Walker Walk, seed 1).
83	
84	\textbf{Result.}
85	\begin{itemize}
86	  \item NVE sustained average: $1.34\times$ over 35K+ window (vs 008d's $4.12\times$)
87	  \item Eval peak: 499.6@75K; final: 448.3@105K (vs 008d's 131@105K)
88	  \item No collapse detected through 105K steps
89	  \item Gradient composition with SGS: obs decoder contribution stays $\sim$24\% (blocked from reaching dt\_emb), preventing the runaway feedback loop
90	\end{itemize}
91	
92	\textbf{Quantification.} Full-SGS eliminates 79\% of excess NVE ($4.12 \rightarrow 1.34$ on a baseline of $\sim$1.0) and achieves $3.4\times$ higher final eval return than the matched CIVO condition. While performance remains below vanilla DreamerV3 (448 vs 916), this gap reflects the inherent cost of multi-step imagination without full architectural support, not residual CIVO.
93	
94	\textbf{Limitation.} This result is from a single seed ($n=1$). We report it as proof-of-concept evidence that the identified mechanism (obs decoder $\rightarrow$ dt\_emb gradient pathway) is causally responsible for CIVO, not as a mature intervention. A second seed is needed before claiming reliable mitigation.
95	
96	### 4.7 Finding 7: Pathway B---A Secondary Instability Mode
97	
98	\textbf{Observation (exp\_008e\_v3\_s2).} Under trained dt\_emb with $d_t=1$ imagination (which should prevent CIVO by eliminating multi-step value estimation), one of two seeds still collapses: eval 715@85K $\rightarrow$ 137@105K, NVE $3.78\times$.
99	
100	\textbf{Differential diagnosis.} This collapse is mechanistically distinct from CIVO:
101	\begin{itemize}
102	  \item CIVO (Pathway A, exp\_008d): value inflates \emph{before} eval drops; entropy \emph{decreases} (policy locks into suboptimal actions)
103	  \item Pathway B (exp\_008e\_v3\_s2): value tracks target closely until late; entropy \emph{increases}; value standard deviation explodes ($7.4 \rightarrow 18.3$), indicating noisy critic gradients destabilize policy
104	\end{itemize}
105	
106	\textbf{Necessary condition test (exp\_020).} Vanilla DreamerV3 with identical seed=2 and $H=15$ (no dt\_emb) remains stable at 837@105K. This rules out inherent DreamerV3 fragility or seed-specific instability as explanations---trained dt\_emb is necessary for Pathway B as well.
107	
108	\textbf{Interpretation.} Trained dt\_emb introduces vulnerability through at least two distinct pathways. CIVO (Pathway A) operates via observation decoder gradient corruption and can be blocked by SGS. Pathway B operates via increased value estimation variance under distributional shift and is not addressed by SGS. This represents residual risk: even with SGS intervention, trained temporal embeddings may destabilize training through secondary mechanisms. We flag this as an open problem requiring further investigation.
109	
110	\textbf{Stochastic nature.} Pathway B manifests in 1/2 seeds under $d_t=1$ imagination. Combined with CIVO's 2/3 collapse rate, trained dt\_emb configurations show an aggregate collapse rate of 67--75\% across conditions, reinforcing the diagnostic conclusion that temporal abstraction via learned embeddings is a high-risk architectural choice in world-model RL.
111	
112	---
113	
114	## Summary of Key Metrics
115	
116	| Finding | Primary Exp | Key Metric | Comparison | Statistical Support |
117	|---------|-------------|-----------|------------|-------------------|
118	| F1 | 005/006/007 | Peak $\rightarrow$ collapse | Baseline 916 stable | $n=3$ environments |
119	| F2 | 008d | NVE $4.12\times$ | No-dt\_emb $1.14\times$ | $\Delta=+2.29$ [0.91, 3.10] |
120	| F3 | 008f/015b/020 | NVE $<1.5\times$, no collapse | 008d/008e\_v3\_s2 collapse | 3 independent ablations |
121	| F4 | 010b | NVE $8.63\times$, Cheetah | 010a stable 654 | $n=1$ (cross-env) |
122	| F5 | 008d gradient | Obs 93\% @ 105K | Obs 25.8\% @ 55K | Temporal evolution |
123	| F6 | 018v2 | NVE $1.34\times$, eval 448 | 008d NVE $4.12\times$, eval 131 | $n=1$ (proof-of-concept) |
124	| F7 | 008e\_v3\_s2 | Collapse 715$\rightarrow$137 | 020 stable 837 | Same-seed control |
125	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "fd35ec8a-c7f5-43be-9028-56ab1c48e2ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/results_section_draft.md",
      "content": "# Results Section Draft (LaTeX-ready)\n\n## 4. Results\n\nWe organize our findings into seven progressively deeper diagnostics, moving from phenomenon characterization (F1--F2) through causal isolation (F3--F4) to mechanistic explanation (F5) and intervention (F6--F7).\n\nAll experiments use DreamerV3 on DeepMind Control Suite unless stated otherwise. We report eval returns (mean over 10 episodes, every 5K steps) and the Normalized Value Excess (NVE), defined as the ratio of the critic's imagined value to the realized evaluation return. An NVE $>1.5\\times$ sustained over $\\geq$10K steps indicates pathological overestimation. Bootstrap 95\\% confidence intervals (10,000 resamples) are reported where sample size permits ($n \\geq 3$).\n\n### 4.1 Finding 1: Variable-Rate Imagination Universally Degrades Performance\n\n\\textbf{Setup.} We augment DreamerV3 with a discrete duration token $d_t \\in \\{1,2,4\\}$ appended to the imagination trajectory, comparing against vanilla DreamerV3 (exp\\_001, eval 916@105K, 970@505K).\n\n\\textbf{Results.} All variable-rate configurations collapse:\n\\begin{itemize}\n  \\item \\textbf{exp\\_005} (learned gating): peak 541@55K $\\rightarrow$ 99@145K (10.4\\% of baseline)\n  \\item \\textbf{exp\\_006} (fixed $d_t=2$): peak 485@35K $\\rightarrow$ 133@65K; value/eval ratio inflates from 31\\% to 272\\%\n  \\item \\textbf{exp\\_007} (fixed $d_t=4$): peak 177@25K, never recovers (33\\% of baseline at best)\n\\end{itemize}\n\nThe severity scales with temporal skip: $d_t=2$ degrades performance by $\\sim$85\\% and $d_t=4$ by $\\sim$81\\% from peak, with larger skips producing earlier and more severe collapses. This establishes the core phenomenon: multi-step imagination in world-model RL induces a failure mode absent from standard single-step training.\n\n### 4.2 Finding 2: Conditioning-Induced Value Overestimation (CIVO) Is the Primary Failure Mode\n\n\\textbf{Setup.} We isolate the role of the trained duration embedding (dt\\_emb) by comparing configurations with and without it under matched architectures ($d_t=2$, $H=8$, subsample ON, Walker Walk).\n\n\\textbf{Primary demonstration (exp\\_008d).} With trained dt\\_emb: eval 167@25K $\\rightarrow$ 83@55K (collapse onset), NVE peaks at $4.12\\times$@55K and remains $>1.5\\times$ through 105K. The critic's imagined values inflate to 1.67$\\times$ the realized return at collapse, and actor loss flips positive by 85K---indicating the critic actively drives policy toward worse actions.\n\n\\textbf{Statistical separation.} Across conditions:\n\\begin{itemize}\n  \\item \\textbf{Trained dt\\_emb} ($n=3$): NVE peak mean $3.43\\times$ [95\\% CI: 2.05, 4.12]; collapse rate 0.667\n  \\item \\textbf{No dt\\_emb} ($n=2$): NVE peak mean $1.14\\times$ [95\\% CI: 1.02, 1.26]; collapse rate 0.000\n  \\item \\textbf{Effect size}: $\\Delta$ NVE peak $= +2.29$ [95\\% CI: +0.91, +3.10]; CI excludes zero\n\\end{itemize}\n\nThe NVE $>1.5\\times$ threshold achieves perfect binary classification: all trained dt\\_emb runs (3/3) exceed it; no baseline runs (0/2) do. The stochastic nature of collapse (2/3 seeds collapse fully) is consistent with a necessary-but-not-sufficient trigger: the trained dt\\_emb creates vulnerability, but whether it manifests depends on the training trajectory.\n\n\\textbf{Variant behavior (exp\\_009b, seed 2).} NVE peaks at $2.04\\times$@25K but self-corrects to $0.38\\times$@105K (eval 278, stable). This transient CIVO confirms that trained dt\\_emb reliably triggers overestimation, though collapse is not deterministic---reinforcing the diagnostic framing over a guaranteed failure claim.\n\n### 4.3 Finding 3: Causal Ablation Confirms dt\\_emb as Necessary Condition\n\n\\textbf{Ablation 1: Remove dt\\_emb entirely (exp\\_008f).} Configuration identical to exp\\_008d except dt\\_emb is replaced with a zero vector. Result: eval stable at 503@105K (no collapse), NVE peaks at $0.97\\times$ (never exceeds $1.5\\times$). Performance is lower than vanilla DreamerV3 due to the multi-step imagination overhead, but critically, no pathological overestimation emerges.\n\n\\textbf{Ablation 2: Freeze dt\\_emb (exp\\_015b).} The duration embedding is initialized randomly and frozen (no gradient updates). Result: NVE peaks at $1.45\\times$@55K (briefly, stays below $1.5\\times$ threshold), with partial recovery to eval 204@105K. The degradation reflects gradient starvation (the model cannot leverage duration information) rather than CIVO---the failure mode is qualitatively different (no sustained value inflation).\n\n\\textbf{Ablation 3: Vanilla DreamerV3 without any gating (exp\\_020).} Seed 2, $H=15$, no dt\\_emb, no gate, no subsample. Result: stable 837@105K with no collapse. A 75K--95K dip (689$\\rightarrow$596) represents normal variance with full recovery to 837. Compared against exp\\_008e\\_v3\\_s2 (same seed, same hyperparameters, but WITH trained dt\\_emb): that run collapses 715$\\rightarrow$137@105K (NVE $3.78\\times$).\n\n\\textbf{Interpretation.} The conjunction of these three ablations establishes trained dt\\_emb as a necessary condition for both CIVO (Pathway A) and the secondary instability mode (Pathway B, \\S4.7). The embedding itself is not toxic---it must be trained, receiving gradient updates that create the pathological feedback loop.\n\n### 4.4 Finding 4: Cross-Environment Generalization (Cheetah Run)\n\n\\textbf{Setup.} To address whether CIVO is specific to the Walker Walk morphology, we replicate the diagnostic configuration (trained dt\\_emb, subsample ON, $d_t=2$, $H=8$) on Cheetah Run (exp\\_010b, seed 1).\n\n\\textbf{Result.} NVE reaches $8.63\\times$ (sustained average; raw peak $14.59\\times$), with eval collapsing from 287@45K $\\rightarrow$ 45@105K. All 5 CIVO diagnostic criteria are met:\n\\begin{enumerate}\n  \\item NVE $> 1.5\\times$ sustained $\\checkmark$ ($8.63\\times$)\n  \\item Monotonic eval decline post-peak $\\checkmark$ (287$\\rightarrow$45)\n  \\item Value inflation precedes eval collapse $\\checkmark$\n  \\item Entropy reduction (policy lock-in) $\\checkmark$\n  \\item Positive actor loss (critic drives degradation) $\\checkmark$\n\\end{enumerate}\n\n\\textbf{Comparison.} The Cheetah baseline (exp\\_010a, same config without trained dt\\_emb) reaches stable 654@105K. The CIVO effect is more severe in Cheetah (NVE $8.63\\times$ vs Walker's $4.12\\times$), possibly because the faster dynamics amplify multi-step prediction errors.\n\n\\textbf{Implication.} CIVO is environment-general. It emerges from the interaction between trained temporal embeddings and the world-model training objective, not from specific kinematic properties of Walker Walk.\n\n### 4.5 Finding 5: Gradient Decomposition Reveals Observation Decoder Dominance\n\n\\textbf{Setup.} We decompose gradients flowing through dt\\_emb by source component using per-loss backward passes at multiple checkpoints during exp\\_008d training (methodology in Appendix~\\ref{app:gradient}).\n\n\\textbf{Gradient composition evolves during training:}\n\\begin{itemize}\n  \\item \\textbf{Step 55K} (pre-collapse): obs decoders 25.8\\%, reward head 23.5\\%, KL dynamics 50.7\\%\n  \\item \\textbf{Step 105K} (post-collapse): obs decoders \\textbf{93\\%}, reward head \\textbf{0\\%}, KL dynamics 7\\%\n\\end{itemize}\n\nThe observation decoder gradient norm grows from 0.601 to 1.505 while total gradient norm \\emph{decreases} (2.33$\\rightarrow$1.62), indicating that other components' gradients collapse as the obs decoder dominates. This constitutes a positive feedback loop: obs decoder gradients reshape dt\\_emb $\\rightarrow$ dt\\_emb misrepresents temporal context $\\rightarrow$ critic overestimates $\\rightarrow$ policy degrades $\\rightarrow$ obs decoder receives higher loss $\\rightarrow$ obs decoder gradients grow further.\n\n\\textbf{Counterfactual: reward-only SGS (exp\\_016e).} Blocking only the reward head gradient from dt\\_emb is a no-op, since reward contributes 0\\% by the time collapse occurs. In fact, this intervention \\emph{worsens} outcomes: NVE reaches $10.42\\times$@95K with eval collapsing to 32 (vs 008d's 131@105K). This confirms that the CIVO mechanism is driven by observation reconstruction, not reward prediction.\n\n### 4.6 Finding 6: Full Selective Gradient Stopping Eliminates CIVO\n\n\\textbf{Setup (exp\\_018v2).} We apply Full-SGS: detaching the observation decoder's gradient path from dt\\_emb while preserving all other gradient flows. Configuration otherwise identical to exp\\_008d (trained dt\\_emb, subsample ON, $d_t=2$, $H=8$, Walker Walk, seed 1).\n\n\\textbf{Result.}\n\\begin{itemize}\n  \\item NVE sustained average: $1.34\\times$ over 35K+ window (vs 008d's $4.12\\times$)\n  \\item Eval peak: 499.6@75K; final: 448.3@105K (vs 008d's 131@105K)\n  \\item No collapse detected through 105K steps\n  \\item Gradient composition with SGS: obs decoder contribution stays $\\sim$24\\% (blocked from reaching dt\\_emb), preventing the runaway feedback loop\n\\end{itemize}\n\n\\textbf{Quantification.} Full-SGS eliminates 79\\% of excess NVE ($4.12 \\rightarrow 1.34$ on a baseline of $\\sim$1.0) and achieves $3.4\\times$ higher final eval return than the matched CIVO condition. While performance remains below vanilla DreamerV3 (448 vs 916), this gap reflects the inherent cost of multi-step imagination without full architectural support, not residual CIVO.\n\n\\textbf{Limitation.} This result is from a single seed ($n=1$). We report it as proof-of-concept evidence that the identified mechanism (obs decoder $\\rightarrow$ dt\\_emb gradient pathway) is causally responsible for CIVO, not as a mature intervention. A second seed is needed before claiming reliable mitigation.\n\n### 4.7 Finding 7: Pathway B---A Secondary Instability Mode\n\n\\textbf{Observation (exp\\_008e\\_v3\\_s2).} Under trained dt\\_emb with $d_t=1$ imagination (which should prevent CIVO by eliminating multi-step value estimation), one of two seeds still collapses: eval 715@85K $\\rightarrow$ 137@105K, NVE $3.78\\times$.\n\n\\textbf{Differential diagnosis.} This collapse is mechanistically distinct from CIVO:\n\\begin{itemize}\n  \\item CIVO (Pathway A, exp\\_008d): value inflates \\emph{before} eval drops; entropy \\emph{decreases} (policy locks into suboptimal actions)\n  \\item Pathway B (exp\\_008e\\_v3\\_s2): value tracks target closely until late; entropy \\emph{increases}; value standard deviation explodes ($7.4 \\rightarrow 18.3$), indicating noisy critic gradients destabilize policy\n\\end{itemize}\n\n\\textbf{Necessary condition test (exp\\_020).} Vanilla DreamerV3 with identical seed=2 and $H=15$ (no dt\\_emb) remains stable at 837@105K. This rules out inherent DreamerV3 fragility or seed-specific instability as explanations---trained dt\\_emb is necessary for Pathway B as well.\n\n\\textbf{Interpretation.} Trained dt\\_emb introduces vulnerability through at least two distinct pathways. CIVO (Pathway A) operates via observation decoder gradient corruption and can be blocked by SGS. Pathway B operates via increased value estimation variance under distributional shift and is not addressed by SGS. This represents residual risk: even with SGS intervention, trained temporal embeddings may destabilize training through secondary mechanisms. We flag this as an open problem requiring further investigation.\n\n\\textbf{Stochastic nature.} Pathway B manifests in 1/2 seeds under $d_t=1$ imagination. Combined with CIVO's 2/3 collapse rate, trained dt\\_emb configurations show an aggregate collapse rate of 67--75\\% across conditions, reinforcing the diagnostic conclusion that temporal abstraction via learned embeddings is a high-risk architectural choice in world-model RL.\n\n---\n\n## Summary of Key Metrics\n\n| Finding | Primary Exp | Key Metric | Comparison | Statistical Support |\n|---------|-------------|-----------|------------|-------------------|\n| F1 | 005/006/007 | Peak $\\rightarrow$ collapse | Baseline 916 stable | $n=3$ environments |\n| F2 | 008d | NVE $4.12\\times$ | No-dt\\_emb $1.14\\times$ | $\\Delta=+2.29$ [0.91, 3.10] |\n| F3 | 008f/015b/020 | NVE $<1.5\\times$, no collapse | 008d/008e\\_v3\\_s2 collapse | 3 independent ablations |\n| F4 | 010b | NVE $8.63\\times$, Cheetah | 010a stable 654 | $n=1$ (cross-env) |\n| F5 | 008d gradient | Obs 93\\% @ 105K | Obs 25.8\\% @ 55K | Temporal evolution |\n| F6 | 018v2 | NVE $1.34\\times$, eval 448 | 008d NVE $4.12\\times$, eval 131 | $n=1$ (proof-of-concept) |\n| F7 | 008e\\_v3\\_s2 | Collapse 715$\\rightarrow$137 | 020 stable 837 | Same-seed control |\n",
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

_source line 12_

Now I have the full context. Let me also check if there are any other relevant files like a ROADMAP or ideas that might inform the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "f1c7f2d9-2b7a-4b19-9df5-873369952662",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzVJmePMvPaaPierGxxUoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20463,
      "cache_read_input_tokens": 23512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20463
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

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EK9ha9wgJFZa5LigaKJp2F`</summary>

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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "2dc7d590-42f0-484f-8dba-6d3f98f264df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzVJmePMvPaaPierGxxUoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20463,
      "cache_read_input_tokens": 23512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20463
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

_source line 14 · 2026-05-16T20:02:45.896Z_

<details><summary>↩ Tool result · `toolu_01EK9ha9wgJFZa5LigaKJp2F`</summary>

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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "bc971077-16d4-4720-bdf0-6b91fa796606",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
I now have enough context to write the Introduction section. Let me synthesize the key information:

1. **Paper positioning**: Diagnostic paper about why temporal abstraction fails in DreamerV3's imagination-based training
2. **Core finding**: Trained dt_embedding causes CIVO (Conditioning-Induced Value Overestimation)
3. **Key contrast with TAWM**: dt-conditioning works in MPC (TD-MPC2) but fails in imagination-based actor-critic
4. **Mechanism**: trained dt_emb → obs decoder gradient dominance (93%) → value overestimation → actor exploitation → collapse
5. **Full-SGS**: Blocking obs decoder gradient to dt_emb eliminates CIVO (proof-of-concept)


6. **Cross-environment validation**: This failure pattern holds consistently across Walker Walk and Cheetah Run

Now I'll structure the introduction to build from motivation through our specific diagnosis and contributions, using the key references to ground the work in the broader MBRL literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "fc06e1a7-acc7-48ef-bec7-84ff8cf1d4fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSr1QPfTGKSxz4WBm7LS5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 43975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 16_

Now I have all the context needed. Let me write the introduction draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "11671120-afa8-4a79-99d1-5d5b68d67bc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSr1QPfTGKSxz4WBm7LS5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 43975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

<details open><summary>🔧 Tool call — Bash · `toolu_01UT4phb3RJZw4CBcjetLJQ9`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/",
  "description": "List existing paper drafts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "88d32014-e40d-4e4c-afdc-ecae355ab5a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSr1QPfTGKSxz4WBm7LS5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 43975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
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

_source line 18 · 2026-05-16T20:03:02.273Z_

<details><summary>↩ Tool result · `toolu_01UT4phb3RJZw4CBcjetLJQ9`</summary>

```text
gradient_decomposition_methodology.md
related_work_draft.md
results_section_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "9bc4ef78-425f-4b30-8c8f-208a06488516",
  "tool_use_result": {
    "stdout": "gradient_decomposition_methodology.md\nrelated_work_draft.md\nresults_section_draft.md",
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

_source line 19_

<details open><summary>🔧 Tool call — Write · `toolu_01NFwkExcyWuu2cYftD8auRL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/introduction_draft.md",
  "content": "# Introduction — Draft\n\n## 1. Introduction\n\nTemporal abstraction---the ability to reason and plan at multiple timescales---is a long-standing aspiration in reinforcement learning \\citep{sutton1999options, precup2000temporal}. In world-model RL, where an agent learns a predictive dynamics model and trains its policy entirely within imagined rollouts \\citep{hafner2023dreamerv3}, temporal abstraction is especially appealing: by conditioning the world model on a duration token $d_t$, one can in principle generate imagined trajectories at variable temporal granularity, improving planning efficiency for slow dynamics without sacrificing precision for fast ones. Recent work on Time-Aware World Models \\citep[TAWM;][]{nhu2025tawm} demonstrates that such $\\Delta t$-conditioning improves performance and data efficiency when combined with model-predictive control in TD-MPC2 \\citep{hansen2024tdmpc2}. These results suggest that variable-rate world models are a viable path toward temporally abstract model-based agents.\n\nHowever, the story changes when variable-rate predictions are used not for online planning but for \\emph{imagination-based actor-critic training}---the paradigm underlying DreamerV3 \\citep{hafner2023dreamerv3} and its predecessors \\citep{hafner2020dreamerv1, hafner2021dreamerv2}. In this setting, the actor and critic are trained entirely on synthetic rollouts generated by the world model. The critic's value estimates are never grounded against real environment returns during training; instead, they bootstrap from the model's own predictions. We find that introducing a trained duration embedding ($d_t$-embedding) into this loop creates a pathological feedback cycle: the critic learns $d_t$-conditioned value estimates that exploit the world model's imprecise multi-step predictions, producing systematic overestimation that the actor then exploits, further degrading policy quality. We term this failure mode \\emph{Conditioning-Induced Value Overestimation} (CIVO).\n\nIn this paper, we present a systematic diagnostic analysis of CIVO in DreamerV3. Through a factorial experiment design that independently varies $d_t$-embedding training, temporal subsampling, imagination horizon, and duration skip on DeepMind Control Suite tasks, we isolate the trained $d_t$-embedding as the necessary condition for pathological value overestimation. We introduce the Normalized Value Excess (NVE)---the ratio of the critic's imagined value to the realized evaluation return, normalized by the baseline's ratio at the same training step---as a diagnostic metric, and show that a threshold of NVE $> 1.5\\times$ achieves perfect binary separation between trained and untrained $d_t$-embedding configurations across all tested seeds. Gradient decomposition reveals the mechanistic pathway: by the time of collapse, 93\\% of the gradient flowing through $d_t$-embedding originates from observation decoders, with reward contributing 0\\%. This motivates Full Selective Gradient Stopping (Full-SGS)---detaching the observation decoder gradient from $d_t$-embedding---which eliminates CIVO as a proof-of-concept intervention, reducing NVE from $4.12\\times$ to $1.34\\times$ and recovering $3.4\\times$ higher evaluation return than the matched CIVO condition.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Phenomenon identification.} We establish that all variable-rate imagination configurations in DreamerV3 degrade performance relative to single-step baselines, with severity monotonically increasing in $d_t$ (Section~4.1). This failure is absent from MPC-based approaches \\citep{nhu2025tawm}, revealing a paradigm-dependent asymmetry in the viability of temporal conditioning.\n\n    \\item \\textbf{Causal diagnosis.} Through controlled ablations across two environments (Walker Walk, Cheetah Run) and multiple seeds, we identify the trained $d_t$-embedding as the necessary condition for CIVO. Removing it eliminates pathological overestimation; freezing it prevents the feedback loop. The NVE $> 1.5\\times$ threshold provides a reliable diagnostic marker with perfect separating power across conditions (Section~4.2--4.4).\n\n    \\item \\textbf{Mechanistic explanation.} Gradient decomposition traces CIVO to observation decoder gradient dominance over $d_t$-embedding: a positive feedback loop where reconstruction loss reshapes temporal conditioning, which corrupts critic estimates, which degrades the actor, which increases reconstruction loss. This reveals the causal pathway and explains why reward-only gradient interventions are ineffective (Section~4.5).\n\n    \\item \\textbf{Proof-of-concept intervention.} Full-SGS, which blocks the identified gradient pathway, eliminates CIVO in matched experiments. We present this as mechanistic validation rather than a mature solution, and characterize residual failure modes (Pathway B instability) that trained $d_t$-embeddings introduce through channels beyond value overestimation (Section~4.6--4.7).\n\\end{enumerate}\n\nOur findings carry a practical implication for the field: before building variable-$d_t$ world-model agents that train via imagination, the CIVO failure mode must be addressed. The specific vulnerability we identify---that temporal conditioning amplifies rather than compensates for model imprecision in imagination-based training---suggests that architectural solutions (e.g., hierarchical temporal abstractions \\citep{gumbsch2024thick, mattes2024hieros} that avoid flat $d_t$-conditioning) may be more promising than parametric fixes.\n\nThe remainder of this paper is organized as follows. Section~2 reviews related work on temporal abstraction, world-model RL, and value overestimation. Section~3 describes our experimental methodology and diagnostic metrics. Section~4 presents findings, progressing from phenomenon characterization through causal isolation to mechanistic explanation. Section~5 discusses implications, limitations, and directions for future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "a36caa5c-1464-4b36-be11-d263c9649034",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01843w9QmEAoYL9E51XstRWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 44440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 597
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

_source line 20 · 2026-05-16T20:03:37.832Z_

<details><summary>↩ Tool result · `toolu_01NFwkExcyWuu2cYftD8auRL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/introduction_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "f976651d-a7ef-4c23-bfc5-52d745c0921e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/introduction_draft.md",
    "content": "# Introduction — Draft\n\n## 1. Introduction\n\nTemporal abstraction---the ability to reason and plan at multiple timescales---is a long-standing aspiration in reinforcement learning \\citep{sutton1999options, precup2000temporal}. In world-model RL, where an agent learns a predictive dynamics model and trains its policy entirely within imagined rollouts \\citep{hafner2023dreamerv3}, temporal abstraction is especially appealing: by conditioning the world model on a duration token $d_t$, one can in principle generate imagined trajectories at variable temporal granularity, improving planning efficiency for slow dynamics without sacrificing precision for fast ones. Recent work on Time-Aware World Models \\citep[TAWM;][]{nhu2025tawm} demonstrates that such $\\Delta t$-conditioning improves performance and data efficiency when combined with model-predictive control in TD-MPC2 \\citep{hansen2024tdmpc2}. These results suggest that variable-rate world models are a viable path toward temporally abstract model-based agents.\n\nHowever, the story changes when variable-rate predictions are used not for online planning but for \\emph{imagination-based actor-critic training}---the paradigm underlying DreamerV3 \\citep{hafner2023dreamerv3} and its predecessors \\citep{hafner2020dreamerv1, hafner2021dreamerv2}. In this setting, the actor and critic are trained entirely on synthetic rollouts generated by the world model. The critic's value estimates are never grounded against real environment returns during training; instead, they bootstrap from the model's own predictions. We find that introducing a trained duration embedding ($d_t$-embedding) into this loop creates a pathological feedback cycle: the critic learns $d_t$-conditioned value estimates that exploit the world model's imprecise multi-step predictions, producing systematic overestimation that the actor then exploits, further degrading policy quality. We term this failure mode \\emph{Conditioning-Induced Value Overestimation} (CIVO).\n\nIn this paper, we present a systematic diagnostic analysis of CIVO in DreamerV3. Through a factorial experiment design that independently varies $d_t$-embedding training, temporal subsampling, imagination horizon, and duration skip on DeepMind Control Suite tasks, we isolate the trained $d_t$-embedding as the necessary condition for pathological value overestimation. We introduce the Normalized Value Excess (NVE)---the ratio of the critic's imagined value to the realized evaluation return, normalized by the baseline's ratio at the same training step---as a diagnostic metric, and show that a threshold of NVE $> 1.5\\times$ achieves perfect binary separation between trained and untrained $d_t$-embedding configurations across all tested seeds. Gradient decomposition reveals the mechanistic pathway: by the time of collapse, 93\\% of the gradient flowing through $d_t$-embedding originates from observation decoders, with reward contributing 0\\%. This motivates Full Selective Gradient Stopping (Full-SGS)---detaching the observation decoder gradient from $d_t$-embedding---which eliminates CIVO as a proof-of-concept intervention, reducing NVE from $4.12\\times$ to $1.34\\times$ and recovering $3.4\\times$ higher evaluation return than the matched CIVO condition.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Phenomenon identification.} We establish that all variable-rate imagination configurations in DreamerV3 degrade performance relative to single-step baselines, with severity monotonically increasing in $d_t$ (Section~4.1). This failure is absent from MPC-based approaches \\citep{nhu2025tawm}, revealing a paradigm-dependent asymmetry in the viability of temporal conditioning.\n\n    \\item \\textbf{Causal diagnosis.} Through controlled ablations across two environments (Walker Walk, Cheetah Run) and multiple seeds, we identify the trained $d_t$-embedding as the necessary condition for CIVO. Removing it eliminates pathological overestimation; freezing it prevents the feedback loop. The NVE $> 1.5\\times$ threshold provides a reliable diagnostic marker with perfect separating power across conditions (Section~4.2--4.4).\n\n    \\item \\textbf{Mechanistic explanation.} Gradient decomposition traces CIVO to observation decoder gradient dominance over $d_t$-embedding: a positive feedback loop where reconstruction loss reshapes temporal conditioning, which corrupts critic estimates, which degrades the actor, which increases reconstruction loss. This reveals the causal pathway and explains why reward-only gradient interventions are ineffective (Section~4.5).\n\n    \\item \\textbf{Proof-of-concept intervention.} Full-SGS, which blocks the identified gradient pathway, eliminates CIVO in matched experiments. We present this as mechanistic validation rather than a mature solution, and characterize residual failure modes (Pathway B instability) that trained $d_t$-embeddings introduce through channels beyond value overestimation (Section~4.6--4.7).\n\\end{enumerate}\n\nOur findings carry a practical implication for the field: before building variable-$d_t$ world-model agents that train via imagination, the CIVO failure mode must be addressed. The specific vulnerability we identify---that temporal conditioning amplifies rather than compensates for model imprecision in imagination-based training---suggests that architectural solutions (e.g., hierarchical temporal abstractions \\citep{gumbsch2024thick, mattes2024hieros} that avoid flat $d_t$-conditioning) may be more promising than parametric fixes.\n\nThe remainder of this paper is organized as follows. Section~2 reviews related work on temporal abstraction, world-model RL, and value overestimation. Section~3 describes our experimental methodology and diagnostic metrics. Section~4 presents findings, progressing from phenomenon characterization through causal isolation to mechanistic explanation. Section~5 discusses implications, limitations, and directions for future work.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 21_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "f8d46fa9-dc8b-43ec-b724-01b47254aad5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPXms1Bac4Ec4G5T5mGHzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 45037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1567
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

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VFMvgmzkVZKHczPDVBBNFE`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "f12a28a5-31be-47ab-aa57-647c80d887e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPXms1Bac4Ec4G5T5mGHzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 45037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1567
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

_source line 23 · 2026-05-16T20:03:40.887Z_

<details><summary>↩ Tool result · `toolu_01VFMvgmzkVZKHczPDVBBNFE`</summary>

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
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "066f954d-f4ee-487c-a941-fcdbf935e401",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 24_

草稿已写入 `artifacts/paper_drafts/introduction_draft.md`。

结构概要：

- **Para 1**: 从temporal abstraction在MBRL中的吸引力切入，引TAWM在MPC中的成功作为正面预期
- **Para 2**: 转折——同样的dt-conditioning在imagination-based actor-critic中变成pathological feedback loop，引入CIVO术语
- **Para 3**: 贡献概述——factorial design、NVE诊断指标（>1.5x perfect separation）、梯度分解（obs decoder 93%）、Full-SGS proof-of-concept
- **Contributions 1-4**: (1) phenomenon identification + paradigm asymmetry, (2) causal diagnosis via ablations, (3) mechanistic explanation via gradient decomposition, (4) Full-SGS + Pathway B residual risk
- **Closing**: practical implication（field must address CIVO before building variable-dt agents）+ paper outline

几个写作决策：
- TAWM对比放在第一段而非contribution list，建立"MPC成功 vs imagination失败"的paradigm asymmetry作为核心tension
- Contribution 4明确标注Full-SGS为"proof-of-concept"而非mature solution，预防R2
- 末段指向hierarchical approaches作为更promising的方向，避免over-claiming
- 未使用"significantly"或"consistently"，所有数值claims可追溯到具体实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "uuid": "6b68203c-ef67-46c4-9107-880defffe2ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTdYX3e4EawhTiGuicXo9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 46604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
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

_source line 25_

草稿已写入 `artifacts/paper_drafts/introduction_draft.md`。

结构概要：

- **Para 1**: 从temporal abstraction在MBRL中的吸引力切入，引TAWM在MPC中的成功作为正面预期
- **Para 2**: 转折——同样的dt-conditioning在imagination-based actor-critic中变成pathological feedback loop，引入CIVO术语
- **Para 3**: 贡献概述——factorial design、NVE诊断指标（>1.5x perfect separation）、梯度分解（obs decoder 93%）、Full-SGS proof-of-concept
- **Contributions 1-4**: (1) phenomenon identification + paradigm asymmetry, (2) causal diagnosis via ablations, (3) mechanistic explanation via gradient decomposition, (4) Full-SGS + Pathway B residual risk
- **Closing**: practical implication（field must address CIVO before building variable-dt agents）+ paper outline

几个写作决策：
- TAWM对比放在第一段而非contribution list，建立"MPC成功 vs imagination失败"的paradigm asymmetry作为核心tension
- Contribution 4明确标注Full-SGS为"proof-of-concept"而非mature solution，预防R2
- 末段指向hierarchical approaches作为更promising的方向，避免over-claiming
- 未使用"significantly"或"consistently"，所有数值claims可追溯到具体实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 82398,
  "duration_api_ms": 83412,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "d54a69f1-c405-4bf2-9c87-10b1f736782d",
  "total_cost_usd": 0.4059905,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 35236,
    "cache_read_input_tokens": 215409,
    "output_tokens": 3056,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35236,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 386,
        "cache_read_input_tokens": 46604,
        "cache_creation_input_tokens": 473,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 473
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1526,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001601,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 3056,
      "cacheReadInputTokens": 215409,
      "cacheCreationInputTokens": 35236,
      "webSearchRequests": 0,
      "costUSD": 0.4043895,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "89df88c1-a6bb-4bb8-829b-22e0c411015f"
}
```

</details>

---
