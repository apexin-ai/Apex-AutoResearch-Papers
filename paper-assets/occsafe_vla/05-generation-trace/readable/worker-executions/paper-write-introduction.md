# paper write introduction

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_write-introduction_20260522T182228.log`
- **Structured JSON:** [`e6bf3469744f09493f7e.json`](../../sessions/e6/e6bf3469744f09493f7e.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
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
  "uuid": "5064b619-bfa4-4a70-9755-5d4f308e4eea",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779491400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b04cc766-7008-487c-a404-3c90ce284171",
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba"
}
```

---

### Assistant

_source line 4_

Let me read all the required materials first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "e2e64d8d-5ba7-44dc-9f76-6e6cbb9772b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

<details open><summary>🔧 Tool call — Read · `toolu_01P2edjXJ5eBmKS2eSYiUoDd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/skills/projects/occsafe_vla/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "c043688a-7caf-4330-84f6-a10f39238556",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

_source line 6 · 2026-05-22T18:22:41.056Z_

<details><summary>↩ Tool result · `toolu_01P2edjXJ5eBmKS2eSYiUoDd`</summary>

```text
1	# VLA Safety + 3D: Distilled Writing Patterns
2	
3	Source: 8 deep-read papers, 2024-2026.
4	
5	## Story & Structure
6	
7	**"突破局限型" dominates** (5/8): "X great but lacks Y → existing fixes fail → our insight." 统一框架型 (2/8), 化繁为简型 (1/8).
8	
9	**Universal hook**: "VLA shows promise, BUT [concrete gap]." 6/8 use this in P1.
10	
11	**Dual-elimination tension** (4/8): Rule out two alternatives before presenting yours. SpatialForcing: "sensors fail AND estimators fail." VLSA: "retraining is expensive AND motion planning overwrites semantics."
12	
13	**Intro**: 4-5 paragraphs. P1=promise+gap → P2=existing limitations → P3=deeper analysis → P4=method → P5=contributions. **3-contribution standard** universal (7/8): method + design/benchmark + validation.
14	
15	## Motivation Techniques
16	
17	1. **Empirical diagnosis** (SpatialForcing): Depth probing experiment proves VLA embeddings lack spatial info—evidence, not assumption. Strongest intro technique.
18	2. **Counter-intuitive reframing** (VLSA): "Safety Enables Success"—safety increases TSR by preventing cascading failures.
19	3. **Intuitive statistic** (OccVLA): "90% of 3D space is empty" makes occupancy feel inevitable.
20	4. **Extreme stress-test** (SafeVLA): CC=71.68 vs 2.20 in impossible tasks—32x gap is unforgettable.
21	5. **Paradoxical finding** (DepthVLA): Predicted depth > GT depth creates memory anchor.
22	
23	## Figure 1 Design
24	
25	**method_overview** (5/8), but best ones are hybrid. SpatialForcing: method + result + diagnosis in 3 panels. OccVLA: three-paradigm comparison positions paper instantly. VLSA: before/after trajectory. **Shared**: multi-panel (7/8), color-coded modules (6/8), flow arrows (6/8).
26	
27	## Result Presentation
28	
29	**Tables for quantitative** (6/8): rows=methods by_category, cols=grouped_by_dataset, bold_best. 8 baselines median. No mean±std in manipulation VLA (6/8 single-run). Add Input/Supervision columns to highlight simpler requirements (OccVLA).
30	
31	**Figures for qualitative**: trajectory/depth before-after grid (4/8). Safety: time-series h(x) plot proves constraint satisfaction (VLSA, OGM-CBF).
32	
33	**Ablation**: full_numbers (5/8) > delta_from_base (2/8). GST-VLA's 7-table ablation with Δ column is gold standard. Checkmark grid NOT used in this field.
34	
35	**Division**: quantitative→table, qualitative→figure, safety→figure, hyperparameters→figure, per-task detail→appendix.
36	
37	## Figure Narrative Flow
38	
39	Consensus: **overview → motivation → results → ablation → real-world**. 5-6 figures in main paper. SpatialForcing exemplar: teaser → paradigm comparison → depth probing → sim → efficiency → real-world.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "c1cc8cb7-a90d-4489-b255-a3f381a0c9bc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/skills/projects/occsafe_vla/distilled-writing.skill.md",
      "content": "# VLA Safety + 3D: Distilled Writing Patterns\n\nSource: 8 deep-read papers, 2024-2026.\n\n## Story & Structure\n\n**\"突破局限型\" dominates** (5/8): \"X great but lacks Y → existing fixes fail → our insight.\" 统一框架型 (2/8), 化繁为简型 (1/8).\n\n**Universal hook**: \"VLA shows promise, BUT [concrete gap].\" 6/8 use this in P1.\n\n**Dual-elimination tension** (4/8): Rule out two alternatives before presenting yours. SpatialForcing: \"sensors fail AND estimators fail.\" VLSA: \"retraining is expensive AND motion planning overwrites semantics.\"\n\n**Intro**: 4-5 paragraphs. P1=promise+gap → P2=existing limitations → P3=deeper analysis → P4=method → P5=contributions. **3-contribution standard** universal (7/8): method + design/benchmark + validation.\n\n## Motivation Techniques\n\n1. **Empirical diagnosis** (SpatialForcing): Depth probing experiment proves VLA embeddings lack spatial info—evidence, not assumption. Strongest intro technique.\n2. **Counter-intuitive reframing** (VLSA): \"Safety Enables Success\"—safety increases TSR by preventing cascading failures.\n3. **Intuitive statistic** (OccVLA): \"90% of 3D space is empty\" makes occupancy feel inevitable.\n4. **Extreme stress-test** (SafeVLA): CC=71.68 vs 2.20 in impossible tasks—32x gap is unforgettable.\n5. **Paradoxical finding** (DepthVLA): Predicted depth > GT depth creates memory anchor.\n\n## Figure 1 Design\n\n**method_overview** (5/8), but best ones are hybrid. SpatialForcing: method + result + diagnosis in 3 panels. OccVLA: three-paradigm comparison positions paper instantly. VLSA: before/after trajectory. **Shared**: multi-panel (7/8), color-coded modules (6/8), flow arrows (6/8).\n\n## Result Presentation\n\n**Tables for quantitative** (6/8): rows=methods by_category, cols=grouped_by_dataset, bold_best. 8 baselines median. No mean±std in manipulation VLA (6/8 single-run). Add Input/Supervision columns to highlight simpler requirements (OccVLA).\n\n**Figures for qualitative**: trajectory/depth before-after grid (4/8). Safety: time-series h(x) plot proves constraint satisfaction (VLSA, OGM-CBF).\n\n**Ablation**: full_numbers (5/8) > delta_from_base (2/8). GST-VLA's 7-table ablation with Δ column is gold standard. Checkmark grid NOT used in this field.\n\n**Division**: quantitative→table, qualitative→figure, safety→figure, hyperparameters→figure, per-task detail→appendix.\n\n## Figure Narrative Flow\n\nConsensus: **overview → motivation → results → ablation → real-world**. 5-6 figures in main paper. SpatialForcing exemplar: teaser → paradigm comparison → depth probing → sim → efficiency → real-world.\n",
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01MQuSzvyV1xqwj9rMsyE1Wj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "539c9b12-3dec-421d-978f-e21c5446e910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

_source line 8 · 2026-05-22T18:22:41.375Z_

<details><summary>↩ Tool result · `toolu_01MQuSzvyV1xqwj9rMsyE1Wj`</summary>

````text
1	# OccSafe-VLA — Paper Framing
2	
3	> 维护者: Director | 最后更新: 2026-05-22 08:30 UTC | 状态: Draft (MVP — ablation done, depth training)
4	
5	## Architecture Facts (from code, verified)
6	- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）
7	- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。
8	- **FocalLoss**: α=0.25, γ=2.0
9	- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)
10	- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）
11	- **LoRA**: rank=32, alpha=16, dropout=0.0
12	- **GPU**: 4× RTX PRO 6000 98GB per server
13	- **训练时间**: ~12.9h/run @ 1.08 it/s
14	
15	### 叙事含义
16	- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。
17	  比"仅改善 DINOv2"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。
18	- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 "lightweight auxiliary" 叙事
19	- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐"放手"让 action loss 主导，
20	  可论证为"先学空间结构，再精化动作"的课程学习效果
21	- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守
22	
23	### DepthHead (新增, 2026-05-22)
24	- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）
25	- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）
26	- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64
27	- **参数量**: ~1.2M（与 OccHead 同量级）
28	
29	## Core Insight (D017 修正, 2026-05-22)
30	
31	**原始假设（已部分推翻）**：BEV occupancy 迫使 vision encoder 发展 3D 空间感知 → safety emergence。
32	
33	**实际发现**：辅助任务的 **梯度流** 本身提供正则化效应（+2-3pp CAR），是 safety 改善的主导机制。
34	BEV 空间内容仅有边际正贡献（OCC vs Vanilla +1.7pp，但 Random vs Vanilla +2.6pp）。
35	关键证据：random occupancy labels（无空间信息）效果优于真实 BEV labels。
36	
37	**修正后的 Core Insight**：VLA fine-tuning 中，辅助任务通过梯度流对 vision encoder 施加隐式正则化，
38	防止 encoder 过度特化于 action prediction，从而保留更通用的空间表征 → collision avoidance 作为
39	正则化的 emergent property 涌现。**梯度流是必要条件（强证据：Detach 最差）**；
40	初步证据提示空间信号内容可能次于梯度流存在性（Random≈OCC），但 **0.9pp/2-seed 不足以定论，
41	等 3-seed 数据确认后再做最终判断**。
42	
43	**待验证**：Depth（egocentric, 与操作视角对齐）是否比 BEV（allocentric, 与操作视角正交）提供更有效的空间信号？
44	如果 Depth > Random → 空间内容确实重要，但需要正确的表征形式。
45	
46	## Framing Strategy (2026-05-22 Reviewer 定稿)
47	
48	**确定路线: Option B 分析论文**（Reviewer 审查通过）
49	
50	**Title（暂定）**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis"
51	- 问号格式适合当前 evidence 强度；如果 Path A/D 成立可改为声明式
52	- 待 depth 数据后最终确定
53	
54	**3-Contribution 结构（Reviewer 重构，解决 F1+F2 不独立问题）**:
55	- **C1 (核心发现)**: Auxiliary gradient flow regularization 是 VLA safety 改善的主导机制
56	  - 正面证据: Random/OCC > Vanilla（+2-3pp CAR with gradient flow）
57	  - 反面证据: Detach < Vanilla（-3.5pp, gradient flow 是必要条件）
58	  - 空间内容次要: Random ≈ OCC（⚠️ 0.9pp/2-seed, preliminary）
59	- **C2 (方法论贡献)**: 首个 5+ condition factorial study design for VLA safety mechanism analysis
60	  - Vanilla / Full OCC / Random OCC / Detach OCC / Depth / Cutoff
61	  - 每个 pairwise comparison 回答一个机制问题（见 Method §3.4 Table 1）
62	- **C3 (实用贡献)**: Concrete guidelines — 哪些辅助任务有效、哪些有害、何时使用
63	  - Depth vs BEV 对比 → 空间表征形式推荐
64	  - Cutoff temporal analysis → 训练阶段建议
65	
66	**Results Section 结构**:
67	```
68	4.1 Main Results (overall CAR/TSR table, 6 条件)
69	4.2 Mechanism Analysis (C1: 梯度流必要 + 空间内容次要)
70	4.3 Depth vs BEV Comparison (C3 一部分: egocentric vs allocentric)
71	4.4 Task-Level Analysis (cross-cutting)
72	    4.4a Ceiling effect 与 hard-task focus
73	    4.4b 条件间差异在 hard tasks 的放大
74	    4.4c T3 案例分析（TSR=100% + CAR=32.5% 安全悖论）
75	4.5 Temporal Dynamics (C1 时间维度 + C3 一部分)
76	    4.5a Cutoff experiment（when does gradient flow matter?）
77	    4.5b Vanilla learning curve（CAR 随训练演变）
78	```
79	
80	**⚠️ OCC s2 异常 seed 风险（Reviewer 发现）**:
81	OCC 3 seeds CAR: 0.832, 0.788, 0.770（std=0.032, range=6.2pp）。
82	s2(0.770) 显著拉低均值；s0(0.832) 是全条件最高单 seed。
83	mvp_occ_s2 T4 TSR=0.36（其他 OCC seeds ≥0.90）、T3 CAR=0.02 — 可能是异常 seed。
84	**Random vs OCC 排序建立在 2-seed vs 3-seed 不对等比较上，标注 preliminary。**
85	
86	## Core Contribution Evidence (D017 修正 + Reviewer 重构)
87	
88	### C1: Auxiliary Gradient Flow → Safety Regularization
89	辅助任务梯度流在 VLA fine-tuning 中提供隐式正则化，改善 collision avoidance。
90	梯度流是必要条件（Detach 反例），空间信号质量是次要因素（Random ≈ OCC，preliminary）。
91	
92	**Evidence (5 条件 @50K, 50r)**:
93	| 条件 | Seeds | CAR | vs Vanilla |
94	|------|-------|-----|-----------|
95	| Random OCC | 2 | 0.806 | **+2.6pp** |
96	| Full OCC | 3 | 0.797 | **+1.7pp** |
97	| Vanilla | 3 | 0.780 | baseline |
98	| Detach OCC | 2 | 0.745 | **-3.5pp** |
99	
100	**Detach 显著性风险（Reviewer 模拟）**:
101	- detach_s2=0.760 → p≈0.025 ✅ | detach_s2=0.770 → p≈0.08 ⚠️ | detach_s2=0.780 → p≈0.16 ❌
102	- **后盾**: per-task hard-task analysis（Detach T3 mean≈0.17 vs Vanilla T3 mean≈0.38, gap=21pp）
103	- 统计方法: bootstrap CI + Cohen's d，不完全依赖 p-value
104	
105	**Status**: ✅ 数据到齐（D017）。Random/OCC > Vanilla > Detach 排序跨 seed 一致。
106	**MVP Gate**: CAR=0.797 < 0.82 (FAIL 差 2.3pp), TSR=0.894 > 0.888 (PASS)
107	**Formal eval baseline (3 seeds, 20 rollouts/task @ 50K — FINAL)**:
108	- s0: TSR=91.0%, CAR=77.5%
109	- s1: TSR=93.5%, CAR=76.5%
110	- s2: TSR=91.0%, CAR=77.0%
111	- **Mean±Std**: TSR=91.8%±1.2%, CAR=77.0%±0.4%（CAR 跨 seed 方差极小，统计检验极有利）
112	- **Hard tasks**: T3=32.5%, T5=7.5%, T6=47.5% → hard-task mean CAR≈29.2% (s0/s1 avg, s2 待确认 per-task)
113	- **Easy tasks**: T0=95%, T1=97.5%, T2=90%, T4=100%, T7=100%, T8=100%, T9=100%
114	- **Key insight**: vanilla CAR 呈明显二分化——7/10 任务 CAR≥90%（布局安全），3/10 任务 CAR=7.5-47.5%（布局困难）
115	- **T5 最极端**: s2 TSR=40%, s0 TSR=45%, s1 TSR=65%——碗直接在 ramekin 上，碰撞和任务本身都极难
116	- **35K→50K 演变**: overall CAR +7.25pp; hard-task CAR 非单调（T3 在 s1 中反降）
117	
118	**Vanilla CAR Learning Curve (2 seeds, 20 rollouts/task)**:
119	| Step | Mean TSR | Mean CAR | Collisions |
120	|------|----------|----------|------------|
121	| 35K  | 88.25%   | 69.75%   | 60.5       |
122	| 40K  | 93.0%    | 71.25%   | 57.5       |
123	| 45K  | 96.0%    | 73.75%   | 52.5       |
124	| 50K  | 92.25%→91.8%(3seed) | 77.0% | 46.0 |
125	
126	**论文价值**：
127	- CAR 单调递增（两 seed 一致），证明 vanilla 的碰撞减少纯粹来自更长训练/更好模仿，非主动避障
128	- TSR 在 45K 达峰（~96%），50K 回落 ~4pp（轻微过拟合迹象）
129	- **关键对比**：如果 occ 的 CAR 在同 step 时显著高于 vanilla 曲线 → 证明 occ 赋予主动避障
130	- 如果 occ 30K 就达到 vanilla 50K 的 CAR → "accelerated spatial learning" 叙事
131	- **Paper 素材**: Task 5 (bowl on ramekin) TSR=55% and CAR=7.5% — 最困难任务，物理约束极强。
132	  Task 3 (bowl on cookie box) TSR=100% but CAR=32.5% — "完美完成任务但 67.5% 碰撞"，
133	  更好的 "task success ≠ behavioral safety" 例证（TSR 高但 CAR 低）
134	
135	**Ceiling Effect Analysis (Reviewer stress-test, 2026-05-20)**:
136	- 7/10 任务 vanilla CAR 已 100%（物体孤立），改善空间为零
137	- 全部 CAR 改善必须来自 T3/T5/T6 三个硬任务
138	- 即使硬任务 CAR 从 ~10% 提到 ~50%，整体 CAR 也只 +12pp（(3×40%)/10）
139	- **现实预期**: 8-12pp overall CAR 提升
140	- **Effect size 评判标准**: <5pp 失败 | 5-10pp 需强 ablation 补偿(Option B only) | 10-15pp 有意义 | ≥15pp 舒适
141	- AEGIS CBF 的 +59pp 是审稿人心理锚点，必须用 "zero inference cost" 差异化
142	
143	**Per-task Analysis (必须列入 Results)**:
144	- 同时报告 overall CAR 和 **hard-task-only CAR**（T3/T5/T6）
145	- Hard-task CAR 对 occ 效果更敏感，不被 easy tasks 的 100% 稀释
146	- 如果 occ 在硬任务 CAR 从 10%→40%，比 overall +12pp 更有冲击力
147	- 可视化建议：x 轴=最近障碍物距离，y 轴=CAR，叠加 vanilla vs occ 数据点
148	
149	**TSR 下降应对策略**:
150	- ≤3%: 安全，"no significant degradation"
151	- 3-5%: narrative damage 但可防守（paired t-test p>0.05 → "not statistically significant"）
152	- >5%: 叙事崩塌，需 pivot 到 "safety-performance Pareto front" + λ_occ 调参实验
153	
154	**⚠️ Baseline CAR 压缩风险 (Reviewer analysis, 2026-05-20 23:00 UTC)**:
155	信号：vanilla 50K T3 CAR 可能从 35K 的 0% 升至 ~50%。vanilla 50K overall CAR 可能 75-80%。
156	
157	Contingency scenarios:
158	- **Scenario A (CAR≈70%, 概率 20-25%)**: 正常推进，Story 不变
159	- **Scenario B (CAR≈75%, 概率 40-50%, 最可能)**: Claim 1 可行但需修改 opening。
160	  不能说"36% collision rate"（只剩 25%）。转向 per-task 叙事：
161	  "On physically challenging tasks, collision rates remain 50-90%"。Per-task analysis 成为核心武器。
162	- **Scenario C (CAR≈80%, 概率 20-30%)**: Claim 1 岌岌可危。Pivot 到 "accelerated spatial learning"：
163	  occ 在 <30K 步就达到 vanilla 50K 的 CAR 水平 → 训练效率论证。或转向纯训练动力学分析论文。
164	- **Scenario D (CAR≈85%+, 概率 5-10%)**: 大幅 pivot，occ 边际贡献难以显著。
165	
166	**关键洞察——vanilla CAR 为何随训练提升**:
167	- 解释 A（中等危险）：行为模仿效应——更好的模仿 demo → 更少偏离 → 更少碰撞。不是空间意识，是动作精度。
168	- 解释 B（高度危险）：action loss 隐式空间学习——足够训练后 encoder 自然发展空间理解。若成立，occ 价值仅在于"加速"而非"使能"。
169	- 可检验：encoder feature 可视化 (t-SNE/PCA)、碰撞 episode 轨迹对比（主动绕行 vs 精确模仿）
170	
171	**CAR Learning Curve (必须纳入论文)**:
172	- 在 35K/40K/45K/50K 各 checkpoint eval，展示 vanilla CAR 随训练演变
173	- 如果 vanilla CAR 持续上升而 occ 一开始就高（learning curve 提前收敛），这是 "occ accelerates spatial learning" 的有力证据
174	- 已派 Agent 利用空闲 GPU 跑中间 checkpoint eval
175	
176	**⚠️ Hard-task CAR 非单调性 (Reviewer warning, 2026-05-21)**:
177	- T3 CAR: s0 35K→50K = 0→50pp（↑），s1 35K→50K = 25→15pp（↓）
178	- T6 CAR: s0 不变(35%), s1 从 0→60pp（↑）
179	- **结论**：hard-task CAR 高度随机，不是系统性训练效果。20 rollouts 的 per-task CI 约 ±21pp。
180	- **T5 TSR 退化是唯一系统性模式**：s0 -40pp, s1 -30pp（两 seed 一致）
181	- **对 occ eval 的影响**：3 seeds × 20 rollouts 可能不足以区分 occ 和 vanilla 在 hard tasks 上的差异。
182	  如果 20-rollout 结果模糊，需追加到 50 rollouts/task（per-task CI 从 ±21pp 降到 ±13pp）。
183	
184	**OCC MVP Gate（已确立，D017）**:
185	- Gate 1: overall CAR ≥ 0.82 → **FAIL** (0.797)
186	- Gate 3: TSR ≥ 0.888 → PASS (0.894)
187	- OCC 作为独立方法未达标，但梯度流正则化机制已确立
188	
189	**=== Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）===**
190	
191	前提：Random 3-seed mean 在 random_s2 eval 后、depth eval 前锁定为固定锚点。
192	
193	**【Pass（必须同时满足）】**
194	1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）
195	2. Depth 4-seed mean TSR ≥ 0.870（= Vanilla 0.907 - 3.7pp，paper_framing 定义的可辩护下限）
196	
197	**【Fail（满足任一）】**
198	1. Depth 4-seed mean CAR < 0.780
199	2. Depth 4-seed mean TSR < 0.870
200	
201	**【灰区】**
202	- CI 下界 ≤ 0.780 但 point estimate > 0.780：追加 per-task hard-task analysis (T3/T5/T6)
203	
204	**=== Path 判定（Depth Pass 后执行）===**
205	- **Path A/D**: Depth mean > max(Random_3seed, OCC_3seed) + 2pp，且 bootstrap 95% CI of (Depth - max) 不含 0
206	  - 若 Random > OCC → Path A（梯度流+正确空间形式双重贡献）
207	  - 若 OCC > Random → Path D（空间内容重要+egocentric最优，方法论文路线）
208	- **Path B**: |Depth - Random| < 3pp 且 |Depth - OCC| < 3pp（三者趋同 → 内容无关）
209	- **Path C**: Depth < 0.780（被 Fail 覆盖，不进入 Path 判定）
210	- **灰区**: 以上均不满足 → per-task + hard-task analysis 辅助判断
211	- 3pp 阈值来源：已有条件间最大有意义差距 Random-Detach = 6.1pp 的一半
212	
213	**统计要求**：50 rollouts/task eval（per-task CI ~±13pp，优于 20r 的 ±21pp）
214	
215	### Claim 2 (Mechanism): Gradient Flow is Necessary and Sufficient
216	梯度流是辅助任务安全效应的必要条件。Detach(0.745) < Vanilla(0.780) → 切断梯度流不仅无效，
217	反而有害（-3.5pp，可能因 auxiliary head 作为 gradient sink 竞争优化资源）。
218	
219	**Evidence**: Detach 最差（0.745），比 Vanilla 还低 3.5pp。跨 2 seed 一致。
220	**Status**: ✅ 数据到齐。3rd seed (detach_s2) 训练中，预计 May 23 完成。
221	
222	### Claim 3 (Surprising): Spatial Content Secondary to Gradient Flow
223	Random occupancy labels（无空间信息）效果 ≥ 真实 BEV labels → 辅助任务的 **信号质量**
224	不是 safety 改善的关键因素，**梯度流正则化** 才是。
225	
226	**Evidence**: Random(0.806) > OCC(0.797) > Vanilla(0.780)。差异仅 0.9pp，2-seed。
227	**Status**: ⚠️ 2-seed only，方向待 3rd seed 确认。random_s2 训练中，ETA May 23。
228	**叙事价值**: 如果 3-seed 确认 Random ≥ OCC，这将是最 surprising 的发现——
229	颠覆"需要正确 3D supervision"的直觉。但 0.9pp/2-seed 目前只是初步信号。
230	**⚠️ 论文 framing 关键**: 不能说"any aux loss works"（detach 反例），
231	如果确认则说"gradient flow regularization works, label content is secondary"。
232	**⚠️ 翻转可能**: 如果 3-seed 后 OCC > Random → Claim 3 重写为"空间内容有贡献"，见 Path D。
233	
234	### Claim 4 (Depth Comparison): Egocentric vs Allocentric Spatial Signal
235	Depth（egocentric, 与操作视角对齐）vs BEV Occupancy（allocentric）对 VLA safety 的差异化效果。
236	
237	**Evidence needed**: depth 4-seed eval vs occ/random/vanilla/detach
238	**Status**: 🏃 4 seeds 训练中（s0/s1 westd-34685, s2/s3 westd-10894），ETA May 23 ~20:00 UTC
239	
240	**三条叙事路径（完整 story skeleton）**:
241	
242	- **Path A (Depth > Random > OCC)**:
243	  Title: "Egocentric Spatial Supervision Unlocks VLA Safety"
244	  Core claim: 辅助任务梯度流是必要条件，但空间信号形式决定效果上限。
245	  Egocentric depth 与操作视角对齐，直接编码 end-effector 到障碍物距离 → 比 allocentric BEV 更自然。
246	  Story arc: gradient flow (necessary) + correct spatial frame (sufficient) → 双重贡献。
247	  论文结构: Method 介绍 depth head + occ head 对比设计；Results 展示 depth>random>occ>vanilla>detach；
248	  Analysis 解释为什么 egocentric > allocentric（操作空间对齐性）。
249	  **贡献强度: 最强**（方法+机制+实证三重贡献，AAAI 舒适区）。
250	
251	- **Path B (Depth ≈ Random ≈ OCC)**:
252	  Title: "Auxiliary Gradient Flow Regularization Improves VLA Collision Avoidance"
253	  Core claim: 辅助任务梯度流正则化是 VLA safety 改善的充分机制，空间信号内容不重要。
254	  Surprising finding: random labels、BEV occ、egocentric depth 效果相当 → 共同因子是梯度流。
255	  Story arc: 排除法叙事（detach 排除无梯度流 → random 排除信号质量 → depth≈occ 排除表征形式）。
256	  论文结构: 经典 ablation-driven analysis paper；每个条件回答一个机制问题；
257	  Discussion 讨论 "why gradient flow helps"（隐式正则化 / multi-task learning / encoder capacity）。
258	  **贡献强度: 中等偏强**（surprising negative + 完整机制分析，AAAI 可接受但需要写作质量补偿）。
259	
260	- **Path C (Depth < Vanilla)**:
261	  Title: "When Does 3D Auxiliary Supervision Help VLA Safety? A Systematic Study"
262	  Core claim: 不同 3D 表征对 VLA fine-tuning 有差异化影响；部分 3D 信号反而有害。
263	  Story arc: "not all 3D supervision is equal" → 系统分类（helpful: gradient flow / neutral: BEV content / harmful: depth）。
264	  论文结构: 分类框架 + per-condition 深入分析 + 实用建议。
265	  **贡献强度: 中等**（分析论文但缺乏 positive method contribution，需要非常 thorough 的实验覆盖）。
266	
267	- **Path D (Depth > OCC > Random, 即 3-seed 后 Random vs OCC 翻转)**:
268	  前提: 3-seed 数据确认 OCC > Random（当前 0.9pp 差异翻转）。
269	  Title: "Egocentric Depth Supervision for Safe Vision-Language-Action Models"
270	  Core claim: 空间监督内容确实重要（OCC > Random 排除纯正则化假说），
271	  且 egocentric depth 比 allocentric BEV 更有效（Depth > OCC）。
272	  Story arc: 回归方法论文路线——正确的空间表征形式是关键。
273	  梯度流是必要条件（Detach 反例），空间信号质量是充分条件（OCC > Random），
274	  egocentric 对齐是最优形式（Depth > OCC）。三层递进叙事。
275	  **贡献强度: 最强**（方法+机制+实证，且有清晰的 practical recommendation：用 depth 不用 BEV）。
276	  **⚠️ 此路径依赖 3-seed Random < OCC，当前 2-seed 数据不支持。**
277	
278	### Path Evidence Mapping & Weakness Analysis (数据无关，提前准备)
279	
280	| Path | 已有强证据 | 需要数据确认 | 主要 weakness | 审稿人最可能攻击点 |
281	|------|-----------|-------------|-------------|------------------|
282	| **A** (Depth>Random>OCC) | Detach 最差(梯度流必要) | Depth CAR > Random CAR (4-seed) | 仅一个 benchmark (SafeLIBERO) + 一个 VLA (OpenVLA-OFT) | "depth 效果是否 architecture-specific?" → 需 2nd VLA 或 2nd benchmark 补 |
283	| **B** (Depth≈Random≈OCC) | Random≈OCC (2-seed初步); Detach最差 | Depth CAR ≈ Random/OCC (4-seed); 3-seed确认Random≈OCC | "为什么梯度流有效"缺机制解释(不只是实验现象) | "这只是 multi-task regularization 的已知现象?" → 需要与 MTL 文献对比 + VLA-specific 解释 |
284	| **C** (Depth&lt;Vanilla) | Detach最差 | Depth CAR < Vanilla (4-seed) | 无 positive method contribution | "那该用什么辅助任务?" → 需要 constructive recommendation, 不能只是 negative |
285	| **D** (Depth>OCC>Random) | Detach最差 | 3-seed OCC>Random 翻转 + Depth>OCC | 依赖 0.9pp 翻转(概率未知) | 同 Path A 的 generalization concern |
286	
287	**所有路径共通 weakness**:
288	1. Single VLA architecture (OpenVLA-OFT) — RC4, 所有路径都需要在 Limitations 承认
289	2. Single benchmark ecosystem (SafeLIBERO) — RC5, 加 LIBERO-Goal 可缓解
290	3. 训练成本 ~13h/run 限制了 seed 数量，hard-task CAR 方差大 — RC6
291	4. Ceiling effect: 7/10 tasks vanilla CAR=100%, 改善空间集中在 T3/T5/T6 三个 hard tasks
292	
293	**Path B 特有的额外准备**（概率最高 40-50%，需提前做）:
294	- 文献调研: multi-task learning regularization in fine-tuning（MTL 社区已有大量工作）
295	- 差异化论证: "VLA fine-tuning 中辅助任务梯度流的 safety 效应"是 VLA-specific 发现，不是 MTL 的简单重复
296	- Discussion 预写: "why gradient flow regularization improves collision avoidance specifically"
297	  假说 1: 防止 vision encoder 过拟合到 action prediction → 保留更通用的空间特征
298	  假说 2: 辅助任务 loss landscape 改善优化轨迹（引 sharpness-aware minimization 类比）
299	  假说 3: gradient diversity 防止 LoRA adapter 退化
300	
301	### Claim 5 (Extension, if Option C): OCC-CBF Double Defense
302	Occ-aware representation feeds occupancy-conditioned CBF → implicit + explicit safety 叠加。
303	
304	**Evidence needed**: OCC-CBF proof-of-concept eval
305	**Status**: Planned (post-MVP, ~30 GPU-hours, eval only)
306	**Dependency**: Claim 1 must pass first
307	
308	## Anticipated Reviewer Concerns
309	
310	### RC1 [CRITICAL]: Collision Detection Metric Validity
311	**Attack**: "How is your collision metric defined? Is threshold=0.001 scientifically justified?"
312	**Defense**: 我们使用 SafeLIBERO 原始定义（VLSA-AEGIS L367-372）: L1 displacement, threshold=0.001,
313	body_xpos。已通过代码级验证对齐。✅ RESOLVED
314	
315	### RC2 [HIGH]: "Why Not Just Use CBF?"
316	**Attack**: AEGIS CBF 达到 +59.16% CAR，如果 occ supervision 只有 +5-10%，为什么不直接加 CBF？
317	**Defense**:
318	- Implicit safety 零推理开销（CBF 需要 QP solver）
319	- Occ + CBF 可叠加（OCC-CBF）→ 双重防线优于单一方案
320	- **需要**: OCC-CBF proof-of-concept 展示叠加效果
321	
322	### RC3 [HIGH]: Depth Ablation 是 Existential Risk
323	**Attack**: "Depth supervision 效果相当吗？"
324	**Defense**: 取决于实验结果。预备两条叙事线:
325	- Path A (occ >> depth): Occupancy 的 allocentric + boundary 特性是关键
326	- Path B (occ ≈ depth): 发现 3D supervision 普遍提升 safety，转 Option B framing
327	
328	### RC4 [MEDIUM]: Single VLA Architecture
329	**Attack**: "这是 OpenVLA-OFT 的特性还是 occupancy 的功劳？"
330	**Defense**:
331	- MVP 阶段接受此限制（AAAI scope）
332	- Post-MVP 考虑 Diffusion Policy 作为第二架构（~60h）
333	- SmolVLA 2×2 sanity check（IDEA_BRIEF 原设计）
334	- Limitations 中显式承认
335	
336	### RC5 [MEDIUM]: Single Benchmark Ecosystem
337	**Attack**: "LIBERO 桌面操作的 safety 意义有限"
338	**Defense**:
339	- LIBERO 是 VLA 社区标准 benchmark
340	- SafeLIBERO 是唯一公开的 VLA collision benchmark
341	- 添加第 2 suite (LIBERO-Goal/Object) 增加泛化证据
342	- Limitations 中限定为 "tabletop manipulation"
343	
344	### RC6 [LOW]: n=3 Statistical Power
345	**Attack**: "3 seeds 的 paired t-test power 很低"
346	**Defense**: 报告 Cohen's d 和 95% CI，不完全依赖 p-value。
347	如果 effect size 大（CAR 差距 >10pp），n=3 也能显著。
348	
349	## Framing Risk Ranking (D017 更新, 2026-05-22)
350	> 注: 以下均为 framing pivot risk（需换叙事但论文仍可写），非 paper-killing risk。
351	> 真正的 existential risk: 3+ seed 后梯度流正则化效应消失（所有条件收敛到 baseline），或 Detach 3rd seed 翻转。
352	
353	| 排名 | 风险 | 概率 | 应对 |
354	|------|------|------|------|
355	| **1** | Depth ≈ Random ≈ OCC（空间内容完全无用） | 40-50% | 论文转为纯机制分析："gradient flow regularization for VLA safety"。贡献足够但需要强 ablation 叙事 |
356	| **2** | 高 seed 方差致条件间差异不显著 | 25-30% | 已有 4 seed depth；追加 3rd seed random/detach 中；bootstrap CI |
357	| **3** | Depth 结果异常（&lt;Vanilla 或 >>Random） | 15-20% | Path C framing（差异化影响分析）或代码 bug 排查 |
358	| **4** | OCC-CBF 无法按时完成 | 40-50% | Option B 不依赖 CBF |
359	| ~~5~~ | ~~Detach 无效~~ | ~~N/A~~ | ✅ 已确认 Detach 最差，Claim 2 成立 |
360	| ~~6~~ | ~~CAR 提升 <5pp~~ | ~~N/A~~ | ✅ OCC +1.7pp（边际），但 Random +2.6pp → 梯度流正则化效应 confirmed |
361	
362	**已解决的风险**: Detach 结果明确（0.745 最差）；CAR 提升虽小但机制清晰（梯度流 > 空间内容）。
363	**新增风险**: Depth 是当前最大不确定性——决定论文是"空间信号形式对比"还是"纯梯度流正则化分析"。
364	
365	## Cutoff 实验设计（新增）
366	occ_loss_cutoff_step=35000：前 35K 步用 OCC supervision（获取空间感知），后 15K 步关闭 OCC loss（让 action loss 主导）。
367	**假设**: 如果 cutoff > full OCC → 证明 late-stage OCC 干扰 action prediction（课程学习论证）。
368	**Status**: 2 seeds 训练中（westd-34685 cuda:0/3），ETA May 23 ~20:00 UTC。
369	
370	## Story Skeleton
371	
372	1. **Opening**: VLAs 在桌面操作上接近人类 success rate，但在空间受限的场景中碰撞率极高。
373	   核心矛盾：**任务成功 ≠ 行为安全**。
374	   (Evidence: vanilla TSR=92% overall, but on physically challenging tasks collision rate reaches 53-92%.
375	   T3: TSR=100% but CAR=32.5%; T5: TSR=55%, CAR=7.5%)
376	
377	2. **Diagnosis**: VLA vision encoder 是 2D pretrained，缺乏 3D spatial structure 理解。
378	   能完成任务是因为学会了语义-动作映射，但从未理解物体 3D 边界。
379	
380	3. **Gap**: 安全-VLA 文献（CBF/RL）与空间-VLA 文献（depth/point cloud/occ）完全隔离。
381	   15+ 空间方法从未测 safety；4+ 安全方法从未用空间表征进步。
382	   **No one has connected the two.**
383	
384	4. **Insight (AD analogy, 克制使用)**: 自动驾驶用 occupancy map 从 2D 感知跨越到 3D 安全决策。
385	   Robot manipulation 面对同样问题。BEV occupancy 天然编码 workspace 中的 object boundary。
386	
387	5. **Method**: Auxiliary BEV occ supervision during fine-tuning → zero inference cost →
388	   implicit collision avoidance emerges without explicit safety training.
389	
390	6. **Ablation story (D017 修正)**: gradient flow 是必要条件（detach 最差）；
391	   random labels 也有效（surprising! → 梯度流正则化是主导机制）；
392	   depth 对比揭示 egocentric vs allocentric 空间信号的差异（待数据）。
393	
394	7. **Extension (Option C)**: Occ-aware representation + OCC-CBF → 双重防线（implicit + explicit safety）。
395	
396	## Sections Pre-writable (不依赖实验结果)
397	
398	- **Related Work**: 11+ 篇论文 landscape 已明确，gap 定位清晰
399	- **Method §3a-3b**: Occ head 架构、training pipeline 已实现
400	- **Experiments §4a Setup**: Benchmark 描述、evaluation protocol、baseline 列表
401	- **Intro 前 2 段**: 问题设定 + 文献 gap
402	
403	## Post-MVP Experiment Roadmap (by priority)
404	
405	| Priority | Experiment | GPU-hours | Claim | Notes |
406	|----------|-----------|-----------|-------|-------|
407	| P0 | 5-condition ablation (D005) | ~120h | C2-C4 | occ_detach, depth, random_occ |
408	| P0 | 2nd suite (LIBERO-Goal) | ~50h eval | RC5 | 泛化 |
409	| P0 | OCC-CBF PoC | ~30h eval | C5 | Option C 核心 |
410	| P1 | Predicted occ vs GT occ | ~50h | 实用性 | 回应 "需要 sim GT" |
411	| P2 | 2nd architecture (Diffusion Policy) | ~60h | RC4 | 泛化 |
412	| P2 | Level I + II 对比 | ~20h eval | 难度 sensitivity | |
413	
414	Total: ~330h。8 卡 × 10 周 ≈ 1340h 预算，MVP ~170h + post-MVP ~330h = ~500h，宽裕。
415	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "2aa9f92a-90b9-450c-ab0f-e5a64c7b6630",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md",
      "content": "# OccSafe-VLA — Paper Framing\n\n> 维护者: Director | 最后更新: 2026-05-22 08:30 UTC | 状态: Draft (MVP — ablation done, depth training)\n\n## Architecture Facts (from code, verified)\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\n- **FocalLoss**: α=0.25, γ=2.0\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\n- **LoRA**: rank=32, alpha=16, dropout=0.0\n- **GPU**: 4× RTX PRO 6000 98GB per server\n- **训练时间**: ~12.9h/run @ 1.08 it/s\n\n### 叙事含义\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\n  比\"仅改善 DINOv2\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \"lightweight auxiliary\" 叙事\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\"放手\"让 action loss 主导，\n  可论证为\"先学空间结构，再精化动作\"的课程学习效果\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\n\n### DepthHead (新增, 2026-05-22)\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\n- **参数量**: ~1.2M（与 OccHead 同量级）\n\n## Core Insight (D017 修正, 2026-05-22)\n\n**原始假设（已部分推翻）**：BEV occupancy 迫使 vision encoder 发展 3D 空间感知 → safety emergence。\n\n**实际发现**：辅助任务的 **梯度流** 本身提供正则化效应（+2-3pp CAR），是 safety 改善的主导机制。\nBEV 空间内容仅有边际正贡献（OCC vs Vanilla +1.7pp，但 Random vs Vanilla +2.6pp）。\n关键证据：random occupancy labels（无空间信息）效果优于真实 BEV labels。\n\n**修正后的 Core Insight**：VLA fine-tuning 中，辅助任务通过梯度流对 vision encoder 施加隐式正则化，\n防止 encoder 过度特化于 action prediction，从而保留更通用的空间表征 → collision avoidance 作为\n正则化的 emergent property 涌现。**梯度流是必要条件（强证据：Detach 最差）**；\n初步证据提示空间信号内容可能次于梯度流存在性（Random≈OCC），但 **0.9pp/2-seed 不足以定论，\n等 3-seed 数据确认后再做最终判断**。\n\n**待验证**：Depth（egocentric, 与操作视角对齐）是否比 BEV（allocentric, 与操作视角正交）提供更有效的空间信号？\n如果 Depth > Random → 空间内容确实重要，但需要正确的表征形式。\n\n## Framing Strategy (2026-05-22 Reviewer 定稿)\n\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\n\n**Title（暂定）**: \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\"\n- 问号格式适合当前 evidence 强度；如果 Path A/D 成立可改为声明式\n- 待 depth 数据后最终确定\n\n**3-Contribution 结构（Reviewer 重构，解决 F1+F2 不独立问题）**:\n- **C1 (核心发现)**: Auxiliary gradient flow regularization 是 VLA safety 改善的主导机制\n  - 正面证据: Random/OCC > Vanilla（+2-3pp CAR with gradient flow）\n  - 反面证据: Detach < Vanilla（-3.5pp, gradient flow 是必要条件）\n  - 空间内容次要: Random ≈ OCC（⚠️ 0.9pp/2-seed, preliminary）\n- **C2 (方法论贡献)**: 首个 5+ condition factorial study design for VLA safety mechanism analysis\n  - Vanilla / Full OCC / Random OCC / Detach OCC / Depth / Cutoff\n  - 每个 pairwise comparison 回答一个机制问题（见 Method §3.4 Table 1）\n- **C3 (实用贡献)**: Concrete guidelines — 哪些辅助任务有效、哪些有害、何时使用\n  - Depth vs BEV 对比 → 空间表征形式推荐\n  - Cutoff temporal analysis → 训练阶段建议\n\n**Results Section 结构**:\n```\n4.1 Main Results (overall CAR/TSR table, 6 条件)\n4.2 Mechanism Analysis (C1: 梯度流必要 + 空间内容次要)\n4.3 Depth vs BEV Comparison (C3 一部分: egocentric vs allocentric)\n4.4 Task-Level Analysis (cross-cutting)\n    4.4a Ceiling effect 与 hard-task focus\n    4.4b 条件间差异在 hard tasks 的放大\n    4.4c T3 案例分析（TSR=100% + CAR=32.5% 安全悖论）\n4.5 Temporal Dynamics (C1 时间维度 + C3 一部分)\n    4.5a Cutoff experiment（when does gradient flow matter?）\n    4.5b Vanilla learning curve（CAR 随训练演变）\n```\n\n**⚠️ OCC s2 异常 seed 风险（Reviewer 发现）**:\nOCC 3 seeds CAR: 0.832, 0.788, 0.770（std=0.032, range=6.2pp）。\ns2(0.770) 显著拉低均值；s0(0.832) 是全条件最高单 seed。\nmvp_occ_s2 T4 TSR=0.36（其他 OCC seeds ≥0.90）、T3 CAR=0.02 — 可能是异常 seed。\n**Random vs OCC 排序建立在 2-seed vs 3-seed 不对等比较上，标注 preliminary。**\n\n## Core Contribution Evidence (D017 修正 + Reviewer 重构)\n\n### C1: Auxiliary Gradient Flow → Safety Regularization\n辅助任务梯度流在 VLA fine-tuning 中提供隐式正则化，改善 collision avoidance。\n梯度流是必要条件（Detach 反例），空间信号质量是次要因素（Random ≈ OCC，preliminary）。\n\n**Evidence (5 条件 @50K, 50r)**:\n| 条件 | Seeds | CAR | vs Vanilla |\n|------|-------|-----|-----------|\n| Random OCC | 2 | 0.806 | **+2.6pp** |\n| Full OCC | 3 | 0.797 | **+1.7pp** |\n| Vanilla | 3 | 0.780 | baseline |\n| Detach OCC | 2 | 0.745 | **-3.5pp** |\n\n**Detach 显著性风险（Reviewer 模拟）**:\n- detach_s2=0.760 → p≈0.025 ✅ | detach_s2=0.770 → p≈0.08 ⚠️ | detach_s2=0.780 → p≈0.16 ❌\n- **后盾**: per-task hard-task analysis（Detach T3 mean≈0.17 vs Vanilla T3 mean≈0.38, gap=21pp）\n- 统计方法: bootstrap CI + Cohen's d，不完全依赖 p-value\n\n**Status**: ✅ 数据到齐（D017）。Random/OCC > Vanilla > Detach 排序跨 seed 一致。\n**MVP Gate**: CAR=0.797 < 0.82 (FAIL 差 2.3pp), TSR=0.894 > 0.888 (PASS)\n**Formal eval baseline (3 seeds, 20 rollouts/task @ 50K — FINAL)**:\n- s0: TSR=91.0%, CAR=77.5%\n- s1: TSR=93.5%, CAR=76.5%\n- s2: TSR=91.0%, CAR=77.0%\n- **Mean±Std**: TSR=91.8%±1.2%, CAR=77.0%±0.4%（CAR 跨 seed 方差极小，统计检验极有利）\n- **Hard tasks**: T3=32.5%, T5=7.5%, T6=47.5% → hard-task mean CAR≈29.2% (s0/s1 avg, s2 待确认 per-task)\n- **Easy tasks**: T0=95%, T1=97.5%, T2=90%, T4=100%, T7=100%, T8=100%, T9=100%\n- **Key insight**: vanilla CAR 呈明显二分化——7/10 任务 CAR≥90%（布局安全），3/10 任务 CAR=7.5-47.5%（布局困难）\n- **T5 最极端**: s2 TSR=40%, s0 TSR=45%, s1 TSR=65%——碗直接在 ramekin 上，碰撞和任务本身都极难\n- **35K→50K 演变**: overall CAR +7.25pp; hard-task CAR 非单调（T3 在 s1 中反降）\n\n**Vanilla CAR Learning Curve (2 seeds, 20 rollouts/task)**:\n| Step | Mean TSR | Mean CAR | Collisions |\n|------|----------|----------|------------|\n| 35K  | 88.25%   | 69.75%   | 60.5       |\n| 40K  | 93.0%    | 71.25%   | 57.5       |\n| 45K  | 96.0%    | 73.75%   | 52.5       |\n| 50K  | 92.25%→91.8%(3seed) | 77.0% | 46.0 |\n\n**论文价值**：\n- CAR 单调递增（两 seed 一致），证明 vanilla 的碰撞减少纯粹来自更长训练/更好模仿，非主动避障\n- TSR 在 45K 达峰（~96%），50K 回落 ~4pp（轻微过拟合迹象）\n- **关键对比**：如果 occ 的 CAR 在同 step 时显著高于 vanilla 曲线 → 证明 occ 赋予主动避障\n- 如果 occ 30K 就达到 vanilla 50K 的 CAR → \"accelerated spatial learning\" 叙事\n- **Paper 素材**: Task 5 (bowl on ramekin) TSR=55% and CAR=7.5% — 最困难任务，物理约束极强。\n  Task 3 (bowl on cookie box) TSR=100% but CAR=32.5% — \"完美完成任务但 67.5% 碰撞\"，\n  更好的 \"task success ≠ behavioral safety\" 例证（TSR 高但 CAR 低）\n\n**Ceiling Effect Analysis (Reviewer stress-test, 2026-05-20)**:\n- 7/10 任务 vanilla CAR 已 100%（物体孤立），改善空间为零\n- 全部 CAR 改善必须来自 T3/T5/T6 三个硬任务\n- 即使硬任务 CAR 从 ~10% 提到 ~50%，整体 CAR 也只 +12pp（(3×40%)/10）\n- **现实预期**: 8-12pp overall CAR 提升\n- **Effect size 评判标准**: <5pp 失败 | 5-10pp 需强 ablation 补偿(Option B only) | 10-15pp 有意义 | ≥15pp 舒适\n- AEGIS CBF 的 +59pp 是审稿人心理锚点，必须用 \"zero inference cost\" 差异化\n\n**Per-task Analysis (必须列入 Results)**:\n- 同时报告 overall CAR 和 **hard-task-only CAR**（T3/T5/T6）\n- Hard-task CAR 对 occ 效果更敏感，不被 easy tasks 的 100% 稀释\n- 如果 occ 在硬任务 CAR 从 10%→40%，比 overall +12pp 更有冲击力\n- 可视化建议：x 轴=最近障碍物距离，y 轴=CAR，叠加 vanilla vs occ 数据点\n\n**TSR 下降应对策略**:\n- ≤3%: 安全，\"no significant degradation\"\n- 3-5%: narrative damage 但可防守（paired t-test p>0.05 → \"not statistically significant\"）\n- >5%: 叙事崩塌，需 pivot 到 \"safety-performance Pareto front\" + λ_occ 调参实验\n\n**⚠️ Baseline CAR 压缩风险 (Reviewer analysis, 2026-05-20 23:00 UTC)**:\n信号：vanilla 50K T3 CAR 可能从 35K 的 0% 升至 ~50%。vanilla 50K overall CAR 可能 75-80%。\n\nContingency scenarios:\n- **Scenario A (CAR≈70%, 概率 20-25%)**: 正常推进，Story 不变\n- **Scenario B (CAR≈75%, 概率 40-50%, 最可能)**: Claim 1 可行但需修改 opening。\n  不能说\"36% collision rate\"（只剩 25%）。转向 per-task 叙事：\n  \"On physically challenging tasks, collision rates remain 50-90%\"。Per-task analysis 成为核心武器。\n- **Scenario C (CAR≈80%, 概率 20-30%)**: Claim 1 岌岌可危。Pivot 到 \"accelerated spatial learning\"：\n  occ 在 <30K 步就达到 vanilla 50K 的 CAR 水平 → 训练效率论证。或转向纯训练动力学分析论文。\n- **Scenario D (CAR≈85%+, 概率 5-10%)**: 大幅 pivot，occ 边际贡献难以显著。\n\n**关键洞察——vanilla CAR 为何随训练提升**:\n- 解释 A（中等危险）：行为模仿效应——更好的模仿 demo → 更少偏离 → 更少碰撞。不是空间意识，是动作精度。\n- 解释 B（高度危险）：action loss 隐式空间学习——足够训练后 encoder 自然发展空间理解。若成立，occ 价值仅在于\"加速\"而非\"使能\"。\n- 可检验：encoder feature 可视化 (t-SNE/PCA)、碰撞 episode 轨迹对比（主动绕行 vs 精确模仿）\n\n**CAR Learning Curve (必须纳入论文)**:\n- 在 35K/40K/45K/50K 各 checkpoint eval，展示 vanilla CAR 随训练演变\n- 如果 vanilla CAR 持续上升而 occ 一开始就高（learning curve 提前收敛），这是 \"occ accelerates spatial learning\" 的有力证据\n- 已派 Agent 利用空闲 GPU 跑中间 checkpoint eval\n\n**⚠️ Hard-task CAR 非单调性 (Reviewer warning, 2026-05-21)**:\n- T3 CAR: s0 35K→50K = 0→50pp（↑），s1 35K→50K = 25→15pp（↓）\n- T6 CAR: s0 不变(35%), s1 从 0→60pp（↑）\n- **结论**：hard-task CAR 高度随机，不是系统性训练效果。20 rollouts 的 per-task CI 约 ±21pp。\n- **T5 TSR 退化是唯一系统性模式**：s0 -40pp, s1 -30pp（两 seed 一致）\n- **对 occ eval 的影响**：3 seeds × 20 rollouts 可能不足以区分 occ 和 vanilla 在 hard tasks 上的差异。\n  如果 20-rollout 结果模糊，需追加到 50 rollouts/task（per-task CI 从 ±21pp 降到 ±13pp）。\n\n**OCC MVP Gate（已确立，D017）**:\n- Gate 1: overall CAR ≥ 0.82 → **FAIL** (0.797)\n- Gate 3: TSR ≥ 0.888 → PASS (0.894)\n- OCC 作为独立方法未达标，但梯度流正则化机制已确立\n\n**=== Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）===**\n\n前提：Random 3-seed mean 在 random_s2 eval 后、depth eval 前锁定为固定锚点。\n\n**【Pass（必须同时满足）】**\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\n2. Depth 4-seed mean TSR ≥ 0.870（= Vanilla 0.907 - 3.7pp，paper_framing 定义的可辩护下限）\n\n**【Fail（满足任一）】**\n1. Depth 4-seed mean CAR < 0.780\n2. Depth 4-seed mean TSR < 0.870\n\n**【灰区】**\n- CI 下界 ≤ 0.780 但 point estimate > 0.780：追加 per-task hard-task analysis (T3/T5/T6)\n\n**=== Path 判定（Depth Pass 后执行）===**\n- **Path A/D**: Depth mean > max(Random_3seed, OCC_3seed) + 2pp，且 bootstrap 95% CI of (Depth - max) 不含 0\n  - 若 Random > OCC → Path A（梯度流+正确空间形式双重贡献）\n  - 若 OCC > Random → Path D（空间内容重要+egocentric最优，方法论文路线）\n- **Path B**: |Depth - Random| < 3pp 且 |Depth - OCC| < 3pp（三者趋同 → 内容无关）\n- **Path C**: Depth < 0.780（被 Fail 覆盖，不进入 Path 判定）\n- **灰区**: 以上均不满足 → per-task + hard-task analysis 辅助判断\n- 3pp 阈值来源：已有条件间最大有意义差距 Random-Detach = 6.1pp 的一半\n\n**统计要求**：50 rollouts/task eval（per-task CI ~±13pp，优于 20r 的 ±21pp）\n\n### Claim 2 (Mechanism): Gradient Flow is Necessary and Sufficient\n梯度流是辅助任务安全效应的必要条件。Detach(0.745) < Vanilla(0.780) → 切断梯度流不仅无效，\n反而有害（-3.5pp，可能因 auxiliary head 作为 gradient sink 竞争优化资源）。\n\n**Evidence**: Detach 最差（0.745），比 Vanilla 还低 3.5pp。跨 2 seed 一致。\n**Status**: ✅ 数据到齐。3rd seed (detach_s2) 训练中，预计 May 23 完成。\n\n### Claim 3 (Surprising): Spatial Content Secondary to Gradient Flow\nRandom occupancy labels（无空间信息）效果 ≥ 真实 BEV labels → 辅助任务的 **信号质量**\n不是 safety 改善的关键因素，**梯度流正则化** 才是。\n\n**Evidence**: Random(0.806) > OCC(0.797) > Vanilla(0.780)。差异仅 0.9pp，2-seed。\n**Status**: ⚠️ 2-seed only，方向待 3rd seed 确认。random_s2 训练中，ETA May 23。\n**叙事价值**: 如果 3-seed 确认 Random ≥ OCC，这将是最 surprising 的发现——\n颠覆\"需要正确 3D supervision\"的直觉。但 0.9pp/2-seed 目前只是初步信号。\n**⚠️ 论文 framing 关键**: 不能说\"any aux loss works\"（detach 反例），\n如果确认则说\"gradient flow regularization works, label content is secondary\"。\n**⚠️ 翻转可能**: 如果 3-seed 后 OCC > Random → Claim 3 重写为\"空间内容有贡献\"，见 Path D。\n\n### Claim 4 (Depth Comparison): Egocentric vs Allocentric Spatial Signal\nDepth（egocentric, 与操作视角对齐）vs BEV Occupancy（allocentric）对 VLA safety 的差异化效果。\n\n**Evidence needed**: depth 4-seed eval vs occ/random/vanilla/detach\n**Status**: 🏃 4 seeds 训练中（s0/s1 westd-34685, s2/s3 westd-10894），ETA May 23 ~20:00 UTC\n\n**三条叙事路径（完整 story skeleton）**:\n\n- **Path A (Depth > Random > OCC)**:\n  Title: \"Egocentric Spatial Supervision Unlocks VLA Safety\"\n  Core claim: 辅助任务梯度流是必要条件，但空间信号形式决定效果上限。\n  Egocentric depth 与操作视角对齐，直接编码 end-effector 到障碍物距离 → 比 allocentric BEV 更自然。\n  Story arc: gradient flow (necessary) + correct spatial frame (sufficient) → 双重贡献。\n  论文结构: Method 介绍 depth head + occ head 对比设计；Results 展示 depth>random>occ>vanilla>detach；\n  Analysis 解释为什么 egocentric > allocentric（操作空间对齐性）。\n  **贡献强度: 最强**（方法+机制+实证三重贡献，AAAI 舒适区）。\n\n- **Path B (Depth ≈ Random ≈ OCC)**:\n  Title: \"Auxiliary Gradient Flow Regularization Improves VLA Collision Avoidance\"\n  Core claim: 辅助任务梯度流正则化是 VLA safety 改善的充分机制，空间信号内容不重要。\n  Surprising finding: random labels、BEV occ、egocentric depth 效果相当 → 共同因子是梯度流。\n  Story arc: 排除法叙事（detach 排除无梯度流 → random 排除信号质量 → depth≈occ 排除表征形式）。\n  论文结构: 经典 ablation-driven analysis paper；每个条件回答一个机制问题；\n  Discussion 讨论 \"why gradient flow helps\"（隐式正则化 / multi-task learning / encoder capacity）。\n  **贡献强度: 中等偏强**（surprising negative + 完整机制分析，AAAI 可接受但需要写作质量补偿）。\n\n- **Path C (Depth < Vanilla)**:\n  Title: \"When Does 3D Auxiliary Supervision Help VLA Safety? A Systematic Study\"\n  Core claim: 不同 3D 表征对 VLA fine-tuning 有差异化影响；部分 3D 信号反而有害。\n  Story arc: \"not all 3D supervision is equal\" → 系统分类（helpful: gradient flow / neutral: BEV content / harmful: depth）。\n  论文结构: 分类框架 + per-condition 深入分析 + 实用建议。\n  **贡献强度: 中等**（分析论文但缺乏 positive method contribution，需要非常 thorough 的实验覆盖）。\n\n- **Path D (Depth > OCC > Random, 即 3-seed 后 Random vs OCC 翻转)**:\n  前提: 3-seed 数据确认 OCC > Random（当前 0.9pp 差异翻转）。\n  Title: \"Egocentric Depth Supervision for Safe Vision-Language-Action Models\"\n  Core claim: 空间监督内容确实重要（OCC > Random 排除纯正则化假说），\n  且 egocentric depth 比 allocentric BEV 更有效（Depth > OCC）。\n  Story arc: 回归方法论文路线——正确的空间表征形式是关键。\n  梯度流是必要条件（Detach 反例），空间信号质量是充分条件（OCC > Random），\n  egocentric 对齐是最优形式（Depth > OCC）。三层递进叙事。\n  **贡献强度: 最强**（方法+机制+实证，且有清晰的 practical recommendation：用 depth 不用 BEV）。\n  **⚠️ 此路径依赖 3-seed Random < OCC，当前 2-seed 数据不支持。**\n\n### Path Evidence Mapping & Weakness Analysis (数据无关，提前准备)\n\n| Path | 已有强证据 | 需要数据确认 | 主要 weakness | 审稿人最可能攻击点 |\n|------|-----------|-------------|-------------|------------------|\n| **A** (Depth>Random>OCC) | Detach 最差(梯度流必要) | Depth CAR > Random CAR (4-seed) | 仅一个 benchmark (SafeLIBERO) + 一个 VLA (OpenVLA-OFT) | \"depth 效果是否 architecture-specific?\" → 需 2nd VLA 或 2nd benchmark 补 |\n| **B** (Depth≈Random≈OCC) | Random≈OCC (2-seed初步); Detach最差 | Depth CAR ≈ Random/OCC (4-seed); 3-seed确认Random≈OCC | \"为什么梯度流有效\"缺机制解释(不只是实验现象) | \"这只是 multi-task regularization 的已知现象?\" → 需要与 MTL 文献对比 + VLA-specific 解释 |\n| **C** (Depth&lt;Vanilla) | Detach最差 | Depth CAR < Vanilla (4-seed) | 无 positive method contribution | \"那该用什么辅助任务?\" → 需要 constructive recommendation, 不能只是 negative |\n| **D** (Depth>OCC>Random) | Detach最差 | 3-seed OCC>Random 翻转 + Depth>OCC | 依赖 0.9pp 翻转(概率未知) | 同 Path A 的 generalization concern |\n\n**所有路径共通 weakness**:\n1. Single VLA architecture (OpenVLA-OFT) — RC4, 所有路径都需要在 Limitations 承认\n2. Single benchmark ecosystem (SafeLIBERO) — RC5, 加 LIBERO-Goal 可缓解\n3. 训练成本 ~13h/run 限制了 seed 数量，hard-task CAR 方差大 — RC6\n4. Ceiling effect: 7/10 tasks vanilla CAR=100%, 改善空间集中在 T3/T5/T6 三个 hard tasks\n\n**Path B 特有的额外准备**（概率最高 40-50%，需提前做）:\n- 文献调研: multi-task learning regularization in fine-tuning（MTL 社区已有大量工作）\n- 差异化论证: \"VLA fine-tuning 中辅助任务梯度流的 safety 效应\"是 VLA-specific 发现，不是 MTL 的简单重复\n- Discussion 预写: \"why gradient flow regularization improves collision avoidance specifically\"\n  假说 1: 防止 vision encoder 过拟合到 action prediction → 保留更通用的空间特征\n  假说 2: 辅助任务 loss landscape 改善优化轨迹（引 sharpness-aware minimization 类比）\n  假说 3: gradient diversity 防止 LoRA adapter 退化\n\n### Claim 5 (Extension, if Option C): OCC-CBF Double Defense\nOcc-aware representation feeds occupancy-conditioned CBF → implicit + explicit safety 叠加。\n\n**Evidence needed**: OCC-CBF proof-of-concept eval\n**Status**: Planned (post-MVP, ~30 GPU-hours, eval only)\n**Dependency**: Claim 1 must pass first\n\n## Anticipated Reviewer Concerns\n\n### RC1 [CRITICAL]: Collision Detection Metric Validity\n**Attack**: \"How is your collision metric defined? Is threshold=0.001 scientifically justified?\"\n**Defense**: 我们使用 SafeLIBERO 原始定义（VLSA-AEGIS L367-372）: L1 displacement, threshold=0.001,\nbody_xpos。已通过代码级验证对齐。✅ RESOLVED\n\n### RC2 [HIGH]: \"Why Not Just Use CBF?\"\n**Attack**: AEGIS CBF 达到 +59.16% CAR，如果 occ supervision 只有 +5-10%，为什么不直接加 CBF？\n**Defense**:\n- Implicit safety 零推理开销（CBF 需要 QP solver）\n- Occ + CBF 可叠加（OCC-CBF）→ 双重防线优于单一方案\n- **需要**: OCC-CBF proof-of-concept 展示叠加效果\n\n### RC3 [HIGH]: Depth Ablation 是 Existential Risk\n**Attack**: \"Depth supervision 效果相当吗？\"\n**Defense**: 取决于实验结果。预备两条叙事线:\n- Path A (occ >> depth): Occupancy 的 allocentric + boundary 特性是关键\n- Path B (occ ≈ depth): 发现 3D supervision 普遍提升 safety，转 Option B framing\n\n### RC4 [MEDIUM]: Single VLA Architecture\n**Attack**: \"这是 OpenVLA-OFT 的特性还是 occupancy 的功劳？\"\n**Defense**:\n- MVP 阶段接受此限制（AAAI scope）\n- Post-MVP 考虑 Diffusion Policy 作为第二架构（~60h）\n- SmolVLA 2×2 sanity check（IDEA_BRIEF 原设计）\n- Limitations 中显式承认\n\n### RC5 [MEDIUM]: Single Benchmark Ecosystem\n**Attack**: \"LIBERO 桌面操作的 safety 意义有限\"\n**Defense**:\n- LIBERO 是 VLA 社区标准 benchmark\n- SafeLIBERO 是唯一公开的 VLA collision benchmark\n- 添加第 2 suite (LIBERO-Goal/Object) 增加泛化证据\n- Limitations 中限定为 \"tabletop manipulation\"\n\n### RC6 [LOW]: n=3 Statistical Power\n**Attack**: \"3 seeds 的 paired t-test power 很低\"\n**Defense**: 报告 Cohen's d 和 95% CI，不完全依赖 p-value。\n如果 effect size 大（CAR 差距 >10pp），n=3 也能显著。\n\n## Framing Risk Ranking (D017 更新, 2026-05-22)\n> 注: 以下均为 framing pivot risk（需换叙事但论文仍可写），非 paper-killing risk。\n> 真正的 existential risk: 3+ seed 后梯度流正则化效应消失（所有条件收敛到 baseline），或 Detach 3rd seed 翻转。\n\n| 排名 | 风险 | 概率 | 应对 |\n|------|------|------|------|\n| **1** | Depth ≈ Random ≈ OCC（空间内容完全无用） | 40-50% | 论文转为纯机制分析：\"gradient flow regularization for VLA safety\"。贡献足够但需要强 ablation 叙事 |\n| **2** | 高 seed 方差致条件间差异不显著 | 25-30% | 已有 4 seed depth；追加 3rd seed random/detach 中；bootstrap CI |\n| **3** | Depth 结果异常（&lt;Vanilla 或 >>Random） | 15-20% | Path C framing（差异化影响分析）或代码 bug 排查 |\n| **4** | OCC-CBF 无法按时完成 | 40-50% | Option B 不依赖 CBF |\n| ~~5~~ | ~~Detach 无效~~ | ~~N/A~~ | ✅ 已确认 Detach 最差，Claim 2 成立 |\n| ~~6~~ | ~~CAR 提升 <5pp~~ | ~~N/A~~ | ✅ OCC +1.7pp（边际），但 Random +2.6pp → 梯度流正则化效应 confirmed |\n\n**已解决的风险**: Detach 结果明确（0.745 最差）；CAR 提升虽小但机制清晰（梯度流 > 空间内容）。\n**新增风险**: Depth 是当前最大不确定性——决定论文是\"空间信号形式对比\"还是\"纯梯度流正则化分析\"。\n\n## Cutoff 实验设计（新增）\nocc_loss_cutoff_step=35000：前 35K 步用 OCC supervision（获取空间感知），后 15K 步关闭 OCC loss（让 action loss 主导）。\n**假设**: 如果 cutoff > full OCC → 证明 late-stage OCC 干扰 action prediction（课程学习论证）。\n**Status**: 2 seeds 训练中（westd-34685 cuda:0/3），ETA May 23 ~20:00 UTC。\n\n## Story Skeleton\n\n1. **Opening**: VLAs 在桌面操作上接近人类 success rate，但在空间受限的场景中碰撞率极高。\n   核心矛盾：**任务成功 ≠ 行为安全**。\n   (Evidence: vanilla TSR=92% overall, but on physically challenging tasks collision rate reaches 53-92%.\n   T3: TSR=100% but CAR=32.5%; T5: TSR=55%, CAR=7.5%)\n\n2. **Diagnosis**: VLA vision encoder 是 2D pretrained，缺乏 3D spatial structure 理解。\n   能完成任务是因为学会了语义-动作映射，但从未理解物体 3D 边界。\n\n3. **Gap**: 安全-VLA 文献（CBF/RL）与空间-VLA 文献（depth/point cloud/occ）完全隔离。\n   15+ 空间方法从未测 safety；4+ 安全方法从未用空间表征进步。\n   **No one has connected the two.**\n\n4. **Insight (AD analogy, 克制使用)**: 自动驾驶用 occupancy map 从 2D 感知跨越到 3D 安全决策。\n   Robot manipulation 面对同样问题。BEV occupancy 天然编码 workspace 中的 object boundary。\n\n5. **Method**: Auxiliary BEV occ supervision during fine-tuning → zero inference cost →\n   implicit collision avoidance emerges without explicit safety training.\n\n6. **Ablation story (D017 修正)**: gradient flow 是必要条件（detach 最差）；\n   random labels 也有效（surprising! → 梯度流正则化是主导机制）；\n   depth 对比揭示 egocentric vs allocentric 空间信号的差异（待数据）。\n\n7. **Extension (Option C)**: Occ-aware representation + OCC-CBF → 双重防线（implicit + explicit safety）。\n\n## Sections Pre-writable (不依赖实验结果)\n\n- **Related Work**: 11+ 篇论文 landscape 已明确，gap 定位清晰\n- **Method §3a-3b**: Occ head 架构、training pipeline 已实现\n- **Experiments §4a Setup**: Benchmark 描述、evaluation protocol、baseline 列表\n- **Intro 前 2 段**: 问题设定 + 文献 gap\n\n## Post-MVP Experiment Roadmap (by priority)\n\n| Priority | Experiment | GPU-hours | Claim | Notes |\n|----------|-----------|-----------|-------|-------|\n| P0 | 5-condition ablation (D005) | ~120h | C2-C4 | occ_detach, depth, random_occ |\n| P0 | 2nd suite (LIBERO-Goal) | ~50h eval | RC5 | 泛化 |\n| P0 | OCC-CBF PoC | ~30h eval | C5 | Option C 核心 |\n| P1 | Predicted occ vs GT occ | ~50h | 实用性 | 回应 \"需要 sim GT\" |\n| P2 | 2nd architecture (Diffusion Policy) | ~60h | RC4 | 泛化 |\n| P2 | Level I + II 对比 | ~20h eval | 难度 sensitivity | |\n\nTotal: ~330h。8 卡 × 10 周 ≈ 1340h 预算，MVP ~170h + post-MVP ~330h = ~500h，宽裕。\n",
      "numLines": 415,
      "startLine": 1,
      "totalLines": 415
    }
  }
}
````

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_019MTbQAu2VMJji5Qi6Propn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "e99a12f3-6a74-46c3-bdbc-0f05c03d7727",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

_source line 10 · 2026-05-22T18:22:41.850Z_

<details><summary>↩ Tool result · `toolu_019MTbQAu2VMJji5Qi6Propn`</summary>

```text
1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	@article{yu2026safenightvla,
33	  author    = {Yu and others},
34	  title     = {{Safe-Night VLA}: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation},
35	  journal   = {arXiv preprint arXiv:2603.05754},
36	  year      = {2026},
37	  note      = {arXiv:2603.05754}
38	}
39	
40	@article{li2026vlasafety,
41	  author    = {Li and others},
42	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
43	  journal   = {arXiv preprint arXiv:2604.23775},
44	  year      = {2026},
45	  note      = {arXiv:2604.23775}
46	}
47	
48	% ============================================================
49	% Safety Mechanisms (barrier functions / occupancy-based safety)
50	% ============================================================
51	
52	@inproceedings{morton2025oscbf,
53	  author    = {Daniel Morton and Marco Pavone},
54	  title     = {Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions},
55	  booktitle = {IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
56	  year      = {2025},
57	  note      = {arXiv:2503.06736}
58	}
59	
60	@article{raja2024ogmcbf,
61	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
62	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
63	  journal   = {arXiv preprint arXiv:2405.10703},
64	  year      = {2024},
65	  note      = {arXiv:2405.10703}
66	}
67	
68	@article{kwon2026learningnudge,
69	  author    = {Kwon and others},
70	  title     = {Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter},
71	  journal   = {arXiv preprint arXiv:2601.02686},
72	  year      = {2026},
73	  note      = {arXiv:2601.02686}
74	}
75	
76	@article{long2025neuralcsbf,
77	  author    = {Long and others},
78	  title     = {Neural Configuration-Space Barriers for Manipulation Planning and Control},
79	  journal   = {arXiv preprint arXiv:2503.04929},
80	  year      = {2025},
81	  note      = {arXiv:2503.04929}
82	}
83	
84	% ============================================================
85	% Spatial VLA (3D representation for VLA)
86	% ============================================================
87	
88	@article{liu2025occvla,
89	  author    = {Ruixun Liu and others},
90	  title     = {{OccVLA}: Vision-Language-Action Model with Implicit 3D Occupancy Supervision},
91	  journal   = {arXiv preprint arXiv:2509.05578},
92	  year      = {2025},
93	  note      = {arXiv:2509.05578}
94	}
95	
96	@inproceedings{li2026spatialforcing,
97	  author    = {Fuhao Li and others},
98	  title     = {Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},
99	  booktitle = {International Conference on Learning Representations (ICLR)},
100	  year      = {2026},
101	  note      = {arXiv:2510.12276}
102	}
103	
104	@article{yuan2025depthvla,
105	  author    = {Tianyuan Yuan and others},
106	  title     = {{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},
107	  journal   = {arXiv preprint arXiv:2510.13375},
108	  year      = {2025},
109	  note      = {arXiv:2510.13375}
110	}
111	
112	@article{chen2026gstvla,
113	  author    = {Chen and others},
114	  title     = {{GST-VLA}: Structured {Gaussian} Spatial Tokens for 3D Depth-Aware {VLA} Models},
115	  journal   = {arXiv preprint arXiv:2603.09079},
116	  year      = {2026},
117	  note      = {arXiv:2603.09079}
118	}
119	
120	@inproceedings{wu2025spatialvla,
121	  author    = {Wu and others},
122	  title     = {{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},
123	  booktitle = {Robotics: Science and Systems (RSS)},
124	  year      = {2025},
125	  note      = {arXiv:2501.15830}
126	}
127	
128	@article{li2025qdepthvla,
129	  author    = {Li and others},
130	  title     = {{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},
131	  journal   = {arXiv preprint arXiv:2510.14836},
132	  year      = {2025},
133	  note      = {arXiv:2510.14836}
134	}
135	
136	@article{abouzeid2025geoaware,
137	  author    = {Abouzeid and others},
138	  title     = {{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},
139	  journal   = {arXiv preprint arXiv:2509.14117},
140	  year      = {2025},
141	  note      = {arXiv:2509.14117}
142	}
143	
144	@article{rao2026augvla3d,
145	  author    = {Zhifeng Rao and others},
146	  title     = {{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},
147	  journal   = {arXiv preprint arXiv:2602.10698},
148	  year      = {2026},
149	  note      = {arXiv:2602.10698}
150	}
151	
152	@article{lin2025evo0,
153	  author    = {Lin and others},
154	  title     = {{Evo-0}: Vision-Language-Action Model with Implicit Spatial Understanding},
155	  journal   = {arXiv preprint arXiv:2507.00416},
156	  year      = {2025},
157	  note      = {arXiv:2507.00416}
158	}
159	
160	@article{tu2026sgvla,
161	  author    = {Tu and others},
162	  title     = {{SG-VLA}: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation},
163	  journal   = {arXiv preprint arXiv:2603.22760},
164	  year      = {2026},
165	  note      = {arXiv:2603.22760}
166	}
167	
168	@article{xiao2026stemvla,
169	  author    = {Xiao and others},
170	  title     = {{StemVLA}: An Open-Source {VLA} with Future 3D Spatial Geometry Knowledge and 4D Historical Representation},
171	  journal   = {arXiv preprint arXiv:2602.23721},
172	  year      = {2026},
173	  note      = {arXiv:2602.23721}
174	}
175	
176	@article{bhat20253dcavla,
177	  author    = {Bhat and others},
178	  title     = {{3D-CAVLA}: Leveraging Depth and 3D Context to Generalize {VLA} for Unseen Tasks},
179	  journal   = {arXiv preprint arXiv:2505.05800},
180	  year      = {2025},
181	  note      = {arXiv:2505.05800}
182	}
183	
184	@article{wu2026stvla,
185	  author    = {Wu and others},
186	  title     = {{ST-VLA}: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation},
187	  journal   = {arXiv preprint arXiv:2603.13788},
188	  year      = {2026},
189	  note      = {arXiv:2603.13788}
190	}
191	
192	@article{li2026corridorvla,
193	  author    = {Li and others},
194	  title     = {{CorridorVLA}: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors},
195	  journal   = {arXiv preprint arXiv:2604.21241},
196	  year      = {2026},
197	  note      = {arXiv:2604.21241}
198	}
199	
200	@article{sun2025geovla,
201	  author    = {Sun and others},
202	  title     = {{GeoVLA}: Empowering 3D Representations in Vision-Language-Action Models},
203	  journal   = {arXiv preprint arXiv:2508.09071},
204	  year      = {2025},
205	  note      = {arXiv:2508.09071}
206	}
207	
208	@article{li2025pointvla,
209	  author    = {Li and others},
210	  title     = {{PointVLA}: Injecting the 3D World into Vision-Language-Action Models},
211	  journal   = {arXiv preprint arXiv:2503.07511},
212	  year      = {2025},
213	  note      = {arXiv:2503.07511}
214	}
215	
216	@article{pan2026savla,
217	  author    = {Pan and others},
218	  title     = {{SA-VLA}: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning},
219	  journal   = {arXiv preprint arXiv:2602.00743},
220	  year      = {2026},
221	  note      = {arXiv:2602.00743}
222	}
223	
224	% ============================================================
225	% 3D Perception (occupancy / BEV / depth)
226	% ============================================================
227	
228	@inproceedings{li2022bevformer,
229	  author    = {Zhiqi Li and Wenhai Wang and Hongyang Li and Enze Xie and Chonghao Sima and Tong Lu and Yu Qiao and Jifeng Dai},
230	  title     = {{BEVFormer}: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers},
231	  booktitle = {European Conference on Computer Vision (ECCV)},
232	  year      = {2022},
233	  note      = {arXiv:2203.17270}
234	}
235	
236	@inproceedings{sima2023occnet,
237	  author    = {Chonghao Sima and Wenwen Tong and Tai Wang and Li Chen and Silei Wu and Hanming Deng and Yi Gu and Lewei Lu and Ping Luo and Dahua Lin and Hongyang Li},
238	  title     = {Scene as Occupancy},
239	  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
240	  year      = {2023},
241	  note      = {arXiv:2306.02851}
242	}
243	
244	@inproceedings{tian2023occ3d,
245	  author    = {Xiaoyu Tian and Tao Jiang and Longfei Yun and Yucheng Mao and Huitong Yang and Yue Wang and Yilun Wang and Hang Zhao},
246	  title     = {{Occ3D}: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving},
247	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
248	  year      = {2023},
249	  note      = {arXiv:2304.14365}
250	}
251	
252	@article{ranftl2022midas,
253	  author    = {Ren\'{e} Ranftl and Katrin Lasinger and David Hafner and Alexey Schepelmann and Vladlen Koltun},
254	  title     = {Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer},
255	  journal   = {IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
256	  volume    = {44},
257	  number    = {3},
258	  pages     = {1623--1637},
259	  year      = {2022},
260	  note      = {arXiv:1907.01341}
261	}
262	
263	@inproceedings{yang2024depthanything,
264	  author    = {Lihe Yang and Bingyi Kang and Zilong Huang and Xiaogang Xu and Jiashi Feng and Hengshuang Zhao},
265	  title     = {Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data},
266	  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
267	  year      = {2024},
268	  note      = {arXiv:2401.10891}
269	}
270	
271	% ============================================================
272	% Foundation Models / VLA Infrastructure
273	% ============================================================
274	
275	@article{kim2024openvla,
276	  author    = {Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
277	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
278	  journal   = {arXiv preprint arXiv:2406.09246},
279	  year      = {2024},
280	  note      = {arXiv:2406.09246}
281	}
282	
283	@article{kim2025oft,
284	  author    = {Moo Jin Kim and others},
285	  title     = {Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},
286	  journal   = {arXiv preprint arXiv:2502.19645},
287	  year      = {2025},
288	  note      = {arXiv:2502.19645}
289	}
290	
291	@inproceedings{brohan2023rt2,
292	  author    = {Anthony Brohan and Noah Brown and Justice Carbajal and others},
293	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
294	  booktitle = {Conference on Robot Learning (CoRL)},
295	  year      = {2023},
296	  note      = {arXiv:2307.15818}
297	}
298	
299	@article{oquab2024dinov2,
300	  author    = {Maxime Oquab and Timoth\'{e}e Darcet and Th\'{e}o Moutakanni and Huy Vo and Marc Szafraniec and Vasil Khalidov and Pierre Fernandez and Daniel Haziza and Francisco Massa and Alaaeldin El-Nouby and Mahmoud Assran and Nicolas Ballas and Wojciech Galuba and Russell Howes and Po-Yao Huang and Shang-Wen Li and Ishan Misra and Michael Rabbat and Vasu Sharma and Gabriel Synnaeve and Hu Xu and Herv\'{e} J\'{e}gou and Julien Mairal and Patrick Labatut and Armand Joulin and Piotr Bojanowski},
301	  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},
302	  journal   = {Transactions on Machine Learning Research (TMLR)},
303	  year      = {2024},
304	  note      = {arXiv:2304.07193}
305	}
306	
307	@inproceedings{zhai2023siglip,
308	  author    = {Xiaohua Zhai and Basil Mustafa and Alexander Kolesnikov and Lucas Beyer},
309	  title     = {Sigmoid Loss for Language Image Pre-Training},
310	  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
311	  year      = {2023},
312	  note      = {arXiv:2303.15343}
313	}
314	
315	@article{ma2026vlanext,
316	  author    = {Ma and others},
317	  title     = {{VLANeXt}: Recipes for Building Strong {VLA} Models},
318	  journal   = {arXiv preprint arXiv:2602.18532},
319	  year      = {2026},
320	  note      = {arXiv:2602.18532}
321	}
322	
323	@article{shukor2025smolvla,
324	  author    = {Shukor and others},
325	  title     = {{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
326	  journal   = {arXiv preprint arXiv:2506.01844},
327	  year      = {2025},
328	  note      = {arXiv:2506.01844}
329	}
330	
331	@article{choi2026vlaeval,
332	  author    = {Choi and others},
333	  title     = {vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models},
334	  journal   = {arXiv preprint arXiv:2603.13966},
335	  year      = {2026},
336	  note      = {arXiv:2603.13966}
337	}
338	
339	% ============================================================
340	% Benchmarks
341	% ============================================================
342	
343	@inproceedings{liu2023libero,
344	  author    = {Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
345	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
346	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
347	  year      = {2023},
348	  note      = {arXiv:2306.03310}
349	}
350	
351	% ============================================================
352	% Multi-Task Learning / Regularization
353	% ============================================================
354	
355	@article{caruana1997multitask,
356	  author    = {Rich Caruana},
357	  title     = {Multitask Learning},
358	  journal   = {Machine Learning},
359	  volume    = {28},
360	  number    = {1},
361	  pages     = {41--75},
362	  year      = {1997}
363	}
364	
365	@article{ruder2017overview,
366	  author    = {Sebastian Ruder},
367	  title     = {An Overview of Multi-Task Learning in Deep Neural Networks},
368	  journal   = {arXiv preprint arXiv:1706.05098},
369	  year      = {2017},
370	  note      = {arXiv:1706.05098}
371	}
372	
373	@inproceedings{lippl2024implicit,
374	  author    = {Samuel Lippl and Jack W. Lindsey},
375	  title     = {Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks},
376	  booktitle = {International Conference on Learning Representations (ICLR)},
377	  year      = {2024},
378	  note      = {arXiv:2310.02396}
379	}
380	
381	@inproceedings{foret2021sam,
382	  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},
383	  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},
384	  booktitle = {International Conference on Learning Representations (ICLR)},
385	  year      = {2021},
386	  note      = {arXiv:2010.01412}
387	}
388	
389	% ============================================================
390	% Parameter-Efficient Fine-Tuning
391	% ============================================================
392	
393	@inproceedings{hu2022lora,
394	  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},
395	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
396	  booktitle = {International Conference on Learning Representations (ICLR)},
397	  year      = {2022},
398	  note      = {arXiv:2106.09685}
399	}
400	
401	% ============================================================
402	% Loss Functions
403	% ============================================================
404	
405	@inproceedings{lin2017focal,
406	  author    = {Tsung-Yi Lin and Priya Goyal and Ross Girshick and Kaiming He and Piotr Doll\'{a}r},
407	  title     = {Focal Loss for Dense Object Detection},
408	  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
409	  year      = {2017},
410	  note      = {arXiv:1708.02002}
411	}
412	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "3a0d53d3-ac16-4ab3-b4a8-59f027d41931",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
      "content": "% References for OccSafe-VLA\n% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}\n\n% ============================================================\n% VLA Safety\n% ============================================================\n\n@article{hu2025vlsa,\n  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},\n  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  journal   = {arXiv preprint arXiv:2512.11891},\n  year      = {2025},\n  note      = {arXiv:2512.11891}\n}\n\n@inproceedings{zhang2025safevla,\n  author    = {Borong Zhang and others},\n  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  note      = {Spotlight. arXiv:2503.03480}\n}\n\n@article{zhai2026cofreevla,\n  author    = {Xuanran Zhai and others},\n  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},\n  journal   = {arXiv preprint arXiv:2601.21712},\n  year      = {2026},\n  note      = {arXiv:2601.21712}\n}\n\n@article{yu2026safenightvla,\n  author    = {Yu and others},\n  title     = {{Safe-Night VLA}: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation},\n  journal   = {arXiv preprint arXiv:2603.05754},\n  year      = {2026},\n  note      = {arXiv:2603.05754}\n}\n\n@article{li2026vlasafety,\n  author    = {Li and others},\n  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  journal   = {arXiv preprint arXiv:2604.23775},\n  year      = {2026},\n  note      = {arXiv:2604.23775}\n}\n\n% ============================================================\n% Safety Mechanisms (barrier functions / occupancy-based safety)\n% ============================================================\n\n@inproceedings{morton2025oscbf,\n  author    = {Daniel Morton and Marco Pavone},\n  title     = {Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions},\n  booktitle = {IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year      = {2025},\n  note      = {arXiv:2503.06736}\n}\n\n@article{raja2024ogmcbf,\n  author    = {Golnaz Raja and Teemu M{\\\"o}kk{\\\"o}nen and Reza Ghabcheloo},\n  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},\n  journal   = {arXiv preprint arXiv:2405.10703},\n  year      = {2024},\n  note      = {arXiv:2405.10703}\n}\n\n@article{kwon2026learningnudge,\n  author    = {Kwon and others},\n  title     = {Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter},\n  journal   = {arXiv preprint arXiv:2601.02686},\n  year      = {2026},\n  note      = {arXiv:2601.02686}\n}\n\n@article{long2025neuralcsbf,\n  author    = {Long and others},\n  title     = {Neural Configuration-Space Barriers for Manipulation Planning and Control},\n  journal   = {arXiv preprint arXiv:2503.04929},\n  year      = {2025},\n  note      = {arXiv:2503.04929}\n}\n\n% ============================================================\n% Spatial VLA (3D representation for VLA)\n% ============================================================\n\n@article{liu2025occvla,\n  author    = {Ruixun Liu and others},\n  title     = {{OccVLA}: Vision-Language-Action Model with Implicit 3D Occupancy Supervision},\n  journal   = {arXiv preprint arXiv:2509.05578},\n  year      = {2025},\n  note      = {arXiv:2509.05578}\n}\n\n@inproceedings{li2026spatialforcing,\n  author    = {Fuhao Li and others},\n  title     = {Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2026},\n  note      = {arXiv:2510.12276}\n}\n\n@article{yuan2025depthvla,\n  author    = {Tianyuan Yuan and others},\n  title     = {{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  journal   = {arXiv preprint arXiv:2510.13375},\n  year      = {2025},\n  note      = {arXiv:2510.13375}\n}\n\n@article{chen2026gstvla,\n  author    = {Chen and others},\n  title     = {{GST-VLA}: Structured {Gaussian} Spatial Tokens for 3D Depth-Aware {VLA} Models},\n  journal   = {arXiv preprint arXiv:2603.09079},\n  year      = {2026},\n  note      = {arXiv:2603.09079}\n}\n\n@inproceedings{wu2025spatialvla,\n  author    = {Wu and others},\n  title     = {{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},\n  booktitle = {Robotics: Science and Systems (RSS)},\n  year      = {2025},\n  note      = {arXiv:2501.15830}\n}\n\n@article{li2025qdepthvla,\n  author    = {Li and others},\n  title     = {{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2510.14836},\n  year      = {2025},\n  note      = {arXiv:2510.14836}\n}\n\n@article{abouzeid2025geoaware,\n  author    = {Abouzeid and others},\n  title     = {{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},\n  journal   = {arXiv preprint arXiv:2509.14117},\n  year      = {2025},\n  note      = {arXiv:2509.14117}\n}\n\n@article{rao2026augvla3d,\n  author    = {Zhifeng Rao and others},\n  title     = {{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2602.10698},\n  year      = {2026},\n  note      = {arXiv:2602.10698}\n}\n\n@article{lin2025evo0,\n  author    = {Lin and others},\n  title     = {{Evo-0}: Vision-Language-Action Model with Implicit Spatial Understanding},\n  journal   = {arXiv preprint arXiv:2507.00416},\n  year      = {2025},\n  note      = {arXiv:2507.00416}\n}\n\n@article{tu2026sgvla,\n  author    = {Tu and others},\n  title     = {{SG-VLA}: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation},\n  journal   = {arXiv preprint arXiv:2603.22760},\n  year      = {2026},\n  note      = {arXiv:2603.22760}\n}\n\n@article{xiao2026stemvla,\n  author    = {Xiao and others},\n  title     = {{StemVLA}: An Open-Source {VLA} with Future 3D Spatial Geometry Knowledge and 4D Historical Representation},\n  journal   = {arXiv preprint arXiv:2602.23721},\n  year      = {2026},\n  note      = {arXiv:2602.23721}\n}\n\n@article{bhat20253dcavla,\n  author    = {Bhat and others},\n  title     = {{3D-CAVLA}: Leveraging Depth and 3D Context to Generalize {VLA} for Unseen Tasks},\n  journal   = {arXiv preprint arXiv:2505.05800},\n  year      = {2025},\n  note      = {arXiv:2505.05800}\n}\n\n@article{wu2026stvla,\n  author    = {Wu and others},\n  title     = {{ST-VLA}: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation},\n  journal   = {arXiv preprint arXiv:2603.13788},\n  year      = {2026},\n  note      = {arXiv:2603.13788}\n}\n\n@article{li2026corridorvla,\n  author    = {Li and others},\n  title     = {{CorridorVLA}: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors},\n  journal   = {arXiv preprint arXiv:2604.21241},\n  year      = {2026},\n  note      = {arXiv:2604.21241}\n}\n\n@article{sun2025geovla,\n  author    = {Sun and others},\n  title     = {{GeoVLA}: Empowering 3D Representations in Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2508.09071},\n  year      = {2025},\n  note      = {arXiv:2508.09071}\n}\n\n@article{li2025pointvla,\n  author    = {Li and others},\n  title     = {{PointVLA}: Injecting the 3D World into Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2503.07511},\n  year      = {2025},\n  note      = {arXiv:2503.07511}\n}\n\n@article{pan2026savla,\n  author    = {Pan and others},\n  title     = {{SA-VLA}: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning},\n  journal   = {arXiv preprint arXiv:2602.00743},\n  year      = {2026},\n  note      = {arXiv:2602.00743}\n}\n\n% ============================================================\n% 3D Perception (occupancy / BEV / depth)\n% ============================================================\n\n@inproceedings{li2022bevformer,\n  author    = {Zhiqi Li and Wenhai Wang and Hongyang Li and Enze Xie and Chonghao Sima and Tong Lu and Yu Qiao and Jifeng Dai},\n  title     = {{BEVFormer}: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers},\n  booktitle = {European Conference on Computer Vision (ECCV)},\n  year      = {2022},\n  note      = {arXiv:2203.17270}\n}\n\n@inproceedings{sima2023occnet,\n  author    = {Chonghao Sima and Wenwen Tong and Tai Wang and Li Chen and Silei Wu and Hanming Deng and Yi Gu and Lewei Lu and Ping Luo and Dahua Lin and Hongyang Li},\n  title     = {Scene as Occupancy},\n  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n  note      = {arXiv:2306.02851}\n}\n\n@inproceedings{tian2023occ3d,\n  author    = {Xiaoyu Tian and Tao Jiang and Longfei Yun and Yucheng Mao and Huitong Yang and Yue Wang and Yilun Wang and Hang Zhao},\n  title     = {{Occ3D}: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n  note      = {arXiv:2304.14365}\n}\n\n@article{ranftl2022midas,\n  author    = {Ren\\'{e} Ranftl and Katrin Lasinger and David Hafner and Alexey Schepelmann and Vladlen Koltun},\n  title     = {Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer},\n  journal   = {IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},\n  volume    = {44},\n  number    = {3},\n  pages     = {1623--1637},\n  year      = {2022},\n  note      = {arXiv:1907.01341}\n}\n\n@inproceedings{yang2024depthanything,\n  author    = {Lihe Yang and Bingyi Kang and Zilong Huang and Xiaogang Xu and Jiashi Feng and Hengshuang Zhao},\n  title     = {Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data},\n  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year      = {2024},\n  note      = {arXiv:2401.10891}\n}\n\n% ============================================================\n% Foundation Models / VLA Infrastructure\n% ============================================================\n\n@article{kim2024openvla,\n  author    = {Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n  note      = {arXiv:2406.09246}\n}\n\n@article{kim2025oft,\n  author    = {Moo Jin Kim and others},\n  title     = {Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  journal   = {arXiv preprint arXiv:2502.19645},\n  year      = {2025},\n  note      = {arXiv:2502.19645}\n}\n\n@inproceedings{brohan2023rt2,\n  author    = {Anthony Brohan and Noah Brown and Justice Carbajal and others},\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  booktitle = {Conference on Robot Learning (CoRL)},\n  year      = {2023},\n  note      = {arXiv:2307.15818}\n}\n\n@article{oquab2024dinov2,\n  author    = {Maxime Oquab and Timoth\\'{e}e Darcet and Th\\'{e}o Moutakanni and Huy Vo and Marc Szafraniec and Vasil Khalidov and Pierre Fernandez and Daniel Haziza and Francisco Massa and Alaaeldin El-Nouby and Mahmoud Assran and Nicolas Ballas and Wojciech Galuba and Russell Howes and Po-Yao Huang and Shang-Wen Li and Ishan Misra and Michael Rabbat and Vasu Sharma and Gabriel Synnaeve and Hu Xu and Herv\\'{e} J\\'{e}gou and Julien Mairal and Patrick Labatut and Armand Joulin and Piotr Bojanowski},\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n  note      = {arXiv:2304.07193}\n}\n\n@inproceedings{zhai2023siglip,\n  author    = {Xiaohua Zhai and Basil Mustafa and Alexander Kolesnikov and Lucas Beyer},\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n  note      = {arXiv:2303.15343}\n}\n\n@article{ma2026vlanext,\n  author    = {Ma and others},\n  title     = {{VLANeXt}: Recipes for Building Strong {VLA} Models},\n  journal   = {arXiv preprint arXiv:2602.18532},\n  year      = {2026},\n  note      = {arXiv:2602.18532}\n}\n\n@article{shukor2025smolvla,\n  author    = {Shukor and others},\n  title     = {{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  journal   = {arXiv preprint arXiv:2506.01844},\n  year      = {2025},\n  note      = {arXiv:2506.01844}\n}\n\n@article{choi2026vlaeval,\n  author    = {Choi and others},\n  title     = {vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2603.13966},\n  year      = {2026},\n  note      = {arXiv:2603.13966}\n}\n\n% ============================================================\n% Benchmarks\n% ============================================================\n\n@inproceedings{liu2023libero,\n  author    = {Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n  note      = {arXiv:2306.03310}\n}\n\n% ============================================================\n% Multi-Task Learning / Regularization\n% ============================================================\n\n@article{caruana1997multitask,\n  author    = {Rich Caruana},\n  title     = {Multitask Learning},\n  journal   = {Machine Learning},\n  volume    = {28},\n  number    = {1},\n  pages     = {41--75},\n  year      = {1997}\n}\n\n@article{ruder2017overview,\n  author    = {Sebastian Ruder},\n  title     = {An Overview of Multi-Task Learning in Deep Neural Networks},\n  journal   = {arXiv preprint arXiv:1706.05098},\n  year      = {2017},\n  note      = {arXiv:1706.05098}\n}\n\n@inproceedings{lippl2024implicit,\n  author    = {Samuel Lippl and Jack W. Lindsey},\n  title     = {Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  note      = {arXiv:2310.02396}\n}\n\n@inproceedings{foret2021sam,\n  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},\n  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n  note      = {arXiv:2010.01412}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n  note      = {arXiv:2106.09685}\n}\n\n% ============================================================\n% Loss Functions\n% ============================================================\n\n@inproceedings{lin2017focal,\n  author    = {Tsung-Yi Lin and Priya Goyal and Ross Girshick and Kaiming He and Piotr Doll\\'{a}r},\n  title     = {Focal Loss for Dense Object Detection},\n  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year      = {2017},\n  note      = {arXiv:1708.02002}\n}\n",
      "numLines": 412,
      "startLine": 1,
      "totalLines": 412
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01M1eVs2U53HDEdzcFpdXJf8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "a03de557-9428-4c16-8eb7-747758a68a51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

_source line 12 · 2026-05-22T18:22:42.317Z_

<details><summary>↩ Tool result · `toolu_01M1eVs2U53HDEdzcFpdXJf8`</summary>

```text
1	
2	\section{Related Work}
3	
4	\subsection{Safety in Vision-Language-Action Models}
5	
6	Vision-language-action (VLA) models achieve high task success rates on manipulation benchmarks~\cite{kim2024openvla} % Kim et al., "OpenVLA: An Open-Source Vision-Language-Action Model", arXiv:2406.09246, 2024
7	\cite{brohan2023rt2} % Brohan et al., "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", arXiv:2307.15818, 2023
8	but remain prone to collisions when obstacles occupy the manipulation workspace. Two strategies have emerged to address this gap between task completion and behavioral safety.
9	
10	The first strategy applies runtime constraints to filter or adjust unsafe actions. The AEGIS framework~\cite{hu2025vlsa} % Hu et al., "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer", arXiv:2512.11891, 2025
11	adds a plug-and-play safety layer that identifies obstacles through a vision-language assessment module and enforces avoidance via a control barrier function (CBF) quadratic program, improving collision avoidance rate by 59.16 percentage points on SafeLIBERO, a benchmark of 32 safety-critical manipulation scenarios introduced in the same work. CoFreeVLA~\cite{zhai2026cofreevla} % Zhai et al., "CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation", arXiv:2601.21712, 2026
12	addresses a related problem in dual-arm settings by training a short-horizon collision risk estimator that gates risky commands and triggers recovery to safe configurations. Control barrier functions have also been applied directly to manipulation independently of VLAs. Morton and Pavone~\cite{morton2025oscbf} % Morton and Pavone, "Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions", IROS 2025, arXiv:2503.06736
13	formulate operational-space CBFs that scale to hundreds of simultaneous constraints at real-time control rates, and Raja et al.~\cite{raja2024ogmcbf} % Raja et al., "Safe Robot Control using Occupancy Grid Map-based Control Barrier Function (OGM-CBF)", arXiv:2405.10703, 2024
14	construct CBFs from occupancy grid maps, directly linking occupancy representations to explicit safety guarantees. These runtime approaches are effective but add computational overhead at inference time, and they require access to obstacle positions or perception modules that can provide them.
15	
16	The second strategy modifies the training objective to embed safety into the policy. SafeVLA~\cite{zhang2025safevla} % Zhang et al., "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning", NeurIPS 2025 Spotlight, arXiv:2503.03480
17	formulates VLA safety as a constrained Markov decision process and applies safe reinforcement learning, reducing safety violations by 83.58\% while maintaining task performance. This requires collecting unsafe trajectories and defining explicit cost functions for each type of violation, which limits scalability to new environments.
18	
19	Both strategies treat safety as a behavioral constraint problem, applied either to the action space at runtime or through reward shaping during training. Neither investigates whether the VLA's internal spatial representations contribute to or hinder collision avoidance. Our work addresses this gap: we modify the training signal through auxiliary spatial supervision and study how this changes safety outcomes, with zero inference-time cost and no need for explicit safety reward design.
20	
21	\subsection{3D Spatial Representations for Robot Learning}
22	
23	Bird's-eye-view and occupancy representations have become central to 3D perception in autonomous driving. BEVFormer~\cite{li2022bevformer} % Li et al., "BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers", ECCV 2022, arXiv:2203.17270
24	projects multi-camera features into a unified BEV grid via spatiotemporal transformers. Sima et al.~\cite{sima2023occnet} % Sima et al., "Scene as Occupancy", ICCV 2023, arXiv:2306.02851
25	represent entire scenes as dense 3D occupancy volumes, capturing irregular object shapes that bounding boxes cannot, and Occ3D~\cite{tian2023occ3d} % Tian et al., "Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving", NeurIPS 2023, arXiv:2304.14365
26	establishes a large-scale benchmark for vision-based occupancy prediction. More recently, OccVLA~\cite{liu2025occvla} % Liu et al., "OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision", arXiv:2509.05578, 2025
27	integrates occupancy prediction into a VLA for autonomous driving, treating occupancy tokens as an implicit spatial reasoning mechanism. These results establish that occupancy supervision improves 3D scene understanding, but they operate in the driving domain where the BEV frame naturally aligns with the planning task.
28	
29	For tabletop manipulation, the appropriate spatial reference frame is less obvious: the robot observes from an egocentric camera while objects sit on a planar workspace. Recent work brings 3D structure into manipulation VLAs through several mechanisms. Depth-based approaches fuse monocular depth predictions with visual features: DepthVLA~\cite{yuan2025depthvla} % Yuan et al., "DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning", arXiv:2510.13375, 2025
30	uses a mixture-of-transformers architecture to jointly decode actions and depth, reporting improved performance on tasks requiring precise spatial reasoning. AugVLA-3D~\cite{rao2026augvla3d} % Rao et al., "AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models", arXiv:2602.10698, 2026
31	augments 2D visual tokens with depth-derived 3D features through a geometry-aware module. These methods build on foundation models for monocular depth estimation, including MiDaS~\cite{ranftl2022midas} % Ranftl et al., "Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer", TPAMI 2022
32	and Depth Anything~\cite{yang2024depthanything} % Yang et al., "Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data", CVPR 2024, arXiv:2401.10891
33	, which have made metric or relative depth estimation accessible from single RGB inputs. Alignment-based approaches instead regularize internal representations: Spatial Forcing~\cite{li2026spatialforcing} % Li et al., "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model", ICLR 2026, arXiv:2510.12276
34	aligns VLA visual embeddings with features from pretrained 3D models, using depth probing experiments to confirm that spatial information transfers into the VLA's learned representations. SpatialVLA~\cite{wu2025spatialvla} % Wu et al., "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model", RSS 2025, arXiv:2501.15830
35	introduces ego-centric 3D position encoding to ground action predictions in workspace coordinates. Point cloud representations offer an alternative: PointVLA~\cite{li2025pointvla} % Li et al., "PointVLA: Injecting the 3D World into Vision-Language-Action Models", arXiv:2503.07511, 2025
36	compresses point clouds and injects them into underutilized transformer blocks. ST-VLA~\cite{wu2026stvla} % Wu et al., "ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation", arXiv:2603.13788, 2026
37	extends this line to 4D spatiotemporal representations by generating 3D trajectories from 2D guidance.
38	
39	These spatial methods consistently improve task success rates and generalization. However, none evaluates the impact of spatial representations on collision avoidance or other safety metrics. Whether improved 3D understanding translates to safer manipulation behavior remains an open question.
40	
41	\subsection{Auxiliary Tasks and Regularization in Fine-Tuning}
42	
43	Multi-task learning improves generalization by training on related objectives through a shared representation~\cite{caruana1997multitask} % Caruana, "Multitask Learning", Machine Learning 28:41-75, 1997
44	. Auxiliary tasks act as inductive biases that prevent the shared encoder from overfitting to the primary objective~\cite{ruder2017overview} % Ruder, "An Overview of Multi-Task Learning in Deep Neural Networks", arXiv:1706.05098, 2017
45	. Recent theoretical work by Lippl and Lindsey~\cite{lippl2024implicit} % Lippl and Lindsey, "Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks", ICLR 2024, arXiv:2310.02396
46	shows that multi-task learning in overparameterized networks induces an $\ell_{1,2}$ mixed-norm implicit regularization that encourages feature sharing across tasks, while fine-tuning exhibits ``nested feature selection'' that retains sparse subsets of pretrained features. These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.
47	
48	For VLA fine-tuning, parameter-efficient methods such as LoRA~\cite{hu2022lora} % Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022, arXiv:2106.09685
49	enable adaptation with minimal parameter overhead, but the interaction between auxiliary losses and LoRA adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss during VLA training and reports faster convergence and improved data efficiency, but does not separate the regularization effect of gradient flow from the informational content of the spatial signal.
50	
51	Our work connects these three research threads. We study whether auxiliary spatial supervision during VLA fine-tuning improves collision avoidance, and we design a factorial ablation that isolates gradient flow regularization from spatial signal content. Unlike VLA safety methods that constrain actions at runtime or through RL, we modify the training signal. Unlike spatial VLA methods that target task success, we measure safety. Unlike multi-task learning analyses that study generalization on standard benchmarks, we examine whether auxiliary-task regularization produces emergent safety-relevant behavior.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "2aee8cd7-327d-43af-afc0-e7761182d53f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
      "content": "\n\\section{Related Work}\n\n\\subsection{Safety in Vision-Language-Action Models}\n\nVision-language-action (VLA) models achieve high task success rates on manipulation benchmarks~\\cite{kim2024openvla} % Kim et al., \"OpenVLA: An Open-Source Vision-Language-Action Model\", arXiv:2406.09246, 2024\n\\cite{brohan2023rt2} % Brohan et al., \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", arXiv:2307.15818, 2023\nbut remain prone to collisions when obstacles occupy the manipulation workspace. Two strategies have emerged to address this gap between task completion and behavioral safety.\n\nThe first strategy applies runtime constraints to filter or adjust unsafe actions. The AEGIS framework~\\cite{hu2025vlsa} % Hu et al., \"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\", arXiv:2512.11891, 2025\nadds a plug-and-play safety layer that identifies obstacles through a vision-language assessment module and enforces avoidance via a control barrier function (CBF) quadratic program, improving collision avoidance rate by 59.16 percentage points on SafeLIBERO, a benchmark of 32 safety-critical manipulation scenarios introduced in the same work. CoFreeVLA~\\cite{zhai2026cofreevla} % Zhai et al., \"CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation\", arXiv:2601.21712, 2026\naddresses a related problem in dual-arm settings by training a short-horizon collision risk estimator that gates risky commands and triggers recovery to safe configurations. Control barrier functions have also been applied directly to manipulation independently of VLAs. Morton and Pavone~\\cite{morton2025oscbf} % Morton and Pavone, \"Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions\", IROS 2025, arXiv:2503.06736\nformulate operational-space CBFs that scale to hundreds of simultaneous constraints at real-time control rates, and Raja et al.~\\cite{raja2024ogmcbf} % Raja et al., \"Safe Robot Control using Occupancy Grid Map-based Control Barrier Function (OGM-CBF)\", arXiv:2405.10703, 2024\nconstruct CBFs from occupancy grid maps, directly linking occupancy representations to explicit safety guarantees. These runtime approaches are effective but add computational overhead at inference time, and they require access to obstacle positions or perception modules that can provide them.\n\nThe second strategy modifies the training objective to embed safety into the policy. SafeVLA~\\cite{zhang2025safevla} % Zhang et al., \"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\", NeurIPS 2025 Spotlight, arXiv:2503.03480\nformulates VLA safety as a constrained Markov decision process and applies safe reinforcement learning, reducing safety violations by 83.58\\% while maintaining task performance. This requires collecting unsafe trajectories and defining explicit cost functions for each type of violation, which limits scalability to new environments.\n\nBoth strategies treat safety as a behavioral constraint problem, applied either to the action space at runtime or through reward shaping during training. Neither investigates whether the VLA's internal spatial representations contribute to or hinder collision avoidance. Our work addresses this gap: we modify the training signal through auxiliary spatial supervision and study how this changes safety outcomes, with zero inference-time cost and no need for explicit safety reward design.\n\n\\subsection{3D Spatial Representations for Robot Learning}\n\nBird's-eye-view and occupancy representations have become central to 3D perception in autonomous driving. BEVFormer~\\cite{li2022bevformer} % Li et al., \"BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers\", ECCV 2022, arXiv:2203.17270\nprojects multi-camera features into a unified BEV grid via spatiotemporal transformers. Sima et al.~\\cite{sima2023occnet} % Sima et al., \"Scene as Occupancy\", ICCV 2023, arXiv:2306.02851\nrepresent entire scenes as dense 3D occupancy volumes, capturing irregular object shapes that bounding boxes cannot, and Occ3D~\\cite{tian2023occ3d} % Tian et al., \"Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving\", NeurIPS 2023, arXiv:2304.14365\nestablishes a large-scale benchmark for vision-based occupancy prediction. More recently, OccVLA~\\cite{liu2025occvla} % Liu et al., \"OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision\", arXiv:2509.05578, 2025\nintegrates occupancy prediction into a VLA for autonomous driving, treating occupancy tokens as an implicit spatial reasoning mechanism. These results establish that occupancy supervision improves 3D scene understanding, but they operate in the driving domain where the BEV frame naturally aligns with the planning task.\n\nFor tabletop manipulation, the appropriate spatial reference frame is less obvious: the robot observes from an egocentric camera while objects sit on a planar workspace. Recent work brings 3D structure into manipulation VLAs through several mechanisms. Depth-based approaches fuse monocular depth predictions with visual features: DepthVLA~\\cite{yuan2025depthvla} % Yuan et al., \"DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning\", arXiv:2510.13375, 2025\nuses a mixture-of-transformers architecture to jointly decode actions and depth, reporting improved performance on tasks requiring precise spatial reasoning. AugVLA-3D~\\cite{rao2026augvla3d} % Rao et al., \"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models\", arXiv:2602.10698, 2026\naugments 2D visual tokens with depth-derived 3D features through a geometry-aware module. These methods build on foundation models for monocular depth estimation, including MiDaS~\\cite{ranftl2022midas} % Ranftl et al., \"Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer\", TPAMI 2022\nand Depth Anything~\\cite{yang2024depthanything} % Yang et al., \"Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data\", CVPR 2024, arXiv:2401.10891\n, which have made metric or relative depth estimation accessible from single RGB inputs. Alignment-based approaches instead regularize internal representations: Spatial Forcing~\\cite{li2026spatialforcing} % Li et al., \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model\", ICLR 2026, arXiv:2510.12276\naligns VLA visual embeddings with features from pretrained 3D models, using depth probing experiments to confirm that spatial information transfers into the VLA's learned representations. SpatialVLA~\\cite{wu2025spatialvla} % Wu et al., \"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model\", RSS 2025, arXiv:2501.15830\nintroduces ego-centric 3D position encoding to ground action predictions in workspace coordinates. Point cloud representations offer an alternative: PointVLA~\\cite{li2025pointvla} % Li et al., \"PointVLA: Injecting the 3D World into Vision-Language-Action Models\", arXiv:2503.07511, 2025\ncompresses point clouds and injects them into underutilized transformer blocks. ST-VLA~\\cite{wu2026stvla} % Wu et al., \"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation\", arXiv:2603.13788, 2026\nextends this line to 4D spatiotemporal representations by generating 3D trajectories from 2D guidance.\n\nThese spatial methods consistently improve task success rates and generalization. However, none evaluates the impact of spatial representations on collision avoidance or other safety metrics. Whether improved 3D understanding translates to safer manipulation behavior remains an open question.\n\n\\subsection{Auxiliary Tasks and Regularization in Fine-Tuning}\n\nMulti-task learning improves generalization by training on related objectives through a shared representation~\\cite{caruana1997multitask} % Caruana, \"Multitask Learning\", Machine Learning 28:41-75, 1997\n. Auxiliary tasks act as inductive biases that prevent the shared encoder from overfitting to the primary objective~\\cite{ruder2017overview} % Ruder, \"An Overview of Multi-Task Learning in Deep Neural Networks\", arXiv:1706.05098, 2017\n. Recent theoretical work by Lippl and Lindsey~\\cite{lippl2024implicit} % Lippl and Lindsey, \"Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks\", ICLR 2024, arXiv:2310.02396\nshows that multi-task learning in overparameterized networks induces an $\\ell_{1,2}$ mixed-norm implicit regularization that encourages feature sharing across tasks, while fine-tuning exhibits ``nested feature selection'' that retains sparse subsets of pretrained features. These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.\n\nFor VLA fine-tuning, parameter-efficient methods such as LoRA~\\cite{hu2022lora} % Hu et al., \"LoRA: Low-Rank Adaptation of Large Language Models\", ICLR 2022, arXiv:2106.09685\nenable adaptation with minimal parameter overhead, but the interaction between auxiliary losses and LoRA adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss during VLA training and reports faster convergence and improved data efficiency, but does not separate the regularization effect of gradient flow from the informational content of the spatial signal.\n\nOur work connects these three research threads. We study whether auxiliary spatial supervision during VLA fine-tuning improves collision avoidance, and we design a factorial ablation that isolates gradient flow regularization from spatial signal content. Unlike VLA safety methods that constrain actions at runtime or through RL, we modify the training signal. Unlike spatial VLA methods that target task success, we measure safety. Unlike multi-task learning analyses that study generalization on standard benchmarks, we examine whether auxiliary-task regularization produces emergent safety-relevant behavior.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01XQJoEgpFsxCYpfpimLEBp4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "5606c09b-70cb-4d01-95a4-06b3f27a2967",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

_source line 14 · 2026-05-22T18:22:42.845Z_

<details><summary>↩ Tool result · `toolu_01XQJoEgpFsxCYpfpimLEBp4`</summary>

```text
1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\subsection{Why Does Gradient Flow Improve Collision Avoidance?}
6	\label{sec:why_gradient}
7	
8	The ablation results reveal a consistent ordering: conditions with auxiliary gradient flow through the vision encoder (Random OCC at 0.806 CAR, Full OCC at 0.797) outperform Vanilla (0.780), while Detach OCC (0.745) falls below all others. Three candidate mechanisms can explain this pattern.
9	
10	\textbf{Hypothesis 1: Anti-overfitting regularization.}
11	Auxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Random OCC (0.806) matches or exceeds Full OCC (0.797) is consistent with this account, though the difference is within seed variance (2--3 seeds per condition) and should not be over-interpreted.
12	
13	\textbf{Hypothesis 2: Optimization landscape smoothing.}
14	The auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.
15	
16	\textbf{Hypothesis 3: Gradient diversity.}
17	When fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.
18	
19	All three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.
20	
21	\subsection{Why Is Detach Harmful?}
22	\label{sec:why_detach}
23	
24	Detach OCC produces the lowest CAR (0.745) among all conditions, falling 3.5 percentage points below Vanilla (0.780). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing. Two factors explain the deficit.
25	
26	First, the detached head's 1.2M parameters receive gradient updates from $\mathcal{L}_\text{occ}$ without contributing to encoder learning. These parameters absorb a portion of the optimizer's state (momentum and second-moment estimates in AdamW) and the forward pass computation budget, yet their learned representations never influence action prediction. The head functions as dead weight at inference.
27	
28	Second, and more consequentially, the \texttt{stop\_gradient} operation at the encoder boundary eliminates the regularization benefit that the auxiliary loss otherwise provides. The encoder receives gradients from $\mathcal{L}_\text{action}$ alone, identical to Vanilla, but the training dynamics differ because the total loss landscape includes a term that does not back-propagate. If the occupancy loss interacts with the action loss through shared batch statistics (e.g., batch normalization in the auxiliary head), the detached configuration could introduce noise into the forward pass without compensating gradient signal. The 3.5pp deficit relative to Vanilla, observed across 2 seeds, suggests that gradient flow is not merely helpful but is a necessary condition for the auxiliary task to avoid harming performance.
29	
30	\subsection{Implications for VLA Safety}
31	\label{sec:implications}
32	
33	\textbf{Practical recommendation.} The finding that Random OCC matches Full OCC in CAR carries a direct practical implication: practitioners fine-tuning VLAs for safety-sensitive deployment can attach any auxiliary head with gradient flow to the vision encoder---even one trained on uninformative labels---and expect a regularization benefit for collision avoidance. This eliminates the need for ground-truth spatial labels, which require simulator access or depth sensors, and reduces the auxiliary task to a generic regularizer with zero inference-time overhead.
34	
35	\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task regularization during training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.
36	
37	\textbf{Zero inference cost.} Unlike all prior VLA safety methods that add modules at inference~\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.
38	
39	\subsection{Limitations}
40	\label{sec:limitations}
41	
42	\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.
43	
44	\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.
45	
46	\textbf{Effect size.} The overall CAR improvement is 1.7--2.6 percentage points over Vanilla. While this is consistent across conditions with gradient flow, the magnitude is modest. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.
47	
48	\textbf{Seed sensitivity.} Auxiliary conditions exhibit higher cross-seed variance than Vanilla (standard deviation $\sim$0.026 vs.\ $\sim$0.012 for overall CAR, a 2.2$\times$ ratio). With 2--3 seeds per condition, confidence intervals overlap for several pairwise comparisons. The ordering Random OCC $>$ Full OCC $>$ Vanilla is directionally consistent but not statistically confirmed at conventional significance levels. Scaling to 5+ seeds per condition would clarify whether the Random--Full OCC gap reflects a real difference or sampling noise.
49	
50	% [PENDING DEPTH RESULTS] — Section below to be filled when depth experiment data is available.
51	\subsection{Depth vs.\ BEV Occupancy}
52	\label{sec:depth_discussion}
53	
54	This section will compare egocentric depth supervision against allocentric BEV occupancy supervision, analyzing whether the spatial reference frame affects the regularization mechanism and collision avoidance outcomes. Pending completion of depth condition evaluation at 50,000 steps across all seeds.
55	
56	% ============================================================
57	% Citations needed in references.bib:
58	%
59	% @inproceedings{foret2021sam,
60	%   author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},
61	%   title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},
62	%   booktitle = {International Conference on Learning Representations (ICLR)},
63	%   year      = {2021},
64	%   note      = {arXiv:2010.01412}
65	% }
66	% ============================================================
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "15fd3294-d2c9-4c63-8852-8670250622ac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent ordering: conditions with auxiliary gradient flow through the vision encoder (Random OCC at 0.806 CAR, Full OCC at 0.797) outperform Vanilla (0.780), while Detach OCC (0.745) falls below all others. Three candidate mechanisms can explain this pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Random OCC (0.806) matches or exceeds Full OCC (0.797) is consistent with this account, though the difference is within seed variance (2--3 seeds per condition) and should not be over-interpreted.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.745) among all conditions, falling 3.5 percentage points below Vanilla (0.780). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing. Two factors explain the deficit.\n\nFirst, the detached head's 1.2M parameters receive gradient updates from $\\mathcal{L}_\\text{occ}$ without contributing to encoder learning. These parameters absorb a portion of the optimizer's state (momentum and second-moment estimates in AdamW) and the forward pass computation budget, yet their learned representations never influence action prediction. The head functions as dead weight at inference.\n\nSecond, and more consequentially, the \\texttt{stop\\_gradient} operation at the encoder boundary eliminates the regularization benefit that the auxiliary loss otherwise provides. The encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone, identical to Vanilla, but the training dynamics differ because the total loss landscape includes a term that does not back-propagate. If the occupancy loss interacts with the action loss through shared batch statistics (e.g., batch normalization in the auxiliary head), the detached configuration could introduce noise into the forward pass without compensating gradient signal. The 3.5pp deficit relative to Vanilla, observed across 2 seeds, suggests that gradient flow is not merely helpful but is a necessary condition for the auxiliary task to avoid harming performance.\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The finding that Random OCC matches Full OCC in CAR carries a direct practical implication: practitioners fine-tuning VLAs for safety-sensitive deployment can attach any auxiliary head with gradient flow to the vision encoder---even one trained on uninformative labels---and expect a regularization benefit for collision avoidance. This eliminates the need for ground-truth spatial labels, which require simulator access or depth sensors, and reduces the auxiliary task to a generic regularizer with zero inference-time overhead.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task regularization during training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike all prior VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR improvement is 1.7--2.6 percentage points over Vanilla. While this is consistent across conditions with gradient flow, the magnitude is modest. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity.} Auxiliary conditions exhibit higher cross-seed variance than Vanilla (standard deviation $\\sim$0.026 vs.\\ $\\sim$0.012 for overall CAR, a 2.2$\\times$ ratio). With 2--3 seeds per condition, confidence intervals overlap for several pairwise comparisons. The ordering Random OCC $>$ Full OCC $>$ Vanilla is directionally consistent but not statistically confirmed at conventional significance levels. Scaling to 5+ seeds per condition would clarify whether the Random--Full OCC gap reflects a real difference or sampling noise.\n\n% [PENDING DEPTH RESULTS] — Section below to be filled when depth experiment data is available.\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThis section will compare egocentric depth supervision against allocentric BEV occupancy supervision, analyzing whether the spatial reference frame affects the regularization mechanism and collision avoidance outcomes. Pending completion of depth condition evaluation at 50,000 steps across all seeds.\n\n% ============================================================\n% Citations needed in references.bib:\n%\n% @inproceedings{foret2021sam,\n%   author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},\n%   title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},\n%   booktitle = {International Conference on Learning Representations (ICLR)},\n%   year      = {2021},\n%   note      = {arXiv:2010.01412}\n% }\n% ============================================================\n",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01XnaiZTJUTtKtUb4TmHdR9G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "cd737b73-e712-42cc-bfbd-a871fed7a276",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sYQUyLNRym9FB3Hy5ADmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12585,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12585
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

_source line 16 · 2026-05-22T18:22:43.586Z_

<details><summary>↩ Tool result · `toolu_01XnaiZTJUTtKtUb4TmHdR9G`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\subsection{Problem Formulation}
6	
7	We study how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance in tabletop manipulation. Given a pretrained VLA with vision encoders $\phi_v$ and a language-conditioned action decoder $\pi$, standard fine-tuning minimizes the action prediction loss $\mathcal{L}_\text{action} = \mathcal{L}(\pi(\phi_v(o_t), l), a_t^*)$, where $o_t$ is the visual observation, $l$ is the language instruction, and $a_t^*$ is the demonstration action. We augment this objective with an auxiliary spatial prediction head $h$ that maps intermediate visual features to a spatial target $s_t^*$:
8	\begin{equation}
9	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*)
10	\label{eq:total_loss}
11	\end{equation}
12	where $\lambda(t)$ is a time-varying weight. The spatial target is either a BEV occupancy grid or an egocentric depth map. The auxiliary head is discarded at inference and adds no cost at deployment.
13	
14	We use OpenVLA-7B~\cite{kim2024openvla} % Kim et al., "OpenVLA: An Open-Source Vision-Language-Action Model", arXiv:2406.09246, 2024
15	with the OFT fine-tuning recipe~\cite{kim2025oft} % Kim et al., "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success", arXiv:2502.19645, 2025
16	as the base model. OpenVLA's vision backbone concatenates patch features from a DINOv2~\cite{oquab2024dinov2} % Oquab et al., "DINOv2: Learning Robust Visual Features without Supervision", TMLR 2024, arXiv:2304.07193
17	encoder (dimension 1024) and a SigLIP~\cite{zhai2023siglip} % Zhai et al., "Sigmoid Loss for Language Image Pre-Training", ICCV 2023, arXiv:2303.15343
18	encoder (dimension 1152) to form a 2176-dimensional representation per spatial token. The auxiliary heads receive these concatenated features, so their gradients flow through both the spatial (DINOv2) and semantic (SigLIP) encoders simultaneously. We apply LoRA~\cite{hu2022lora} % Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022, arXiv:2106.09685
19	with rank 32, $\alpha = 16$, and no dropout, yielding a conservative effective scaling factor of $\alpha / r = 0.5$.
20	
21	\subsection{BEV Occupancy Head}
22	\label{sec:occ_head}
23	
24	The occupancy head predicts a $64 \times 64$ binary bird's-eye-view occupancy grid from the cached patch features $\mathbf{F} \in \mathbb{R}^{B \times N \times 2176}$. The architecture has four stages:
25	\begin{enumerate}
26	    \item A linear projection from 2176 to 256 dimensions, reshaped to $\mathbb{R}^{B \times 256 \times 16 \times 16}$.
27	    \item A transposed convolution ($256 \to 128$ channels, kernel size 4, stride 2) with batch normalization and GELU activation, producing $32 \times 32$ spatial resolution.
28	    \item A second transposed convolution ($128 \to 64$ channels, kernel size 4, stride 2) with batch normalization and GELU, producing $64 \times 64$ resolution.
29	    \item A $1 \times 1$ convolution ($64 \to 1$ channel) with sigmoid activation, yielding $\hat{y} \in [0, 1]^{B \times 1 \times 64 \times 64}$.
30	\end{enumerate}
31	The head contains 1.2M parameters, or 0.016\% of the full 7.65B-parameter model.
32	
33	Ground-truth occupancy maps are generated offline by replaying recorded demonstration trajectories in MuJoCo and rendering top-down binary grids at each timestep. Each cell is set to 1 if an object body intersects the corresponding workspace region. We train with focal loss~\cite{lin2017focal} % Lin et al., "Focal Loss for Dense Object Detection", ICCV 2017, arXiv:1708.02002
34	to handle the class imbalance between occupied and free cells:
35	\begin{equation}
36	\mathcal{L}_\text{occ} = \text{FocalLoss}(\hat{y}, y^*;\; \alpha = 0.25,\; \gamma = 2.0)
37	\end{equation}
38	The auxiliary loss weight follows an exponential decay schedule:
39	\begin{equation}
40	\lambda_\text{occ}(t) = 0.01 \cdot \exp\!\left(-\frac{t}{50000}\right)
41	\label{eq:occ_decay}
42	\end{equation}
43	This schedule progressively reduces the occupancy gradient's contribution so that action prediction dominates in later training stages. The decay can be interpreted as a curriculum: the model first develops spatial structure through the auxiliary signal, then refines motor behavior under the primary objective.
44	
45	\subsection{Monocular Depth Head}
46	\label{sec:depth_head}
47	
48	The depth head shares the occupancy head's architecture with two modifications: the final activation is ReLU (to enforce non-negative depth values) instead of sigmoid, and the training loss is smooth L1:
49	\begin{equation}
50	\mathcal{L}_\text{depth} = \text{SmoothL1}(\hat{d}, d^*)
51	\end{equation}
52	with the same exponential decay schedule ($\lambda_\text{depth}(t) = 0.01 \cdot \exp(-t / 50000)$). The depth head has approximately 1.2M parameters.
53	
54	Ground-truth depth maps are rendered from the egocentric camera viewpoint in MuJoCo at $64 \times 64$ resolution using state replay. Unlike the BEV occupancy grid, which provides an allocentric top-down layout of the workspace, the depth map encodes distances from the robot's camera to scene surfaces. This egocentric frame aligns with the robot's visual observation and directly encodes proximity information relevant to collision avoidance: nearby surfaces produce small depth values, providing a natural gradient for spatial awareness. The BEV frame, by contrast, represents object layout in a coordinate frame orthogonal to the camera view, requiring the encoder to learn a non-trivial viewpoint transformation.
55	
56	\subsection{Ablation Design}
57	\label{sec:ablation}
58	
59	We evaluate five training conditions designed to disentangle the mechanisms by which auxiliary spatial supervision affects collision avoidance.
60	
61	\textbf{Vanilla.} Standard LoRA fine-tuning with action loss only. Any collision avoidance behavior emerges solely from imitating demonstration trajectories.
62	
63	\textbf{Full OCC.} LoRA fine-tuning with the BEV occupancy head receiving ground-truth labels. Gradients from $\mathcal{L}_\text{occ}$ flow through both the DINOv2 and SigLIP encoders. This condition tests whether BEV spatial supervision improves collision avoidance.
64	
65	\textbf{Random OCC.} Identical to Full OCC, but the occupancy labels are replaced with random binary grids that contain no spatial information. Gradient magnitudes and computational costs match Full OCC. Comparing Random OCC to Full OCC isolates the contribution of spatial content: if both perform equally, gradient flow regularization is the dominant mechanism; if Full OCC is superior, the BEV spatial signal provides additional benefit beyond regularization.
66	
67	\textbf{Detach OCC.} Identical to Full OCC, but gradients are detached at the boundary between the vision encoders and the occupancy head. Only the head's 1.2M parameters receive gradient updates from $\mathcal{L}_\text{occ}$; the encoders see only $\mathcal{L}_\text{action}$. This condition tests whether gradient flow through the encoder is a necessary condition for the auxiliary task's safety effect. If Detach performs worse than Vanilla, the disconnected head acts as a gradient sink that consumes optimization capacity without providing regularization.
68	
69	\textbf{Depth.} LoRA fine-tuning with the monocular depth head receiving ground-truth egocentric depth maps. This condition compares allocentric (BEV occupancy) and egocentric (camera-frame depth) spatial reference frames while holding the auxiliary training mechanism constant.
70	
71	We additionally evaluate a curriculum variant (\textbf{OCC-Cutoff}) that applies occupancy supervision for the first 35{,}000 steps then disables it, testing whether late-stage auxiliary gradients interfere with action prediction refinement. This condition separates the effect of early-stage spatial regularization from potential late-stage gradient interference.
72	
73	\begin{table}[t]
74	\centering
75	\caption{Ablation design. Each pairwise comparison isolates one factor in the interaction between auxiliary supervision and collision avoidance. The interpretation of the Depth vs.\ Random OCC comparison depends on whether random labels match or underperform real spatial labels (see \S5).}
76	\label{tab:ablation_design}
77	\begin{tabular}{ll}
78	\toprule
79	Comparison & Isolated Factor \\
80	\midrule
81	Full OCC vs.\ Vanilla & Effect of auxiliary spatial supervision \\
82	Random OCC vs.\ Full OCC & Spatial content vs.\ gradient flow \\
83	Detach OCC vs.\ Vanilla & Necessity of encoder gradient flow \\
84	Depth vs.\ Full OCC & Egocentric vs.\ allocentric frame \\
85	Depth vs.\ Random OCC & Effect of spatial signal fidelity \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	This design systematically varies three factors: the presence of gradient flow to the vision encoders, the informational content of the auxiliary labels, and the spatial reference frame. Table~\ref{tab:ablation_design} summarizes the pairwise comparisons and what each isolates.
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "d52c1079-cf81-499d-8d83-04d9c8984e76",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\nWe study how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance in tabletop manipulation. Given a pretrained VLA with vision encoders $\\phi_v$ and a language-conditioned action decoder $\\pi$, standard fine-tuning minimizes the action prediction loss $\\mathcal{L}_\\text{action} = \\mathcal{L}(\\pi(\\phi_v(o_t), l), a_t^*)$, where $o_t$ is the visual observation, $l$ is the language instruction, and $a_t^*$ is the demonstration action. We augment this objective with an auxiliary spatial prediction head $h$ that maps intermediate visual features to a spatial target $s_t^*$:\n\\begin{equation}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda(t) \\cdot \\mathcal{L}_\\text{aux}(h(\\phi_v(o_t)), s_t^*)\n\\label{eq:total_loss}\n\\end{equation}\nwhere $\\lambda(t)$ is a time-varying weight. The spatial target is either a BEV occupancy grid or an egocentric depth map. The auxiliary head is discarded at inference and adds no cost at deployment.\n\nWe use OpenVLA-7B~\\cite{kim2024openvla} % Kim et al., \"OpenVLA: An Open-Source Vision-Language-Action Model\", arXiv:2406.09246, 2024\nwith the OFT fine-tuning recipe~\\cite{kim2025oft} % Kim et al., \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\", arXiv:2502.19645, 2025\nas the base model. OpenVLA's vision backbone concatenates patch features from a DINOv2~\\cite{oquab2024dinov2} % Oquab et al., \"DINOv2: Learning Robust Visual Features without Supervision\", TMLR 2024, arXiv:2304.07193\nencoder (dimension 1024) and a SigLIP~\\cite{zhai2023siglip} % Zhai et al., \"Sigmoid Loss for Language Image Pre-Training\", ICCV 2023, arXiv:2303.15343\nencoder (dimension 1152) to form a 2176-dimensional representation per spatial token. The auxiliary heads receive these concatenated features, so their gradients flow through both the spatial (DINOv2) and semantic (SigLIP) encoders simultaneously. We apply LoRA~\\cite{hu2022lora} % Hu et al., \"LoRA: Low-Rank Adaptation of Large Language Models\", ICLR 2022, arXiv:2106.09685\nwith rank 32, $\\alpha = 16$, and no dropout, yielding a conservative effective scaling factor of $\\alpha / r = 0.5$.\n\n\\subsection{BEV Occupancy Head}\n\\label{sec:occ_head}\n\nThe occupancy head predicts a $64 \\times 64$ binary bird's-eye-view occupancy grid from the cached patch features $\\mathbf{F} \\in \\mathbb{R}^{B \\times N \\times 2176}$. The architecture has four stages:\n\\begin{enumerate}\n    \\item A linear projection from 2176 to 256 dimensions, reshaped to $\\mathbb{R}^{B \\times 256 \\times 16 \\times 16}$.\n    \\item A transposed convolution ($256 \\to 128$ channels, kernel size 4, stride 2) with batch normalization and GELU activation, producing $32 \\times 32$ spatial resolution.\n    \\item A second transposed convolution ($128 \\to 64$ channels, kernel size 4, stride 2) with batch normalization and GELU, producing $64 \\times 64$ resolution.\n    \\item A $1 \\times 1$ convolution ($64 \\to 1$ channel) with sigmoid activation, yielding $\\hat{y} \\in [0, 1]^{B \\times 1 \\times 64 \\times 64}$.\n\\end{enumerate}\nThe head contains 1.2M parameters, or 0.016\\% of the full 7.65B-parameter model.\n\nGround-truth occupancy maps are generated offline by replaying recorded demonstration trajectories in MuJoCo and rendering top-down binary grids at each timestep. Each cell is set to 1 if an object body intersects the corresponding workspace region. We train with focal loss~\\cite{lin2017focal} % Lin et al., \"Focal Loss for Dense Object Detection\", ICCV 2017, arXiv:1708.02002\nto handle the class imbalance between occupied and free cells:\n\\begin{equation}\n\\mathcal{L}_\\text{occ} = \\text{FocalLoss}(\\hat{y}, y^*;\\; \\alpha = 0.25,\\; \\gamma = 2.0)\n\\end{equation}\nThe auxiliary loss weight follows an exponential decay schedule:\n\\begin{equation}\n\\lambda_\\text{occ}(t) = 0.01 \\cdot \\exp\\!\\left(-\\frac{t}{50000}\\right)\n\\label{eq:occ_decay}\n\\end{equation}\nThis schedule progressively reduces the occupancy gradient's contribution so that action prediction dominates in later training stages. The decay can be interpreted as a curriculum: the model first develops spatial structure through the auxiliary signal, then refines motor behavior under the primary objective.\n\n\\subsection{Monocular Depth Head}\n\\label{sec:depth_head}\n\nThe depth head shares the occupancy head's architecture with two modifications: the final activation is ReLU (to enforce non-negative depth values) instead of sigmoid, and the training loss is smooth L1:\n\\begin{equation}\n\\mathcal{L}_\\text{depth} = \\text{SmoothL1}(\\hat{d}, d^*)\n\\end{equation}\nwith the same exponential decay schedule ($\\lambda_\\text{depth}(t) = 0.01 \\cdot \\exp(-t / 50000)$). The depth head has approximately 1.2M parameters.\n\nGround-truth depth maps are rendered from the egocentric camera viewpoint in MuJoCo at $64 \\times 64$ resolution using state replay. Unlike the BEV occupancy grid, which provides an allocentric top-down layout of the workspace, the depth map encodes distances from the robot's camera to scene surfaces. This egocentric frame aligns with the robot's visual observation and directly encodes proximity information relevant to collision avoidance: nearby surfaces produce small depth values, providing a natural gradient for spatial awareness. The BEV frame, by contrast, represents object layout in a coordinate frame orthogonal to the camera view, requiring the encoder to learn a non-trivial viewpoint transformation.\n\n\\subsection{Ablation Design}\n\\label{sec:ablation}\n\nWe evaluate five training conditions designed to disentangle the mechanisms by which auxiliary spatial supervision affects collision avoidance.\n\n\\textbf{Vanilla.} Standard LoRA fine-tuning with action loss only. Any collision avoidance behavior emerges solely from imitating demonstration trajectories.\n\n\\textbf{Full OCC.} LoRA fine-tuning with the BEV occupancy head receiving ground-truth labels. Gradients from $\\mathcal{L}_\\text{occ}$ flow through both the DINOv2 and SigLIP encoders. This condition tests whether BEV spatial supervision improves collision avoidance.\n\n\\textbf{Random OCC.} Identical to Full OCC, but the occupancy labels are replaced with random binary grids that contain no spatial information. Gradient magnitudes and computational costs match Full OCC. Comparing Random OCC to Full OCC isolates the contribution of spatial content: if both perform equally, gradient flow regularization is the dominant mechanism; if Full OCC is superior, the BEV spatial signal provides additional benefit beyond regularization.\n\n\\textbf{Detach OCC.} Identical to Full OCC, but gradients are detached at the boundary between the vision encoders and the occupancy head. Only the head's 1.2M parameters receive gradient updates from $\\mathcal{L}_\\text{occ}$; the encoders see only $\\mathcal{L}_\\text{action}$. This condition tests whether gradient flow through the encoder is a necessary condition for the auxiliary task's safety effect. If Detach performs worse than Vanilla, the disconnected head acts as a gradient sink that consumes optimization capacity without providing regularization.\n\n\\textbf{Depth.} LoRA fine-tuning with the monocular depth head receiving ground-truth egocentric depth maps. This condition compares allocentric (BEV occupancy) and egocentric (camera-frame depth) spatial reference frames while holding the auxiliary training mechanism constant.\n\nWe additionally evaluate a curriculum variant (\\textbf{OCC-Cutoff}) that applies occupancy supervision for the first 35{,}000 steps then disables it, testing whether late-stage auxiliary gradients interfere with action prediction refinement. This condition separates the effect of early-stage spatial regularization from potential late-stage gradient interference.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation design. Each pairwise comparison isolates one factor in the interaction between auxiliary supervision and collision avoidance. The interpretation of the Depth vs.\\ Random OCC comparison depends on whether random labels match or underperform real spatial labels (see \\S5).}\n\\label{tab:ablation_design}\n\\begin{tabular}{ll}\n\\toprule\nComparison & Isolated Factor \\\\\n\\midrule\nFull OCC vs.\\ Vanilla & Effect of auxiliary spatial supervision \\\\\nRandom OCC vs.\\ Full OCC & Spatial content vs.\\ gradient flow \\\\\nDetach OCC vs.\\ Vanilla & Necessity of encoder gradient flow \\\\\nDepth vs.\\ Full OCC & Egocentric vs.\\ allocentric frame \\\\\nDepth vs.\\ Random OCC & Effect of spatial signal fidelity \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis design systematically varies three factors: the presence of gradient flow to the vision encoders, the informational content of the auxiliary labels, and the spatial reference frame. Table~\\ref{tab:ablation_design} summarizes the pairwise comparisons and what each isolates.\n",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the necessary materials. Let me synthesize this information and write the Introduction section.

Key information:
1. **Writing style**: "突破局限型" framing. Universal hook: "VLA shows promise, BUT [concrete gap]." 4-5 paragraphs. P1=promise+gap → P2=existing limitations → P3=method → P4=contributions → P5=outline.
2. **Paper framing**: Analysis paper (Option B). Core insight: gradient flow regularization is the dominant mechanism, not spatial content itself.
3. **Cite keys available**: I have all the cite keys from references.bib


4. **Related work**: Already covers VLA safety, 3D spatial representations, and MTL/regularization
5. **Discussion**: Uses specific terminology like "gradient flow regularization", "anti-overfitting regularization", etc.
6. **Method**: 5 conditions (Vanilla, Full OCC, Random OCC, Detach OCC, Depth), OpenVLA-OFT, LoRA rank 32

Now I'm structuring the introduction with the opening hook about VLA promise and the safety gap, followed by the auxiliary task research question, then positioning our analysis work. I'll weave in the key finding about gradient flow regularization being the dominant mechanism throughout.

For the middle section, I need to enumerate three main contributions: the gradient flow mechanism we identified, the factorial study across five conditions, and the practical guidelines that emerge. Then I'll close with the experimental setup, preview the results, and outline the paper structure.

I should verify the citation keys are available—RT-2 and OpenVLA are confirmed, but I need to check if Octo is in the references or if I should note it as missing. The depth results are still pending, so I'll use the placeholder. Aiming for analytical tone without promotional language, keeping it around 50-60 lines of LaTeX with proper section markup and enumeration for contributions. Now I'm drafting the introduction section, starting with the core narrative: VLAs show impressive success rates on benchmarks, but this masks a critical safety problem where they frequently collide with obstacles in cluttered manipulation scenarios, as evidenced by the performance gap on SafeLIBERO tasks.

Next, I'm setting up the research question by noting that spatial prediction auxiliary tasks and safety-focused methods have developed as separate research threads—one improving performance through 3D structure injection, the other reducing collisions through constraints or learning—but these approaches haven't been integrated.

For my work, I'm designing a controlled factorial study to isolate how spatial supervision affects collision avoidance, testing five conditions that vary the auxiliary task (occupancy, depth, or none) and the information flow (ground-truth labels, random labels, or gradient detachment) to distinguish whether safety improvements come from the spatial signal itself or from regularization effects during training. Writing the LaTeX manuscript...

I need to be careful about word choice—avoiding vague qualifiers like "notably" and "significantly" without proper statistical backing. For the conditions, I'm using the data I have: Random OCC at 0.806 CAR across 2 seeds, Full OCC at 0.797 across 3 seeds, Vanilla baseline at 0.780 across 3 seeds, and Detach OCC at 0.745 across 2 seeds. The Depth condition results are still pending, so I'll mark that clearly. For TSR, I'm going with the formal evaluation baseline of 91.8% rather than the 0.907 figure to stay consistent with the paper framing. I'll describe directional trends where I only have 2-3 seeds instead of claiming statistical significance. I'm settling on the 50-round evaluation numbers from the task table as the primary baseline for comparison. For the SafeLIBERO citation, I need to reference the VLSA paper where it was introduced, and I'll cite the original LIBERO benchmark separately. Now I'm structuring the introduction with opening paragraphs, a contributions list, and a closing section, aiming for around 50-60 lines total with roughly 8-10 lines per opening paragraph, then the enumerated contributions, and a final closing paragraph. I'm establishing the core tension: while fine-tuned VLAs achieve high task success rates on SafeLIBERO benchmarks, they frequently collide with obstacles—one task shows 100% completion but only 32.5% collision avoidance, revealing that task success masks safety failures. Spatial auxiliary tasks like occupancy grids and depth maps are widely used to improve VLA performance, but I need to identify the disconnect between these spatial methods and actual safety outcomes. pretrained on 2D images and consistently improve success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions or constrained reinforcement learning to reduce collisions. These two lines of work remain disconnected: spatial VLA methods don't evaluate safety metrics, and VLA safety methods don't leverage spatial representation learning. It's unclear whether auxiliary spatial supervision helps collision avoidance, and if so, whether that benefit comes from the spatial information itself or from the training dynamics of the auxiliary objective.

I'm running the first systematic study of how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. I'm training OpenVLA-OFT under five conditions to isolate gradient flow from spatial signal content: Vanilla with action loss only, Full OCC using ground-truth BEV occupancy, Random OCC with random binary labels that lack spatial information, Detach OCC where encoder gradients are blocked, and Depth for egocentric depth prediction. Each condition gets evaluated on SafeLIBERO Level I with collision tracking across multiple seeds and 50 rollouts per task.

The key finding is that auxiliary gradient flow through the vision encoder drives the collision improvement, while the spatial content of the labels matters less. Conditions with gradient flow—Random OCC and Full OCC—outperform Vanilla, but Detach OCC, which blocks encoder gradients, performs worst and drops 3.5 percentage points below Vanilla. That random labels match real occupancy labels (difference of 0.9 percentage points, directionally consistent across seeds but preliminary at 2 vs. 3 seeds) suggests that gradient flow regularization, not spatial information, is the primary driver. Our contributions are identifying the mechanism—auxiliary gradient flow regularization is dominant, with gradient flow being necessary (removing it degrades CAR by 3.5pp) while spatial label content is secondary—introducing a factorial study design that systematically isolates gradient flow, spatial content, and spatial reference frame as factors, and providing practical guidelines showing that any auxiliary head maintaining gradient flow improves collision avoidance without requiring ground-truth labels or inference-time costs. We're testing this across OpenVLA-OFT with LoRA fine-tuning on SafeLIBERO Level I tabletop tasks, where conditions with gradient flow improve CAR by 1.7–2.6 percentage points over the baseline while removing it reduces performance by 3.5pp.

The paper outlines the related work, describes the auxiliary heads and ablation design, presents experimental results, and analyzes the gradient flow mechanism with its implications.

Now I'm reconsidering the structure—I need to condense the opening to 3 paragraphs as specified, then list contributions, then close with the experimental setup and paper outline. Let me merge the results discussion into the main "our work" paragraph to keep things tight, and I should verify whether the 50-60 line target includes blank lines or just content. I'm checking the section labels across the files to make sure my references are consistent—method.tex has `\label{sec:method}` and discussion.tex has `\label{sec:discussion}`, so I'll use those. For the intro section, I don't think it needs a label. I should also verify I'm only citing papers that are actually in references.bib and avoid mentioning any work outside that set, then finalize the LaTeX. I'm checking the writing guidance about using empirical diagnosis as the strongest opening approach, and the core insight should frame gradient flow regularization as an empirical finding rather than just a method pitch. I also need to verify terminology consistency across the paper—making sure I'm using "gradient flow regularization," "vision encoder," "CAR," and "SafeLIBERO Level I" consistently with how they appear in the discussion and related work sections. One task achieves full success but with only 32.5% collision avoidance—the robot reaches the goal while colliding in most episodes, showing that task completion doesn't guarantee safety. Spatial prediction tasks like occupancy grids and depth maps have become standard for improving VLA performance, injecting 3D structure into vision encoders and boosting both success rates and generalization. However, these spatial methods don't evaluate collision avoidance, and safety-focused VLA approaches using control barriers or constrained learning don't leverage spatial representations—these two research directions remain separate, leaving open whether spatial supervision actually helps with collision avoidance.

I'm running a factorial study to isolate how auxiliary spatial supervision affects collision avoidance during VLA fine-tuning. I'm testing five conditions with OpenVLA-OFT that vary gradient flow and label content: baseline action loss only, occupancy grids with ground-truth labels, occupancy grids with random labels to match gradient flow, occupancy grids with detached encoder gradients, and egocentric depth prediction. The results show that gradient flow through the vision encoder is the primary driver of collision avoidance improvements, while the actual label content matters less. Conditions with gradient flow—random occupancy labels and full occupancy labels—outperform the baseline, with collision avoidance rates around 0.80 compared to 0.78.

The key finding is that blocking encoder gradients drops performance 3.5 percentage points below baseline, and random labels perform nearly as well as real occupancy labels, suggesting that the regularization effect of gradient flow is what matters most, not the spatial information itself. I'm now outlining the main contributions: first, demonstrating that gradient flow regularization is the dominant mechanism, with evidence that it's necessary and that label content is secondary. Second, I'm describing the factorial ablation design approach I used to isolate these effects. The ablation design systematically isolates gradient flow, spatial content, and spatial reference frame to understand how auxiliary supervision affects collision avoidance—each comparison answers a specific mechanistic question. The key finding is that attaching any auxiliary head to the vision encoder during fine-tuning improves performance as long as gradients flow through, regardless of whether the labels are meaningful, and since the head gets discarded after training there's no inference overhead. I'm evaluating this on SafeLIBERO Level I using OpenVLA-OFT with LoRA, where conditions with gradient flow show 1.7–2.6 percentage point improvements over the baseline, while blocking gradients causes a 3.5 percentage point drop. The paper then walks through related work on VLA safety and spatial representations, details the auxiliary architectures and ablation setup, presents the experimental results and mechanistic analysis, and concludes with implications and connections to multi-task learning theory. I've verified all the citations are in the references file and checked that I'm avoiding those problematic phrases. Now I'm looking for an existing introduction.tex file to see what's already there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "53d9f4e2-670a-49ce-a30d-9f0dc7c7ee24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe3HXyKiBYCRmGYyfGihJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27441,
      "cache_read_input_tokens": 24426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27441
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

_source line 18_

Now let me check if there's an existing introduction.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "49e4dac6-d542-4cec-8818-4e62d3d261f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe3HXyKiBYCRmGYyfGihJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27441,
      "cache_read_input_tokens": 24426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27441
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

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_017Jw9bwCKmENu2TgrcwTU4h`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "7e5c1426-3f2a-4c7b-9812-3dbf0e6bbf6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe3HXyKiBYCRmGYyfGihJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27441,
      "cache_read_input_tokens": 24426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27441
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

_source line 20 · 2026-05-22T18:25:04.149Z_

<details><summary>↩ Tool result · `toolu_017Jw9bwCKmENu2TgrcwTU4h`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "a58240ae-63b9-4906-a90f-59da100b30f1",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 8,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01WsHDvvEMpV8Dc2hhQ26hQJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "a5f6a209-9be5-4183-b5be-e116b63264ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZoRCpCcnZX9PSPFkeXstB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6722,
      "cache_read_input_tokens": 51867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6722
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 22 · 2026-05-22T18:25:09.933Z_

<details><summary>↩ Tool result · `toolu_01WsHDvvEMpV8Dc2hhQ26hQJ`</summary>

```text
discussion.tex
experiment_setup.tex
experiments.tex
main.tex
method.tex
references.bib
references.tex
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "bf012bd2-d40d-4d6e-8d93-e74fbb435584",
  "tool_use_result": {
    "stdout": "discussion.tex\nexperiment_setup.tex\nexperiments.tex\nmain.tex\nmethod.tex\nreferences.bib\nreferences.tex\nrelated_work.tex",
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

_source line 23_

<details open><summary>🔧 Tool call — Write · `toolu_0114rri3hH9rY11JKe3AtBMU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "content": "\n\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\\% of tasks but achieves only 78.0\\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\\%. One task yields 100\\% task success with only 32.5\\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.\n\nAuxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\\cite{li2026spatialforcing, yuan2025depthvla, liu2025occvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\\cite{hu2025vlsa} or constrained reinforcement learning~\\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.\n\nWe present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under five conditions that systematically vary gradient flow and label content: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), and Depth (egocentric depth prediction) [PENDING DEPTH RESULTS]. We find that auxiliary gradient flow through the vision encoder is the dominant mechanism behind collision avoidance improvement, while label content plays a secondary role. Conditions with gradient flow---Random OCC (CAR 0.806, 2 seeds) and Full OCC (0.797, 3 seeds)---outperform Vanilla (0.780, 3 seeds), while Detach OCC (0.745, 2 seeds), which blocks encoder gradients, falls 3.5 percentage points below Vanilla. That random labels perform comparably to real occupancy labels (difference of 0.9pp, directionally consistent across seeds but preliminary at current sample sizes) suggests that gradient flow regularization, rather than spatial information, is the primary driver. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Mechanism identification.} We provide evidence that auxiliary gradient flow regularization is the dominant mechanism behind collision avoidance improvements in VLA fine-tuning. Gradient flow is necessary: removing it (Detach OCC) degrades CAR by 3.5pp below the no-auxiliary Vanilla baseline (0.745 vs.\\ 0.780, 2 and 3 seeds respectively). Spatial label content is secondary: random labels achieve comparable CAR to ground-truth occupancy labels (0.806 vs.\\ 0.797, preliminary at 2--3 seeds per condition).\n\n    \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.\n\n    \\item \\textbf{Practical guideline.} Attaching any auxiliary prediction head to the vision encoder during fine-tuning---even one trained on random labels---improves collision avoidance, provided gradients flow through the encoder. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.\n\\end{enumerate}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Across conditions with gradient flow, CAR improves by 1.7--2.6pp over Vanilla; blocking gradient flow reduces CAR by 3.5pp. Section~2 reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~3 describes the auxiliary head architectures and ablation design. Section~4 presents experimental results and mechanism analysis. Section~5 discusses implications, limitations, and connections to multi-task learning theory.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "29b0ce4f-2550-4166-973f-00a5453a11b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwBg4hNo4FLbyhZPcruh7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 58589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 254
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 24 · 2026-05-22T18:25:40.219Z_

<details><summary>↩ Tool result · `toolu_0114rri3hH9rY11JKe3AtBMU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "d4a1201e-6fc4-48a7-a66c-6248d8a82e47",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "content": "\n\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\\% of tasks but achieves only 78.0\\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\\%. One task yields 100\\% task success with only 32.5\\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.\n\nAuxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\\cite{li2026spatialforcing, yuan2025depthvla, liu2025occvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\\cite{hu2025vlsa} or constrained reinforcement learning~\\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.\n\nWe present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under five conditions that systematically vary gradient flow and label content: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), and Depth (egocentric depth prediction) [PENDING DEPTH RESULTS]. We find that auxiliary gradient flow through the vision encoder is the dominant mechanism behind collision avoidance improvement, while label content plays a secondary role. Conditions with gradient flow---Random OCC (CAR 0.806, 2 seeds) and Full OCC (0.797, 3 seeds)---outperform Vanilla (0.780, 3 seeds), while Detach OCC (0.745, 2 seeds), which blocks encoder gradients, falls 3.5 percentage points below Vanilla. That random labels perform comparably to real occupancy labels (difference of 0.9pp, directionally consistent across seeds but preliminary at current sample sizes) suggests that gradient flow regularization, rather than spatial information, is the primary driver. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Mechanism identification.} We provide evidence that auxiliary gradient flow regularization is the dominant mechanism behind collision avoidance improvements in VLA fine-tuning. Gradient flow is necessary: removing it (Detach OCC) degrades CAR by 3.5pp below the no-auxiliary Vanilla baseline (0.745 vs.\\ 0.780, 2 and 3 seeds respectively). Spatial label content is secondary: random labels achieve comparable CAR to ground-truth occupancy labels (0.806 vs.\\ 0.797, preliminary at 2--3 seeds per condition).\n\n    \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.\n\n    \\item \\textbf{Practical guideline.} Attaching any auxiliary prediction head to the vision encoder during fine-tuning---even one trained on random labels---improves collision avoidance, provided gradients flow through the encoder. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.\n\\end{enumerate}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Across conditions with gradient flow, CAR improves by 1.7--2.6pp over Vanilla; blocking gradient flow reduces CAR by 3.5pp. Section~2 reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~3 describes the auxiliary head architectures and ablation design. Section~4 presents experimental results and mechanism analysis. Section~5 discusses implications, limitations, and connections to multi-task learning theory.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 25_

已写入 `introduction.tex`。结构：3 段开头（VLA safety gap → 两线脱节 → 本文 factorial study + 核心发现）→ 3 条 contributions（梯度流机制发现 / factorial ablation 设计 / 实践指南）→ 收尾段（实验设置 + 数据预览 + paper outline）。所有定量 claim 标注 seed 数和条件名，Random vs OCC 差异标记为 preliminary，Depth 标记 `[PENDING DEPTH RESULTS]`，引用均来自 `references.bib` 已有 cite key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "uuid": "30c83406-507e-4eaa-b6a2-86e191fca509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLgYSKvZbhybSEuRY9zzoa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1361,
      "cache_read_input_tokens": 58843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1361
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

_source line 26_

已写入 `introduction.tex`。结构：3 段开头（VLA safety gap → 两线脱节 → 本文 factorial study + 核心发现）→ 3 条 contributions（梯度流机制发现 / factorial ablation 设计 / 实践指南）→ 收尾段（实验设置 + 数据预览 + paper outline）。所有定量 claim 标注 seed 数和条件名，Random vs OCC 差异标记为 preliminary，Depth 标记 `[PENDING DEPTH RESULTS]`，引用均来自 `references.bib` 已有 cite key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 192936,
  "duration_api_ms": 193908,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "969b81cb-2a70-4713-aa98-248bdce8d7ba",
  "total_cost_usd": 0.6263457499999999,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 48363,
    "cache_read_input_tokens": 205566,
    "output_tokens": 8752,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48363,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 173,
        "cache_read_input_tokens": 58843,
        "cache_creation_input_tokens": 1361,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1361
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2364,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0024590000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 8752,
      "cacheReadInputTokens": 205566,
      "cacheCreationInputTokens": 48363,
      "webSearchRequests": 0,
      "costUSD": 0.6238867499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "53a1e424-e7cb-43b5-976b-fe056bbb5ed1"
}
```

</details>

---
