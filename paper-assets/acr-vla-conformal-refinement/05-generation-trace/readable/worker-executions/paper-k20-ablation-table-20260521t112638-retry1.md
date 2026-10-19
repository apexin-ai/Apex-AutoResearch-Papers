# paper k20 ablation table 20260521T112638 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_k20-ablation-table_20260521T112638_retry1.log`
- **Structured JSON:** [`ee68f585197b213d7c7f.json`](../../sessions/ee/ee68f585197b213d7c7f.json)

## Before a recorded user message

37 recorded events

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
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "861a31f3-96ad-4ea7-afe6-94e54633fd26",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779379800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2d9ee89e-3007-4f56-92ea-5bfc334c6782",
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "b707eaa2-1785-464a-893e-be74f485f366",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BhTVdU7v7gAkrttD1ZbeZ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14629,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14629
      },
      "output_tokens": 0,
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

<details open><summary>🔧 Tool call — Bash · `toolu_019nFVLTcECsT8NmgK3QqCf6`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "9398fe53-e23c-4e20-aba5-af27a31d1a36",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BhTVdU7v7gAkrttD1ZbeZ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14629,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14629
      },
      "output_tokens": 0,
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

_source line 6 · 2026-05-21T11:26:56.136Z_

<details><summary>↩ Tool result · `toolu_019nFVLTcECsT8NmgK3QqCf6`</summary>

```text
total 32
drwxr-xr-x  3 ubuntu ubuntu 4096 May 15 19:11 .
drwxr-xr-x 11 ubuntu ubuntu 4096 May 21 10:54 ..
-rw-r--r--  1 ubuntu ubuntu 5934 May 15 19:11 figure_plan.md
-rw-r--r--  1 ubuntu ubuntu 9281 May 15 19:10 outline.md
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 19:11 sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "3363c526-d314-48f6-a440-24c53c11f260",
  "tool_use_result": {
    "stdout": "total 32\ndrwxr-xr-x  3 ubuntu ubuntu 4096 May 15 19:11 .\ndrwxr-xr-x 11 ubuntu ubuntu 4096 May 21 10:54 ..\n-rw-r--r--  1 ubuntu ubuntu 5934 May 15 19:11 figure_plan.md\n-rw-r--r--  1 ubuntu ubuntu 9281 May 15 19:10 outline.md\ndrwxr-xr-x  2 ubuntu ubuntu 4096 May 15 19:11 sections",
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

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01BZbNPyHUKu6HQqqgJx5hSB`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "ac3bc6bc-448b-4a63-8647-6a76c6e51635",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012TPeYNxa9C6NfRpnhhG8kz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 30870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 384
      },
      "output_tokens": 68,
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

_source line 8 · 2026-05-21T11:26:58.881Z_

<details><summary>↩ Tool result · `toolu_01BZbNPyHUKu6HQqqgJx5hSB`</summary>

```text
total 16
drwxr-xr-x 2 ubuntu ubuntu 4096 May 15 19:11 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 15 19:11 ..
-rw-r--r-- 1 ubuntu ubuntu 8090 May 15 19:11 related_work.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "617be21b-5003-4dbe-890e-3a2ab03b0da7",
  "tool_use_result": {
    "stdout": "total 16\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 15 19:11 .\ndrwxr-xr-x 3 ubuntu ubuntu 4096 May 15 19:11 ..\n-rw-r--r-- 1 ubuntu ubuntu 8090 May 15 19:11 related_work.md",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "23d12ca7-cfc8-4c9f-868f-a230b6b76c92",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DFaaLbwZnPsgMCRNNMvSxt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 31254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
      },
      "output_tokens": 71,
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01112vKRjMMk5qENEA8EGVS9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "c902c01a-1867-4511-8285-8d5fe5204dbc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DFaaLbwZnPsgMCRNNMvSxt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 31254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
      },
      "output_tokens": 71,
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

_source line 11 · 2026-05-21T11:27:02.016Z_

<details><summary>↩ Tool result · `toolu_01112vKRjMMk5qENEA8EGVS9`</summary>

```text
1	# ACR-VLA: Observation-Conditioned Learned Correction for Robust Vision-Language-Action Models
2	
3	**Target**: CoRL 2026 (Abstract DDL ~May 26, Full paper DDL ~Jun 2)
4	**Format**: 8 pages + references, CoRL template
5	
6	---
7	
8	## Title Candidates
9	
10	1. **ACR-VLA: Sample-Then-Correct — Observation-Conditioned Action Refinement for Robust Vision-Language-Action Models**
11	2. **Beyond Sample Selection: Learned Action Correction Improves VLA Robustness Under Distribution Shift**
12	3. **When Conformal Features Fail: Observation-Conditioned Correction for Vision-Language-Action Models**
13	
14	---
15	
16	## 1. Introduction (~1.5 pages)
17	
18	**Key points**:
19	- Flow-matching VLAs (pi0, SmolVLA) achieve near-saturation on standard benchmarks (97-99%) but exhibit robustness gaps under distribution shift (LIBERO-Plus)
20	- Existing inference-time approaches: sample selection only (ReconVLA), task-level RL (SC-VLA), high-latency verifiers (VLA-Pilot 2.41s/step) — none explore learned action correction on frozen VLAs
21	- Our contribution: **sample-then-correct pipeline** — conformal sample selection (K=10) followed by a lightweight observation-conditioned Conformal Refinement Module (CRM, ~250K params, ~3ms overhead)
22	- Three findings:
23	  1. Sample-then-correct > sample-then-select: obs_only CRM +7pp over argmin on LIBERO object (19% vs 12%, exp: `eval-acr-object-v4-obs-only` vs `eval-argmin-only-object`)
24	  2. Observation features > conformal features for correction conditioning (honest negative: per-DOF conformal features ≈ argmin, exp: `eval-acr-object-v4-small`)
25	  3. Correction magnitude control is critical and previously unrecognized — norm=1.42 → 0%, norm=0.1 → 19% (exp: `eval-acr-spatial-v4-default-r3`, magnitude sweep D032)
26	
27	**Figure**: Fig. 1 — Pipeline overview diagram (sample → conformal selection → CRM correction → execution)
28	
29	---
30	
31	## 2. Related Work (~1.5 pages)
32	
33	→ See `paper/sections/related_work.md` for full draft.
34	
35	Three subsections:
36	- (a) VLA Robustness and Inference-Time Adaptation
37	- (b) Conformal Prediction in Robotics
38	- (c) Residual Correction and Learned Action Refinement
39	
40	---
41	
42	## 3. Method (~2 pages)
43	
44	### 3.1 Problem Setup and Notation
45	- Frozen VLA policy π_θ generating K action samples via flow matching
46	- Distribution shift setting: train on nominal env, deploy under perturbation (LIBERO-Plus object/spatial)
47	- Goal: inference-time module that improves closed-loop success without retraining π_θ
48	
49	### 3.2 Conformal Sample Selection
50	- Generate K=10 action samples from flow-matching VLA
51	- Compute nonconformity scores (CGS-based Mahalanobis scoring [Braun et al., 2025])
52	- Select best sample via argmin nonconformity score
53	- This stage approximates ReconVLA's selection strategy — serves as our primary baseline
54	
55	**Key refs**: [Angelopoulos & Bates, 2023], [Braun et al., 2025], [Chen et al., 2026]
56	
57	### 3.3 Conformal Refinement Module (CRM)
58	- Architecture: lightweight MLP (~250K params) mapping conditioning features → action residual δ
59	- Output: a_corrected = a_selected + clip(δ, norm_max)
60	- **CRM Variants** (systematic ablation):
61	  - **obs_only**: conditions on VLA observation features (image + language embeddings)
62	  - **perdof**: conditions on per-DOF conformal statistics (interval widths, coverage indicators per action dimension)
63	  - **scalar**: conditions on scalar conformal score only
64	- Training: offline L2 regression on calibration set, predicting residual to expert action
65	- Magnitude control: clip correction norm to norm_max (key hyperparameter)
66	
67	**Figure**: Fig. 2 — CRM architecture diagram showing obs_only vs perdof vs scalar conditioning paths
68	
69	### 3.4 Correction Magnitude Control
70	- Unbounded correction (norm=1.42) → catastrophic failure (0% SR)
71	- Observation-conditioned CRM robust across norm ∈ [0.03, 0.3]
72	- Per-DOF CRM collapses at norm ≥ 0.2
73	- Hypothesis: per-DOF features produce overconfident directional corrections that compound at high magnitude
74	
75	---
76	
77	## 4. Experiments (~2.5 pages)
78	
79	### 4.1 Experimental Setup
80	- **Backbone**: SmolVLA (450M params, flow matching) [Shukor et al., 2025]
81	- **Benchmark**: LIBERO-Plus [Fei et al., 2025] — spatial (position perturbation) and object (object substitution) suites, 10 tasks each
82	- **Evaluation**: 10 rollouts per task, success rate (SR), 2 seeds (seed=42, seed=43)
83	- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10, perdof CRM, scalar CRM, obs_only CRM
84	- **Statistical tests**: Fisher exact test on combined seeds (200 trials), bootstrap CI
85	
86	### 4.2 Main Results: Object Manipulation (Main Story)
87	
88	**Table 1**: Object benchmark 10-task success rates (seed=42 FINAL + seed=43 pending)
89	
90	| Method | SR (seed=42) | Δ vs argmin | exp_id |
91	|--------|-------------|-------------|--------|
92	| obs_only 0.1 | **19.0%** | **+7.0pp** | `eval-acr-object-v4-obs-only` |
93	| obs_only 0.2 | 18.0% (5/10) | +6.0pp | running |
94	| argmin K=10 | 12.0% | baseline | `eval-argmin-only-object` |
95	| VLA-only K=1 | 12.0% | 0pp | `eval-vla-only-object-k1` |
96	| VLA-mean K=10 | 12.0% | 0pp | — |
97	| perdof 0.1 | 11.0% | -1.0pp | `eval-acr-object-v4-small` |
98	| scalar 0.1 | 9.0% | -3.0pp | `eval-acr-object-v4-scalar` |
99	
100	**Key message**: obs_only CRM is the only method that significantly improves over sample selection. Per-DOF conformal features and scalar scores fail to provide useful correction signal.
101	
102	**Figure**: Fig. 3 — Bar chart comparing all 6 methods on object benchmark (with error bars from seed=43)
103	
104	### 4.3 Spatial Manipulation: An Honest Negative Result
105	
106	**Table 2**: Spatial benchmark 10-task success rates (LOCKED)
107	
108	| Method | SR | Δ vs argmin | exp_id |
109	|--------|-----|-------------|--------|
110	| obs_only 0.1 | 35% | +1pp | `eval-acr-spatial-v4-obs-only-r3` |
111	| perdof 0.1 | 35% | +1pp | `eval-acr-spatial-v4-small-r2` |
112	| argmin K=10 | 34% | baseline | `eval-argmin-only-spatial-r2` |
113	| scalar 0.1 | 32% | -2pp | `eval-acr-spatial-v4-scalar` |
114	| VLA-mean K=10 | 32% | -2pp | — |
115	| VLA-only K=1 | 30% | -4pp | — |
116	
117	**Key message**: No CRM variant helps on spatial tasks. Hypothesis: spatial perturbation (position offset) causes fundamentally different error modes that action correction cannot address — requires re-planning, not action refinement. Object substitution creates correctable action distribution shifts.
118	
119	### 4.4 Correction Magnitude Sensitivity (Key Empirical Contribution)
120	
121	**Table 3 / Figure**: Magnitude sweep on spatial (4 norm values × 2 CRM variants)
122	
123	| norm | obs_only SR | perdof SR | gap | exp_id |
124	|------|------------|-----------|-----|--------|
125	| 0.03 | 55.0% (4t) | 30.0% (10t) | +25pp* | magnitude sweep D032 |
126	| 0.05 | 35.0% (10t) | 31.0% (10t) | +4.0pp | `eval-mag-obsonly-norm005` |
127	| 0.2 | 35.0% (10t) | 28.3% (6t) | +6.7pp | `eval-mag-obsonly-norm02` |
128	| 0.3 | 36.0% (10t) | 26.0% (10t) | +10pp | `eval-mag-perdof-norm03` |
129	
130	**Figure**: Fig. 4 — Line plot: SR vs correction norm for obs_only and perdof. obs_only flat, perdof declining.
131	
132	**Key message**: obs_only CRM maintains stable performance across 10× range of correction magnitudes. perdof CRM collapses at high norm → overconfident directional corrections from noisy per-DOF features.
133	
134	### 4.5 Statistical Significance (seed=43 results, pending)
135	- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)
136	- Per-task breakdown showing consistency
137	- Bootstrap 95% CI for success rate differences
138	
139	---
140	
141	## 5. Discussion (~0.5 pages)
142	
143	### Why obs_only works and perdof doesn't
144	- Observation embeddings encode task-relevant semantic information (object identity, spatial layout) that is stable across distribution shifts
145	- Per-DOF conformal statistics estimated from K=10 samples are noisy — covariance estimation from 10 samples in 7D action space is ill-conditioned
146	- Magnitude sweep evidence: perdof collapses at high norm = CRM learns overconfident corrections from noisy per-DOF features; obs_only corrections remain conservative/stable
147	- Connection to literature: [Ovadia et al., 2019] show UQ degrades under shift; [Sampson et al., 2024] show per-dimension marginal CP loses inter-DOF coherence
148	
149	### Limitations
150	- Simulation only (LIBERO); real-robot transfer untested
151	- SmolVLA backbone only; generalization to other VLAs (OpenVLA, pi0) untested
152	- Spatial tasks show no improvement — CRM cannot address perturbations requiring re-planning
153	- CRM trained per-benchmark (not zero-shot); requires calibration data from target distribution
154	
155	### Future Work
156	- Real-robot experiments
157	- Adaptive magnitude scheduling (decay over episode, uncertainty-conditioned)
158	- Combining with training-time robustness methods (SRPO, RobustVLA)
159	- Multi-VLA evaluation
160	
161	---
162	
163	## 6. Conclusion (~0.25 pages)
164	- First systematic study of inference-time learned action correction for frozen VLAs
165	- Sample-then-correct > sample-then-select (+7pp on LIBERO object)
166	- Observation features > conformal features for correction conditioning (honest negative)
167	- Correction magnitude control is critical and previously unrecognized
168	
169	---
170	
171	## Appendix (supplementary)
172	- Per-task breakdown tables (all 10 tasks × all methods)
173	- CRM training details (architecture, hyperparameters, training data)
174	- Conformal prediction background (CGS, nonconformity scores)
175	- Additional magnitude sweep results
176	- Compute analysis (K=10 overhead, CRM inference time)
177	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "742211bd-da91-4cff-81e5-44f7cf662b16",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md",
      "content": "# ACR-VLA: Observation-Conditioned Learned Correction for Robust Vision-Language-Action Models\n\n**Target**: CoRL 2026 (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\n**Format**: 8 pages + references, CoRL template\n\n---\n\n## Title Candidates\n\n1. **ACR-VLA: Sample-Then-Correct — Observation-Conditioned Action Refinement for Robust Vision-Language-Action Models**\n2. **Beyond Sample Selection: Learned Action Correction Improves VLA Robustness Under Distribution Shift**\n3. **When Conformal Features Fail: Observation-Conditioned Correction for Vision-Language-Action Models**\n\n---\n\n## 1. Introduction (~1.5 pages)\n\n**Key points**:\n- Flow-matching VLAs (pi0, SmolVLA) achieve near-saturation on standard benchmarks (97-99%) but exhibit robustness gaps under distribution shift (LIBERO-Plus)\n- Existing inference-time approaches: sample selection only (ReconVLA), task-level RL (SC-VLA), high-latency verifiers (VLA-Pilot 2.41s/step) — none explore learned action correction on frozen VLAs\n- Our contribution: **sample-then-correct pipeline** — conformal sample selection (K=10) followed by a lightweight observation-conditioned Conformal Refinement Module (CRM, ~250K params, ~3ms overhead)\n- Three findings:\n  1. Sample-then-correct > sample-then-select: obs_only CRM +7pp over argmin on LIBERO object (19% vs 12%, exp: `eval-acr-object-v4-obs-only` vs `eval-argmin-only-object`)\n  2. Observation features > conformal features for correction conditioning (honest negative: per-DOF conformal features ≈ argmin, exp: `eval-acr-object-v4-small`)\n  3. Correction magnitude control is critical and previously unrecognized — norm=1.42 → 0%, norm=0.1 → 19% (exp: `eval-acr-spatial-v4-default-r3`, magnitude sweep D032)\n\n**Figure**: Fig. 1 — Pipeline overview diagram (sample → conformal selection → CRM correction → execution)\n\n---\n\n## 2. Related Work (~1.5 pages)\n\n→ See `paper/sections/related_work.md` for full draft.\n\nThree subsections:\n- (a) VLA Robustness and Inference-Time Adaptation\n- (b) Conformal Prediction in Robotics\n- (c) Residual Correction and Learned Action Refinement\n\n---\n\n## 3. Method (~2 pages)\n\n### 3.1 Problem Setup and Notation\n- Frozen VLA policy π_θ generating K action samples via flow matching\n- Distribution shift setting: train on nominal env, deploy under perturbation (LIBERO-Plus object/spatial)\n- Goal: inference-time module that improves closed-loop success without retraining π_θ\n\n### 3.2 Conformal Sample Selection\n- Generate K=10 action samples from flow-matching VLA\n- Compute nonconformity scores (CGS-based Mahalanobis scoring [Braun et al., 2025])\n- Select best sample via argmin nonconformity score\n- This stage approximates ReconVLA's selection strategy — serves as our primary baseline\n\n**Key refs**: [Angelopoulos & Bates, 2023], [Braun et al., 2025], [Chen et al., 2026]\n\n### 3.3 Conformal Refinement Module (CRM)\n- Architecture: lightweight MLP (~250K params) mapping conditioning features → action residual δ\n- Output: a_corrected = a_selected + clip(δ, norm_max)\n- **CRM Variants** (systematic ablation):\n  - **obs_only**: conditions on VLA observation features (image + language embeddings)\n  - **perdof**: conditions on per-DOF conformal statistics (interval widths, coverage indicators per action dimension)\n  - **scalar**: conditions on scalar conformal score only\n- Training: offline L2 regression on calibration set, predicting residual to expert action\n- Magnitude control: clip correction norm to norm_max (key hyperparameter)\n\n**Figure**: Fig. 2 — CRM architecture diagram showing obs_only vs perdof vs scalar conditioning paths\n\n### 3.4 Correction Magnitude Control\n- Unbounded correction (norm=1.42) → catastrophic failure (0% SR)\n- Observation-conditioned CRM robust across norm ∈ [0.03, 0.3]\n- Per-DOF CRM collapses at norm ≥ 0.2\n- Hypothesis: per-DOF features produce overconfident directional corrections that compound at high magnitude\n\n---\n\n## 4. Experiments (~2.5 pages)\n\n### 4.1 Experimental Setup\n- **Backbone**: SmolVLA (450M params, flow matching) [Shukor et al., 2025]\n- **Benchmark**: LIBERO-Plus [Fei et al., 2025] — spatial (position perturbation) and object (object substitution) suites, 10 tasks each\n- **Evaluation**: 10 rollouts per task, success rate (SR), 2 seeds (seed=42, seed=43)\n- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10, perdof CRM, scalar CRM, obs_only CRM\n- **Statistical tests**: Fisher exact test on combined seeds (200 trials), bootstrap CI\n\n### 4.2 Main Results: Object Manipulation (Main Story)\n\n**Table 1**: Object benchmark 10-task success rates (seed=42 FINAL + seed=43 pending)\n\n| Method | SR (seed=42) | Δ vs argmin | exp_id |\n|--------|-------------|-------------|--------|\n| obs_only 0.1 | **19.0%** | **+7.0pp** | `eval-acr-object-v4-obs-only` |\n| obs_only 0.2 | 18.0% (5/10) | +6.0pp | running |\n| argmin K=10 | 12.0% | baseline | `eval-argmin-only-object` |\n| VLA-only K=1 | 12.0% | 0pp | `eval-vla-only-object-k1` |\n| VLA-mean K=10 | 12.0% | 0pp | — |\n| perdof 0.1 | 11.0% | -1.0pp | `eval-acr-object-v4-small` |\n| scalar 0.1 | 9.0% | -3.0pp | `eval-acr-object-v4-scalar` |\n\n**Key message**: obs_only CRM is the only method that significantly improves over sample selection. Per-DOF conformal features and scalar scores fail to provide useful correction signal.\n\n**Figure**: Fig. 3 — Bar chart comparing all 6 methods on object benchmark (with error bars from seed=43)\n\n### 4.3 Spatial Manipulation: An Honest Negative Result\n\n**Table 2**: Spatial benchmark 10-task success rates (LOCKED)\n\n| Method | SR | Δ vs argmin | exp_id |\n|--------|-----|-------------|--------|\n| obs_only 0.1 | 35% | +1pp | `eval-acr-spatial-v4-obs-only-r3` |\n| perdof 0.1 | 35% | +1pp | `eval-acr-spatial-v4-small-r2` |\n| argmin K=10 | 34% | baseline | `eval-argmin-only-spatial-r2` |\n| scalar 0.1 | 32% | -2pp | `eval-acr-spatial-v4-scalar` |\n| VLA-mean K=10 | 32% | -2pp | — |\n| VLA-only K=1 | 30% | -4pp | — |\n\n**Key message**: No CRM variant helps on spatial tasks. Hypothesis: spatial perturbation (position offset) causes fundamentally different error modes that action correction cannot address — requires re-planning, not action refinement. Object substitution creates correctable action distribution shifts.\n\n### 4.4 Correction Magnitude Sensitivity (Key Empirical Contribution)\n\n**Table 3 / Figure**: Magnitude sweep on spatial (4 norm values × 2 CRM variants)\n\n| norm | obs_only SR | perdof SR | gap | exp_id |\n|------|------------|-----------|-----|--------|\n| 0.03 | 55.0% (4t) | 30.0% (10t) | +25pp* | magnitude sweep D032 |\n| 0.05 | 35.0% (10t) | 31.0% (10t) | +4.0pp | `eval-mag-obsonly-norm005` |\n| 0.2 | 35.0% (10t) | 28.3% (6t) | +6.7pp | `eval-mag-obsonly-norm02` |\n| 0.3 | 36.0% (10t) | 26.0% (10t) | +10pp | `eval-mag-perdof-norm03` |\n\n**Figure**: Fig. 4 — Line plot: SR vs correction norm for obs_only and perdof. obs_only flat, perdof declining.\n\n**Key message**: obs_only CRM maintains stable performance across 10× range of correction magnitudes. perdof CRM collapses at high norm → overconfident directional corrections from noisy per-DOF features.\n\n### 4.5 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences\n\n---\n\n## 5. Discussion (~0.5 pages)\n\n### Why obs_only works and perdof doesn't\n- Observation embeddings encode task-relevant semantic information (object identity, spatial layout) that is stable across distribution shifts\n- Per-DOF conformal statistics estimated from K=10 samples are noisy — covariance estimation from 10 samples in 7D action space is ill-conditioned\n- Magnitude sweep evidence: perdof collapses at high norm = CRM learns overconfident corrections from noisy per-DOF features; obs_only corrections remain conservative/stable\n- Connection to literature: [Ovadia et al., 2019] show UQ degrades under shift; [Sampson et al., 2024] show per-dimension marginal CP loses inter-DOF coherence\n\n### Limitations\n- Simulation only (LIBERO); real-robot transfer untested\n- SmolVLA backbone only; generalization to other VLAs (OpenVLA, pi0) untested\n- Spatial tasks show no improvement — CRM cannot address perturbations requiring re-planning\n- CRM trained per-benchmark (not zero-shot); requires calibration data from target distribution\n\n### Future Work\n- Real-robot experiments\n- Adaptive magnitude scheduling (decay over episode, uncertainty-conditioned)\n- Combining with training-time robustness methods (SRPO, RobustVLA)\n- Multi-VLA evaluation\n\n---\n\n## 6. Conclusion (~0.25 pages)\n- First systematic study of inference-time learned action correction for frozen VLAs\n- Sample-then-correct > sample-then-select (+7pp on LIBERO object)\n- Observation features > conformal features for correction conditioning (honest negative)\n- Correction magnitude control is critical and previously unrecognized\n\n---\n\n## Appendix (supplementary)\n- Per-task breakdown tables (all 10 tasks × all methods)\n- CRM training details (architecture, hyperparameters, training data)\n- Conformal prediction background (CGS, nonconformity scores)\n- Additional magnitude sweep results\n- Compute analysis (K=10 overhead, CRM inference time)\n",
      "numLines": 177,
      "startLine": 1,
      "totalLines": 177
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "9d99a0c4-2205-45ec-b5d8-ccd3e29a9da9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PcKZY6Jqo4zA5vEi1cxLwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4602,
      "cache_read_input_tokens": 31525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4602
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014En5DrRgzAkKHcPMf2F9q3`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "5a5b40a8-0dee-4ef4-940f-8f28cbba4bfa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PcKZY6Jqo4zA5vEi1cxLwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4602,
      "cache_read_input_tokens": 31525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4602
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

_source line 14 · 2026-05-21T11:27:10.304Z_

<details><summary>↩ Tool result · `toolu_014En5DrRgzAkKHcPMf2F9q3`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

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
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "9a2efbf2-36e9-4d30-a042-99d062e82358",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018mZoyEGAy9Uk3v5tEAWXme`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "tags": [
      "k20"
    ]
  },
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "fe03cb75-7c10-49dc-9850-be806237ebde",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GuhqxALvVNNKbxJHM61gBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 22399,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22399
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 32461
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T11:27:16.406Z_

<details><summary>↩ Tool result · `toolu_018mZoyEGAy9Uk3v5tEAWXme`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.426}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "166bf51a-8bf4-4ce9-b4bb-d9cceaad8388",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.426}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.426}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RkM5S7P1nuw6qXbiJhczB7`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "LOCKED"
  },
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "4deb7947-3ca3-45c3-8ce1-31d8d3a42cb8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LhWTQvAi87a7axfZr4pTH2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 38733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 251
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

_source line 18 · 2026-05-21T11:27:20.623Z_

<details><summary>↩ Tool result · `toolu_01RkM5S7P1nuw6qXbiJhczB7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3146}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "2bbdd70c-f747-4106-94b9-2d368ebf0d26",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.3146}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3146}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Y8HsT28hocU3B9XMhDygq8`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "35bfd666-f843-49af-acc0-ec39104c807b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DbbjcAVCHNAHdC2Fpgge8k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 38984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 20 · 2026-05-21T11:27:24.861Z_

<details><summary>↩ Tool result · `toolu_01Y8HsT28hocU3B9XMhDygq8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T10:19:18.528Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T10:19:09.036Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T10:18:58.812Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-21T10:18:48.305Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-21T10:18:37.555Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-21T10:18:27.592Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"notes\": \"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\", \"conclusion\": \"killed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T07:09:59.922Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"notes\": \"LOW-PRIORITY: may be killed when π0.5 fix passes quick verify. GPU 0 on bjb2-28827, tmux session: spatial_obs_only_s45\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-21T05:22:58.984Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:31.173Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"notes\": \"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:00.886Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:13:12.047Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"notes\": \"[2026-05-21 修正] 之前的\\\"task 9/10 异常退出\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-21T05:07:12.893Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-21T05:07:10.342Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-21T05:07:08.046Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:47:49.745Z\", \"updated_at\": \"2026-05-21T05:07:05.713Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601): tests K=20 vs K=10 compute tradeoff.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:49.893Z\", \"updated_at\": \"2026-05-21T05:07:03.314Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed42. K-value sweep (plan_601): tests whether increasing from K=10 to K=20 further improves SR, justifying K=10 as compute-efficient choice.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:08.378Z\", \"updated_at\": \"2026-05-21T04:55:07.524Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed53. Multi-seed robustness for magnitude curve plan_500.\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-21T04:55:05.083Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:57.442Z\", \"updated_at\": \"2026-05-21T04:55:02.734Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=17% (17/100)，与 obs_only norm02 均值 (16.8%±1.8%) 一致。新增第 7 个 seed 数据点。\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:07:41.505Z\", \"updated_at\": \"2026-05-21T04:55:00.434Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:11.557Z\", \"updated_at\": \"2026-05-21T04:54:57.990Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-21T04:54:54.506Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-21T04:54:51.647Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-21T04:54:44.901Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-21T04:54:42.439Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:21.840Z\", \"updated_at\": \"2026-05-21T04:54:39.963Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"notes\": \"Partial result: killed at task 8/10 but SR=16% consistent with norm02 mean (16.8%). Reclassified from failed to success per Director instruction.\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-21T04:54:37.451Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:49:55.438Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"notes\": \"监控误报进程消失。实际正常完成 SR=14.0% (14/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.1_seed67.json (bjb1-18228，注意保存在 /root/logs/ 而非项目 logs/)。进程在完成后自然退出，非异常终止。\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-21T04:48:32.810Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-21T04:48:27.282Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\", \"notes\": \"Experiment completed successfully but stuck in ANALYZING >24h. Manual resolution on 2026-05-21: JSON output confirmed complete (10 tasks × 10 rollouts = 100 total). Overall SR=10%. Per-task SR range: 0.0-0.2.\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:31.390Z\", \"updated_at\": \"2026-05-21T04:48:15.442Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:31:32.794Z\", \"updated_at\": \"2026-05-21T04:48:05.210Z\", \"hypothesis\": \"VLA-only baseline seed46 on LIBERO-Object. 第 5 个 VLA-only seed 补全 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-21T04:47:51.213Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-21T04:47:46.335Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:49.074Z\", \"updated_at\": \"2026-05-21T04:47:42.399Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-21T04:47:36.667Z\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\", \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-21T04:47:19.616Z\", \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:15.856Z\", \"updated_at\": \"2026-05-21T04:46:30.740Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}, \"notes\": \"Cron false positive — 实际正常完成 SR=35.0% (35/100), trigger_rate=98.0%, mean_unc=0.2619。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:37:28.279Z\", \"updated_at\": \"2026-05-21T04:45:27.640Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:13.764Z\", \"updated_at\": \"2026-05-21T04:44:12.088Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}, \"notes\": \"Cron false positive — 实际正常完成 SR=34.0% (34/100), trigger_rate=97.6%, mean_unc=0.2679。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:17.907Z\", \"updated_at\": \"2026-05-21T04:42:43.669Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:51.140Z\", \"updated_at\": \"2026-05-21T04:42:32.790Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:25:56.030Z\", \"updated_at\": \"2026-05-21T04:34:43.303Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\", \"notes\": \"Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts = 100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only baseline 相当，确认 random selection 无法有效利用 K=10 candidates。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:52.130Z\", \"updated_at\": \"2026-05-21T04:34:38.177Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T04:34:04.735Z\", \"updated_at\": \"2026-05-21T04:34:32.245Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:18:47.309Z\", \"updated_at\": \"2026-05-21T04:32:53.123Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed50. 补齐 Spatial baseline 样本量，与 CRM Spatial 配对统计检验。\", \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:58.271Z\", \"updated_at\": \"2026-05-21T04:32:42.275Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed50. 补齐 Spatial CRM 样本量 (n→7+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:47.989Z\", \"updated_at\": \"2026-05-21T04:32:32.158Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed49. 补齐 Spatial CRM 样本量 (n→6+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:30.715Z\", \"updated_at\": \"2026-05-21T04:32:24.008Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed44. K=20 第三个 seed，n=3 可报告 error bars，确认 K-value diminishing returns。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:28.230Z\", \"updated_at\": \"2026-05-21T04:32:17.159Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed43. K=20 第二个 seed，与 K=10 seed43 配对，增强 K-value curve K=20 端的统计可靠性。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-21T04:32:11.044Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed42. 扩展 K-value curve 到 K=20，验证收益曲线在 K=10→K=20 段是否趋平（预期 ≤+1pp over K=10 的 17.6%）。用 K=10 训练的 CRM 模型，eval 时生成 20 个 VLA 样本。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T04:01:22.020Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed60. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T03:59:27.286Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\", \"notes\": \"PID 802634(旧)→802639(旧,killed)→811006(r2,MEAN_STD fix). Dual process conflict resolved. Monitoring until task 5.\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:57:48.001Z\", \"updated_at\": \"2026-05-21T03:33:43.610Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:33.689Z\", \"updated_at\": \"2026-05-21T03:30:13.218Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed54. Norm sweep: filling ε=0.1 gap, bringing n to 7+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:31.269Z\", \"updated_at\": \"2026-05-21T03:30:10.368Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed53. Norm sweep: filling ε=0.1 gap, bringing n to 6+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:23.747Z\", \"updated_at\": \"2026-05-21T03:30:07.112Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 5+.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判。已手动修正。\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:04.127Z\", \"updated_at\": \"2026-05-21T03:30:04.361Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:20.171Z\", \"updated_at\": \"2026-05-21T03:29:59.855Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed49. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:39.518Z\", \"updated_at\": \"2026-05-21T03:29:57.231Z\", \"hypothesis\": \"CRM obs_only with ε=0.1 and K=10 on LIBERO-Object seed48. Low-norm data point for plan_500 magnitude curve, strengthening Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-21T03:29:54.309Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:51.040Z\", \"updated_at\": \"2026-05-21T03:29:47.720Z\", \"hypothesis\": \"obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标准化到 n_rollouts=10 与其他 seed 一致。当前 obs_only ε=0.1 有 5 seeds。\", \"parent\": \"eval-obs-only-object-norm01-seed45\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-21T03:29:43.639Z\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:23:01.005Z\", \"updated_at\": \"2026-05-21T03:29:41.343Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:35.665Z\", \"updated_at\": \"2026-05-21T03:29:39.045Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed50. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:27.458Z\", \"updated_at\": \"2026-05-21T03:29:36.190Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。日志在 bjb1-32546。\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-21T03:29:30.312Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-21T03:29:23.229Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-21T03:29:16.871Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:27.742Z\", \"updated_at\": \"2026-05-21T03:29:14.257Z\", \"hypothesis\": \"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-21T03:29:10.509Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:04.999Z\", \"updated_at\": \"2026-05-21T03:29:06.231Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:02.708Z\", \"updated_at\": \"2026-05-21T03:29:02.399Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed on bjb1-18228). C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:34.507Z\", \"updated_at\": \"2026-05-21T03:28:57.483Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed46. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive: 实验正常完成 SR=15.0%, JSON 已写入。进程退出后 cron 无 sentinel/W&B 标记 → 误判 failed。已修正 conclusion=success。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:01.117Z\", \"updated_at\": \"2026-05-21T03:28:48.787Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-21T03:28:46.427Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:45:20.860Z\", \"updated_at\": \"2026-05-21T03:28:43.998Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"parent\": \"eval-obs-only-object-norm003-seed43\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-21T03:28:41.514Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=14% (14/100)。norm003 magnitude curve 数据点，在 VLA-only (10.9%) 和 norm02 (16.8%) 之间。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:14:50.423Z\", \"updated_at\": \"2026-05-21T03:19:50.462Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed57. Norm sweep: additional ε=0.1 data point.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=19.0%。\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:19:48.034Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive confirmed. Output JSON 已存在 (1490 bytes)，日志显示正常完成。Overall SR=14.0% (14/100)。进程已退出，无异常。\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:00:59.021Z\", \"updated_at\": \"2026-05-21T03:19:45.881Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive（第N次）：eval 脚本正常完成但不写 sentinel/W&B，被 cron 误判 failed。实际 SR=15.0% (15/100)。手动修正 conclusion=success。\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:18.450Z\", \"updated_at\": \"2026-05-21T03:19:43.346Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=16.0%。\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:25:26.898Z\", \"updated_at\": \"2026-05-21T03:19:41.023Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed59. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=13.0%。\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:28:30.000Z\", \"updated_at\": \"2026-05-21T03:19:38.737Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:13.220Z\", \"updated_at\": \"2026-05-21T03:17:06.237Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:10.875Z\", \"updated_at\": \"2026-05-21T03:17:01.964Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:57:21.662Z\", \"updated_at\": \"2026-05-21T03:16:58.507Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.05 outlier verification.\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:08.600Z\", \"updated_at\": \"2026-05-21T03:16:54.862Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r3. Redo of killed seed63-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:58.578Z\", \"updated_at\": \"2026-05-21T03:16:49.849Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.05 has outlier seeds, expanding for variance verification.\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:06.396Z\", \"updated_at\": \"2026-05-21T03:16:44.624Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r3. Redo of killed seed62-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:54.184Z\", \"updated_at\": \"2026-05-21T03:16:34.818Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed78. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:50.541Z\", \"updated_at\": \"2026-05-21T03:16:26.327Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}}, \"count\": 100, \"total\": 567, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2795}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "f519f569-95dc-49e5-bc1e-80ffdce34702",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-pi05-vla-only-spatial-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:27.768Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:19:18.528Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\\\"}, \\\"eval-pi05-vla-only-spatial-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:25.180Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:19:09.036Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\\\"}, \\\"eval-pi05-vla-only-spatial-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:22.540Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:18:58.812Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\\\"}, \\\"eval-pi05-vla-only-object-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:19.985Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:18:48.305Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\\\"}, \\\"eval-pi05-vla-only-object-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:17.435Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:18:37.555Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\\\"}, \\\"eval-pi05-vla-only-object-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:14.823Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:18:27.592Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\\\"}, \\\"eval-pi05-baseline-object-seed42-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:30:28.663Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:02:33.602Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\\\", \\\"parent\\\": \\\"eval-pi05-baseline-object-seed42\\\", \\\"notes\\\": \\\"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k20-obs-only-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:11:50.702Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:47.255Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.34, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k20-obs-only-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:11:46.321Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:42.676Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.34, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k20-obs-only-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:11:41.832Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:37.114Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.35, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k20-obs-only-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T06:11:55.095Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:30:32.202Z\\\", \\\"hypothesis\\\": \\\"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.19, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"checkpoint_path\\\": \\\"obs_only_K10_eps02_default\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-spatial-obs-only-seed45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-21T07:09:30.589Z\\\", \\\"updated_at\\\": \\\"2026-05-21T07:09:59.922Z\\\", \\\"hypothesis\\\": \\\"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\\\", \\\"notes\\\": \\\"LOW-PRIORITY: may be killed when π0.5 fix passes quick verify. GPU 0 on bjb2-28827, tmux session: spatial_obs_only_s45\\\"}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T13:50:21.016Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:22:58.984Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm003-seed66\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T01:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:14:31.173Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.115, \\\"total_successes\\\": 23, \\\"total_rollouts\\\": 200, \\\"n_rollouts_per_task\\\": 20, \\\"n_tasks\\\": 10, \\\"output_json\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\\\"}, \\\"notes\\\": \\\"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\\\"}, \\\"eval-obs-only-object-norm01-seed66\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T01:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:14:00.886Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.135, \\\"total_successes\\\": 27, \\\"total_rollouts\\\": 200, \\\"n_rollouts_per_task\\\": 20, \\\"n_tasks\\\": 10, \\\"output_json\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\\\"}}, \\\"eval-obs-only-object-norm005-seed66\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T01:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:13:12.047Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\\\", \\\"notes\\\": \\\"[2026-05-21 修正] 之前的\\\\\\\"task 9/10 异常退出\\\\\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.11, \\\"total_successes\\\": 22, \\\"total_rollouts\\\": 200, \\\"n_rollouts_per_task\\\": 20, \\\"n_tasks\\\": 10, \\\"output_json\\\": \\\"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\\\"}}, \\\"eval-obs-only-object-norm003-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:10:29.526Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k20-obs-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T17:19:11.419Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:12.893Z\\\", \\\"hypothesis\\\": \\\"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}}, \\\"eval-k20-obs-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T15:31:55.966Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:10.342Z\\\", \\\"hypothesis\\\": \\\"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}}, \\\"eval-k20-obs-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T15:33:50.688Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:08.046Z\\\", \\\"hypothesis\\\": \\\"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.2}}, \\\"eval-crm-object-k20-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T08:47:49.745Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:05.713Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601): tests K=20 vs K=10 compute tradeoff.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}}, \\\"eval-crm-object-k20-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T08:02:49.893Z\\\", \\\"updated_at\\\": \\\"2026-05-21T05:07:03.314Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only K=20 on Object seed42. K-value sweep (plan_601): tests whether increasing from K=10 to K=20 further improves SR, justifying K=10 as compute-efficient choice.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.2}}, \\\"eval-obs-only-object-norm02-seed53\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T19:45:08.378Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:55:07.524Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}, \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed53. Multi-seed robustness for magnitude curve plan_500.\\\"}, \\\"eval-obs-only-object-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:06:16.022Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:55:05.083Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm02-seed51\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T17:31:57.442Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:55:02.734Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.17}, \\\"notes\\\": \\\"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=17% (17/100)，与 obs_only norm02 均值 (16.8%±1.8%) 一致。新增第 7 个 seed 数据点。\\\"}, \\\"eval-obs-only-object-norm02-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T13:07:41.505Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:55:00.434Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}}, \\\"eval-obs-only-object-norm02-seed48-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T10:33:11.557Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:57.990Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.18}}, \\\"eval-obs-only-object-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T21:32:40.226Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:54.506Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.2}}, \\\"eval-obs-only-object-norm02-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T16:04:31.207Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:51.647Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm02-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T07:44:19.258Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:44.901Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}, \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\\\"}, \\\"eval-obs-only-object-norm02-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T01:32:15.187Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:42.439Z\\\", \\\"hypothesis\\\": \\\"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T10:48:21.840Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:39.963Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}, \\\"notes\\\": \\\"Partial result: killed at task 8/10 but SR=16% consistent with norm02 mean (16.8%). Reclassified from failed to success per Director instruction.\\\"}, \\\"eval-obs-only-object-norm02-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T18:58:27.783Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:54:37.451Z\\\", \\\"hypothesis\\\": \\\"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\\\", \\\"parent\\\": \\\"eval-obs-only-object-norm02-seed43\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:50:15.572Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.1}, \\\"notes\\\": \\\"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\\\"}, \\\"eval-obs-only-object-norm01-seed67\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T02:35:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:49:55.438Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"监控误报进程消失。实际正常完成 SR=14.0% (14/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.1_seed67.json (bjb1-18228，注意保存在 /root/logs/ 而非项目 logs/)。进程在完成后自然退出，非异常终止。\\\"}, \\\"eval-vla-only-object-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T21:24:17.487Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:48:32.810Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.09}}, \\\"eval-vla-only-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T21:15:12.591Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:48:27.282Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.1}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Experiment completed successfully but stuck in ANALYZING >24h. Manual resolution on 2026-05-21: JSON output confirmed complete (10 tasks × 10 rollouts = 100 total). Overall SR=10%. Per-task SR range: 0.0-0.2.\\\"}, \\\"eval-vla-only-object-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T20:10:31.390Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:48:15.442Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.1}}, \\\"eval-vla-only-object-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T01:31:32.794Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:48:05.210Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline seed46 on LIBERO-Object. 第 5 个 VLA-only seed 补全 baseline。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T08:34:53.953Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:47:51.213Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.09}, \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\\\", \\\"parent\\\": \\\"eval-object-v8-full\\\"}, \\\"eval-vla-only-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T01:33:13.916Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:47:46.335Z\\\", \\\"hypothesis\\\": \\\"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.1}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-plan-a-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:32:49.074Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:47:42.399Z\\\", \\\"hypothesis\\\": \\\"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.19, \\\"sr_pct\\\": \\\"19.0%\\\", \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"mean_uncertainty\\\": 0.1468, \\\"trigger_rate\\\": 0.838}}, \\\"eval-vla-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T16:50:14.071Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:47:36.667Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\\\", \\\"parent\\\": \\\"eval-object-v8-full\\\"}, \\\"eval-vla-only-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T02:54:57.323Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:47:19.616Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12}}, \\\"eval-plan-a-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:15.856Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:46:30.740Z\\\", \\\"hypothesis\\\": \\\"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.35, \\\"total_rollouts\\\": 100, \\\"total_successes\\\": 35, \\\"mean_uncertainty\\\": 0.2619, \\\"trigger_rate\\\": 0.98}, \\\"notes\\\": \\\"Cron false positive — 实际正常完成 SR=35.0% (35/100), trigger_rate=98.0%, mean_unc=0.2619。日志在 bjb1-32546。已手动修正。\\\"}, \\\"eval-plan-a-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:37:28.279Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:45:27.640Z\\\", \\\"hypothesis\\\": \\\"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.2, \\\"sr_pct\\\": \\\"20.0%\\\", \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"mean_uncertainty\\\": 0.1448, \\\"trigger_rate\\\": 0.832}}, \\\"eval-plan-a-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:13.764Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:44:12.088Z\\\", \\\"hypothesis\\\": \\\"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.34, \\\"total_rollouts\\\": 100, \\\"total_successes\\\": 34, \\\"mean_uncertainty\\\": 0.2679, \\\"trigger_rate\\\": 0.976}, \\\"notes\\\": \\\"Cron false positive — 实际正常完成 SR=34.0% (34/100), trigger_rate=97.6%, mean_unc=0.2679。日志在 bjb1-32546。已手动修正。\\\"}, \\\"eval-plan-a-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:17.907Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:42:43.669Z\\\", \\\"hypothesis\\\": \\\"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.36, \\\"sr_pct\\\": \\\"36.0%\\\", \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"mean_uncertainty\\\": 0.2661, \\\"trigger_rate\\\": 0.978}}, \\\"eval-plan-a-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:32:51.140Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:42:32.790Z\\\", \\\"hypothesis\\\": \\\"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.16, \\\"sr_pct\\\": \\\"16.0%\\\", \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"mean_uncertainty\\\": 0.1457, \\\"trigger_rate\\\": 0.84}}, \\\"eval-random-selection-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T02:25:56.030Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:34:43.303Z\\\", \\\"hypothesis\\\": \\\"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\\\", \\\"notes\\\": \\\"Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts = 100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only baseline 相当，确认 random selection 无法有效利用 K=10 candidates。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.11, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.1}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T23:10:52.130Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:34:38.177Z\\\", \\\"hypothesis\\\": \\\"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.09, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total_rollouts\\\": 100, \\\"per_task_sr\\\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-random-selection-object-seed42-r3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T04:34:04.735Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:34:32.245Z\\\", \\\"hypothesis\\\": \\\"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\\\"}, \\\"eval-vla-only-spatial-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T01:18:47.309Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:32:53.123Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Spatial seed50. 补齐 Spatial baseline 样本量，与 CRM Spatial 配对统计检验。\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.3, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total\\\": 100}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-crm-spatial-k10-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T02:42:58.271Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:32:42.275Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only K=10 on LIBERO-Spatial seed50. 补齐 Spatial CRM 样本量 (n→7+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\\\"}, \\\"eval-crm-spatial-k10-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T02:42:47.989Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:32:32.158Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only K=10 on LIBERO-Spatial seed49. 补齐 Spatial CRM 样本量 (n→6+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"total\\\": 100}}, \\\"eval-obs-only-object-norm02-k20-seed44\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-19T14:27:30.715Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:32:24.008Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed44. K=20 第三个 seed，n=3 可报告 error bars，确认 K-value diminishing returns。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-k20-seed43\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-19T14:27:28.230Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:32:17.159Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed43. K=20 第二个 seed，与 K=10 seed43 配对，增强 K-value curve K=20 端的统计可靠性。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-k20-seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-17T13:34:42.612Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:32:11.044Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed42. 扩展 K-value curve 到 K=20，验证收益曲线在 K=10→K=20 段是否趋平（预期 ≤+1pp over K=10 的 17.6%）。用 K=10 训练的 CRM 模型，eval 时生成 20 个 VLA 样本。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm01-seed60\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T00:45:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T04:01:22.020Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed60. Norm sweep filling ε=0.1 gap.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.3}, \\\"n_rollouts\\\": 10, \\\"source\\\": \\\"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\\\"}}, \\\"eval-pi05-baseline-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T01:50:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:59:27.286Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\\\", \\\"notes\\\": \\\"PID 802634(旧)→802639(旧,killed)→811006(r2,MEAN_STD fix). Dual process conflict resolved. Monitoring until task 5.\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0}}, \\\"eval-obs-only-object-norm003-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T02:57:48.001Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:33:43.610Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.\\\"}, \\\"eval-obs-only-object-norm01-seed54\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:33.689Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:30:13.218Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed54. Norm sweep: filling ε=0.1 gap, bringing n to 7+.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed53\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:31.269Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:30:10.368Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed53. Norm sweep: filling ε=0.1 gap, bringing n to 6+.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.19}}, \\\"eval-obs-only-object-norm01-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:23.747Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:30:07.112Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 5+.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"notes\\\": \\\"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判。已手动修正。\\\"}, \\\"eval-obs-only-object-norm01-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T19:45:04.127Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:30:04.361Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}}, \\\"eval-obs-only-object-norm01-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:06:20.171Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:59.855Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed49. Low-norm data point for plan_500.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm01-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T23:02:39.518Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:57.231Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only with ε=0.1 and K=10 on LIBERO-Object seed48. Low-norm data point for plan_500 magnitude curve, strengthening Figure 2 error bars at small ε.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm01-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T06:51:15.721Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:54.309Z\\\", \\\"hypothesis\\\": \\\"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.17}, \\\"notes\\\": \\\"采集时间 2026-05-19, 进程已自然结束\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T13:05:51.040Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:47.720Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标准化到 n_rollouts=10 与其他 seed 一致。当前 obs_only ε=0.1 有 5 seeds。\\\", \\\"parent\\\": \\\"eval-obs-only-object-norm01-seed45\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.17}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm01-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T07:12:01.937Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:43.639Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\\\", \\\"parent\\\": \\\"eval-acr-object-obs-only-norm02\\\"}, \\\"eval-obs-only-object-norm005-seed55\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:23:01.005Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:41.343Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55. Norm sweep seed balance for ε=0.05.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"notes\\\": \\\"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\\\"}, \\\"eval-obs-only-object-norm005-seed50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:35.665Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:39.045Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed50. Norm sweep seed balance for ε=0.05.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm005-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:17:27.458Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:36.190Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49. Norm sweep seed balance for ε=0.05.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"notes\\\": \\\"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。日志在 bjb1-32546。\\\"}, \\\"eval-obs-only-object-norm005-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T05:56:19.347Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:30.312Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm005-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T19:14:06.226Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:23.229Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\\\", \\\"notes\\\": \\\"采集时间 2026-05-19, 进程已自然结束\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm005-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T23:10:56.103Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:16.871Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12}}, \\\"eval-obs-only-object-norm005-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:32:27.742Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:14.257Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm005-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:32:15.980Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:10.509Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"notes\\\": \\\"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm003-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T11:56:04.999Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:06.231Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T11:56:02.708Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:29:02.399Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed on bjb1-18228). C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T16:50:34.507Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:57.483Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed46. Norm sweep seed balance for ε=0.03.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"notes\\\": \\\"Cron false positive: 实验正常完成 SR=15.0%, JSON 已写入。进程退出后 cron 无 sentinel/W&B 标记 → 误判 failed。已修正 conclusion=success。\\\"}, \\\"eval-obs-only-object-norm003-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T15:16:07.852Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:51.768Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\\\", \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T21:09:01.117Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:48.787Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T15:15:11.377Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:46.427Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T01:45:20.860Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:43.998Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"parent\\\": \\\"eval-obs-only-object-norm003-seed43\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm003-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:33:23.925Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:28:41.514Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\\\", \\\"notes\\\": \\\"Cron false positive (日志路径不匹配)。实际正常完成 SR=14% (14/100)。norm003 magnitude curve 数据点，在 VLA-only (10.9%) 和 norm02 (16.8%) 之间。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}}, \\\"eval-obs-only-object-norm01-seed57\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T23:14:50.423Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:19:50.462Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed57. Norm sweep: additional ε=0.1 data point.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=19.0%。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.19}}, \\\"eval-obs-only-object-norm005-seed65\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T00:30:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:19:48.034Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Cron false positive confirmed. Output JSON 已存在 (1490 bytes)，日志显示正常完成。Overall SR=14.0% (14/100)。进程已退出，无异常。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.14}}, \\\"eval-obs-only-object-norm005-seed61\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T02:00:59.021Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:19:45.881Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"notes\\\": \\\"Cron false positive（第N次）：eval 脚本正常完成但不写 sentinel/W&B，被 cron 误判 failed。实际 SR=15.0% (15/100)。手动修正 conclusion=success。\\\", \\\"hypothesis\\\": \\\"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\\\"}, \\\"eval-obs-only-object-norm005-seed58\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T23:18:18.450Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:19:43.346Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=16.0%。\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm003-seed59\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T23:25:26.898Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:19:41.023Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed59. Norm sweep seed balance for ε=0.03.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13}, \\\"notes\\\": \\\"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=13.0%。\\\"}, \\\"eval-obs-only-object-norm003-seed56\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:28:30.000Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:19:38.737Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15}, \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\\\"}, \\\"eval-obs-only-object-norm01-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:15:13.220Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:17:06.237Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.1 补种.\\\"}, \\\"eval-obs-only-object-norm01-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:15:10.875Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:17:01.964Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.1 补种.\\\"}, \\\"eval-obs-only-object-norm005-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T02:57:21.662Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:16:58.507Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.05 outlier verification.\\\"}, \\\"eval-obs-only-object-norm003-seed63-r3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:15:08.600Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:16:54.862Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r3. Redo of killed seed63-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\\\"}, \\\"eval-obs-only-object-norm005-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:14:58.578Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:16:49.849Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.05 has outlier seeds, expanding for variance verification.\\\"}, \\\"eval-obs-only-object-norm003-seed62-r3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:15:06.396Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:16:44.624Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r3. Redo of killed seed62-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\\\"}, \\\"eval-obs-only-object-norm003-seed78\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:14:54.184Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:16:34.818Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed78. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\\\"}, \\\"eval-obs-only-object-norm003-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-21T03:14:50.541Z\\\", \\\"updated_at\\\": \\\"2026-05-21T03:16:26.327Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\\\"}}, \\\"count\\\": 100, \\\"total\\\": 567, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2795}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T10:19:18.528Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T10:19:09.036Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T10:18:58.812Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-21T10:18:48.305Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-21T10:18:37.555Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-21T10:18:27.592Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"notes\": \"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\", \"conclusion\": \"killed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T07:09:59.922Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"notes\": \"LOW-PRIORITY: may be killed when π0.5 fix passes quick verify. GPU 0 on bjb2-28827, tmux session: spatial_obs_only_s45\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-21T05:22:58.984Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:31.173Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"notes\": \"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:00.886Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:13:12.047Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"notes\": \"[2026-05-21 修正] 之前的\\\"task 9/10 异常退出\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-21T05:07:12.893Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-21T05:07:10.342Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-21T05:07:08.046Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:47:49.745Z\", \"updated_at\": \"2026-05-21T05:07:05.713Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601): tests K=20 vs K=10 compute tradeoff.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:49.893Z\", \"updated_at\": \"2026-05-21T05:07:03.314Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed42. K-value sweep (plan_601): tests whether increasing from K=10 to K=20 further improves SR, justifying K=10 as compute-efficient choice.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:08.378Z\", \"updated_at\": \"2026-05-21T04:55:07.524Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed53. Multi-seed robustness for magnitude curve plan_500.\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-21T04:55:05.083Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:57.442Z\", \"updated_at\": \"2026-05-21T04:55:02.734Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=17% (17/100)，与 obs_only norm02 均值 (16.8%±1.8%) 一致。新增第 7 个 seed 数据点。\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:07:41.505Z\", \"updated_at\": \"2026-05-21T04:55:00.434Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:11.557Z\", \"updated_at\": \"2026-05-21T04:54:57.990Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-21T04:54:54.506Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-21T04:54:51.647Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-21T04:54:44.901Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-21T04:54:42.439Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:21.840Z\", \"updated_at\": \"2026-05-21T04:54:39.963Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"notes\": \"Partial result: killed at task 8/10 but SR=16% consistent with norm02 mean (16.8%). Reclassified from failed to success per Director instruction.\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-21T04:54:37.451Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:49:55.438Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"notes\": \"监控误报进程消失。实际正常完成 SR=14.0% (14/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.1_seed67.json (bjb1-18228，注意保存在 /root/logs/ 而非项目 logs/)。进程在完成后自然退出，非异常终止。\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-21T04:48:32.810Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-21T04:48:27.282Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\", \"notes\": \"Experiment completed successfully but stuck in ANALYZING >24h. Manual resolution on 2026-05-21: JSON output confirmed complete (10 tasks × 10 rollouts = 100 total). Overall SR=10%. Per-task SR range: 0.0-0.2.\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:31.390Z\", \"updated_at\": \"2026-05-21T04:48:15.442Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:31:32.794Z\", \"updated_at\": \"2026-05-21T04:48:05.210Z\", \"hypothesis\": \"VLA-only baseline seed46 on LIBERO-Object. 第 5 个 VLA-only seed 补全 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-21T04:47:51.213Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-21T04:47:46.335Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:49.074Z\", \"updated_at\": \"2026-05-21T04:47:42.399Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-21T04:47:36.667Z\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\", \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-21T04:47:19.616Z\", \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:15.856Z\", \"updated_at\": \"2026-05-21T04:46:30.740Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}, \"notes\": \"Cron false positive — 实际正常完成 SR=35.0% (35/100), trigger_rate=98.0%, mean_unc=0.2619。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:37:28.279Z\", \"updated_at\": \"2026-05-21T04:45:27.640Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:13.764Z\", \"updated_at\": \"2026-05-21T04:44:12.088Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}, \"notes\": \"Cron false positive — 实际正常完成 SR=34.0% (34/100), trigger_rate=97.6%, mean_unc=0.2679。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:17.907Z\", \"updated_at\": \"2026-05-21T04:42:43.669Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:51.140Z\", \"updated_at\": \"2026-05-21T04:42:32.790Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:25:56.030Z\", \"updated_at\": \"2026-05-21T04:34:43.303Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\", \"notes\": \"Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts = 100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only baseline 相当，确认 random selection 无法有效利用 K=10 candidates。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:52.130Z\", \"updated_at\": \"2026-05-21T04:34:38.177Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T04:34:04.735Z\", \"updated_at\": \"2026-05-21T04:34:32.245Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:18:47.309Z\", \"updated_at\": \"2026-05-21T04:32:53.123Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed50. 补齐 Spatial baseline 样本量，与 CRM Spatial 配对统计检验。\", \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:58.271Z\", \"updated_at\": \"2026-05-21T04:32:42.275Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed50. 补齐 Spatial CRM 样本量 (n→7+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:47.989Z\", \"updated_at\": \"2026-05-21T04:32:32.158Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed49. 补齐 Spatial CRM 样本量 (n→6+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:30.715Z\", \"updated_at\": \"2026-05-21T04:32:24.008Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed44. K=20 第三个 seed，n=3 可报告 error bars，确认 K-value diminishing returns。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:28.230Z\", \"updated_at\": \"2026-05-21T04:32:17.159Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed43. K=20 第二个 seed，与 K=10 seed43 配对，增强 K-value curve K=20 端的统计可靠性。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-21T04:32:11.044Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed42. 扩展 K-value curve 到 K=20，验证收益曲线在 K=10→K=20 段是否趋平（预期 ≤+1pp over K=10 的 17.6%）。用 K=10 训练的 CRM 模型，eval 时生成 20 个 VLA 样本。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T04:01:22.020Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed60. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T03:59:27.286Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\", \"notes\": \"PID 802634(旧)→802639(旧,killed)→811006(r2,MEAN_STD fix). Dual process conflict resolved. Monitoring until task 5.\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:57:48.001Z\", \"updated_at\": \"2026-05-21T03:33:43.610Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:33.689Z\", \"updated_at\": \"2026-05-21T03:30:13.218Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed54. Norm sweep: filling ε=0.1 gap, bringing n to 7+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:31.269Z\", \"updated_at\": \"2026-05-21T03:30:10.368Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed53. Norm sweep: filling ε=0.1 gap, bringing n to 6+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:23.747Z\", \"updated_at\": \"2026-05-21T03:30:07.112Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 5+.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判。已手动修正。\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:04.127Z\", \"updated_at\": \"2026-05-21T03:30:04.361Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:20.171Z\", \"updated_at\": \"2026-05-21T03:29:59.855Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed49. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:39.518Z\", \"updated_at\": \"2026-05-21T03:29:57.231Z\", \"hypothesis\": \"CRM obs_only with ε=0.1 and K=10 on LIBERO-Object seed48. Low-norm data point for plan_500 magnitude curve, strengthening Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-21T03:29:54.309Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:51.040Z\", \"updated_at\": \"2026-05-21T03:29:47.720Z\", \"hypothesis\": \"obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标准化到 n_rollouts=10 与其他 seed 一致。当前 obs_only ε=0.1 有 5 seeds。\", \"parent\": \"eval-obs-only-object-norm01-seed45\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-21T03:29:43.639Z\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:23:01.005Z\", \"updated_at\": \"2026-05-21T03:29:41.343Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:35.665Z\", \"updated_at\": \"2026-05-21T03:29:39.045Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed50. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:27.458Z\", \"updated_at\": \"2026-05-21T03:29:36.190Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。日志在 bjb1-32546。\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-21T03:29:30.312Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-21T03:29:23.229Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-21T03:29:16.871Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:27.742Z\", \"updated_at\": \"2026-05-21T03:29:14.257Z\", \"hypothesis\": \"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-21T03:29:10.509Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:04.999Z\", \"updated_at\": \"2026-05-21T03:29:06.231Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:02.708Z\", \"updated_at\": \"2026-05-21T03:29:02.399Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed on bjb1-18228). C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:34.507Z\", \"updated_at\": \"2026-05-21T03:28:57.483Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed46. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive: 实验正常完成 SR=15.0%, JSON 已写入。进程退出后 cron 无 sentinel/W&B 标记 → 误判 failed。已修正 conclusion=success。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:01.117Z\", \"updated_at\": \"2026-05-21T03:28:48.787Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-21T03:28:46.427Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:45:20.860Z\", \"updated_at\": \"2026-05-21T03:28:43.998Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"parent\": \"eval-obs-only-object-norm003-seed43\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-21T03:28:41.514Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=14% (14/100)。norm003 magnitude curve 数据点，在 VLA-only (10.9%) 和 norm02 (16.8%) 之间。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:14:50.423Z\", \"updated_at\": \"2026-05-21T03:19:50.462Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed57. Norm sweep: additional ε=0.1 data point.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=19.0%。\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:19:48.034Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive confirmed. Output JSON 已存在 (1490 bytes)，日志显示正常完成。Overall SR=14.0% (14/100)。进程已退出，无异常。\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:00:59.021Z\", \"updated_at\": \"2026-05-21T03:19:45.881Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive（第N次）：eval 脚本正常完成但不写 sentinel/W&B，被 cron 误判 failed。实际 SR=15.0% (15/100)。手动修正 conclusion=success。\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:18.450Z\", \"updated_at\": \"2026-05-21T03:19:43.346Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=16.0%。\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:25:26.898Z\", \"updated_at\": \"2026-05-21T03:19:41.023Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed59. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=13.0%。\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:28:30.000Z\", \"updated_at\": \"2026-05-21T03:19:38.737Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:13.220Z\", \"updated_at\": \"2026-05-21T03:17:06.237Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:10.875Z\", \"updated_at\": \"2026-05-21T03:17:01.964Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:57:21.662Z\", \"updated_at\": \"2026-05-21T03:16:58.507Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.05 outlier verification.\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:08.600Z\", \"updated_at\": \"2026-05-21T03:16:54.862Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r3. Redo of killed seed63-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:58.578Z\", \"updated_at\": \"2026-05-21T03:16:49.849Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.05 has outlier seeds, expanding for variance verification.\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:06.396Z\", \"updated_at\": \"2026-05-21T03:16:44.624Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r3. Redo of killed seed62-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:54.184Z\", \"updated_at\": \"2026-05-21T03:16:34.818Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed78. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:50.541Z\", \"updated_at\": \"2026-05-21T03:16:26.327Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}}, \"count\": 100, \"total\": 567, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2795}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "84dcd775-bbcb-4947-9987-66f1ebbabde1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012Az6aYJJLJD5BuEDbFJtrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24811,
      "cache_read_input_tokens": 39230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24811
      },
      "output_tokens": 71,
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

<details open><summary>🔧 Tool call — Read · `toolu_01YXBUQnWVRFZE3tSvfjvbui`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.md",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "d9b016bc-ae2e-418f-b132-64a67ddaf133",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012Az6aYJJLJD5BuEDbFJtrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24811,
      "cache_read_input_tokens": 39230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24811
      },
      "output_tokens": 71,
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

_source line 23 · 2026-05-21T11:27:37.208Z_

<details><summary>↩ Tool result · `toolu_01YXBUQnWVRFZE3tSvfjvbui`</summary>

```text
1	# Related Work
2	
3	## VLA Robustness and Inference-Time Adaptation
4	
5	Vision-Language-Action (VLA) models have rapidly advanced general-purpose robot control by leveraging large-scale vision-language pretraining [Brohan et al., 2023; Kim et al., 2024]. Flow-matching architectures such as pi0 [Black et al., 2024] and SmolVLA [Shukor et al., 2025] achieve strong performance on standard benchmarks but remain brittle under distribution shift, as systematically documented by LIBERO-Plus [Fei et al., 2025] and LIBERO-PRO [Xu et al., 2025].
6	
7	Several lines of work address VLA robustness at *training time*. RobustVLA [Zhang et al., 2025] applies Jacobian and smoothness regularization via RL post-training. SRPO [Fei et al., 2025] uses self-referential policy optimization to reach 82.1% on LIBERO-Plus. DiG-Flow [Zhang et al., 2025] introduces representation-level discrepancy guidance. ACoT-VLA [AgibotTech, 2026] adds chain-of-thought reasoning to VLA action prediction. VLA-GSE [Jiang et al., 2026] employs parameter-efficient fine-tuning with specialized experts. AFIL [2026] leverages failure trajectories as negative guidance during training. These methods require modifying the VLA training pipeline; our work is complementary, operating purely at inference time on a frozen model.
8	
9	At *inference time*, the landscape is sparser. ReconVLA [Chen et al., 2026] applies conformal prediction to produce calibrated uncertainty estimates and selects the best action from K candidates — a pure sample-selection strategy. VLA-Pilot [2025] uses a multimodal LLM verifier with evolutionary diffusion optimization for zero-shot policy steering, but incurs 2.41s per step. SC-VLA [Li et al., 2026] performs online action refinement via sparse future state prediction and residual RL, requiring environment interaction. TT-VLA [Liu et al., 2026] adapts VLAs through test-time reinforcement learning with progress-based rewards. A2C2 [Sendai et al., 2025] proposes an asynchronous action chunk correction head — the closest architecture to our CRM, but trained jointly with the VLA rather than as a post-hoc module. SAFE [Gu et al., 2025] focuses on failure detection using internal VLA features and conformal prediction to determine *when* to intervene. Our work differs from all of the above by (1) operating on a fully frozen VLA with no environment interaction, (2) systematically comparing correction conditioning features, and (3) identifying correction magnitude as a critical factor.
10	
11	SnapFlow [Luan et al., 2026] takes the opposite computational trade-off — distilling multi-step flow matching into a single inference step — while we invest additional compute (K=10 samples + CRM correction) to improve robustness.
12	
13	## Conformal Prediction in Robotics
14	
15	Conformal prediction (CP) provides distribution-free coverage guarantees without distributional assumptions [Shafer & Vovk, 2008; Angelopoulos & Bates, 2023]. Extensions to non-exchangeable settings [Barber et al., 2023] and online adaptation via Adaptive Conformal Inference (ACI) [Gibbs & Candès, 2021] enable deployment under the distribution shifts inherent in robot operation.
16	
17	In multivariate action spaces, Conformalized Gaussian Scoring (CGS) [Braun et al., 2025] provides Mahalanobis-based nonconformity scores respecting inter-dimensional correlations, which we adopt for sample selection. Conformalized Quantile Regression (CQR) [Romano et al., 2019] offers per-dimension heteroscedastic coverage. Recent work explores alternatives: Fan and Sesia [2025] develop coordinate-wise standardization for tighter marginal intervals, and Klein et al. [2025] use optimal transport ordering for principled multivariate quantiles.
18	
19	Several works apply CP to robot planning and control. Zhao et al. [2024] use adaptive CP for uncertainty detection in high-DOF teleoperation at RSS 2024. Wang and Ning [2025] integrate CP into trajectory optimization loops with coverage guarantees. Zhou et al. [2025] combine ACP with control barrier functions for formally safe RL at ICRA 2025. Gonzales et al. [2026] pair conformal risk control with CBFs for human-robot interaction safety. Lekeufack et al. [2024] develop conformal decision theory for calibrated autonomous decisions. In the CP-for-robotics literature, CLAPS [2025] extends CP to Lie group configuration spaces, and LCP [2025] learns context-aware nonconformity functions for robot planning.
20	
21	A distinct thread uses CP for *downstream decision-making* rather than coverage: Jin and Candès [2023] use conformal p-values for selection with FDR control, and Huang et al. [2023] deploy CP in learned feature spaces. SafeDiffCon [2025] uses CP uncertainty quantiles to guide diffusion-based control at ICML 2025. Yuan et al. [2026] calibrate VLM+policy composition for strategy selection (act/ask/learn) using CP. Our work connects to this thread: we use conformal scores for sample selection, then investigate whether conformal statistics can additionally serve as conditioning features for learned correction — finding, surprisingly, that they cannot.
22	
23	The emerging area of VLA-specific uncertainty quantification provides further context. Zollo and Zemel [2025] present the first systematic calibration study for VLAs, introducing prompt ensembles and action-wise Platt scaling. Tang et al. [2026] identify the "averaging trap" in VLA uncertainty where mean aggregation dilutes critical signals. Xing et al. [2026] propose single-pass uncertainty via velocity divergence in flow matching models. Valle et al. [2025] establish evaluation metrics for VLA uncertainty. These works focus on *measuring* uncertainty; we focus on *acting on it* through learned correction.
24	
25	## Residual Correction and Learned Action Refinement
26	
27	Residual policy learning [Silver et al., 2018] establishes the framework of learning a correction on top of a base controller, with bounded corrections shown to preserve stability [Johannink et al., 2019]. This paradigm has been extended to VLA settings: PLD [Xiao et al., 2026] applies residual RL with scheduled magnitude bounds on LIBERO at ICLR 2026, and DAWN [Ma et al., 2026] analyzes scale mismatch between base policy and residual in value estimation. DRC [Pan et al., 2025] introduces temporal decay of correction magnitude over episodes. TRANSIC [Jiang et al., 2024] demonstrates that ungated residual corrections lead to model collapse, motivating gated correction mechanisms — closely related to our finding that unbounded correction magnitude (norm=1.42) yields catastrophic 0% success rate.
28	
29	A separate line of supervised (non-RL) correction includes DAgger [Ross et al., 2011], which reduces compounding error via iterative expert corrections, and its variants: CR-DAgger [Cai et al., 2025] learns compliant residual corrections from human interventions, and RaC [2025] scales recovery and correction from human intervention data. Reactive Diffusion Policy [Xue et al., 2025] uses a two-level slow-fast architecture with supervised fast correction. DART [Laskey et al., 2017] injects optimized noise for compounding error robustness without online interaction. Our CRM follows the supervised correction paradigm — trained offline via L2 regression on calibration data — but uniquely conditions on VLA observation features and constrains correction magnitude, avoiding the RL training loops required by PLD, SC-VLA, and DAWN.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "dbfb2e56-ff5b-45ae-abe2-6e8fc7fc9826",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.md",
      "content": "# Related Work\n\n## VLA Robustness and Inference-Time Adaptation\n\nVision-Language-Action (VLA) models have rapidly advanced general-purpose robot control by leveraging large-scale vision-language pretraining [Brohan et al., 2023; Kim et al., 2024]. Flow-matching architectures such as pi0 [Black et al., 2024] and SmolVLA [Shukor et al., 2025] achieve strong performance on standard benchmarks but remain brittle under distribution shift, as systematically documented by LIBERO-Plus [Fei et al., 2025] and LIBERO-PRO [Xu et al., 2025].\n\nSeveral lines of work address VLA robustness at *training time*. RobustVLA [Zhang et al., 2025] applies Jacobian and smoothness regularization via RL post-training. SRPO [Fei et al., 2025] uses self-referential policy optimization to reach 82.1% on LIBERO-Plus. DiG-Flow [Zhang et al., 2025] introduces representation-level discrepancy guidance. ACoT-VLA [AgibotTech, 2026] adds chain-of-thought reasoning to VLA action prediction. VLA-GSE [Jiang et al., 2026] employs parameter-efficient fine-tuning with specialized experts. AFIL [2026] leverages failure trajectories as negative guidance during training. These methods require modifying the VLA training pipeline; our work is complementary, operating purely at inference time on a frozen model.\n\nAt *inference time*, the landscape is sparser. ReconVLA [Chen et al., 2026] applies conformal prediction to produce calibrated uncertainty estimates and selects the best action from K candidates — a pure sample-selection strategy. VLA-Pilot [2025] uses a multimodal LLM verifier with evolutionary diffusion optimization for zero-shot policy steering, but incurs 2.41s per step. SC-VLA [Li et al., 2026] performs online action refinement via sparse future state prediction and residual RL, requiring environment interaction. TT-VLA [Liu et al., 2026] adapts VLAs through test-time reinforcement learning with progress-based rewards. A2C2 [Sendai et al., 2025] proposes an asynchronous action chunk correction head — the closest architecture to our CRM, but trained jointly with the VLA rather than as a post-hoc module. SAFE [Gu et al., 2025] focuses on failure detection using internal VLA features and conformal prediction to determine *when* to intervene. Our work differs from all of the above by (1) operating on a fully frozen VLA with no environment interaction, (2) systematically comparing correction conditioning features, and (3) identifying correction magnitude as a critical factor.\n\nSnapFlow [Luan et al., 2026] takes the opposite computational trade-off — distilling multi-step flow matching into a single inference step — while we invest additional compute (K=10 samples + CRM correction) to improve robustness.\n\n## Conformal Prediction in Robotics\n\nConformal prediction (CP) provides distribution-free coverage guarantees without distributional assumptions [Shafer & Vovk, 2008; Angelopoulos & Bates, 2023]. Extensions to non-exchangeable settings [Barber et al., 2023] and online adaptation via Adaptive Conformal Inference (ACI) [Gibbs & Candès, 2021] enable deployment under the distribution shifts inherent in robot operation.\n\nIn multivariate action spaces, Conformalized Gaussian Scoring (CGS) [Braun et al., 2025] provides Mahalanobis-based nonconformity scores respecting inter-dimensional correlations, which we adopt for sample selection. Conformalized Quantile Regression (CQR) [Romano et al., 2019] offers per-dimension heteroscedastic coverage. Recent work explores alternatives: Fan and Sesia [2025] develop coordinate-wise standardization for tighter marginal intervals, and Klein et al. [2025] use optimal transport ordering for principled multivariate quantiles.\n\nSeveral works apply CP to robot planning and control. Zhao et al. [2024] use adaptive CP for uncertainty detection in high-DOF teleoperation at RSS 2024. Wang and Ning [2025] integrate CP into trajectory optimization loops with coverage guarantees. Zhou et al. [2025] combine ACP with control barrier functions for formally safe RL at ICRA 2025. Gonzales et al. [2026] pair conformal risk control with CBFs for human-robot interaction safety. Lekeufack et al. [2024] develop conformal decision theory for calibrated autonomous decisions. In the CP-for-robotics literature, CLAPS [2025] extends CP to Lie group configuration spaces, and LCP [2025] learns context-aware nonconformity functions for robot planning.\n\nA distinct thread uses CP for *downstream decision-making* rather than coverage: Jin and Candès [2023] use conformal p-values for selection with FDR control, and Huang et al. [2023] deploy CP in learned feature spaces. SafeDiffCon [2025] uses CP uncertainty quantiles to guide diffusion-based control at ICML 2025. Yuan et al. [2026] calibrate VLM+policy composition for strategy selection (act/ask/learn) using CP. Our work connects to this thread: we use conformal scores for sample selection, then investigate whether conformal statistics can additionally serve as conditioning features for learned correction — finding, surprisingly, that they cannot.\n\nThe emerging area of VLA-specific uncertainty quantification provides further context. Zollo and Zemel [2025] present the first systematic calibration study for VLAs, introducing prompt ensembles and action-wise Platt scaling. Tang et al. [2026] identify the \"averaging trap\" in VLA uncertainty where mean aggregation dilutes critical signals. Xing et al. [2026] propose single-pass uncertainty via velocity divergence in flow matching models. Valle et al. [2025] establish evaluation metrics for VLA uncertainty. These works focus on *measuring* uncertainty; we focus on *acting on it* through learned correction.\n\n## Residual Correction and Learned Action Refinement\n\nResidual policy learning [Silver et al., 2018] establishes the framework of learning a correction on top of a base controller, with bounded corrections shown to preserve stability [Johannink et al., 2019]. This paradigm has been extended to VLA settings: PLD [Xiao et al., 2026] applies residual RL with scheduled magnitude bounds on LIBERO at ICLR 2026, and DAWN [Ma et al., 2026] analyzes scale mismatch between base policy and residual in value estimation. DRC [Pan et al., 2025] introduces temporal decay of correction magnitude over episodes. TRANSIC [Jiang et al., 2024] demonstrates that ungated residual corrections lead to model collapse, motivating gated correction mechanisms — closely related to our finding that unbounded correction magnitude (norm=1.42) yields catastrophic 0% success rate.\n\nA separate line of supervised (non-RL) correction includes DAgger [Ross et al., 2011], which reduces compounding error via iterative expert corrections, and its variants: CR-DAgger [Cai et al., 2025] learns compliant residual corrections from human interventions, and RaC [2025] scales recovery and correction from human intervention data. Reactive Diffusion Policy [Xue et al., 2025] uses a two-level slow-fast architecture with supervised fast correction. DART [Laskey et al., 2017] injects optimized noise for compounding error robustness without online interaction. Our CRM follows the supervised correction paradigm — trained offline via L2 regression on calibration data — but uniquely conditions on VLA observation features and constrains correction magnitude, avoiding the RL training loops required by PLD, SC-VLA, and DAWN.\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 32
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "b8e04f51-d1c9-4a63-a6df-b7aa4a6f7f0e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KprSywRkWEZTREQtGWsftw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3595,
      "cache_read_input_tokens": 64041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3595
      },
      "output_tokens": 48,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016ZPkDR7eTYamaWWroba4eE`</summary>

```json
{
  "query": "write paper section edit",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "d057edaf-a7bb-4a9a-bfd1-ed70659a154c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KprSywRkWEZTREQtGWsftw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3595,
      "cache_read_input_tokens": 64041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3595
      },
      "output_tokens": 48,
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

_source line 26 · 2026-05-21T11:27:50.220Z_

<details><summary>↩ Tool result · `toolu_016ZPkDR7eTYamaWWroba4eE`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "NotebookEdit"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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

```json
{
  "type": "tool_reference",
  "tool_name": "Monitor"
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
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "4239e994-d4c2-4f0a-a982-95e04ff94c8b",
  "tool_use_result": {
    "matches": [
      "NotebookEdit",
      "TodoWrite",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "Monitor"
    ],
    "query": "write paper section edit",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "fb981409-a22d-40f3-963a-453b349a1cf5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01K7SyGsj1y4MMEBgXKGp6DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8472,
      "cache_read_input_tokens": 67636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8472
      },
      "output_tokens": 0,
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

<details open><summary>🔧 Tool call — Write · `toolu_015CWeuHeZnU1QRTV2ZC6vvZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
  "content": "# Ablation: K-Value Sweep\n\nWe sweep the number of VLA samples K ∈ {2, 10, 20} drawn from the flow-matching policy and held fixed at the obs_only CRM head (ε = 0.2). The VLA-only K=1 baseline is reported for reference. Increasing K beyond 2 yields no measurable success-rate gain on either suite, supporting our adaptive K=2 configuration (Plan A) as Pareto-optimal in compute.\n\n**Table A: Effect of K on closed-loop success rate (mean ± std across seeds).**\n\n| K | Object SR (%) | Spatial SR (%) | n_seeds | Object exp_ids | Spatial exp_ids |\n|---|--------------:|---------------:|--------:|----------------|-----------------|\n| 1 (VLA-only) | 10.8 ± 1.3 | 29.4 ± 1.5 | ≥4 / ≥4 | `eval-vla-only-object-*` | `eval-pi05-vla-only-spatial-*` |\n| 2 (Plan A, adaptive) | **18.3 ± 2.1** | **35.0 ± 1.0** | 3 / 3 | `eval-plan-a-object-seed{42,43,44}` | `eval-plan-a-spatial-seed{42,43,44}` |\n| 10 | 16.8 ± 1.8 | 34.5 ± 1.5 | ≥3 / ≥3 | obs_only norm0.2 seed pool | spatial obs_only seed pool |\n| 20 | 18.8 ± 1.0 | 34.3 ± 0.6 | 4 / 3 | `eval-k20-obs-only-object-seed{42,43,44,45}` | `eval-k20-obs-only-spatial-seed{42,43,44}` |\n\nPer-seed K=20 raw numbers (Object): 20%, 18%, 18%, 19%. Per-seed K=20 raw (Spatial): 35%, 34%, 34%. All K=20 runs use the same CRM checkpoint (`obs_only_K10_eps02_default`) and differ only in the number of candidate actions resampled at inference.\n\n**Diminishing returns beyond K=2.** Moving from K=1 → K=2 captures the bulk of the gain on both benchmarks (+7.5pp Object, +5.6pp Spatial). Subsequent doublings of K provide no additional improvement: on Object, K=10 (16.8%) and K=20 (18.8%) bracket the K=2 mean (18.3%) within one standard deviation; on Spatial, the three K values lie within 0.7pp of one another (34.3-35.0%) and the K=20 standard deviation (0.6%) overlaps the K=2 and K=10 confidence ranges. The pattern is consistent with the obs_only CRM's correction signal being driven by the observation features rather than by candidate diversity — once two samples provide an uncertainty estimate sufficient to trigger correction, additional candidates are absorbed by the same correction head without measurable benefit.\n\n**Implication for compute–accuracy trade-off.** A single flow-matching forward pass dominates inference cost; K=20 requires 10× more VLA forwards than K=2 with no return on closed-loop SR. The adaptive K=2 configuration (Plan A) — which performs a second forward only when the pairwise L2 distance between the first two samples exceeds τ=P50=0.0749 — pays at most 2× VLA compute and triggers correction on roughly 84% of steps on Object and 98% on Spatial, while matching K=20 SR within noise. We therefore adopt K=2 (Plan A) as the default in all downstream experiments and recommend it as the operating point for deployment.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "80270628-b834-4a65-87a1-53ac8ebe805e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01K7SyGsj1y4MMEBgXKGp6DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8472,
      "cache_read_input_tokens": 67636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8472
      },
      "output_tokens": 0,
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

_source line 29 · 2026-05-21T11:28:21.548Z_

<details><summary>↩ Tool result · `toolu_015CWeuHeZnU1QRTV2ZC6vvZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "51daecbd-ed4f-4426-9b15-61aacd83641d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
    "content": "# Ablation: K-Value Sweep\n\nWe sweep the number of VLA samples K ∈ {2, 10, 20} drawn from the flow-matching policy and held fixed at the obs_only CRM head (ε = 0.2). The VLA-only K=1 baseline is reported for reference. Increasing K beyond 2 yields no measurable success-rate gain on either suite, supporting our adaptive K=2 configuration (Plan A) as Pareto-optimal in compute.\n\n**Table A: Effect of K on closed-loop success rate (mean ± std across seeds).**\n\n| K | Object SR (%) | Spatial SR (%) | n_seeds | Object exp_ids | Spatial exp_ids |\n|---|--------------:|---------------:|--------:|----------------|-----------------|\n| 1 (VLA-only) | 10.8 ± 1.3 | 29.4 ± 1.5 | ≥4 / ≥4 | `eval-vla-only-object-*` | `eval-pi05-vla-only-spatial-*` |\n| 2 (Plan A, adaptive) | **18.3 ± 2.1** | **35.0 ± 1.0** | 3 / 3 | `eval-plan-a-object-seed{42,43,44}` | `eval-plan-a-spatial-seed{42,43,44}` |\n| 10 | 16.8 ± 1.8 | 34.5 ± 1.5 | ≥3 / ≥3 | obs_only norm0.2 seed pool | spatial obs_only seed pool |\n| 20 | 18.8 ± 1.0 | 34.3 ± 0.6 | 4 / 3 | `eval-k20-obs-only-object-seed{42,43,44,45}` | `eval-k20-obs-only-spatial-seed{42,43,44}` |\n\nPer-seed K=20 raw numbers (Object): 20%, 18%, 18%, 19%. Per-seed K=20 raw (Spatial): 35%, 34%, 34%. All K=20 runs use the same CRM checkpoint (`obs_only_K10_eps02_default`) and differ only in the number of candidate actions resampled at inference.\n\n**Diminishing returns beyond K=2.** Moving from K=1 → K=2 captures the bulk of the gain on both benchmarks (+7.5pp Object, +5.6pp Spatial). Subsequent doublings of K provide no additional improvement: on Object, K=10 (16.8%) and K=20 (18.8%) bracket the K=2 mean (18.3%) within one standard deviation; on Spatial, the three K values lie within 0.7pp of one another (34.3-35.0%) and the K=20 standard deviation (0.6%) overlaps the K=2 and K=10 confidence ranges. The pattern is consistent with the obs_only CRM's correction signal being driven by the observation features rather than by candidate diversity — once two samples provide an uncertainty estimate sufficient to trigger correction, additional candidates are absorbed by the same correction head without measurable benefit.\n\n**Implication for compute–accuracy trade-off.** A single flow-matching forward pass dominates inference cost; K=20 requires 10× more VLA forwards than K=2 with no return on closed-loop SR. The adaptive K=2 configuration (Plan A) — which performs a second forward only when the pairwise L2 distance between the first two samples exceeds τ=P50=0.0749 — pays at most 2× VLA compute and triggers correction on roughly 84% of steps on Object and 98% on Spatial, while matching K=20 SR within noise. We therefore adopt K=2 (Plan A) as the default in all downstream experiments and recommend it as the operating point for deployment.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "1c2d3845-e245-420a-8820-1c77bb626ce0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Rp6SKbrHUYVBjJf4DVsT8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2384,
      "cache_read_input_tokens": 76108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2384
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

### Assistant

_source line 31_

Now update the outline to point to the new section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "71bd5b58-6d78-4462-85a2-d8c38cd83011",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Rp6SKbrHUYVBjJf4DVsT8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2384,
      "cache_read_input_tokens": 76108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2384
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

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01TiLJNZArjCaK9q6ka14pLY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md",
  "old_string": "### 4.5 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences",
  "new_string": "### 4.5 K-Value Sweep Ablation\n\n→ See `paper/sections/ablation_k_sweep.md` for full draft.\n\n**Key message**: K=2 (Plan A) ≈ K=10 ≈ K=20 on both Object (18.3% / 16.8% / 18.8%) and Spatial (35.0% / 34.5% / 34.3%). Diminishing returns beyond K=2 justify Plan A (adaptive K=2) as Pareto-optimal — matches K=20 SR with ≤2× VLA compute. K=20 exp_ids: `eval-k20-obs-only-object-seed{42,43,44,45}`, `eval-k20-obs-only-spatial-seed{42,43,44}`.\n\n### 4.6 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "fa8bb254-e4bf-4463-b263-872a395ad610",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Rp6SKbrHUYVBjJf4DVsT8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2384,
      "cache_read_input_tokens": 76108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2384
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

_source line 33 · 2026-05-21T11:28:31.894Z_

<details><summary>↩ Tool result · `toolu_01TiLJNZArjCaK9q6ka14pLY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "def345b5-e251-4d1a-b6e0-9b2c6713d9c3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md",
    "oldString": "### 4.5 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences",
    "newString": "### 4.5 K-Value Sweep Ablation\n\n→ See `paper/sections/ablation_k_sweep.md` for full draft.\n\n**Key message**: K=2 (Plan A) ≈ K=10 ≈ K=20 on both Object (18.3% / 16.8% / 18.8%) and Spatial (35.0% / 34.5% / 34.3%). Diminishing returns beyond K=2 justify Plan A (adaptive K=2) as Pareto-optimal — matches K=20 SR with ≤2× VLA compute. K=20 exp_ids: `eval-k20-obs-only-object-seed{42,43,44,45}`, `eval-k20-obs-only-spatial-seed{42,43,44}`.\n\n### 4.6 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences",
    "originalFile": "# ACR-VLA: Observation-Conditioned Learned Correction for Robust Vision-Language-Action Models\n\n**Target**: CoRL 2026 (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\n**Format**: 8 pages + references, CoRL template\n\n---\n\n## Title Candidates\n\n1. **ACR-VLA: Sample-Then-Correct — Observation-Conditioned Action Refinement for Robust Vision-Language-Action Models**\n2. **Beyond Sample Selection: Learned Action Correction Improves VLA Robustness Under Distribution Shift**\n3. **When Conformal Features Fail: Observation-Conditioned Correction for Vision-Language-Action Models**\n\n---\n\n## 1. Introduction (~1.5 pages)\n\n**Key points**:\n- Flow-matching VLAs (pi0, SmolVLA) achieve near-saturation on standard benchmarks (97-99%) but exhibit robustness gaps under distribution shift (LIBERO-Plus)\n- Existing inference-time approaches: sample selection only (ReconVLA), task-level RL (SC-VLA), high-latency verifiers (VLA-Pilot 2.41s/step) — none explore learned action correction on frozen VLAs\n- Our contribution: **sample-then-correct pipeline** — conformal sample selection (K=10) followed by a lightweight observation-conditioned Conformal Refinement Module (CRM, ~250K params, ~3ms overhead)\n- Three findings:\n  1. Sample-then-correct > sample-then-select: obs_only CRM +7pp over argmin on LIBERO object (19% vs 12%, exp: `eval-acr-object-v4-obs-only` vs `eval-argmin-only-object`)\n  2. Observation features > conformal features for correction conditioning (honest negative: per-DOF conformal features ≈ argmin, exp: `eval-acr-object-v4-small`)\n  3. Correction magnitude control is critical and previously unrecognized — norm=1.42 → 0%, norm=0.1 → 19% (exp: `eval-acr-spatial-v4-default-r3`, magnitude sweep D032)\n\n**Figure**: Fig. 1 — Pipeline overview diagram (sample → conformal selection → CRM correction → execution)\n\n---\n\n## 2. Related Work (~1.5 pages)\n\n→ See `paper/sections/related_work.md` for full draft.\n\nThree subsections:\n- (a) VLA Robustness and Inference-Time Adaptation\n- (b) Conformal Prediction in Robotics\n- (c) Residual Correction and Learned Action Refinement\n\n---\n\n## 3. Method (~2 pages)\n\n### 3.1 Problem Setup and Notation\n- Frozen VLA policy π_θ generating K action samples via flow matching\n- Distribution shift setting: train on nominal env, deploy under perturbation (LIBERO-Plus object/spatial)\n- Goal: inference-time module that improves closed-loop success without retraining π_θ\n\n### 3.2 Conformal Sample Selection\n- Generate K=10 action samples from flow-matching VLA\n- Compute nonconformity scores (CGS-based Mahalanobis scoring [Braun et al., 2025])\n- Select best sample via argmin nonconformity score\n- This stage approximates ReconVLA's selection strategy — serves as our primary baseline\n\n**Key refs**: [Angelopoulos & Bates, 2023], [Braun et al., 2025], [Chen et al., 2026]\n\n### 3.3 Conformal Refinement Module (CRM)\n- Architecture: lightweight MLP (~250K params) mapping conditioning features → action residual δ\n- Output: a_corrected = a_selected + clip(δ, norm_max)\n- **CRM Variants** (systematic ablation):\n  - **obs_only**: conditions on VLA observation features (image + language embeddings)\n  - **perdof**: conditions on per-DOF conformal statistics (interval widths, coverage indicators per action dimension)\n  - **scalar**: conditions on scalar conformal score only\n- Training: offline L2 regression on calibration set, predicting residual to expert action\n- Magnitude control: clip correction norm to norm_max (key hyperparameter)\n\n**Figure**: Fig. 2 — CRM architecture diagram showing obs_only vs perdof vs scalar conditioning paths\n\n### 3.4 Correction Magnitude Control\n- Unbounded correction (norm=1.42) → catastrophic failure (0% SR)\n- Observation-conditioned CRM robust across norm ∈ [0.03, 0.3]\n- Per-DOF CRM collapses at norm ≥ 0.2\n- Hypothesis: per-DOF features produce overconfident directional corrections that compound at high magnitude\n\n---\n\n## 4. Experiments (~2.5 pages)\n\n### 4.1 Experimental Setup\n- **Backbone**: SmolVLA (450M params, flow matching) [Shukor et al., 2025]\n- **Benchmark**: LIBERO-Plus [Fei et al., 2025] — spatial (position perturbation) and object (object substitution) suites, 10 tasks each\n- **Evaluation**: 10 rollouts per task, success rate (SR), 2 seeds (seed=42, seed=43)\n- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10, perdof CRM, scalar CRM, obs_only CRM\n- **Statistical tests**: Fisher exact test on combined seeds (200 trials), bootstrap CI\n\n### 4.2 Main Results: Object Manipulation (Main Story)\n\n**Table 1**: Object benchmark 10-task success rates (seed=42 FINAL + seed=43 pending)\n\n| Method | SR (seed=42) | Δ vs argmin | exp_id |\n|--------|-------------|-------------|--------|\n| obs_only 0.1 | **19.0%** | **+7.0pp** | `eval-acr-object-v4-obs-only` |\n| obs_only 0.2 | 18.0% (5/10) | +6.0pp | running |\n| argmin K=10 | 12.0% | baseline | `eval-argmin-only-object` |\n| VLA-only K=1 | 12.0% | 0pp | `eval-vla-only-object-k1` |\n| VLA-mean K=10 | 12.0% | 0pp | — |\n| perdof 0.1 | 11.0% | -1.0pp | `eval-acr-object-v4-small` |\n| scalar 0.1 | 9.0% | -3.0pp | `eval-acr-object-v4-scalar` |\n\n**Key message**: obs_only CRM is the only method that significantly improves over sample selection. Per-DOF conformal features and scalar scores fail to provide useful correction signal.\n\n**Figure**: Fig. 3 — Bar chart comparing all 6 methods on object benchmark (with error bars from seed=43)\n\n### 4.3 Spatial Manipulation: An Honest Negative Result\n\n**Table 2**: Spatial benchmark 10-task success rates (LOCKED)\n\n| Method | SR | Δ vs argmin | exp_id |\n|--------|-----|-------------|--------|\n| obs_only 0.1 | 35% | +1pp | `eval-acr-spatial-v4-obs-only-r3` |\n| perdof 0.1 | 35% | +1pp | `eval-acr-spatial-v4-small-r2` |\n| argmin K=10 | 34% | baseline | `eval-argmin-only-spatial-r2` |\n| scalar 0.1 | 32% | -2pp | `eval-acr-spatial-v4-scalar` |\n| VLA-mean K=10 | 32% | -2pp | — |\n| VLA-only K=1 | 30% | -4pp | — |\n\n**Key message**: No CRM variant helps on spatial tasks. Hypothesis: spatial perturbation (position offset) causes fundamentally different error modes that action correction cannot address — requires re-planning, not action refinement. Object substitution creates correctable action distribution shifts.\n\n### 4.4 Correction Magnitude Sensitivity (Key Empirical Contribution)\n\n**Table 3 / Figure**: Magnitude sweep on spatial (4 norm values × 2 CRM variants)\n\n| norm | obs_only SR | perdof SR | gap | exp_id |\n|------|------------|-----------|-----|--------|\n| 0.03 | 55.0% (4t) | 30.0% (10t) | +25pp* | magnitude sweep D032 |\n| 0.05 | 35.0% (10t) | 31.0% (10t) | +4.0pp | `eval-mag-obsonly-norm005` |\n| 0.2 | 35.0% (10t) | 28.3% (6t) | +6.7pp | `eval-mag-obsonly-norm02` |\n| 0.3 | 36.0% (10t) | 26.0% (10t) | +10pp | `eval-mag-perdof-norm03` |\n\n**Figure**: Fig. 4 — Line plot: SR vs correction norm for obs_only and perdof. obs_only flat, perdof declining.\n\n**Key message**: obs_only CRM maintains stable performance across 10× range of correction magnitudes. perdof CRM collapses at high norm → overconfident directional corrections from noisy per-DOF features.\n\n### 4.5 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences\n\n---\n\n## 5. Discussion (~0.5 pages)\n\n### Why obs_only works and perdof doesn't\n- Observation embeddings encode task-relevant semantic information (object identity, spatial layout) that is stable across distribution shifts\n- Per-DOF conformal statistics estimated from K=10 samples are noisy — covariance estimation from 10 samples in 7D action space is ill-conditioned\n- Magnitude sweep evidence: perdof collapses at high norm = CRM learns overconfident corrections from noisy per-DOF features; obs_only corrections remain conservative/stable\n- Connection to literature: [Ovadia et al., 2019] show UQ degrades under shift; [Sampson et al., 2024] show per-dimension marginal CP loses inter-DOF coherence\n\n### Limitations\n- Simulation only (LIBERO); real-robot transfer untested\n- SmolVLA backbone only; generalization to other VLAs (OpenVLA, pi0) untested\n- Spatial tasks show no improvement — CRM cannot address perturbations requiring re-planning\n- CRM trained per-benchmark (not zero-shot); requires calibration data from target distribution\n\n### Future Work\n- Real-robot experiments\n- Adaptive magnitude scheduling (decay over episode, uncertainty-conditioned)\n- Combining with training-time robustness methods (SRPO, RobustVLA)\n- Multi-VLA evaluation\n\n---\n\n## 6. Conclusion (~0.25 pages)\n- First systematic study of inference-time learned action correction for frozen VLAs\n- Sample-then-correct > sample-then-select (+7pp on LIBERO object)\n- Observation features > conformal features for correction conditioning (honest negative)\n- Correction magnitude control is critical and previously unrecognized\n\n---\n\n## Appendix (supplementary)\n- Per-task breakdown tables (all 10 tasks × all methods)\n- CRM training details (architecture, hyperparameters, training data)\n- Conformal prediction background (CGS, nonconformity scores)\n- Additional magnitude sweep results\n- Compute analysis (K=10 overhead, CRM inference time)\n",
    "structuredPatch": [
      {
        "oldStart": 131,
        "oldLines": 7,
        "newStart": 131,
        "newLines": 13,
        "lines": [
          " ",
          " **Key message**: obs_only CRM maintains stable performance across 10× range of correction magnitudes. perdof CRM collapses at high norm → overconfident directional corrections from noisy per-DOF features.",
          " ",
          "-### 4.5 Statistical Significance (seed=43 results, pending)",
          "+### 4.5 K-Value Sweep Ablation",
          "+",
          "+→ See `paper/sections/ablation_k_sweep.md` for full draft.",
          "+",
          "+**Key message**: K=2 (Plan A) ≈ K=10 ≈ K=20 on both Object (18.3% / 16.8% / 18.8%) and Spatial (35.0% / 34.5% / 34.3%). Diminishing returns beyond K=2 justify Plan A (adaptive K=2) as Pareto-optimal — matches K=20 SR with ≤2× VLA compute. K=20 exp_ids: `eval-k20-obs-only-object-seed{42,43,44,45}`, `eval-k20-obs-only-spatial-seed{42,43,44}`.",
          "+",
          "+### 4.6 Statistical Significance (seed=43 results, pending)",
          " - Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)",
          " - Per-task breakdown showing consistency",
          " - Bootstrap 95% CI for success rate differences"
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

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01VAA6HrvQgZh2utVu3Ucxts`</summary>

```json
{
  "name": "ablation_k_sweep_section",
  "type": "paper",
  "description": "Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
  "tags": [
    "paper",
    "ablation",
    "k_sweep",
    "k20"
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
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "86eaf548-0a9e-45e2-b5e2-624a070cae9d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018U7Locz6UJVxqJgRHEF6BY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 78492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
      },
      "output_tokens": 50,
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

_source line 35 · 2026-05-21T11:28:37.489Z_

<details><summary>↩ Tool result · `toolu_01VAA6HrvQgZh2utVu3Ucxts`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_9622ce\", \"name\": \"ablation_k_sweep_section\", \"type\": \"paper\", \"description\": \"Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/ablation_k_sweep.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T11:28:37.256209+00:00\", \"tags\": [\"paper\", \"ablation\", \"k_sweep\", \"k20\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "ea7fbbb3-3fca-48b2-a00d-657c4e3eeb4a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_9622ce\\\", \\\"name\\\": \\\"ablation_k_sweep_section\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/ablation_k_sweep.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T11:28:37.256209+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"ablation\\\", \\\"k_sweep\\\", \\\"k20\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_9622ce\", \"name\": \"ablation_k_sweep_section\", \"type\": \"paper\", \"description\": \"Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/ablation_k_sweep.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T11:28:37.256209+00:00\", \"tags\": [\"paper\", \"ablation\", \"k_sweep\", \"k20\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

写入完成。

**新建文件**: `paper/sections/ablation_k_sweep.md`
- Table A: K ∈ {1, 2, 10, 20} 双 benchmark SR（K=20 数字 18.8±1.0% Object / 34.3±0.6% Spatial 来自 4 + 3 个 seed，per-seed 原始值列出）
- 列出全部 K=20 exp_ids：`eval-k20-obs-only-object-seed{42,43,44,45}`、`eval-k20-obs-only-spatial-seed{42,43,44}`
- "Diminishing returns beyond K=2" 段：K=10/K=20 与 K=2 在一个 std 内重叠
- "Implication" 段：K=20 = 10× VLA forwards 无收益 → 推荐 Plan A (K=2 adaptive，trigger_rate 84%/98%) 为操作点

**更新 outline.md**: 新增 §4.5 K-Value Sweep Ablation 指向新 section，原 §4.5 Statistical Significance → §4.6。

**Artifact 已注册**: `art_20260521_9622ce`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "uuid": "f2ddaab2-3b13-48eb-882c-0fb7fe4809cc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018x4VQMMmozg65se9jdvXCb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 79319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 854
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

_source line 37_

写入完成。

**新建文件**: `paper/sections/ablation_k_sweep.md`
- Table A: K ∈ {1, 2, 10, 20} 双 benchmark SR（K=20 数字 18.8±1.0% Object / 34.3±0.6% Spatial 来自 4 + 3 个 seed，per-seed 原始值列出）
- 列出全部 K=20 exp_ids：`eval-k20-obs-only-object-seed{42,43,44,45}`、`eval-k20-obs-only-spatial-seed{42,43,44}`
- "Diminishing returns beyond K=2" 段：K=10/K=20 与 K=2 在一个 std 内重叠
- "Implication" 段：K=20 = 10× VLA forwards 无收益 → 推荐 Plan A (K=2 adaptive，trigger_rate 84%/98%) 为操作点

**更新 outline.md**: 新增 §4.5 K-Value Sweep Ablation 指向新 section，原 §4.5 Statistical Significance → §4.6。

**Artifact 已注册**: `art_20260521_9622ce`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 112628,
  "duration_api_ms": 109846,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "252674b8-0a33-48fb-b8ee-c6a7f145a27c",
  "total_cost_usd": 1.00070375,
  "usage": {
    "input_tokens": 28,
    "cache_creation_input_tokens": 83725,
    "cache_read_input_tokens": 608767,
    "output_tokens": 6862,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 83725,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 392,
        "cache_read_input_tokens": 79319,
        "cache_creation_input_tokens": 854,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 854
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1254,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001349,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 28,
      "outputTokens": 6862,
      "cacheReadInputTokens": 608767,
      "cacheCreationInputTokens": 83725,
      "webSearchRequests": 0,
      "costUSD": 0.99935475,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "689e6e9f-c76b-41e4-ab18-23cf86cecb6c"
}
```

</details>

---
