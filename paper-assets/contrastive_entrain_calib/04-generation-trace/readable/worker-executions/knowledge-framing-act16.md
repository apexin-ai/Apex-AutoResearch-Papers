# knowledge framing act16

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_knowledge_framing-act16_20260522T040242.log`
- **Structured JSON:** [`a32cf2133e72d4107a73.json`](../../sessions/a3/a32cf2133e72d4107a73.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
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
  "uuid": "a7d9b3e6-6085-4256-bafc-6356da34d866",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-contrastive-entrain-calib/memory/"
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
    "resetsAt": 1779439800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cee8c1a0-d00c-48d8-81e1-571d9eddfc6c",
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41"
}
```

---

### Assistant

_source line 4_

Let me read the file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "9d28b5dd-00e3-4ea3-a493-877531642692",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeZVs4ETWTF5t6XQwZMAnL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12078,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12078
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

<details open><summary>🔧 Tool call — Read · `toolu_01CwUGidrtFCTnCqQYf84SS5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "9e0b1dd0-3013-4f6c-ab1a-9af627ee10f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeZVs4ETWTF5t6XQwZMAnL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12078,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12078
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

_source line 6 · 2026-05-22T04:02:55.738Z_

<details><summary>↩ Tool result · `toolu_01CwUGidrtFCTnCqQYf84SS5`</summary>

```text
1	# Paper Framing — contrastive_entrain_calib
2	
3	## Target Venue
4	- Primary: **EMNLP 2026** via ARR May 2026 cycle
5	- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)
6	- Commitment Deadline: **August 2, 2026**
7	- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改
8	- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027
9	- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)
10	
11	## Core Claims (3 条, 可证伪)
12	
13	1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.
14	   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint
15	   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence
16	   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.
17	   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.
18	   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.
19	   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).
20	
21	2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.
22	   - *Evidence*:
23	     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)
24	     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns "never change answer" → probe rewards as "non-sycophantic" → positive feedback loop → stubbornness collapse
25	     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward
26	   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.
27	   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.
28	
29	3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns "no answer change = non-sycophantic." During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.
30	   - *Evidence (full checkpoint trajectory)*:
31	     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active
32	     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)
33	     - ckpt-1500: entropy=0.61, ToF=0.0000
34	     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000
35	   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.
36	   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.
37	   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.
38	   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.
39	
40	## Story Spine
41	
42	**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."
43	
44	**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.
45	
46	**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a "probe reward trap" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.
47	
48	**Investigated approaches**: We test two reward formulations for R1:
49	- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).
50	- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.
51	- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a "slow-motion binary probe" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.
52	Combined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.
53	
54	**R3-only GRPO baseline (exp-003, D042 full trajectory)**:
55	| ckpt | ToF | NoF | SYCONScore | vs vanilla |
56	|------|-----|-----|------------|------------|
57	| vanilla | 0.072 | 0.945 | 0.134 | — |
58	| 1000 | 0.039 | 0.945 | 0.074 | -44% |
59	| 2000 | 0.044 | 0.983 | 0.085 | -37% |
60	| 3000 | 0.050 | 0.972 | 0.095 | -29% |
61	| 4000 | 0.061 | 0.967 | 0.114 | -14% |
62	| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |
63	| 5000 | 0.061 | 0.967 | 0.114 | -14% |
64	| 5500 | 0.061 | 0.972 | 0.114 | -14% |
65	| 6000 | 0.044 | 0.972 | 0.085 | -37% |
66	| 6500 | 0.083 | 0.983 | 0.153 | +14% |
67	| 7000 | 0.055 | 0.972 | 0.105 | -22% |
68	| 7500 | — | — | 0.105 | -22% |
69	| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |
70	
71	> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。
72	
73	**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。
74	
75	**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：
76	| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |
77	|------|-----|-----|------------|------------|-------------------|
78	| 500 | 0.044 | 0.950 | 0.085 | -37% | — |
79	| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |
80	| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |
81	| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |
82	| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |
83	| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |
84	| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |
85	方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-2500 (0.105)，远低于 vanilla (0.134)，之后持续下降到 0.074。方向与 seed 1 完全一致。
86	
87	**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。
88	
89	**论文叙事 — Scheme C 双层结构 (D041→D042)**：
90	
91	**Layer 1: d_syc rewards actively harmful**
92	- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）
93	- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）
94	- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度
95	
96	**Layer 2: GRPO stubbornness emergence + reliability gap**
97	- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持
98	- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）
99	- R3 (NLI) 无法区分"正确坚持"和"错误顽固"——sparse reward 的固有限制
100	- **Reliability gap**: ACT 13/13 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 为 0/7
101	
102	**Positive control: SFT succeeds (with nuance)**
103	- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301
104	- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复
105	- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头
106	- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。
107	- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x
108	- 证明 sycophancy calibration IS achievable via dense supervision
109	
110	**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。
111	
112	**Reliability gap 对比框架 (D047)**:
113	- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)
114	- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla
115	- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）
116	- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%
117	
118	**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).
119	
120	**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:
121	1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)
122	2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only
123	3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence
124	4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish "model correctly revises belief" from "model sycophantically capitulates" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).
125	
126	**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.
127	
128	**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the "too weak" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.
129	
130	**Probe reward trap (D031/D032 — key finding)**: Binary probe learns "no answer change = non-sycophantic" from contrastive training data. In GRPO:
131	1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)
132	2. High R1 reward → gradient reinforces stubbornness
133	3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high
134	4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)
135	5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.
136	
137	**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:
138	- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108
139	- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)
140	Cross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.
141	
142	**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:
143	
144	Why does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:
145	
146	1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation
147	2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation
148	3. **Yet SYCONScore drops 15%** (0.134 → 0.114)
149	
150	Conclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.
151	
152	This three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.
153	
154	**Stubbornness taxonomy (exp-008v3 binary probe trap)**:
155	181/181 valid samples show 100% stubbornness. Six failure modes identified:
156	- **Sycophantic stubbornness** (24%): says "you're right" but doesn't change answer — simultaneously sycophantic AND stubborn
157	- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning
158	- **Acknowledge-but-maintain** (24%): "however/but" hedge then maintains original answer
159	- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction
160	- Format corruption: 87% responses start with "Ah, interesting", 96% truncated at 512 tokens
161	
162	**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.
163	
164	**Headline result template**: "We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL."
165	
166	## Venue Fit Risks
167	
168	- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.
169	- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.
170	- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
171	- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).
172	- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim "cross-architecture phenomenon" with qualifier in Limitations ("tested on two 8B-parameter models; larger models and additional architectures remain future work"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.
173	- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
174	- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.
175	
176	## Anticipated Reviewer Concerns & Experimental Responses
177	
178	| Concern | Experiment | Priority |
179	|---------|-----------|----------|
180	| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
181	| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
182	| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
183	| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |
184	| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
185	| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
186	| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |
187	| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
188	| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |
189	| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
190	| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
191	| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |
192	| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |
193	| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |
194	| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "1f98c04e-b727-44a9-8bbe-839ad1017861",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
      "content": "# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\n- Commitment Deadline: **August 2, 2026**\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\n   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.\n   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).\n\n2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.\n   - *Evidence*:\n     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)\n     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns \"never change answer\" → probe rewards as \"non-sycophantic\" → positive feedback loop → stubbornness collapse\n     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward\n   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.\n   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.\n\n3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns \"no answer change = non-sycophantic.\" During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.\n   - *Evidence (full checkpoint trajectory)*:\n     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active\n     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)\n     - ckpt-1500: entropy=0.61, ToF=0.0000\n     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000\n   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.\n   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.\n   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.\n   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a \"probe reward trap\" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.\n\n**Investigated approaches**: We test two reward formulations for R1:\n- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).\n- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.\n- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a \"slow-motion binary probe\" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.\nCombined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.\n\n**R3-only GRPO baseline (exp-003, D042 full trajectory)**:\n| ckpt | ToF | NoF | SYCONScore | vs vanilla |\n|------|-----|-----|------------|------------|\n| vanilla | 0.072 | 0.945 | 0.134 | — |\n| 1000 | 0.039 | 0.945 | 0.074 | -44% |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% |\n| 4000 | 0.061 | 0.967 | 0.114 | -14% |\n| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |\n| 5000 | 0.061 | 0.967 | 0.114 | -14% |\n| 5500 | 0.061 | 0.972 | 0.114 | -14% |\n| 6000 | 0.044 | 0.972 | 0.085 | -37% |\n| 6500 | 0.083 | 0.983 | 0.153 | +14% |\n| 7000 | 0.055 | 0.972 | 0.105 | -22% |\n| 7500 | — | — | 0.105 | -22% |\n| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |\n\n> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。\n\n**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。\n\n**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：\n| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |\n|------|-----|-----|------------|------------|-------------------|\n| 500 | 0.044 | 0.950 | 0.085 | -37% | — |\n| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |\n| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |\n| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |\n| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |\n方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-2500 (0.105)，远低于 vanilla (0.134)，之后持续下降到 0.074。方向与 seed 1 完全一致。\n\n**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。\n\n**论文叙事 — Scheme C 双层结构 (D041→D042)**：\n\n**Layer 1: d_syc rewards actively harmful**\n- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）\n- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）\n- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度\n\n**Layer 2: GRPO stubbornness emergence + reliability gap**\n- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持\n- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）\n- R3 (NLI) 无法区分\"正确坚持\"和\"错误顽固\"——sparse reward 的固有限制\n- **Reliability gap**: ACT 13/13 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 为 0/7\n\n**Positive control: SFT succeeds (with nuance)**\n- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301\n- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复\n- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头\n- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。\n- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x\n- 证明 sycophancy calibration IS achievable via dense supervision\n\n**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。\n\n**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）\n- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%\n\n**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).\n\n**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:\n1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)\n2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only\n3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence\n4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish \"model correctly revises belief\" from \"model sycophantically capitulates\" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).\n\n**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.\n\n**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the \"too weak\" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.\n\n**Probe reward trap (D031/D032 — key finding)**: Binary probe learns \"no answer change = non-sycophantic\" from contrastive training data. In GRPO:\n1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)\n2. High R1 reward → gradient reinforces stubbornness\n3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high\n4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)\n5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.\n\n**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:\n- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108\n- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)\nCross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.\n\n**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:\n\nWhy does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:\n\n1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation\n2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation\n3. **Yet SYCONScore drops 15%** (0.134 → 0.114)\n\nConclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.\n\nThis three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.\n\n**Stubbornness taxonomy (exp-008v3 binary probe trap)**:\n181/181 valid samples show 100% stubbornness. Six failure modes identified:\n- **Sycophantic stubbornness** (24%): says \"you're right\" but doesn't change answer — simultaneously sycophantic AND stubborn\n- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning\n- **Acknowledge-but-maintain** (24%): \"however/but\" hedge then maintains original answer\n- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction\n- Format corruption: 87% responses start with \"Ah, interesting\", 96% truncated at 512 tokens\n\n**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.\n\n**Headline result template**: \"We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL.\"\n\n## Venue Fit Risks\n\n- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim \"cross-architecture phenomenon\" with qualifier in Limitations (\"tested on two 8B-parameter models; larger models and additional architectures remain future work\"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |\n| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |\n| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. Let me identify all the changes needed:

1. **Replace "13/13" → "16/16"** in ACT-related contexts
   - Line 100: "ACT 13/13 checkpoints > vanilla"
   - Line 113: "13/13 D027 eval checkpoints > vanilla"

2. **Reliability gap 对比框架 (D047)** update (lines 112-116):
   - Update ACT line with new data points
   - Update R3-only seed 2 (was 0/7, now 1/9)
   - Add the cross-seed totals line
   - Update the efficiency gap line

3. **Supplement ACT missing data points** in trajectory description (line 103):
   - Current: "0.170→0.255→**0.214**(dip)→0.262→0.301"
   - Need to add ckpt-500=0.1699, ckpt-2000=0.2550, ckpt-8000=0.3013

4. **三层区分总结** (line 110): Update ACT-related references

Let me check lines 100 and 110 more carefully to ensure I'm making the right edits.

Looking at the reliability gap framework, I need to update the numbers: ACT should show 16/16 (100%) across all seeds, while R3-only shows 4/21 (19%) total. For seed 2 specifically, R3-only has 1/9 checkpoints exceeding vanilla with a +7% improvement at ckpt-4000, but the remaining 8/9 fall below vanilla. This means line 100 needs to shift from "ACT 13/13" to "ACT 16/16" and the seed 2 reference needs updating from 0/7 to reflect the actual count. 我在检查第110行的三层区分总结，需要把seed 2的数据从0/7更新到1/9。同时还要确认第100行和第113行的13/13出现次数，以及第103行关于SYCONScore轨迹的描述是否需要调整。 I need to expand the trajectory notation to include the checkpoint labels at each point, so instead of just the scores, I'll show which checkpoint each score corresponds to—ckpt-500 at 0.1699, ckpt-2000 at 0.2550, ckpt-8000 at 0.3013, and fill in the intermediate checkpoints for the dip and recovery points as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "44942080-72f2-46b0-aa69-d6c69a46c800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSX9FxgnCeMSqAHYqzRtc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 23919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9118
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

_source line 8_

I'll make all four edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "1f8111b9-7ad4-4338-9699-244b7dc52a77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSX9FxgnCeMSqAHYqzRtc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 23919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9118
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Dfi62nDtRd32B1oN3h184J`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
  "old_string": "- **Reliability gap**: ACT 13/13 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 为 0/7",
  "new_string": "- **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "34579ad2-546c-49e5-af57-f134cc6332b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSX9FxgnCeMSqAHYqzRtc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 23919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9118
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

_source line 10 · 2026-05-22T04:03:24.097Z_

<details><summary>↩ Tool result · `toolu_01Dfi62nDtRd32B1oN3h184J`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "6e854ce5-04b2-458d-a5e4-b996d2936912",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
    "oldString": "- **Reliability gap**: ACT 13/13 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 为 0/7",
    "newString": "- **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9",
    "originalFile": "# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\n- Commitment Deadline: **August 2, 2026**\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\n   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.\n   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).\n\n2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.\n   - *Evidence*:\n     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)\n     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns \"never change answer\" → probe rewards as \"non-sycophantic\" → positive feedback loop → stubbornness collapse\n     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward\n   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.\n   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.\n\n3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns \"no answer change = non-sycophantic.\" During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.\n   - *Evidence (full checkpoint trajectory)*:\n     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active\n     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)\n     - ckpt-1500: entropy=0.61, ToF=0.0000\n     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000\n   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.\n   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.\n   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.\n   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a \"probe reward trap\" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.\n\n**Investigated approaches**: We test two reward formulations for R1:\n- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).\n- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.\n- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a \"slow-motion binary probe\" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.\nCombined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.\n\n**R3-only GRPO baseline (exp-003, D042 full trajectory)**:\n| ckpt | ToF | NoF | SYCONScore | vs vanilla |\n|------|-----|-----|------------|------------|\n| vanilla | 0.072 | 0.945 | 0.134 | — |\n| 1000 | 0.039 | 0.945 | 0.074 | -44% |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% |\n| 4000 | 0.061 | 0.967 | 0.114 | -14% |\n| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |\n| 5000 | 0.061 | 0.967 | 0.114 | -14% |\n| 5500 | 0.061 | 0.972 | 0.114 | -14% |\n| 6000 | 0.044 | 0.972 | 0.085 | -37% |\n| 6500 | 0.083 | 0.983 | 0.153 | +14% |\n| 7000 | 0.055 | 0.972 | 0.105 | -22% |\n| 7500 | — | — | 0.105 | -22% |\n| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |\n\n> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。\n\n**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。\n\n**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：\n| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |\n|------|-----|-----|------------|------------|-------------------|\n| 500 | 0.044 | 0.950 | 0.085 | -37% | — |\n| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |\n| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |\n| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |\n| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |\n方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-2500 (0.105)，远低于 vanilla (0.134)，之后持续下降到 0.074。方向与 seed 1 完全一致。\n\n**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。\n\n**论文叙事 — Scheme C 双层结构 (D041→D042)**：\n\n**Layer 1: d_syc rewards actively harmful**\n- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）\n- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）\n- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度\n\n**Layer 2: GRPO stubbornness emergence + reliability gap**\n- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持\n- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）\n- R3 (NLI) 无法区分\"正确坚持\"和\"错误顽固\"——sparse reward 的固有限制\n- **Reliability gap**: ACT 13/13 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 为 0/7\n\n**Positive control: SFT succeeds (with nuance)**\n- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301\n- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复\n- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头\n- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。\n- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x\n- 证明 sycophancy calibration IS achievable via dense supervision\n\n**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。\n\n**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）\n- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%\n\n**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).\n\n**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:\n1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)\n2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only\n3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence\n4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish \"model correctly revises belief\" from \"model sycophantically capitulates\" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).\n\n**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.\n\n**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the \"too weak\" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.\n\n**Probe reward trap (D031/D032 — key finding)**: Binary probe learns \"no answer change = non-sycophantic\" from contrastive training data. In GRPO:\n1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)\n2. High R1 reward → gradient reinforces stubbornness\n3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high\n4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)\n5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.\n\n**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:\n- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108\n- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)\nCross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.\n\n**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:\n\nWhy does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:\n\n1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation\n2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation\n3. **Yet SYCONScore drops 15%** (0.134 → 0.114)\n\nConclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.\n\nThis three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.\n\n**Stubbornness taxonomy (exp-008v3 binary probe trap)**:\n181/181 valid samples show 100% stubbornness. Six failure modes identified:\n- **Sycophantic stubbornness** (24%): says \"you're right\" but doesn't change answer — simultaneously sycophantic AND stubborn\n- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning\n- **Acknowledge-but-maintain** (24%): \"however/but\" hedge then maintains original answer\n- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction\n- Format corruption: 87% responses start with \"Ah, interesting\", 96% truncated at 512 tokens\n\n**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.\n\n**Headline result template**: \"We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL.\"\n\n## Venue Fit Risks\n\n- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim \"cross-architecture phenomenon\" with qualifier in Limitations (\"tested on two 8B-parameter models; larger models and additional architectures remain future work\"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |\n| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |\n| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |\n",
    "structuredPatch": [
      {
        "oldStart": 97,
        "oldLines": 7,
        "newStart": 97,
        "newLines": 7,
        "lines": [
          " - R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持",
          " - GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）",
          " - R3 (NLI) 无法区分\"正确坚持\"和\"错误顽固\"——sparse reward 的固有限制",
          "-- **Reliability gap**: ACT 13/13 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 为 0/7",
          "+- **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9",
          " ",
          " **Positive control: SFT succeeds (with nuance)**",
          " - exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301"
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01V1ghTEMY1RbjyuSxG5NxDz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
  "old_string": "**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）\n- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%",
  "new_string": "**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 1/9 > vanilla（ckpt-4000 +7%），其余 8/9 低于 vanilla\n- **跨 seed 合计**: ACT 16/16 (100%) vs R3-only 4/21 (19%)\n- **效率差 ~16x**: ACT 500 步即 +27%，R3-only 8000 步才 +7.3%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "030d453b-e048-4a33-b4aa-1a915c19acae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLg5DbXuYM57SkuYrSf7um",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 33037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1531
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

_source line 12 · 2026-05-22T04:03:34.529Z_

<details><summary>↩ Tool result · `toolu_01V1ghTEMY1RbjyuSxG5NxDz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "cf3a2132-72a3-486c-b4ea-ec7b894e9bcc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
    "oldString": "**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）\n- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%",
    "newString": "**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 1/9 > vanilla（ckpt-4000 +7%），其余 8/9 低于 vanilla\n- **跨 seed 合计**: ACT 16/16 (100%) vs R3-only 4/21 (19%)\n- **效率差 ~16x**: ACT 500 步即 +27%，R3-only 8000 步才 +7.3%",
    "originalFile": "# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\n- Commitment Deadline: **August 2, 2026**\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\n   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.\n   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).\n\n2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.\n   - *Evidence*:\n     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)\n     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns \"never change answer\" → probe rewards as \"non-sycophantic\" → positive feedback loop → stubbornness collapse\n     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward\n   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.\n   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.\n\n3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns \"no answer change = non-sycophantic.\" During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.\n   - *Evidence (full checkpoint trajectory)*:\n     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active\n     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)\n     - ckpt-1500: entropy=0.61, ToF=0.0000\n     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000\n   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.\n   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.\n   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.\n   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a \"probe reward trap\" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.\n\n**Investigated approaches**: We test two reward formulations for R1:\n- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).\n- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.\n- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a \"slow-motion binary probe\" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.\nCombined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.\n\n**R3-only GRPO baseline (exp-003, D042 full trajectory)**:\n| ckpt | ToF | NoF | SYCONScore | vs vanilla |\n|------|-----|-----|------------|------------|\n| vanilla | 0.072 | 0.945 | 0.134 | — |\n| 1000 | 0.039 | 0.945 | 0.074 | -44% |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% |\n| 4000 | 0.061 | 0.967 | 0.114 | -14% |\n| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |\n| 5000 | 0.061 | 0.967 | 0.114 | -14% |\n| 5500 | 0.061 | 0.972 | 0.114 | -14% |\n| 6000 | 0.044 | 0.972 | 0.085 | -37% |\n| 6500 | 0.083 | 0.983 | 0.153 | +14% |\n| 7000 | 0.055 | 0.972 | 0.105 | -22% |\n| 7500 | — | — | 0.105 | -22% |\n| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |\n\n> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。\n\n**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。\n\n**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：\n| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |\n|------|-----|-----|------------|------------|-------------------|\n| 500 | 0.044 | 0.950 | 0.085 | -37% | — |\n| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |\n| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |\n| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |\n| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |\n方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-2500 (0.105)，远低于 vanilla (0.134)，之后持续下降到 0.074。方向与 seed 1 完全一致。\n\n**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。\n\n**论文叙事 — Scheme C 双层结构 (D041→D042)**：\n\n**Layer 1: d_syc rewards actively harmful**\n- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）\n- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）\n- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度\n\n**Layer 2: GRPO stubbornness emergence + reliability gap**\n- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持\n- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）\n- R3 (NLI) 无法区分\"正确坚持\"和\"错误顽固\"——sparse reward 的固有限制\n- **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9\n\n**Positive control: SFT succeeds (with nuance)**\n- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301\n- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复\n- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头\n- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。\n- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x\n- 证明 sycophancy calibration IS achievable via dense supervision\n\n**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。\n\n**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）\n- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%\n\n**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).\n\n**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:\n1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)\n2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only\n3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence\n4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish \"model correctly revises belief\" from \"model sycophantically capitulates\" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).\n\n**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.\n\n**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the \"too weak\" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.\n\n**Probe reward trap (D031/D032 — key finding)**: Binary probe learns \"no answer change = non-sycophantic\" from contrastive training data. In GRPO:\n1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)\n2. High R1 reward → gradient reinforces stubbornness\n3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high\n4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)\n5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.\n\n**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:\n- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108\n- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)\nCross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.\n\n**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:\n\nWhy does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:\n\n1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation\n2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation\n3. **Yet SYCONScore drops 15%** (0.134 → 0.114)\n\nConclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.\n\nThis three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.\n\n**Stubbornness taxonomy (exp-008v3 binary probe trap)**:\n181/181 valid samples show 100% stubbornness. Six failure modes identified:\n- **Sycophantic stubbornness** (24%): says \"you're right\" but doesn't change answer — simultaneously sycophantic AND stubborn\n- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning\n- **Acknowledge-but-maintain** (24%): \"however/but\" hedge then maintains original answer\n- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction\n- Format corruption: 87% responses start with \"Ah, interesting\", 96% truncated at 512 tokens\n\n**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.\n\n**Headline result template**: \"We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL.\"\n\n## Venue Fit Risks\n\n- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim \"cross-architecture phenomenon\" with qualifier in Limitations (\"tested on two 8B-parameter models; larger models and additional architectures remain future work\"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |\n| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |\n| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |\n",
    "structuredPatch": [
      {
        "oldStart": 110,
        "oldLines": 10,
        "newStart": 110,
        "newLines": 11,
        "lines": [
          " **三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。",
          " ",
          " **Reliability gap 对比框架 (D047)**:",
          "-- **ACT (SFT)**: 13/13 D027 eval checkpoints > vanilla（最低 ckpt-1500 = 0.170, +27%），稳定上升至 ckpt-7000 = 0.286 (+114%)",
          "+- **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)",
          " - **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla",
          "-- **R3-only seed 2**: 0/7 > vanilla（峰值 ckpt-2500 = 0.105, 仍 -22%）",
          "-- **效率差 ~16x**: ACT 1000 步即 +53%，R3-only 8000 步才 +7.3%",
          "+- **R3-only seed 2**: 1/9 > vanilla（ckpt-4000 +7%），其余 8/9 低于 vanilla",
          "+- **跨 seed 合计**: ACT 16/16 (100%) vs R3-only 4/21 (19%)",
          "+- **效率差 ~16x**: ACT 500 步即 +27%，R3-only 8000 步才 +7.3%",
          " ",
          " **Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).",
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_015zPgrzG3WGKUr5iNLm27F6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
  "old_string": "- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301",
  "new_string": "- exp-004 ACT (SFT) SYCONScore trajectory (16/16 checkpoints > vanilla): ckpt-500=0.170(+27%)→ckpt-2000=0.255(+91%)→ckpt-3000=0.239→ckpt-4000=**0.214**(dip)→ckpt-5000=0.239→ckpt-6000=0.262→ckpt-8000=0.301(+126%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "71afe916-144d-41de-a5ee-b244ca59a234",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aep4ssL7veyFc9sFqK3MQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 34568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 14 · 2026-05-22T04:03:39.491Z_

<details><summary>↩ Tool result · `toolu_015zPgrzG3WGKUr5iNLm27F6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "c5ef2284-483c-4445-ab63-8ad50a7d8f19",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
    "oldString": "- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301",
    "newString": "- exp-004 ACT (SFT) SYCONScore trajectory (16/16 checkpoints > vanilla): ckpt-500=0.170(+27%)→ckpt-2000=0.255(+91%)→ckpt-3000=0.239→ckpt-4000=**0.214**(dip)→ckpt-5000=0.239→ckpt-6000=0.262→ckpt-8000=0.301(+126%)",
    "originalFile": "# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\n- Commitment Deadline: **August 2, 2026**\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\n   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.\n   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).\n\n2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.\n   - *Evidence*:\n     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)\n     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns \"never change answer\" → probe rewards as \"non-sycophantic\" → positive feedback loop → stubbornness collapse\n     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward\n   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.\n   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.\n\n3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns \"no answer change = non-sycophantic.\" During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.\n   - *Evidence (full checkpoint trajectory)*:\n     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active\n     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)\n     - ckpt-1500: entropy=0.61, ToF=0.0000\n     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000\n   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.\n   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.\n   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.\n   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a \"probe reward trap\" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.\n\n**Investigated approaches**: We test two reward formulations for R1:\n- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).\n- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.\n- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a \"slow-motion binary probe\" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.\nCombined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.\n\n**R3-only GRPO baseline (exp-003, D042 full trajectory)**:\n| ckpt | ToF | NoF | SYCONScore | vs vanilla |\n|------|-----|-----|------------|------------|\n| vanilla | 0.072 | 0.945 | 0.134 | — |\n| 1000 | 0.039 | 0.945 | 0.074 | -44% |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% |\n| 4000 | 0.061 | 0.967 | 0.114 | -14% |\n| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |\n| 5000 | 0.061 | 0.967 | 0.114 | -14% |\n| 5500 | 0.061 | 0.972 | 0.114 | -14% |\n| 6000 | 0.044 | 0.972 | 0.085 | -37% |\n| 6500 | 0.083 | 0.983 | 0.153 | +14% |\n| 7000 | 0.055 | 0.972 | 0.105 | -22% |\n| 7500 | — | — | 0.105 | -22% |\n| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |\n\n> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。\n\n**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。\n\n**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：\n| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |\n|------|-----|-----|------------|------------|-------------------|\n| 500 | 0.044 | 0.950 | 0.085 | -37% | — |\n| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |\n| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |\n| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |\n| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |\n方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-2500 (0.105)，远低于 vanilla (0.134)，之后持续下降到 0.074。方向与 seed 1 完全一致。\n\n**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。\n\n**论文叙事 — Scheme C 双层结构 (D041→D042)**：\n\n**Layer 1: d_syc rewards actively harmful**\n- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）\n- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）\n- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度\n\n**Layer 2: GRPO stubbornness emergence + reliability gap**\n- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持\n- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）\n- R3 (NLI) 无法区分\"正确坚持\"和\"错误顽固\"——sparse reward 的固有限制\n- **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9\n\n**Positive control: SFT succeeds (with nuance)**\n- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301\n- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复\n- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头\n- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。\n- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x\n- 证明 sycophancy calibration IS achievable via dense supervision\n\n**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。\n\n**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 1/9 > vanilla（ckpt-4000 +7%），其余 8/9 低于 vanilla\n- **跨 seed 合计**: ACT 16/16 (100%) vs R3-only 4/21 (19%)\n- **效率差 ~16x**: ACT 500 步即 +27%，R3-only 8000 步才 +7.3%\n\n**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).\n\n**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:\n1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)\n2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only\n3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence\n4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish \"model correctly revises belief\" from \"model sycophantically capitulates\" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).\n\n**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.\n\n**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the \"too weak\" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.\n\n**Probe reward trap (D031/D032 — key finding)**: Binary probe learns \"no answer change = non-sycophantic\" from contrastive training data. In GRPO:\n1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)\n2. High R1 reward → gradient reinforces stubbornness\n3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high\n4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)\n5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.\n\n**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:\n- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108\n- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)\nCross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.\n\n**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:\n\nWhy does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:\n\n1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation\n2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation\n3. **Yet SYCONScore drops 15%** (0.134 → 0.114)\n\nConclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.\n\nThis three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.\n\n**Stubbornness taxonomy (exp-008v3 binary probe trap)**:\n181/181 valid samples show 100% stubbornness. Six failure modes identified:\n- **Sycophantic stubbornness** (24%): says \"you're right\" but doesn't change answer — simultaneously sycophantic AND stubborn\n- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning\n- **Acknowledge-but-maintain** (24%): \"however/but\" hedge then maintains original answer\n- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction\n- Format corruption: 87% responses start with \"Ah, interesting\", 96% truncated at 512 tokens\n\n**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.\n\n**Headline result template**: \"We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL.\"\n\n## Venue Fit Risks\n\n- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim \"cross-architecture phenomenon\" with qualifier in Limitations (\"tested on two 8B-parameter models; larger models and additional architectures remain future work\"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |\n| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |\n| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |\n",
    "structuredPatch": [
      {
        "oldStart": 100,
        "oldLines": 7,
        "newStart": 100,
        "newLines": 7,
        "lines": [
          " - **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9",
          " ",
          " **Positive control: SFT succeeds (with nuance)**",
          "-- exp-004 ACT (SFT) SYCONScore trajectory: 0.170→0.255→**0.214**(dip)→0.262→0.301",
          "+- exp-004 ACT (SFT) SYCONScore trajectory (16/16 checkpoints > vanilla): ckpt-500=0.170(+27%)→ckpt-2000=0.255(+91%)→ckpt-3000=0.239→ckpt-4000=**0.214**(dip)→ckpt-5000=0.239→ckpt-6000=0.262→ckpt-8000=0.301(+126%)",
          " - **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复",
          " - 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头",
          " - **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。"
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_014iMBnq1oEQGY9r2uNonnFc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
  "old_string": "seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)",
  "new_string": "seed 1 仅 3/12 checkpoints > vanilla, seed 2 仅 1/9), SFT = dips but self-recovers and keeps improving (16/16 > vanilla, 0.170→0.301)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "6bcca667-9e53-444b-b34c-65a672e4fcd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzsgwvVN5JKDH53AkgqBYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 35276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
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

_source line 16 · 2026-05-22T04:03:43.525Z_

<details><summary>↩ Tool result · `toolu_014iMBnq1oEQGY9r2uNonnFc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "2d5fee4d-0de2-4c89-a1f6-f24b7cbfb655",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md",
    "oldString": "seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)",
    "newString": "seed 1 仅 3/12 checkpoints > vanilla, seed 2 仅 1/9), SFT = dips but self-recovers and keeps improving (16/16 > vanilla, 0.170→0.301)",
    "originalFile": "# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\n- Commitment Deadline: **August 2, 2026**\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\n   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.\n   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).\n\n2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.\n   - *Evidence*:\n     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)\n     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns \"never change answer\" → probe rewards as \"non-sycophantic\" → positive feedback loop → stubbornness collapse\n     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward\n   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.\n   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.\n\n3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns \"no answer change = non-sycophantic.\" During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.\n   - *Evidence (full checkpoint trajectory)*:\n     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active\n     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)\n     - ckpt-1500: entropy=0.61, ToF=0.0000\n     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000\n   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.\n   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.\n   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.\n   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a \"probe reward trap\" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.\n\n**Investigated approaches**: We test two reward formulations for R1:\n- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).\n- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.\n- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a \"slow-motion binary probe\" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.\nCombined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.\n\n**R3-only GRPO baseline (exp-003, D042 full trajectory)**:\n| ckpt | ToF | NoF | SYCONScore | vs vanilla |\n|------|-----|-----|------------|------------|\n| vanilla | 0.072 | 0.945 | 0.134 | — |\n| 1000 | 0.039 | 0.945 | 0.074 | -44% |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% |\n| 4000 | 0.061 | 0.967 | 0.114 | -14% |\n| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |\n| 5000 | 0.061 | 0.967 | 0.114 | -14% |\n| 5500 | 0.061 | 0.972 | 0.114 | -14% |\n| 6000 | 0.044 | 0.972 | 0.085 | -37% |\n| 6500 | 0.083 | 0.983 | 0.153 | +14% |\n| 7000 | 0.055 | 0.972 | 0.105 | -22% |\n| 7500 | — | — | 0.105 | -22% |\n| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |\n\n> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。\n\n**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。\n\n**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：\n| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |\n|------|-----|-----|------------|------------|-------------------|\n| 500 | 0.044 | 0.950 | 0.085 | -37% | — |\n| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |\n| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |\n| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |\n| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |\n| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |\n| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |\n方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-2500 (0.105)，远低于 vanilla (0.134)，之后持续下降到 0.074。方向与 seed 1 完全一致。\n\n**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。\n\n**论文叙事 — Scheme C 双层结构 (D041→D042)**：\n\n**Layer 1: d_syc rewards actively harmful**\n- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）\n- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）\n- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度\n\n**Layer 2: GRPO stubbornness emergence + reliability gap**\n- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持\n- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）\n- R3 (NLI) 无法区分\"正确坚持\"和\"错误顽固\"——sparse reward 的固有限制\n- **Reliability gap**: ACT 16/16 checkpoints > vanilla; R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/9\n\n**Positive control: SFT succeeds (with nuance)**\n- exp-004 ACT (SFT) SYCONScore trajectory (16/16 checkpoints > vanilla): ckpt-500=0.170(+27%)→ckpt-2000=0.255(+91%)→ckpt-3000=0.239→ckpt-4000=**0.214**(dip)→ckpt-5000=0.239→ckpt-6000=0.262→ckpt-8000=0.301(+126%)\n- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复\n- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头\n- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。\n- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x\n- 证明 sycophancy calibration IS achievable via dense supervision\n\n**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。\n\n**Reliability gap 对比框架 (D047)**:\n- **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)\n- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla\n- **R3-only seed 2**: 1/9 > vanilla（ckpt-4000 +7%），其余 8/9 低于 vanilla\n- **跨 seed 合计**: ACT 16/16 (100%) vs R3-only 4/21 (19%)\n- **效率差 ~16x**: ACT 500 步即 +27%，R3-only 8000 步才 +7.3%\n\n**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).\n\n**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:\n1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)\n2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only\n3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence\n4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish \"model correctly revises belief\" from \"model sycophantically capitulates\" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).\n\n**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.\n\n**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the \"too weak\" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.\n\n**Probe reward trap (D031/D032 — key finding)**: Binary probe learns \"no answer change = non-sycophantic\" from contrastive training data. In GRPO:\n1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)\n2. High R1 reward → gradient reinforces stubbornness\n3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high\n4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)\n5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.\n\n**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:\n- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108\n- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)\nCross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.\n\n**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:\n\nWhy does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:\n\n1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation\n2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation\n3. **Yet SYCONScore drops 15%** (0.134 → 0.114)\n\nConclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.\n\nThis three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.\n\n**Stubbornness taxonomy (exp-008v3 binary probe trap)**:\n181/181 valid samples show 100% stubbornness. Six failure modes identified:\n- **Sycophantic stubbornness** (24%): says \"you're right\" but doesn't change answer — simultaneously sycophantic AND stubborn\n- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning\n- **Acknowledge-but-maintain** (24%): \"however/but\" hedge then maintains original answer\n- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction\n- Format corruption: 87% responses start with \"Ah, interesting\", 96% truncated at 512 tokens\n\n**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.\n\n**Headline result template**: \"We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL.\"\n\n## Venue Fit Risks\n\n- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim \"cross-architecture phenomenon\" with qualifier in Limitations (\"tested on two 8B-parameter models; larger models and additional architectures remain future work\"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |\n| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |\n| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |\n",
    "structuredPatch": [
      {
        "oldStart": 107,
        "oldLines": 7,
        "newStart": 107,
        "newLines": 7,
        "lines": [
          " - 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x",
          " - 证明 sycophancy calibration IS achievable via dense supervision",
          " ",
          "-**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 为 0/7), SFT = dips but self-recovers and keeps improving (0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。",
          "+**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 仅 1/9), SFT = dips but self-recovers and keeps improving (16/16 > vanilla, 0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。",
          " ",
          " **Reliability gap 对比框架 (D047)**:",
          " - **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)"
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

全部修改完成：

1. **13/13 → 16/16**: Line 100 和 Line 113 两处已替换
2. **Reliability gap 对比框架**: ACT 最低点改为 ckpt-500=0.170，终点改为 ckpt-8000=0.301(+126%)；R3-only seed 2 改为 1/9；新增跨 seed 合计行；效率差起点改为 500 步
3. **ACT trajectory**: 补入 checkpoint 标签和百分比，标注 16/16 checkpoints > vanilla
4. **三层区分总结**: seed 2 从 0/7 改为 1/9，SFT 描述补入 16/16 > vanilla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "uuid": "2aeccbf4-6cda-47d8-a3ab-630ef357bed0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMqnQqTas7LDUDDVwhPAqi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 35649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
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

_source line 18_

全部修改完成：

1. **13/13 → 16/16**: Line 100 和 Line 113 两处已替换
2. **Reliability gap 对比框架**: ACT 最低点改为 ckpt-500=0.170，终点改为 ckpt-8000=0.301(+126%)；R3-only seed 2 改为 1/9；新增跨 seed 合计行；效率差起点改为 500 步
3. **ACT trajectory**: 补入 checkpoint 标签和百分比，标注 16/16 checkpoints > vanilla
4. **三层区分总结**: seed 2 从 0/7 改为 1/9，SFT 描述补入 16/16 > vanilla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 57684,
  "duration_api_ms": 59158,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "37acf907-6168-4e9d-ba6d-ecb076bc1e41",
  "total_cost_usd": 0.3138385,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 24118,
    "cache_read_input_tokens": 174290,
    "output_tokens": 2977,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24118,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 203,
        "cache_read_input_tokens": 35649,
        "cache_creation_input_tokens": 310,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 310
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1346,
      "outputTokens": 29,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001491,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 2977,
      "cacheReadInputTokens": 174290,
      "cacheCreationInputTokens": 24118,
      "webSearchRequests": 0,
      "costUSD": 0.3123475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d6ce7546-a2a3-4b59-9af8-99de4284f1d7"
}
```

</details>

---
