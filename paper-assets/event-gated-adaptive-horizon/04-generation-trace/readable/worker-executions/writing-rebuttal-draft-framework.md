# writing rebuttal draft framework

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659.log`
- **Structured JSON:** [`97c603aa897212b545c8.json`](../../sessions/97/97c603aa897212b545c8.json)

## Before a recorded user message

30 recorded events

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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
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
  "uuid": "a8fadfc4-2ec8-4f27-bfef-1c5d73f46674",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779451200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d99cb460-8eb3-497b-8ec8-460b2eee2caf",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Assistant

_source line 4_

I'll start by loading all the required input sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "d7f17ae3-73b0-4b00-9b71-878593d7eeaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014T9u7dYB1ha2AaUsoxUr6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13189,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13189
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014swgNAtBSbibqqx9vHcBjt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "8d6d1ca5-096c-4e4c-9f85-6a5cb6bdb1c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014T9u7dYB1ha2AaUsoxUr6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13189,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13189
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

_source line 6 · 2026-05-22T07:37:13.346Z_

<details><summary>↩ Tool result · `toolu_014swgNAtBSbibqqx9vHcBjt`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "f9377d3f-86e6-448b-ba3b-30d080e3c271",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me load all the input sources in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "8b344727-29fe-4241-9c8f-7a59c85c35be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

Loading all input sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "bf46feb4-1f1b-4b40-9df1-ed027703d45e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U7CyPqMX2cyQZ2xfuepjYs`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "artifacts/review_reports/round_1.md",
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "877f6619-6c6e-48f4-831b-78391f6f2aa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 10 · 2026-05-22T07:37:20.028Z_

<details><summary>↩ Tool result · `toolu_01U7CyPqMX2cyQZ2xfuepjYs`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_reports/round_1.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "0b3d6b12-a946-4d0b-b8f5-549f324ea0c0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_reports/round_1.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_reports/round_1.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_011HCbEyYMJUG2buRsnmRhrE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_loeo_crossval_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "db04743d-8588-4321-b95a-e34b20cba96c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 12 · 2026-05-22T07:37:21.591Z_

<details><summary>↩ Tool result · `toolu_011HCbEyYMJUG2buRsnmRhrE`</summary>

````text
1	# NVE Leave-One-Environment-Out Cross-Validation
2	
3	**Date**: 2026-05-22
4	**Purpose**: Demonstrate that NVE threshold θ=1.5× is not post-hoc by showing it generalizes across environments via leave-one-environment-out (LOEO) cross-validation.
5	
6	## Dataset
7	
8	20 experiments across 3 environments. Each experiment has a peak NVE (35K+ window) and a binary CIVO label (ground truth based on whether runaway value overestimation + eval collapse occurred).
9	
10	### Walker (N=13, baseline=exp_001_baseline)
11	
12	| Experiment | Peak NVE | Label | Config |
13	|---|---|---|---|
14	| exp_006_fixed_dt2 | 4.84 | CIVO | trained dt_emb, dt=2, H=15 |
15	| exp_008d_subsample_on_h8 | 4.13 | CIVO | trained dt_emb, subsample ON, H=8 |
16	| exp_009b_008d_walker_s2 | 1.62 | CIVO | 008d config, seed 2 (self-correction) |
17	| exp_008d_civo_trigger_s3 | 1.53 | CIVO | 008d config, seed 3 (late-onset) |
18	| exp_001_baseline (s1) | 1.00 | non-CIVO | vanilla DreamerV3 |
19	| exp_009d_baseline_s1 | 1.00 | non-CIVO | baseline seed 1 extended |
20	| exp_009a_baseline_s2 | 1.34 | non-CIVO | baseline seed 2 |
21	| exp_008a_no_subsample_dt2 | 0.93 | non-CIVO | unexposed dt_emb (subsample OFF) |
22	| exp_008e_v3_walker_s1 | 0.94 | non-CIVO | dt=1 imagination, healthy |
23	| exp_008e_v3_walker_s2 | 3.78 | non-CIVO | dt=1 imagination, IRD collapse (non-CIVO mechanism) |
24	| exp_008f_no_dt_embed | 0.97 | non-CIVO | no dt_emb ablation |
25	| exp_009c_008f_walker_s2 | 1.14 | non-CIVO | no dt_emb, seed 2 |
26	| exp_015b_frozen_dt_emb | 1.45 | non-CIVO | frozen dt_emb |
27	
28	### Cheetah (N=5, baseline=exp_010a_cheetah_baseline_s1)
29	
30	| Experiment | Peak NVE | Label | Config |
31	|---|---|---|---|
32	| exp_010b_s1 (seed 1) | 8.27 | CIVO | trained dt_emb, subsample ON, H=8 |
33	| exp_010b_s0 (seed 0) | 70.64 | CIVO | same config, eval collapsed to 0.83 |
34	| exp_010a_baseline | 1.00 | non-CIVO | vanilla DreamerV3 Cheetah |
35	| exp_008a_cheetah_s0 | 0.49† | non-CIVO | unexposed dt_emb on Cheetah |
36	| exp_008a_cheetah_s1 | 0.48† | non-CIVO | unexposed dt_emb on Cheetah |
37	
38	†NVE at 105K step; true peak may be slightly higher but well below 1.5×.
39	
40	### PickCube (N=2, baseline=exp_019a_v2_pickcube_baseline)
41	
42	| Experiment | Peak NVE | Label | Config |
43	|---|---|---|---|
44	| exp_019b_civo_trigger | 3.78 | CIVO | trained dt_emb, subsample ON, H=8; transient CIVO at 52.5K, eval 26.6 vs baseline 58.6 (−55%) |
45	| exp_019a_v2_baseline | 1.00 | non-CIVO | vanilla DreamerV3 PickCube |
46	
47	## Method
48	
49	For each fold:
50	1. Remove all experiments from one environment (held-out set)
51	2. On the remaining training set, scan θ from 0.5 to 5.0 (step 0.1) to find the range maximizing binary classification accuracy (predict CIVO if peak NVE ≥ θ)
52	3. Compute training-set AUROC (threshold-independent)
53	4. Apply θ=1.5 to the held-out set, report accuracy and AUROC
54	
55	AUROC uses the Wilcoxon-Mann-Whitney statistic (fraction of concordant positive-negative pairs).
56	
57	## Results
58	
59	### Fold 1: Hold-out PickCube → Train on Walker + Cheetah (N=18)
60	
61	**Training set**: 6 CIVO, 12 non-CIVO
62	
63	| Metric | Value |
64	|---|---|
65	| Training AUROC | 70/72 = **0.972** |
66	| Optimal θ range (max accuracy) | (1.45, 1.53] |
67	| Training accuracy at θ=1.5 | 17/18 = **0.944** |
68	| Training error | 1 FP: exp_008e_v3_s2 (NVE=3.78, IRD mechanism) |
69	
70	**Held-out PickCube (N=2)**:
71	
72	| Metric | Value |
73	|---|---|
74	| Accuracy at θ=1.5 | 2/2 = **1.000** |
75	| AUROC | 1/1 = **1.000** |
76	| Clopper-Pearson 95% CI (accuracy) | [0.158, 1.000] |
77	
78	### Fold 2: Hold-out Cheetah → Train on Walker + PickCube (N=15)
79	
80	**Training set**: 5 CIVO, 10 non-CIVO
81	
82	| Metric | Value |
83	|---|---|
84	| Training AUROC | 47.5/50 = **0.950** |
85	| Optimal θ range (max accuracy) | (1.45, 1.53] |
86	| Training accuracy at θ=1.5 | 14/15 = **0.933** |
87	| Training error | 1 FP: exp_008e_v3_s2 (NVE=3.78, IRD mechanism) |
88	
89	**Held-out Cheetah (N=5)**:
90	
91	| Metric | Value |
92	|---|---|
93	| Accuracy at θ=1.5 | 5/5 = **1.000** |
94	| AUROC | 6/6 = **1.000** |
95	| Clopper-Pearson 95% CI (accuracy) | [0.478, 1.000] |
96	
97	### Fold 3: Hold-out Walker → Train on Cheetah + PickCube (N=7)
98	
99	**Training set**: 3 CIVO, 4 non-CIVO
100	
101	| Metric | Value |
102	|---|---|
103	| Training AUROC | 12/12 = **1.000** |
104	| Optimal θ range (max accuracy) | (1.00, 3.78) — any θ in this range achieves 7/7 |
105	| Training accuracy at θ=1.5 | 7/7 = **1.000** |
106	| Training error | None |
107	
108	**Held-out Walker (N=13)**:
109	
110	| Metric | Value |
111	|---|---|
112	| Accuracy at θ=1.5 | 12/13 = **0.923** |
113	| AUROC | 34/36 = **0.944** |
114	| Clopper-Pearson 95% CI (accuracy) | [0.640, 0.998] |
115	| Error | 1 FP: exp_008e_v3_s2 (NVE=3.78, IRD collapse, non-CIVO mechanism) |
116	
117	### Summary Table
118	
119	| Held-out Env | N_train | N_test | θ_opt range | Train Acc (θ=1.5) | Test Acc (θ=1.5) | Test AUROC |
120	|---|---|---|---|---|---|---|
121	| PickCube | 18 | 2 | (1.45, 1.53] | 0.944 | **1.000** | **1.000** |
122	| Cheetah | 15 | 5 | (1.45, 1.53] | 0.933 | **1.000** | **1.000** |
123	| Walker | 7 | 13 | (1.00, 3.78) | 1.000 | **0.923** | **0.944** |
124	| **Mean** | — | — | — | 0.959 | **0.974** | **0.981** |
125	
126	## Key Findings
127	
128	1. **θ=1.5 is within the optimal accuracy range for all three training folds.** In Folds 1 and 2 (where Walker data dominates training), the optimal range is narrow: (1.45, 1.53]. In Fold 3 (Cheetah+PickCube only), the range is wider (1.0, 3.78) due to strong separation between CIVO (min NVE=3.78) and non-CIVO (max NVE=1.0).
129	
130	2. **Mean held-out accuracy = 0.974, mean AUROC = 0.981.** The threshold generalizes across all three environments without retuning.
131	
132	3. **The single cross-validation error** is exp_008e_v3_s2 (Walker), an IRD (Imagination-Reality Divergence) collapse with peak NVE=3.78. This is a mechanistically distinct failure mode where eval collapse *precedes* the NVE rise (NVE was 0.68 at 85K when eval was still 534, then jumped to 3.78 at 105K as eval crashed to 137). The NVE threshold correctly identifies this as anomalous but cannot distinguish CIVO from IRD based on peak NVE alone.
133	
134	4. **CIVO severity varies dramatically across environments** — Walker CIVO peaks at NVE 1.53–4.84, Cheetah at 8.27–70.64 (10×+ higher), PickCube at 3.78 (transient, self-correcting). Despite this variation, θ=1.5 correctly separates CIVO from non-CIVO in all environments.
135	
136	## Limitations
137	
138	- **PickCube sample size (N=2)**: Fold 1 held-out results are statistically weak (CP 95% CI: [0.158, 1.000]).
139	- **Cheetah negatives**: Peak NVE for exp_008a_cheetah_s0/s1 uses the 105K-step value (0.49/0.48) rather than true peak across all steps ≥35K. Given these are unexposed dt_emb experiments, the peak is almost certainly <1.0.
140	- **IRD confound**: The only FP (exp_008e_v3_s2, NVE=3.78) is a non-CIVO failure mode. NVE alone cannot distinguish CIVO from IRD; trajectory-shape analysis (NVE rise precedes vs follows eval decline) is needed. This is discussed in the paper's Appendix.
141	
142	## LaTeX Table (for Appendix)
143	
144	```latex
145	\begin{table}[h]
146	\centering
147	\caption{Leave-one-environment-out cross-validation of NVE threshold $\theta=1.5\times$.
148	For each fold, the threshold is validated on an environment whose data was \emph{not} used
149	to select $\theta$. The optimal threshold range on each training set is reported;
150	$\theta=1.5$ falls within the optimal range in all three folds.}
151	\label{tab:nve_loeo}
152	\begin{tabular}{lccccc}
153	\toprule
154	Held-out & $N_{\text{train}}$ & $N_{\text{test}}$ & $\theta_{\text{opt}}$ range & Test Accuracy & Test AUROC \\
155	\midrule
156	PickCube & 18 & 2 & $(1.45,\, 1.53]$ & 2/2 (1.000) & 1.000 \\
157	Cheetah  & 15 & 5 & $(1.45,\, 1.53]$ & 5/5 (1.000) & 1.000 \\
158	Walker   &  7 & 13 & $(1.00,\, 3.78)$ & 12/13 (0.923) & 0.944 \\
159	\midrule
160	\textbf{Mean} & — & — & — & \textbf{0.974} & \textbf{0.981} \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	```
165	
166	## Data Provenance
167	
168	- Walker NVE data: `artifacts/nve_threshold_sensitivity.json` (12 experiments) + exp_006 from `nve_threshold_analysis.json`
169	- Cheetah NVE data: `registry.yaml` (exp_010b peak NVE via `artifacts/analysis/exp_010b_peak_nve_calculation.json`; exp_008a_cheetah NVE from registry metrics)
170	- PickCube NVE data: `registry.yaml` (exp_019b nve_peak=3.78; baseline=1.0)
171	- CIVO labels: ground truth from registry conclusions and experiment analysis reports
172	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "4040798e-a6c6-466d-8539-b2fe78e566f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_loeo_crossval_report.md",
      "content": "# NVE Leave-One-Environment-Out Cross-Validation\n\n**Date**: 2026-05-22\n**Purpose**: Demonstrate that NVE threshold θ=1.5× is not post-hoc by showing it generalizes across environments via leave-one-environment-out (LOEO) cross-validation.\n\n## Dataset\n\n20 experiments across 3 environments. Each experiment has a peak NVE (35K+ window) and a binary CIVO label (ground truth based on whether runaway value overestimation + eval collapse occurred).\n\n### Walker (N=13, baseline=exp_001_baseline)\n\n| Experiment | Peak NVE | Label | Config |\n|---|---|---|---|\n| exp_006_fixed_dt2 | 4.84 | CIVO | trained dt_emb, dt=2, H=15 |\n| exp_008d_subsample_on_h8 | 4.13 | CIVO | trained dt_emb, subsample ON, H=8 |\n| exp_009b_008d_walker_s2 | 1.62 | CIVO | 008d config, seed 2 (self-correction) |\n| exp_008d_civo_trigger_s3 | 1.53 | CIVO | 008d config, seed 3 (late-onset) |\n| exp_001_baseline (s1) | 1.00 | non-CIVO | vanilla DreamerV3 |\n| exp_009d_baseline_s1 | 1.00 | non-CIVO | baseline seed 1 extended |\n| exp_009a_baseline_s2 | 1.34 | non-CIVO | baseline seed 2 |\n| exp_008a_no_subsample_dt2 | 0.93 | non-CIVO | unexposed dt_emb (subsample OFF) |\n| exp_008e_v3_walker_s1 | 0.94 | non-CIVO | dt=1 imagination, healthy |\n| exp_008e_v3_walker_s2 | 3.78 | non-CIVO | dt=1 imagination, IRD collapse (non-CIVO mechanism) |\n| exp_008f_no_dt_embed | 0.97 | non-CIVO | no dt_emb ablation |\n| exp_009c_008f_walker_s2 | 1.14 | non-CIVO | no dt_emb, seed 2 |\n| exp_015b_frozen_dt_emb | 1.45 | non-CIVO | frozen dt_emb |\n\n### Cheetah (N=5, baseline=exp_010a_cheetah_baseline_s1)\n\n| Experiment | Peak NVE | Label | Config |\n|---|---|---|---|\n| exp_010b_s1 (seed 1) | 8.27 | CIVO | trained dt_emb, subsample ON, H=8 |\n| exp_010b_s0 (seed 0) | 70.64 | CIVO | same config, eval collapsed to 0.83 |\n| exp_010a_baseline | 1.00 | non-CIVO | vanilla DreamerV3 Cheetah |\n| exp_008a_cheetah_s0 | 0.49† | non-CIVO | unexposed dt_emb on Cheetah |\n| exp_008a_cheetah_s1 | 0.48† | non-CIVO | unexposed dt_emb on Cheetah |\n\n†NVE at 105K step; true peak may be slightly higher but well below 1.5×.\n\n### PickCube (N=2, baseline=exp_019a_v2_pickcube_baseline)\n\n| Experiment | Peak NVE | Label | Config |\n|---|---|---|---|\n| exp_019b_civo_trigger | 3.78 | CIVO | trained dt_emb, subsample ON, H=8; transient CIVO at 52.5K, eval 26.6 vs baseline 58.6 (−55%) |\n| exp_019a_v2_baseline | 1.00 | non-CIVO | vanilla DreamerV3 PickCube |\n\n## Method\n\nFor each fold:\n1. Remove all experiments from one environment (held-out set)\n2. On the remaining training set, scan θ from 0.5 to 5.0 (step 0.1) to find the range maximizing binary classification accuracy (predict CIVO if peak NVE ≥ θ)\n3. Compute training-set AUROC (threshold-independent)\n4. Apply θ=1.5 to the held-out set, report accuracy and AUROC\n\nAUROC uses the Wilcoxon-Mann-Whitney statistic (fraction of concordant positive-negative pairs).\n\n## Results\n\n### Fold 1: Hold-out PickCube → Train on Walker + Cheetah (N=18)\n\n**Training set**: 6 CIVO, 12 non-CIVO\n\n| Metric | Value |\n|---|---|\n| Training AUROC | 70/72 = **0.972** |\n| Optimal θ range (max accuracy) | (1.45, 1.53] |\n| Training accuracy at θ=1.5 | 17/18 = **0.944** |\n| Training error | 1 FP: exp_008e_v3_s2 (NVE=3.78, IRD mechanism) |\n\n**Held-out PickCube (N=2)**:\n\n| Metric | Value |\n|---|---|\n| Accuracy at θ=1.5 | 2/2 = **1.000** |\n| AUROC | 1/1 = **1.000** |\n| Clopper-Pearson 95% CI (accuracy) | [0.158, 1.000] |\n\n### Fold 2: Hold-out Cheetah → Train on Walker + PickCube (N=15)\n\n**Training set**: 5 CIVO, 10 non-CIVO\n\n| Metric | Value |\n|---|---|\n| Training AUROC | 47.5/50 = **0.950** |\n| Optimal θ range (max accuracy) | (1.45, 1.53] |\n| Training accuracy at θ=1.5 | 14/15 = **0.933** |\n| Training error | 1 FP: exp_008e_v3_s2 (NVE=3.78, IRD mechanism) |\n\n**Held-out Cheetah (N=5)**:\n\n| Metric | Value |\n|---|---|\n| Accuracy at θ=1.5 | 5/5 = **1.000** |\n| AUROC | 6/6 = **1.000** |\n| Clopper-Pearson 95% CI (accuracy) | [0.478, 1.000] |\n\n### Fold 3: Hold-out Walker → Train on Cheetah + PickCube (N=7)\n\n**Training set**: 3 CIVO, 4 non-CIVO\n\n| Metric | Value |\n|---|---|\n| Training AUROC | 12/12 = **1.000** |\n| Optimal θ range (max accuracy) | (1.00, 3.78) — any θ in this range achieves 7/7 |\n| Training accuracy at θ=1.5 | 7/7 = **1.000** |\n| Training error | None |\n\n**Held-out Walker (N=13)**:\n\n| Metric | Value |\n|---|---|\n| Accuracy at θ=1.5 | 12/13 = **0.923** |\n| AUROC | 34/36 = **0.944** |\n| Clopper-Pearson 95% CI (accuracy) | [0.640, 0.998] |\n| Error | 1 FP: exp_008e_v3_s2 (NVE=3.78, IRD collapse, non-CIVO mechanism) |\n\n### Summary Table\n\n| Held-out Env | N_train | N_test | θ_opt range | Train Acc (θ=1.5) | Test Acc (θ=1.5) | Test AUROC |\n|---|---|---|---|---|---|---|\n| PickCube | 18 | 2 | (1.45, 1.53] | 0.944 | **1.000** | **1.000** |\n| Cheetah | 15 | 5 | (1.45, 1.53] | 0.933 | **1.000** | **1.000** |\n| Walker | 7 | 13 | (1.00, 3.78) | 1.000 | **0.923** | **0.944** |\n| **Mean** | — | — | — | 0.959 | **0.974** | **0.981** |\n\n## Key Findings\n\n1. **θ=1.5 is within the optimal accuracy range for all three training folds.** In Folds 1 and 2 (where Walker data dominates training), the optimal range is narrow: (1.45, 1.53]. In Fold 3 (Cheetah+PickCube only), the range is wider (1.0, 3.78) due to strong separation between CIVO (min NVE=3.78) and non-CIVO (max NVE=1.0).\n\n2. **Mean held-out accuracy = 0.974, mean AUROC = 0.981.** The threshold generalizes across all three environments without retuning.\n\n3. **The single cross-validation error** is exp_008e_v3_s2 (Walker), an IRD (Imagination-Reality Divergence) collapse with peak NVE=3.78. This is a mechanistically distinct failure mode where eval collapse *precedes* the NVE rise (NVE was 0.68 at 85K when eval was still 534, then jumped to 3.78 at 105K as eval crashed to 137). The NVE threshold correctly identifies this as anomalous but cannot distinguish CIVO from IRD based on peak NVE alone.\n\n4. **CIVO severity varies dramatically across environments** — Walker CIVO peaks at NVE 1.53–4.84, Cheetah at 8.27–70.64 (10×+ higher), PickCube at 3.78 (transient, self-correcting). Despite this variation, θ=1.5 correctly separates CIVO from non-CIVO in all environments.\n\n## Limitations\n\n- **PickCube sample size (N=2)**: Fold 1 held-out results are statistically weak (CP 95% CI: [0.158, 1.000]).\n- **Cheetah negatives**: Peak NVE for exp_008a_cheetah_s0/s1 uses the 105K-step value (0.49/0.48) rather than true peak across all steps ≥35K. Given these are unexposed dt_emb experiments, the peak is almost certainly <1.0.\n- **IRD confound**: The only FP (exp_008e_v3_s2, NVE=3.78) is a non-CIVO failure mode. NVE alone cannot distinguish CIVO from IRD; trajectory-shape analysis (NVE rise precedes vs follows eval decline) is needed. This is discussed in the paper's Appendix.\n\n## LaTeX Table (for Appendix)\n\n```latex\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n```\n\n## Data Provenance\n\n- Walker NVE data: `artifacts/nve_threshold_sensitivity.json` (12 experiments) + exp_006 from `nve_threshold_analysis.json`\n- Cheetah NVE data: `registry.yaml` (exp_010b peak NVE via `artifacts/analysis/exp_010b_peak_nve_calculation.json`; exp_008a_cheetah NVE from registry metrics)\n- PickCube NVE data: `registry.yaml` (exp_019b nve_peak=3.78; baseline=1.0)\n- CIVO labels: ground truth from registry conclusions and experiment analysis reports\n",
      "numLines": 172,
      "startLine": 1,
      "totalLines": 172
    }
  }
}
````

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01S27xk28yB5TCJHRrwYXPtF`</summary>

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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "f6569295-dd14-4643-b3c9-c625ec5cb56d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 14 · 2026-05-22T07:37:23.203Z_

<details><summary>↩ Tool result · `toolu_01S27xk28yB5TCJHRrwYXPtF`</summary>

```text
Error: result (265,453 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "4a7edc40-e1c1-464a-ae25-ce0ea9b214f9",
  "tool_use_result": {
    "content": "Error: result (265,453 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-22T06:16:00.000Z\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-22T06:13:30.000Z\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-22T03:41:49.000Z\"}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-22T03:41:49.000Z\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"completed_at\": \"2026-05-22T02:35:33.617Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"completed_at\": \"2026-05-22T02:11:36.842Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.177Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"completed_at\": \"2026-05-21T19:45:52.311Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"completed_at\": \"2026-05-21T19:45:31.290Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T19:38:29.196731+00:00\"}]}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:38:24.346Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T16:11:39.130025+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T16:08:03.906985+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:07:58.973Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T07:48:17.595Z\", \"training_hours\": 8.33}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/\", \"completed_at\": \"2026-05-21T12:18:09.552Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"retry_count\": 0, \"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah\", \"completed_at\": \"2026-05-21T12:14:19.189109+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:46.032647+00:00\"}]}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:37.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"logdir/exp_033_wide_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T12:08:15.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:31.184962+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:26.400Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T03:46:14.882Z\", \"training_hours\": 8.27}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031b_tcn_pickcube_s0_sigma05/latest.pt\", \"completed_at\": \"2026-05-21T08:43:18.481253+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T08:41:51.310620+00:00\"}]}, \"failure_reason\": \"NVE late-stage decline is floor effect (value signal collapse), not CIVO recovery. Eval flat 25-29 throughout — agent never learned meaningful manipulation. Confirmed by Reviewer. TCN PickCube: 0/2 (σ=0.2 and σ=0.5 both failed).\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:41:45.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T07:47:55.131382+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T07:45:13.742811+00:00\"}]}, \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:45:08.395Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt\", \"completed_at\": \"2026-05-21T05:50:59.612299+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T05:48:16.069863+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"pid\": \"973387\", \"reproduce\": {\"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032b_dual_critic_walker_s1\\\"\", \"finished_at\": \"2026-05-21T05:48:11.173Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-20T23:22:55.338Z\", \"training_hours\": 6.42}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"completed_at\": \"2026-05-21T03:39:24.356918+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T03:32:52.751412+00:00\"}]}, \"failure_reason\": \"Sudden CIVO blowup: NVE appeared healthy at 95K (0.666, declining from 0.855@85K), then catastrophic spike to 3.0@105K. Eval collapsed 349.6→71.8. Late-stage NVE recovery to 0.4@215K = value adaptation (eval stayed at 104.5, never recovered). TCN σ=0.2 Walker: 2/4 seeds CIVO failure (s2: NVE 2.77, s3: NVE 3.0).\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T03:32:47.021Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031_tcn_pickcube_s0_sigma02\", \"completed_at\": \"2026-05-20T23:52:48.308Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T23:50:00.801433+00:00\"}]}, \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"reproduce\": {\"finished_at\": \"2026-05-20T23:49:56.649Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"completed_at\": \"2026-05-20T22:58:31.008151+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"failure_reason\": \"CIVO confirmed: NVE accelerated 1.01→1.65→2.77@105K (008d-like pattern), eval collapsed 177.7→32.0. Late-stage NVE decline to 1.06@155K = value adaptation to collapsed policy, NOT CIVO self-recovery (eval remained at 56.5, never recovered). Killed at 156K to free GPU for dual-critic experiment.\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"completed_at\": \"2026-05-20T22:34:07.916411+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T22:28:30.207347+00:00\"}]}, \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:28:26.022Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T19:30:34.687287+00:00\"}]}, \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T19:30:28.923Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"completed_at\": \"2026-05-20T16:47:18.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"completed_at\": \"2026-05-20T16:49:02.778Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"completed_at\": \"2026-05-20T12:38:02.085Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:19:31.331Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:10:00.827Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"completed_at\": \"2026-05-20T09:24:09.016Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"completed_at\": \"2026-05-20T08:31:12.389Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"completed_at\": \"2026-05-20T06:14:31.720Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"completed_at\": \"2026-05-20T03:14:06.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"completed_at\": \"2026-05-20T03:02:46.556Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"completed_at\": \"2026-05-20T03:02:43.170Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"completed_at\": \"2026-05-20T03:02:39.948Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"completed_at\": \"2026-05-20T03:02:36.670Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"completed_at\": \"2026-05-20T03:02:32.583Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T23:06:42.122Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"completed_at\": \"2026-05-19T21:23:44.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"completed_at\": \"2026-05-19T17:44:27.212Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T09:02:40.466Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"completed_at\": \"2026-05-19T09:00:10.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"completed_at\": \"2026-05-19T06:26:03.295Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:47.459Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:45.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"completed_at\": \"2026-05-19T00:13:55.909Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"completed_at\": \"2026-05-18T23:18:51.672Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"completed_at\": \"2026-05-18T21:40:10.763Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"completed_at\": \"2026-05-18T21:40:09.329Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"completed_at\": \"2026-05-18T18:41:05.369Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"completed_at\": \"2026-05-18T18:20:00.278Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"completed_at\": \"2026-05-18T18:19:58.491Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"completed_at\": \"2026-05-18T17:12:05.307Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"completed_at\": \"2026-05-18T11:33:57.033Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:31:45.212576+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:31:41.800Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"completed_at\": \"2026-05-18T11:24:41.197Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:20:58.896484+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:20:55.020Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/latest.pt\", \"completed_at\": \"2026-05-18T08:16:42.716Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:12:12.866455+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:12:09.402Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt\", \"completed_at\": \"2026-05-18T08:10:06.059Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008d_civo_trigger_s4\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/latest.pt\", \"completed_at\": \"2026-05-18T05:17:45.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/metrics.jsonl\", \"metrics\": {\"civo_alert_105K\": 1, \"civo_confirmed\": true, \"delta_ve_105K\": 2.05, \"eval_return_trajectory\": {\"105K\": 63.6, \"15K\": 171.4, \"25K\": 189.5, \"35K\": 153.8, \"45K\": 158.2, \"55K\": 229.3, \"5K\": 30.9, \"65K\": 333.6, \"75K\": 302.4, \"85K\": 383.3, \"95K\": 240.3}, \"final_eval_return_105K\": 63.6, \"final_step\": 112000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 383.3, \"peak_eval_step\": 85000, \"target_step\": 105000, \"value_mean_105K\": 192.65, \"value_mean_95K\": 235.42, \"ve_ratio_105K\": 3.03}, \"parent\": \"exp_008d_civo_trigger_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:17:45.132Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"completed_at\": \"2026-05-18T05:11:15.900Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/metrics.jsonl\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"completed_at\": \"2026-05-18T02:00:15.236Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-18T01:56:17.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:52:09.175571+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"pid\": \"706158\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-18T01:52:05.296Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T20:35:13.253Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T20:35:16.021173+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T22:57:54.400584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:57:48.608Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T22:49:15.021Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T22:45:35.442053+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"pid\": \"696201\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:45:32.093Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T19:28:08.484Z\", \"training_hours\": 3.29}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"completed_at\": \"2026-05-17T20:34:04.841Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T20:31:37.915652+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:31:34.777Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"completed_at\": \"2026-05-16T16:16:00.478Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T16:11:35.101384+00:00\"}]}, \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:11:32.766Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"completed_at\": \"2026-05-17T19:29:52.643Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T19:25:39.255677+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:25:34.295Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo_trigger/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:35:47.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"error_summary\": \"KeyError in dreamer.py:421 — configs[\\\"maniskill\\\"] not found. Config block missing from dreamer.py.\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T03:35:50.727034+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:49:42.379952+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17 04:01: Registry shows DONE(failed) from first attempt (KeyError transient). Actual state: RUNNING (PID 646809, step 8400+, started 11:39 UTC). Cron monitoring via submit_on_allocated tmux session. Will need manual status correction when cron detects completion.\"}}, \"failure_reason\": \"Traceback → Traceback (most recent call last): File \\\"/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\", line 421, in &lt;module> recursive_update(defaults, configs[name]) ~~~~~~~^^^^^^ KeyError: 'maniskill'\", \"gpu\": \"cuda:0\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019b_pickcube_civo_trigger.log\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger\\\"\", \"finished_at\": \"2026-05-17T14:49:39.328Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T03:25:03.091Z\", \"training_hours\": 11.41}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T14:01:23.413Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:56:29.726988+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"pid\": \"670554\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"finished_at\": \"2026-05-17T13:56:27.483Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"completed_at\": \"2026-05-17T07:44:38.596Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:44:42.334281+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T10:47:17.307752+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Config error: used --configs dmc_vision (CNN+image, wrong modality) instead of dmc_proprio, and --compile True (torch.compile inductor crash). Killed and resubmitting with correct config.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:47:12.534Z\"}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"completed_at\": \"2026-05-16T21:07:12.193Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"account\": \"root\", \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"completed_at\": \"2026-05-14T04:09:46.829Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"completed_at\": \"2026-05-13T09:58:31.673Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"completed_at\": \"2026-05-13T15:23:26.384Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_15K\": 153.86, \"fps\": 8.1, \"gate_dt_mean_15K\": 1, \"gate_scale_15K\": 0, \"step\": 20000}}}, \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"latest_metrics\": {\"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"checked_at\": \"2026-05-13\", \"eval_return\": 465.67, \"eval_return_trajectory\": {\"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"5K\": 31, \"65K\": 465.7}, \"fps\": 6.69, \"gap_vs_baseline\": -150.2, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_bonus\": 0.0865, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_scale\": 0.10004, \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"pid\": 51721, \"prev_eval_return\": 541.18, \"process_status\": \"running\", \"step\": 65000, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"uptime\": \"2h31m\"}, \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s3/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:24:26.004Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T03:18:40.430236+00:00\"}]}, \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:18:37.221Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018v2_full_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-16T17:24:44.481Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T17:17:46.576638+00:00\"}]}, \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:17:44.050Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_008d_subsample_on_h8\": {\"completed_at\": \"2026-05-14T04:50:52.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:04.661Z\"}, \"exp_018_full_sgs_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt\", \"completed_at\": \"2026-05-16T23:47:49.458Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"pid\": \"612876\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_009b_008d_walker_s2\": {\"account\": \"root\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 0 sustained nve>1.5x across 4 consecutive checkpoints and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 39.27, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0, \"ve_ratio\": 0}, {\"baseline_ve\": null, \"eval_return\": 144.31, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 4.47, \"ve_ratio\": 0.031}, {\"baseline_ve\": 0.087, \"eval_return\": 141.12, \"normalized_ve\": 2.05, \"step\": 25000, \"value_mean\": 25.14, \"ve_ratio\": 0.178}, {\"baseline_ve\": 0.241, \"eval_return\": 164.14, \"normalized_ve\": 1.24, \"step\": 35000, \"value_mean\": 49.02, \"ve_ratio\": 0.299}, {\"baseline_ve\": 0.331, \"eval_return\": 141.04, \"normalized_ve\": 1.62, \"step\": 45000, \"value_mean\": 75.59, \"ve_ratio\": 0.536}, {\"baseline_ve\": 0.404, \"eval_return\": 172.33, \"normalized_ve\": 1.41, \"step\": 55000, \"value_mean\": 98.28, \"ve_ratio\": 0.57}, {\"baseline_ve\": 0.563, \"eval_return\": 209.16, \"normalized_ve\": 0.94, \"step\": 65000, \"value_mean\": 110.91, \"ve_ratio\": 0.53}, {\"baseline_ve\": 0.719, \"eval_return\": 197.46, \"normalized_ve\": 0.66, \"step\": 75000, \"value_mean\": 93.49, \"ve_ratio\": 0.474}, {\"baseline_ve\": 0.701, \"eval_return\": 236.49, \"normalized_ve\": 0.51, \"step\": 85000, \"value_mean\": 83.86, \"ve_ratio\": 0.355}, {\"baseline_ve\": 0.632, \"eval_return\": 278.54, \"normalized_ve\": 0.43, \"step\": 95000, \"value_mean\": 75.72, \"ve_ratio\": 0.272}, {\"baseline_ve\": 0.656, \"eval_return\": 267.93, \"normalized_ve\": 0.38, \"step\": 105000, \"value_mean\": 67.27, \"ve_ratio\": 0.251}], \"target_steps\": 105000, \"trend\": \"Eval rising throughout: 39→144→141→164→141→172→209→197→236→279→268. Value peaks at 110.91@65K then self-corrects downward to 67.27@105K. v/e ratio peaks 0.57@55K then monotonically declines to 0.25@105K. NO delusional critic collapse — value self-corrects while eval improves.\", \"verdict\": \"NEGATIVE — hypothesis was to replicate collapse, collapse NOT reproduced. However, pathological nve>1.5x episode confirmed (2.05x@25K, 1.62x@45K), consistent with trained dt_emb inducing pathological overestimation. Self-correction to 0.38x@105K distinguishes from seed 0's sustained overestimation → collapse.\", \"vs_baseline_105K\": \"-70.8%\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"887053\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:34.989Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"completed_at\": \"2026-05-15T19:35:10.508Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"failure_reason\": \"Same hang as 016c — SummaryWriter.flush() deadlock after add_video with moviepy 2.x. try/except insufficient because flush() blocks on incomplete async video encode. Fix: Logger.video() → no-op.\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"completed_at\": \"2026-05-13T15:23:24.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"fps\": 8.3, \"step\": 245000, \"train_return_244K\": \"935-976\"}}}, \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"latest_metrics\": {\"checked_at\": \"2026-05-13\", \"eta_hours\": 1.8, \"eval_return\": 953.37, \"eval_step\": 445000, \"fps\": 7.29, \"pid\": 9409, \"prev_eval_return\": 964.96, \"process_status\": \"running\", \"step\": 452000, \"steps_remaining\": 48000, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"uptime\": \"16h35m\"}, \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"completed_at\": \"2026-05-17T00:24:10.180Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_s3_no_dt_embed_walker/checkpoint.ckpt\", \"completed_at\": \"2026-05-16T20:09:51.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"601233\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"completed_at\": \"2026-05-16T19:43:57.604Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T19:40:49.938571+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"pid\": \"596344\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-16T19:40:47.795Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T13:43:00.745Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"pid\": \"586751\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T12:00:04.473Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T12:43:09.226Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T12:40:17.132664+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_walker_s1.log\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"pid\": \"577467\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_018_full_sgs_walker_s1 --steps 105000 --full_sgs True --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T12:40:14.687Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T09:50:18.238Z\", \"training_hours\": 2.83}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"pid\": \"536890\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"training_hours\": 13.18}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T12:10:01.788Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:10:04.203907+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:24:17.652463+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T09:48:44.475703+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T09:48:42.388Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T12:06:19.592Z\", \"training_hours\": 21.71}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"completed_at\": \"2026-05-16T04:46:30.361Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"completed_at\": \"2026-05-16T01:39:17.916Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T22:31:16.457Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:26:05.863Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer). EGL fix confirmed working: eval at step 5000 completed successfully (eval_return=31.0). OOM occurred during training loop startup after eval. Likely system RAM OOM (replay buffer + model + eval concurrent memory peak).\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:08:12.013Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:08:15.731787+00:00\"}]}, \"failure_reason\": \"误杀: Director 基于 Reviewer 错误诊断下令 kill（认为 zombie PID 522009 导致 eval deadlock），但日志证明 EGL fix (MUJOCO_EGL_DEVICE_ID=1) 已生效，eval 正常运行中 (iter=500, t=95.9s)。EGL fix 确认有效。\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009h_008f_walker_s0.log\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"522450\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T19:08:09.836Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:10:52.235Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:10:53.928926+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 524244, \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T19:10:51.013Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:59:55.315Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:59:59.820061+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM). Root cause: MUJOCO_GL=egl defaults to EGL device 0 while CUDA_VISIBLE_DEVICES=1 binds CUDA to GPU 1, causing cross-GPU context conflict and eval deadlock at step 5000.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009g_008f_walker_s0.log\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"517413\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:59:53.840Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_009f_008f_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:46:03.293Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:46:05.155411+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:52:15.790170+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Seed duplication: 009f used seed=1 same as parent 008f, producing deterministic repeat (prefill returns identical). Killed by Director order.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"516110\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:52:12.322Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T18:44:58.143Z\", \"training_hours\": 0.12}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:54:04.806Z\"}, \"exp_016_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:43:52.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:43:57.605618+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"514417\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T18:43:51.025Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"completed_at\": \"2026-05-15T12:12:25.846Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T18:27:09.189680+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次提交。首次失败原因: --device cuda:1 但 CUDA_VISIBLE_DEVICES=1 后进程内只有 cuda:0。已修正为 --device cuda:0。PID 144831, 从头开始 (step=0)。预计 ~5h 完成 105K steps。\"}}, \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:27:07.138Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"completed_at\": \"2026-05-15T11:54:55.153Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"pid\": 122271, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009e_008d_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T11:26:52.478Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 1 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/metrics.jsonl\", \"metrics\": {\"actor_loss_sign_flip\": 85000, \"baseline_105K\": 915.67, \"collapse_rate_note\": \"Independent rate = 1/2 (seed 1 collapsed, seed 2 self-corrected). 008d and 009e share seed=1, count as one independent observation.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0, \"ve_ratio\": 0}, {\"eval_return\": 153.7, \"step\": 15000, \"value_mean\": 3.4, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 167.2, \"normalized_ve\": 1.78, \"step\": 25000, \"value_mean\": 25.9, \"ve_ratio\": 0.155}, {\"baseline_ve\": 0.241, \"eval_return\": 146.3, \"normalized_ve\": 1.71, \"step\": 35000, \"value_mean\": 60.2, \"ve_ratio\": 0.411}, {\"baseline_ve\": 0.331, \"eval_return\": 140.8, \"normalized_ve\": 2.09, \"step\": 45000, \"value_mean\": 97.5, \"ve_ratio\": 0.693}, {\"baseline_ve\": 0.404, \"eval_return\": 82.7, \"normalized_ve\": 4.12, \"step\": 55000, \"value_mean\": 137.9, \"ve_ratio\": 1.666}, {\"baseline_ve\": 0.563, \"eval_return\": 250, \"normalized_ve\": 1.23, \"step\": 65000, \"value_mean\": 173.8, \"ve_ratio\": 0.695}, {\"baseline_ve\": 0.719, \"eval_return\": 178.1, \"normalized_ve\": 1.48, \"step\": 75000, \"value_mean\": 189.9, \"ve_ratio\": 1.066}, {\"baseline_ve\": 0.701, \"eval_return\": 201.93, \"normalized_ve\": 1.15, \"step\": 85000, \"value_mean\": 163.08, \"ve_ratio\": 0.808}, {\"baseline_ve\": 0.632, \"eval_return\": 132.79, \"normalized_ve\": 1.73, \"step\": 95000, \"value_mean\": 144.82, \"ve_ratio\": 1.091}, {\"baseline_ve\": 0.656, \"eval_return\": 131.08, \"normalized_ve\": 1.57, \"step\": 105000, \"value_mean\": 135.37, \"ve_ratio\": 1.033}], \"final_eval_return\": 131.08, \"final_nve\": 1.57, \"final_value_mean\": 135.37, \"final_ve_ratio\": 1.033, \"peak_nve\": 4.12, \"peak_nve_step\": 55000, \"target_steps\": 105000, \"vs_baseline_105K\": \"-85.7%\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 119108, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:31:04.722Z\"}, \"exp_009a_baseline_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:33:12.892Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"pid\": \"142508\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:08.969Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:00:20.816Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"43437\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"898127\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"140980\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"training_hours\": 6.95}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"account\": \"root\", \"completed_at\": \"2026-05-14T01:13:11.533Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"extra\": {\"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\", \"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\"}, \"gpu\": \"cuda:0\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"latest_metrics\": {\"checked_at\": \"2026-05-14\", \"eval_return\": 485.3, \"eval_return_trajectory\": {\"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3, \"5K\": 31}, \"eval_step\": 35000, \"fps\": 6.6, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"pid\": 85029, \"prev_eval_return\": 321.4, \"process_status\": \"running\", \"step\": 36000}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"pid\": \"85029\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-13T22:12:00.446Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"completed_at\": \"2026-05-13T04:50:14.987Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\", \"retry_count\": 0, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 117, \"total\": 117, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4471}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BdLjzmisavAo1aSt5z7Pp7`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "report.md",
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "43099874-c361-4d43-b3dd-495cbfaedf10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 16 · 2026-05-22T07:37:23.447Z_

<details><summary>↩ Tool result · `toolu_01BdLjzmisavAo1aSt5z7Pp7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T05:49:46Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 117 个实验 — DONE 114, RUNNING 3\\n**DONE 分布**: failed 12, killed 21, negative 35, success 46\\n\\n### GPU 占用\\n- **分配**: 4 张 — bjb1-45299:cuda:0, bjb1-45299:cuda:1, bjb1-40020:cuda:0, bjb1-40020:cuda:1\\n- **实际运行**: 3 张 — bjb1-45299:cuda:1(exp_041_dual_critic_walker_s3), bjb1-40020:cuda:0(exp_042_frozen_dt_emb_walker), bjb1-40020:cuda:1(exp_043_008f_walker_s1)\\n\\n### 💾 磁盘余量\\n- **bjb1-45299**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n- **bjb1-40020**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/root/autodl-pub`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 389G/438G 可用（已用 7%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_041_dual_critic_walker_s3` | bjb1-45299 | cuda:1 | 51098 | `…nt-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log` |\\n| `exp_042_frozen_dt_emb_walker` | bjb1-40020 | cuda:0 | 251336 | `…-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker` |\\n| `exp_043_008f_walker_s1` | bjb1-40020 | cuda:1 | 250627 | `…/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_040_wide_dual_critic_cheetah` [failed] — 2026-05-22T05:49:43 — EXIT_CODE=1 (generic error — check log tail)\\n- `exp_039_narrow_dual_critic_walker_s1` [success] — 2026-05-22T02:35:33\\n- `exp_038_dual_critic_walker_s2` [negative] — 2026-05-22T02:11:36\\n- `exp_037_wide_critic_cheetah` [negative] — 2026-05-21T19:45:52\\n- `exp_036_dual_critic_pickcube` [negative] — 2026-05-21T19:45:31\\n\\n### 🔴 最近失败原因 (top 3)\\n- `exp_040_wide_dual_critic_cheetah`: EXIT_CODE=1 (generic error — check log tail)\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_042_frozen_dt_emb_walker | dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb. | — | — | — |\\n| exp_043_008f_walker_s1 | Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。 | — | — | — |\\n| exp_041_dual_critic_walker_s3 | D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_040_wide_dual_critic_cheetah** (failed): Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。 ← 基于 exp_032_dual_critic_walker\\n- **exp_039_narrow_dual_critic_walker_s1** (success): Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\\n- **exp_038_dual_critic_walker_s2** (negative): Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments. ← 基于 exp_032_dual_critic_walker\\n\\n## 趋势\\n成功 46 / 负向 35 / 失败 12 / 共 114\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-40020: 空闲 cuda:0, cuda:1\\nbjb1-45299: 无 GPU 信息\\n\\n## 告警\\n- 016e: 已被终止 — unknown\\n- exp_002_event_gated: 训练失败 — unknown\\n- exp_006: 已被终止 — unknown\\n- exp_008a: 已被终止 — unknown\\n- exp_008a_untrained_s1: 已被终止 — unknown\\n- exp_008a_untrained_s2: 已被终止 — unknown\\n- exp_008c: 已被终止 — unknown\\n- exp_008d: 已被终止 — unknown\\n- exp_008d_civo_trigger_s2: 已被终止 — unknown\\n- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown\\n- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008f_s2: 已被终止 — unknown\\n- exp_009c_s2: 已被终止 — unknown\\n- exp_009d_baseline_walker_s1: 已被终止 — unknown\\n- exp_009f_008f_walker_s1: 已被终止 — unknown\\n- exp_009g_008f_walker_s0: 已被终止 — unknown\\n- exp_009h_008f_walker_s0: 训练失败 — unknown\\n- exp_016_sgs_walker_s1: 训练失败 — unknown\\n- exp_016b_sgs_walker_s1: 训练失败 — unknown\\n- exp_016c_sgs_walker_s1: 训练失败 — unknown\\n- exp_016d_sgs_walker_s1: 训练失败 — unknown\\n- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown\\n- exp_018_full_sgs_walker_s1: 已被终止 — unknown\\n- exp_019a_pickcube_baseline: 已被终止 — unknown\\n- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown\\n- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown\\n- exp_025_obs_sgs_walker_s1: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s3: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s4: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown\\n- exp_040_wide_dual_critic_cheetah: 训练失败 — unknown\\n\", \"total_chars\": 5145, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "a93efccc-05cf-4e06-9955-8e4b4913e45d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T05:49:46Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 117 个实验 — DONE 114, RUNNING 3\\\\n**DONE 分布**: failed 12, killed 21, negative 35, success 46\\\\n\\\\n### GPU 占用\\\\n- **分配**: 4 张 — bjb1-45299:cuda:0, bjb1-45299:cuda:1, bjb1-40020:cuda:0, bjb1-40020:cuda:1\\\\n- **实际运行**: 3 张 — bjb1-45299:cuda:1(exp_041_dual_critic_walker_s3), bjb1-40020:cuda:0(exp_042_frozen_dt_emb_walker), bjb1-40020:cuda:1(exp_043_008f_walker_s1)\\\\n\\\\n### 💾 磁盘余量\\\\n- **bjb1-45299**:\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\\\n- **bjb1-40020**:\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/root/autodl-pub`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 389G/438G 可用（已用 7%）\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `exp_041_dual_critic_walker_s3` | bjb1-45299 | cuda:1 | 51098 | `…nt-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log` |\\\\n| `exp_042_frozen_dt_emb_walker` | bjb1-40020 | cuda:0 | 251336 | `…-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker` |\\\\n| `exp_043_008f_walker_s1` | bjb1-40020 | cuda:1 | 250627 | `…/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `exp_040_wide_dual_critic_cheetah` [failed] — 2026-05-22T05:49:43 — EXIT_CODE=1 (generic error — check log tail)\\\\n- `exp_039_narrow_dual_critic_walker_s1` [success] — 2026-05-22T02:35:33\\\\n- `exp_038_dual_critic_walker_s2` [negative] — 2026-05-22T02:11:36\\\\n- `exp_037_wide_critic_cheetah` [negative] — 2026-05-21T19:45:52\\\\n- `exp_036_dual_critic_pickcube` [negative] — 2026-05-21T19:45:31\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `exp_040_wide_dual_critic_cheetah`: EXIT_CODE=1 (generic error — check log tail)\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-22\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| exp_042_frozen_dt_emb_walker | dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb. | — | — | — |\\\\n| exp_043_008f_walker_s1 | Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\\\\\"trained dt_emb → CIVO\\\\\\\"。 | — | — | — |\\\\n| exp_041_dual_critic_walker_s3 | D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。 | — | — | — |\\\\n\\\\n## 待处理\\\\n（无）\\\\n\\\\n## 近期结论\\\\n- **exp_040_wide_dual_critic_cheetah** (failed): Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。 ← 基于 exp_032_dual_critic_walker\\\\n- **exp_039_narrow_dual_critic_walker_s1** (success): Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\\\\n- **exp_038_dual_critic_walker_s2** (negative): Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments. ← 基于 exp_032_dual_critic_walker\\\\n\\\\n## 趋势\\\\n成功 46 / 负向 35 / 失败 12 / 共 114\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nbjb1-40020: 空闲 cuda:0, cuda:1\\\\nbjb1-45299: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- 016e: 已被终止 — unknown\\\\n- exp_002_event_gated: 训练失败 — unknown\\\\n- exp_006: 已被终止 — unknown\\\\n- exp_008a: 已被终止 — unknown\\\\n- exp_008a_untrained_s1: 已被终止 — unknown\\\\n- exp_008a_untrained_s2: 已被终止 — unknown\\\\n- exp_008c: 已被终止 — unknown\\\\n- exp_008d: 已被终止 — unknown\\\\n- exp_008d_civo_trigger_s2: 已被终止 — unknown\\\\n- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown\\\\n- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown\\\\n- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown\\\\n- exp_008f_s2: 已被终止 — unknown\\\\n- exp_009c_s2: 已被终止 — unknown\\\\n- exp_009d_baseline_walker_s1: 已被终止 — unknown\\\\n- exp_009f_008f_walker_s1: 已被终止 — unknown\\\\n- exp_009g_008f_walker_s0: 已被终止 — unknown\\\\n- exp_009h_008f_walker_s0: 训练失败 — unknown\\\\n- exp_016_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_016b_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_016c_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_016d_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown\\\\n- exp_018_full_sgs_walker_s1: 已被终止 — unknown\\\\n- exp_019a_pickcube_baseline: 已被终止 — unknown\\\\n- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown\\\\n- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown\\\\n- exp_025_obs_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_025_obs_sgs_walker_s3: 训练失败 — unknown\\\\n- exp_025_obs_sgs_walker_s4: 训练失败 — unknown\\\\n- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown\\\\n- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown\\\\n- exp_040_wide_dual_critic_cheetah: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 5145, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T05:49:46Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 117 个实验 — DONE 114, RUNNING 3\\n**DONE 分布**: failed 12, killed 21, negative 35, success 46\\n\\n### GPU 占用\\n- **分配**: 4 张 — bjb1-45299:cuda:0, bjb1-45299:cuda:1, bjb1-40020:cuda:0, bjb1-40020:cuda:1\\n- **实际运行**: 3 张 — bjb1-45299:cuda:1(exp_041_dual_critic_walker_s3), bjb1-40020:cuda:0(exp_042_frozen_dt_emb_walker), bjb1-40020:cuda:1(exp_043_008f_walker_s1)\\n\\n### 💾 磁盘余量\\n- **bjb1-45299**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n- **bjb1-40020**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/root/autodl-pub`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 389G/438G 可用（已用 7%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_041_dual_critic_walker_s3` | bjb1-45299 | cuda:1 | 51098 | `…nt-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log` |\\n| `exp_042_frozen_dt_emb_walker` | bjb1-40020 | cuda:0 | 251336 | `…-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker` |\\n| `exp_043_008f_walker_s1` | bjb1-40020 | cuda:1 | 250627 | `…/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_040_wide_dual_critic_cheetah` [failed] — 2026-05-22T05:49:43 — EXIT_CODE=1 (generic error — check log tail)\\n- `exp_039_narrow_dual_critic_walker_s1` [success] — 2026-05-22T02:35:33\\n- `exp_038_dual_critic_walker_s2` [negative] — 2026-05-22T02:11:36\\n- `exp_037_wide_critic_cheetah` [negative] — 2026-05-21T19:45:52\\n- `exp_036_dual_critic_pickcube` [negative] — 2026-05-21T19:45:31\\n\\n### 🔴 最近失败原因 (top 3)\\n- `exp_040_wide_dual_critic_cheetah`: EXIT_CODE=1 (generic error — check log tail)\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_042_frozen_dt_emb_walker | dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb. | — | — | — |\\n| exp_043_008f_walker_s1 | Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。 | — | — | — |\\n| exp_041_dual_critic_walker_s3 | D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_040_wide_dual_critic_cheetah** (failed): Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。 ← 基于 exp_032_dual_critic_walker\\n- **exp_039_narrow_dual_critic_walker_s1** (success): Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\\n- **exp_038_dual_critic_walker_s2** (negative): Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments. ← 基于 exp_032_dual_critic_walker\\n\\n## 趋势\\n成功 46 / 负向 35 / 失败 12 / 共 114\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-40020: 空闲 cuda:0, cuda:1\\nbjb1-45299: 无 GPU 信息\\n\\n## 告警\\n- 016e: 已被终止 — unknown\\n- exp_002_event_gated: 训练失败 — unknown\\n- exp_006: 已被终止 — unknown\\n- exp_008a: 已被终止 — unknown\\n- exp_008a_untrained_s1: 已被终止 — unknown\\n- exp_008a_untrained_s2: 已被终止 — unknown\\n- exp_008c: 已被终止 — unknown\\n- exp_008d: 已被终止 — unknown\\n- exp_008d_civo_trigger_s2: 已被终止 — unknown\\n- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown\\n- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008f_s2: 已被终止 — unknown\\n- exp_009c_s2: 已被终止 — unknown\\n- exp_009d_baseline_walker_s1: 已被终止 — unknown\\n- exp_009f_008f_walker_s1: 已被终止 — unknown\\n- exp_009g_008f_walker_s0: 已被终止 — unknown\\n- exp_009h_008f_walker_s0: 训练失败 — unknown\\n- exp_016_sgs_walker_s1: 训练失败 — unknown\\n- exp_016b_sgs_walker_s1: 训练失败 — unknown\\n- exp_016c_sgs_walker_s1: 训练失败 — unknown\\n- exp_016d_sgs_walker_s1: 训练失败 — unknown\\n- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown\\n- exp_018_full_sgs_walker_s1: 已被终止 — unknown\\n- exp_019a_pickcube_baseline: 已被终止 — unknown\\n- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown\\n- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown\\n- exp_025_obs_sgs_walker_s1: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s3: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s4: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown\\n- exp_040_wide_dual_critic_cheetah: 训练失败 — unknown\\n\", \"total_chars\": 5145, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QT6Qs17H4h9zFGFu4axZLt`</summary>

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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "fcb82373-df91-450e-a91d-85df7424827a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 18 · 2026-05-22T07:37:23.879Z_

<details><summary>↩ Tool result · `toolu_01QT6Qs17H4h9zFGFu4axZLt`</summary>

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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "7a6bc376-1d7a-4eb5-ae91-2ad6c37e929d",
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0135cUAw7ALkQ6smvhgrJrRx`</summary>

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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "aa58a31f-a1d8-4052-b7ab-c77bc62f1df3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 20 · 2026-05-22T07:37:24.874Z_

<details><summary>↩ Tool result · `toolu_0135cUAw7ALkQ6smvhgrJrRx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n> 不可从 registry/代码派生的决策原因、约束、经验教训。\\n\\n## 竞品实验参考\\n（待补充）\\n\\n## 经验教训\\n\\n### Dual-Critic 机制发现 (2026-05-21)\\n- exp_032/032b Walker dual-critic: v1≈v2 (gap <0.5), min 无 pessimism 效果，但 CIVO 仍被抑制 → 机制是 implicit regularization，不是传统 Double-Q pessimism\\n- exp_033 wide-critic (2.89M params, 2.44× normal): CIVO 仍触发 (NVE 4.7) → 参数量本身不能防 CIVO\\n- exp_034 Cheetah dual-critic: NVE 1.8 (vs baseline 70.64, 降 40×) 但仍超 1.5 阈值 → 部分抑制但不完全。Dual-wave CIVO pattern\\n\\n### 2×2 Factorial 完成 (2026-05-21)\\n- {single, dual} × {normal ~1.2M, scaled ~2.4-2.9M}:\\n  - single + normal = baseline (CIVO → collapse)\\n  - single + scaled = exp_033 (CIVO NVE 4.7 → partial recovery, eval 408)\\n  - dual + normal = exp_035 (CIVO NVE 2.75 → full recovery, eval 697.8) — Director override success\\n  - dual + scaled = exp_032 (CIVO prevented, NVE ≤1.1, eval 787.7)\\n- **双维度 insight**: Prevention = min+capacity synergy; Recovery = min 主导 (697.8 vs 408)\\n\\n### Cross-Environment 完整结果 (2026-05-21 更新)\\n- **Walker**: dual-critic 2/2 CIVO prevented (s0=787.7, s1=551.8)，但 s2 (exp_038) 出现 non-CIVO collapse (peak 354→120, NVE≤0.3)。Narrow dual s0 recovery 697.8, s1 (exp_039) collapsing\\n- **Cheetah**: dual-critic negative (NVE 1.8, eval 97.5); wide single negative (peak 350→146 decay)。两种干预都不够\\n- **PickCube**: CIVO 根本不发生（NVE 自行修正至 0.2）。subsample+dt_emb 配置本身损害性能（vanilla 58.6→config 26.6）。Dual-critic 无关（v1=v2）\\n- **结论**: 干预在 locomotion 中部分有效（Walker > Cheetah），manipulation 域 CIVO 不触发 → scope limitation\\n\\n### Non-CIVO Collapse 发现 (2026-05-21)\\n- exp_038 Walker dual s2: eval 崩溃但 NVE≤0.3 → 存在独立于 CIVO 的崩溃机制\\n- Dual-critic 专门解决 value overestimation cascade，不是万能防崩溃方案\\n- 论文需区分 \\\"CIVO prevention\\\" vs \\\"general stability\\\"\\n\\n### TCN 全景 (2026-05-21)\\n- Walker: σ=0.2 部分有效 (2/4 seeds), σ=0.1 和 σ=0.5 失败\\n- Cheetah: 全部失败 (σ=0.2/0.5/1.0)\\n- PickCube: 全部失败 (σ=0.2/0.5)\\n- 结论：TCN 窗口极窄，仅 Walker σ=0.2 部分 work\\n\\n### NVE 诊断经验 (2026-05-21)\\n- Late-stage NVE 下降需区分 genuine CIVO recovery vs floor effect\\n- 关键判据：eval 是否同步恢复。Eval 恢复 → genuine；eval 平坦 → floor effect\\n- exp_031b 教训：NVE 3.3→0.2 看似恢复，但 eval 25-29 平坦 → floor effect / negative\\n\\n### Registry 工具问题 (2026-05-21)\\n- read_registry 工具有时只返回部分实验（11/101），直接读 YAML 更可靠\\n- update_registry 工具有时会创建新条目覆盖直接 YAML 编辑，需要验证\\n- 状态转换有限制（如 PREPARING 只能 → PENDING/QUEUED，不能直接 → RUNNING）\\n- 有 parent 字段的实验被当 eval 实验，需要额外提供 checkpoint_source/eval_data\\n\", \"total_chars\": 2328, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "62fc324d-2d15-4071-816f-e76fafb65c29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\\\", \\\"content\\\": \\\"# Memory — event-gated-adaptive-horizon\\\\n\\\\n> 不可从 registry/代码派生的决策原因、约束、经验教训。\\\\n\\\\n## 竞品实验参考\\\\n（待补充）\\\\n\\\\n## 经验教训\\\\n\\\\n### Dual-Critic 机制发现 (2026-05-21)\\\\n- exp_032/032b Walker dual-critic: v1≈v2 (gap <0.5), min 无 pessimism 效果，但 CIVO 仍被抑制 → 机制是 implicit regularization，不是传统 Double-Q pessimism\\\\n- exp_033 wide-critic (2.89M params, 2.44× normal): CIVO 仍触发 (NVE 4.7) → 参数量本身不能防 CIVO\\\\n- exp_034 Cheetah dual-critic: NVE 1.8 (vs baseline 70.64, 降 40×) 但仍超 1.5 阈值 → 部分抑制但不完全。Dual-wave CIVO pattern\\\\n\\\\n### 2×2 Factorial 完成 (2026-05-21)\\\\n- {single, dual} × {normal ~1.2M, scaled ~2.4-2.9M}:\\\\n  - single + normal = baseline (CIVO → collapse)\\\\n  - single + scaled = exp_033 (CIVO NVE 4.7 → partial recovery, eval 408)\\\\n  - dual + normal = exp_035 (CIVO NVE 2.75 → full recovery, eval 697.8) — Director override success\\\\n  - dual + scaled = exp_032 (CIVO prevented, NVE ≤1.1, eval 787.7)\\\\n- **双维度 insight**: Prevention = min+capacity synergy; Recovery = min 主导 (697.8 vs 408)\\\\n\\\\n### Cross-Environment 完整结果 (2026-05-21 更新)\\\\n- **Walker**: dual-critic 2/2 CIVO prevented (s0=787.7, s1=551.8)，但 s2 (exp_038) 出现 non-CIVO collapse (peak 354→120, NVE≤0.3)。Narrow dual s0 recovery 697.8, s1 (exp_039) collapsing\\\\n- **Cheetah**: dual-critic negative (NVE 1.8, eval 97.5); wide single negative (peak 350→146 decay)。两种干预都不够\\\\n- **PickCube**: CIVO 根本不发生（NVE 自行修正至 0.2）。subsample+dt_emb 配置本身损害性能（vanilla 58.6→config 26.6）。Dual-critic 无关（v1=v2）\\\\n- **结论**: 干预在 locomotion 中部分有效（Walker > Cheetah），manipulation 域 CIVO 不触发 → scope limitation\\\\n\\\\n### Non-CIVO Collapse 发现 (2026-05-21)\\\\n- exp_038 Walker dual s2: eval 崩溃但 NVE≤0.3 → 存在独立于 CIVO 的崩溃机制\\\\n- Dual-critic 专门解决 value overestimation cascade，不是万能防崩溃方案\\\\n- 论文需区分 \\\\\\\"CIVO prevention\\\\\\\" vs \\\\\\\"general stability\\\\\\\"\\\\n\\\\n### TCN 全景 (2026-05-21)\\\\n- Walker: σ=0.2 部分有效 (2/4 seeds), σ=0.1 和 σ=0.5 失败\\\\n- Cheetah: 全部失败 (σ=0.2/0.5/1.0)\\\\n- PickCube: 全部失败 (σ=0.2/0.5)\\\\n- 结论：TCN 窗口极窄，仅 Walker σ=0.2 部分 work\\\\n\\\\n### NVE 诊断经验 (2026-05-21)\\\\n- Late-stage NVE 下降需区分 genuine CIVO recovery vs floor effect\\\\n- 关键判据：eval 是否同步恢复。Eval 恢复 → genuine；eval 平坦 → floor effect\\\\n- exp_031b 教训：NVE 3.3→0.2 看似恢复，但 eval 25-29 平坦 → floor effect / negative\\\\n\\\\n### Registry 工具问题 (2026-05-21)\\\\n- read_registry 工具有时只返回部分实验（11/101），直接读 YAML 更可靠\\\\n- update_registry 工具有时会创建新条目覆盖直接 YAML 编辑，需要验证\\\\n- 状态转换有限制（如 PREPARING 只能 → PENDING/QUEUED，不能直接 → RUNNING）\\\\n- 有 parent 字段的实验被当 eval 实验，需要额外提供 checkpoint_source/eval_data\\\\n\\\", \\\"total_chars\\\": 2328, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n> 不可从 registry/代码派生的决策原因、约束、经验教训。\\n\\n## 竞品实验参考\\n（待补充）\\n\\n## 经验教训\\n\\n### Dual-Critic 机制发现 (2026-05-21)\\n- exp_032/032b Walker dual-critic: v1≈v2 (gap <0.5), min 无 pessimism 效果，但 CIVO 仍被抑制 → 机制是 implicit regularization，不是传统 Double-Q pessimism\\n- exp_033 wide-critic (2.89M params, 2.44× normal): CIVO 仍触发 (NVE 4.7) → 参数量本身不能防 CIVO\\n- exp_034 Cheetah dual-critic: NVE 1.8 (vs baseline 70.64, 降 40×) 但仍超 1.5 阈值 → 部分抑制但不完全。Dual-wave CIVO pattern\\n\\n### 2×2 Factorial 完成 (2026-05-21)\\n- {single, dual} × {normal ~1.2M, scaled ~2.4-2.9M}:\\n  - single + normal = baseline (CIVO → collapse)\\n  - single + scaled = exp_033 (CIVO NVE 4.7 → partial recovery, eval 408)\\n  - dual + normal = exp_035 (CIVO NVE 2.75 → full recovery, eval 697.8) — Director override success\\n  - dual + scaled = exp_032 (CIVO prevented, NVE ≤1.1, eval 787.7)\\n- **双维度 insight**: Prevention = min+capacity synergy; Recovery = min 主导 (697.8 vs 408)\\n\\n### Cross-Environment 完整结果 (2026-05-21 更新)\\n- **Walker**: dual-critic 2/2 CIVO prevented (s0=787.7, s1=551.8)，但 s2 (exp_038) 出现 non-CIVO collapse (peak 354→120, NVE≤0.3)。Narrow dual s0 recovery 697.8, s1 (exp_039) collapsing\\n- **Cheetah**: dual-critic negative (NVE 1.8, eval 97.5); wide single negative (peak 350→146 decay)。两种干预都不够\\n- **PickCube**: CIVO 根本不发生（NVE 自行修正至 0.2）。subsample+dt_emb 配置本身损害性能（vanilla 58.6→config 26.6）。Dual-critic 无关（v1=v2）\\n- **结论**: 干预在 locomotion 中部分有效（Walker > Cheetah），manipulation 域 CIVO 不触发 → scope limitation\\n\\n### Non-CIVO Collapse 发现 (2026-05-21)\\n- exp_038 Walker dual s2: eval 崩溃但 NVE≤0.3 → 存在独立于 CIVO 的崩溃机制\\n- Dual-critic 专门解决 value overestimation cascade，不是万能防崩溃方案\\n- 论文需区分 \\\"CIVO prevention\\\" vs \\\"general stability\\\"\\n\\n### TCN 全景 (2026-05-21)\\n- Walker: σ=0.2 部分有效 (2/4 seeds), σ=0.1 和 σ=0.5 失败\\n- Cheetah: 全部失败 (σ=0.2/0.5/1.0)\\n- PickCube: 全部失败 (σ=0.2/0.5)\\n- 结论：TCN 窗口极窄，仅 Walker σ=0.2 部分 work\\n\\n### NVE 诊断经验 (2026-05-21)\\n- Late-stage NVE 下降需区分 genuine CIVO recovery vs floor effect\\n- 关键判据：eval 是否同步恢复。Eval 恢复 → genuine；eval 平坦 → floor effect\\n- exp_031b 教训：NVE 3.3→0.2 看似恢复，但 eval 25-29 平坦 → floor effect / negative\\n\\n### Registry 工具问题 (2026-05-21)\\n- read_registry 工具有时只返回部分实验（11/101），直接读 YAML 更可靠\\n- update_registry 工具有时会创建新条目覆盖直接 YAML 编辑，需要验证\\n- 状态转换有限制（如 PREPARING 只能 → PENDING/QUEUED，不能直接 → RUNNING）\\n- 有 parent 字段的实验被当 eval 实验，需要额外提供 checkpoint_source/eval_data\\n\", \"total_chars\": 2328, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01V9RfxSUZcechH94fjzTCcS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/signed_reward_error.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "acf12ded-6c1a-44a5-9a5f-21df248fbed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 22 · 2026-05-22T07:37:25.417Z_

<details><summary>↩ Tool result · `toolu_01V9RfxSUZcechH94fjzTCcS`</summary>

````text
1	# Signed Reward Error Analysis
2	
3	**Date**: 2026-05-15
4	**Script**: `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/signed_reward_error.py`
5	**Raw data**: `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/signed_reward_error_results.json`
6	
7	## Objective
8	
9	Test whether exp_008d (trained dt_emb + subsample) systematically **overpredicts** reward on dt=2 transitions — the hypothesized mechanism behind CIVO (Catastrophic Imagined Value Overestimation).
10	
11	## Method
12	
13	- Loaded 8 latest training episodes per experiment
14	- Built encoder + RSSM + reward_head from checkpoint weights
15	- For dt=1: fed full episodes through RSSM.observe, compared reward_head prediction to actual reward
16	- For dt=2: subsampled episodes (every 2nd step), computed cumulative discounted reward (r[t] + 0.997·r[t+1]), fed through RSSM.observe with dt_labels=2
17	- Signed error = predicted_reward − actual_reward (positive = overprediction)
18	- All computation on CPU, no GPU interference
19	
20	## Results
21	
22	| Experiment | dt | Mean SE | Std SE | Median SE | %Over | N | Mean Actual | Mean Pred |
23	|---|---|---|---|---|---|---|---|---|
24	| **baseline_s1** | 1 | **+0.001** | 0.023 | −0.001 | 39.6% | 4000 | 1.893 | 1.894 |
25	| **exp_008d** | 1 | **+0.018** | 0.072 | +0.009 | 61.8% | 4000 | 0.361 | 0.379 |
26	| **exp_008d** | 2 | **−0.599** | 0.722 | −0.331 | 8.0% | 1992 | 0.721 | 0.121 |
27	| **exp_008f** | 1 | **−0.710** | 0.704 | −0.490 | 14.0% | 4000 | 0.921 | 0.211 |
28	| **exp_008f** | 2 | **−1.645** | 1.485 | −1.445 | 5.0% | 1992 | 1.840 | 0.195 |
29	
30	## Key Findings
31	
32	### 1. 008d does NOT overpredict on dt=2 — it UNDERPREDICTS
33	
34	The hypothesis was that 008d would show positive mean signed error on dt=2 transitions. Instead:
35	- dt=1: Mean SE = +0.018 (slight overprediction, 61.8% of samples)
36	- dt=2: Mean SE = **−0.599** (massive underprediction, only 8% overpredict)
37	
38	The reward head predicts 0.121 on average but the actual cumulative reward is 0.721. The model systematically underpredicts by ~83%.
39	
40	### 2. 008f is uncalibrated at both dt values
41	
42	008f (no dt_emb) shows massive underprediction everywhere:
43	- dt=1: predicts 0.211 vs actual 0.921 (SE = −0.710)
44	- dt=2: predicts 0.195 vs actual 1.840 (SE = −1.645)
45	
46	This suggests the 008f model's world model is fundamentally poorly calibrated — likely because it can't distinguish dt=1 from dt=2 transitions, corrupting the posterior.
47	
48	### 3. Baseline is well-calibrated
49	
50	The baseline reward head is nearly perfectly calibrated (Mean SE ≈ 0, Std 0.023), confirming the analysis methodology is sound.
51	
52	### 4. Performance gap context
53	
54	- Baseline actual reward: 1.893 (well-trained agent)
55	- 008d actual reward: 0.361 (collapsed/early training)
56	- 008f actual reward: 0.921 (intermediate)
57	
58	The low actual rewards for 008d confirm it's in a collapsed state, consistent with the CIVO hypothesis but through a different mechanism than reward overprediction.
59	
60	## Interpretation
61	
62	The CIVO mechanism may not operate through **observation-level** reward overprediction. This analysis used the RSSM **posterior** (conditioned on real observations). During imagination (which drives actor/critic training), the RSSM uses the **prior** (no observation correction), and the dt_embedding may cause different behavior:
63	
64	1. The posterior corrects for observation mismatch — even if the prior drifts, the posterior pulls back
65	2. During imagination, the dt_embedding could amplify state drift, leading to overoptimistic value estimates even if per-step reward prediction is unbiased or negative-biased
66	3. The value overshoot could come from the **critic** (accumulated returns), not per-step reward prediction
67	
68	## Recommended Follow-up
69	
70	1. **Prior-based analysis**: Run RSSM in imagination mode (img_step, no observations) with dt=1 vs dt=2, compare prior reward predictions — this would directly test the imagination-level mechanism
71	2. **Value prediction comparison**: Compare critic value estimates between dt=1 and dt=2 imagined trajectories
72	3. **Reward head input analysis**: Check if the dt_embedding causes the RSSM to produce features in regions where the reward head is poorly calibrated
73	
74	## Visualization Data
75	
76	For future plotting (reward error distributions):
77	
78	```python
79	# Available in signed_reward_error_results.json
80	# Suggested plots:
81	# 1. Box plot: signed error by experiment × dt
82	# 2. Histogram: signed error distribution overlay (008d dt=1 vs dt=2)
83	# 3. Scatter: predicted vs actual reward, colored by experiment
84	```
85	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "5b785345-3d37-440e-8591-89b236da4039",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/signed_reward_error.md",
      "content": "# Signed Reward Error Analysis\n\n**Date**: 2026-05-15\n**Script**: `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/signed_reward_error.py`\n**Raw data**: `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/signed_reward_error_results.json`\n\n## Objective\n\nTest whether exp_008d (trained dt_emb + subsample) systematically **overpredicts** reward on dt=2 transitions — the hypothesized mechanism behind CIVO (Catastrophic Imagined Value Overestimation).\n\n## Method\n\n- Loaded 8 latest training episodes per experiment\n- Built encoder + RSSM + reward_head from checkpoint weights\n- For dt=1: fed full episodes through RSSM.observe, compared reward_head prediction to actual reward\n- For dt=2: subsampled episodes (every 2nd step), computed cumulative discounted reward (r[t] + 0.997·r[t+1]), fed through RSSM.observe with dt_labels=2\n- Signed error = predicted_reward − actual_reward (positive = overprediction)\n- All computation on CPU, no GPU interference\n\n## Results\n\n| Experiment | dt | Mean SE | Std SE | Median SE | %Over | N | Mean Actual | Mean Pred |\n|---|---|---|---|---|---|---|---|---|\n| **baseline_s1** | 1 | **+0.001** | 0.023 | −0.001 | 39.6% | 4000 | 1.893 | 1.894 |\n| **exp_008d** | 1 | **+0.018** | 0.072 | +0.009 | 61.8% | 4000 | 0.361 | 0.379 |\n| **exp_008d** | 2 | **−0.599** | 0.722 | −0.331 | 8.0% | 1992 | 0.721 | 0.121 |\n| **exp_008f** | 1 | **−0.710** | 0.704 | −0.490 | 14.0% | 4000 | 0.921 | 0.211 |\n| **exp_008f** | 2 | **−1.645** | 1.485 | −1.445 | 5.0% | 1992 | 1.840 | 0.195 |\n\n## Key Findings\n\n### 1. 008d does NOT overpredict on dt=2 — it UNDERPREDICTS\n\nThe hypothesis was that 008d would show positive mean signed error on dt=2 transitions. Instead:\n- dt=1: Mean SE = +0.018 (slight overprediction, 61.8% of samples)\n- dt=2: Mean SE = **−0.599** (massive underprediction, only 8% overpredict)\n\nThe reward head predicts 0.121 on average but the actual cumulative reward is 0.721. The model systematically underpredicts by ~83%.\n\n### 2. 008f is uncalibrated at both dt values\n\n008f (no dt_emb) shows massive underprediction everywhere:\n- dt=1: predicts 0.211 vs actual 0.921 (SE = −0.710)\n- dt=2: predicts 0.195 vs actual 1.840 (SE = −1.645)\n\nThis suggests the 008f model's world model is fundamentally poorly calibrated — likely because it can't distinguish dt=1 from dt=2 transitions, corrupting the posterior.\n\n### 3. Baseline is well-calibrated\n\nThe baseline reward head is nearly perfectly calibrated (Mean SE ≈ 0, Std 0.023), confirming the analysis methodology is sound.\n\n### 4. Performance gap context\n\n- Baseline actual reward: 1.893 (well-trained agent)\n- 008d actual reward: 0.361 (collapsed/early training)\n- 008f actual reward: 0.921 (intermediate)\n\nThe low actual rewards for 008d confirm it's in a collapsed state, consistent with the CIVO hypothesis but through a different mechanism than reward overprediction.\n\n## Interpretation\n\nThe CIVO mechanism may not operate through **observation-level** reward overprediction. This analysis used the RSSM **posterior** (conditioned on real observations). During imagination (which drives actor/critic training), the RSSM uses the **prior** (no observation correction), and the dt_embedding may cause different behavior:\n\n1. The posterior corrects for observation mismatch — even if the prior drifts, the posterior pulls back\n2. During imagination, the dt_embedding could amplify state drift, leading to overoptimistic value estimates even if per-step reward prediction is unbiased or negative-biased\n3. The value overshoot could come from the **critic** (accumulated returns), not per-step reward prediction\n\n## Recommended Follow-up\n\n1. **Prior-based analysis**: Run RSSM in imagination mode (img_step, no observations) with dt=1 vs dt=2, compare prior reward predictions — this would directly test the imagination-level mechanism\n2. **Value prediction comparison**: Compare critic value estimates between dt=1 and dt=2 imagined trajectories\n3. **Reward head input analysis**: Check if the dt_embedding causes the RSSM to produce features in regions where the reward head is poorly calibrated\n\n## Visualization Data\n\nFor future plotting (reward error distributions):\n\n```python\n# Available in signed_reward_error_results.json\n# Suggested plots:\n# 1. Box plot: signed error by experiment × dt\n# 2. Histogram: signed error distribution overlay (008d dt=1 vs dt=2)\n# 3. Scatter: predicted vs actual reward, colored by experiment\n```\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
````

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Jy2p9cgJMYCmMd7JNRWeL2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/auroc_label_fix_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "56b8932c-1d10-438b-9b7e-2b62c534dc77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137B3RK992Kpcw23cqZAq2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 17,
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

_source line 24 · 2026-05-22T07:37:26.377Z_

<details><summary>↩ Tool result · `toolu_01Jy2p9cgJMYCmMd7JNRWeL2`</summary>

````text
1	# AUROC Label Consistency Fix Report
2	
3	**Date**: 2026-05-22
4	**Issue**: exp_008e_v3_s2 labeled as non-CIVO (FP) in n=16 analysis but as CIVO-positive (TP) in n=29 analysis.
5	
6	## 1. Label Fix
7	
8	| Field | Before | After |
9	|-------|--------|-------|
10	| exp_id | 008e_v3_s2 | 008e_v3_s2 |
11	| n=16 label | non-CIVO (negative) | non-CIVO (negative) — **unchanged** |
12	| n=29 label | **CIVO (positive)** | **non-CIVO / IRD (negative)** — **fixed** |
13	| NVE peak | 3.780 @ 105K | 3.780 @ 105K |
14	
15	**Rationale**: D039/D040 mechanism analysis concluded eval-driven collapse (eval 715→137 at 85K-105K), not value-driven. Entropy increases (exploration expands) rather than decreases (CIVO pattern requires entropy collapse). NVE rise is a consequence of eval denominator collapse, not a causal predictor.
16	
17	## 2. Updated AUROC Values
18	
19	### n=16 Analysis (no change)
20	
21	The n=16 analysis already had 008e_v3_s2 correctly labeled as non-CIVO.
22	
23	| Metric | Value |
24	|--------|-------|
25	| AUROC | 0.969 |
26	| n | 16 (8 pos / 8 neg) |
27	| Accuracy @ θ=1.5× | 93.8% (15/16) |
28	| TP / FP / FN / TN | 8 / 1 / 0 / 7 |
29	| 95% CI (accuracy) | [69.8%, 99.8%] |
30	
31	### n=29 Analysis (corrected)
32	
33	| Metric | Original | Corrected | Δ |
34	|--------|----------|-----------|---|
35	| AUROC | 0.971 | **0.953** | −0.018 |
36	| 95% Bootstrap CI | [0.904, 1.000] | **[0.867, 1.000]** | wider |
37	| n_pos / n_neg | 13 / 16 | **12 / 17** | |
38	| Accuracy @ θ=1.5× | 93.1% (27/29) | **89.7% (26/29)** | −1 correct |
39	| FP @ θ=1.5× | 2 | **3** | +1 |
40	| TPR @ θ=1.5× | 1.00 | 1.00 | — |
41	| FPR @ θ=1.5× | 0.12 | **0.18** | +0.06 |
42	| Concordant pairs | 202/208 | **194.5/204** | |
43	
44	## 3. Confusion Matrix (corrected n=29, θ=1.5×)
45	
46	```
47	                Predicted CIVO    Predicted non-CIVO
48	True CIVO          TP = 12             FN = 0
49	True non-CIVO      FP = 3              TN = 14
50	```
51	
52	Precision = 12/15 = 80.0%, Recall = 12/12 = 100%, F1 = 88.9%
53	
54	## 4. FP and FN Details
55	
56	### False Positives (3)
57	
58	| exp_id | NVE peak | Predicted | True | Mechanism |
59	|--------|----------|-----------|------|-----------|
60	| 025_obs_sgs_s2 | 1.730 | CIVO | non-CIVO | Obs-decoder SGS failure damages shared RSSM latent space, causing systematic value miscalibration. NVE elevation is a side effect of representation damage, not the CIVO positive feedback loop. |
61	| 028_rave_ceil15 | 2.230 | CIVO | non-CIVO | RAVE anchor pollution: the EMA value anchor itself becomes inflated under CIVO dynamics, producing overestimation through a value anchoring pathway distinct from dt_emb-driven CIVO. |
62	| 008e_v3_s2 | 3.780 | CIVO | non-CIVO (IRD) | Imagination-Reality Divergence. Eval-driven collapse (eval 715→137 at 85K-105K) where NVE rise is consequence of eval denominator collapse, not cause. Entropy increases (more exploration), opposite of CIVO pattern (entropy collapse → exploitation lock-in). dt_emb is trained but imagination uses dt=1 (gating locked), preventing the multi-rate imagination exposure required for CIVO. |
63	
64	### False Negatives (0)
65	
66	None. All 12 CIVO-positive experiments are correctly detected at θ=1.5×.
67	
68	## 5. Label Consistency Check
69	
70	### 008e_v3_s2
71	
72	| Analysis | Label | Consistent? |
73	|----------|-------|-------------|
74	| n=16 | non-CIVO (FP at θ=1.5×) | ✓ (was already correct) |
75	| n=29 | **non-CIVO** (was CIVO, now fixed) | ✓ (now consistent) |
76	| n=12 (nve_threshold_sensitivity.json) | non-CIVO (label=0, IRD) | ✓ |
77	| n=8 (nve_threshold_v3_ci_supplement_d054.json) | non-CIVO (negative) | ✓ |
78	
79	### 025_obs_sgs_s2
80	
81	Only present in n=29 analysis (SGS experiments postdate n=16 analysis). Labeled non-CIVO in n=29. **No cross-analysis inconsistency possible.** ✓
82	
83	### 028_rave_ceil15
84	
85	Only present in n=29 analysis (RAVE experiments postdate n=16 analysis). Labeled non-CIVO in n=29. **No cross-analysis inconsistency possible.** ✓
86	
87	## 6. Impact on Paper Claims
88	
89	The corrected AUROC (0.953 → from 0.971) still supports the paper's diagnostic validity claim. The 95% CI [0.867, 1.000] remains well above chance (0.5). The additional FP (008e_v3_s2) is mechanistically distinct from CIVO, reinforcing the paper's argument that NVE detects value overestimation broadly — a feature for practitioners rather than a limitation.
90	
91	The n=16 analysis (AUROC=0.969) is unaffected.
92	
93	## 7. Files Modified
94	
95	- `artifacts/auroc_label_fix_result.json` — structured recomputation output
96	- `artifacts/auroc_label_fix_recompute.py` — recomputation script
97	- This report: `artifacts/auroc_label_fix_report.md`
98	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "5c803f23-ab90-4d6c-9732-f0b6db2ceb05",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/auroc_label_fix_report.md",
      "content": "# AUROC Label Consistency Fix Report\n\n**Date**: 2026-05-22\n**Issue**: exp_008e_v3_s2 labeled as non-CIVO (FP) in n=16 analysis but as CIVO-positive (TP) in n=29 analysis.\n\n## 1. Label Fix\n\n| Field | Before | After |\n|-------|--------|-------|\n| exp_id | 008e_v3_s2 | 008e_v3_s2 |\n| n=16 label | non-CIVO (negative) | non-CIVO (negative) — **unchanged** |\n| n=29 label | **CIVO (positive)** | **non-CIVO / IRD (negative)** — **fixed** |\n| NVE peak | 3.780 @ 105K | 3.780 @ 105K |\n\n**Rationale**: D039/D040 mechanism analysis concluded eval-driven collapse (eval 715→137 at 85K-105K), not value-driven. Entropy increases (exploration expands) rather than decreases (CIVO pattern requires entropy collapse). NVE rise is a consequence of eval denominator collapse, not a causal predictor.\n\n## 2. Updated AUROC Values\n\n### n=16 Analysis (no change)\n\nThe n=16 analysis already had 008e_v3_s2 correctly labeled as non-CIVO.\n\n| Metric | Value |\n|--------|-------|\n| AUROC | 0.969 |\n| n | 16 (8 pos / 8 neg) |\n| Accuracy @ θ=1.5× | 93.8% (15/16) |\n| TP / FP / FN / TN | 8 / 1 / 0 / 7 |\n| 95% CI (accuracy) | [69.8%, 99.8%] |\n\n### n=29 Analysis (corrected)\n\n| Metric | Original | Corrected | Δ |\n|--------|----------|-----------|---|\n| AUROC | 0.971 | **0.953** | −0.018 |\n| 95% Bootstrap CI | [0.904, 1.000] | **[0.867, 1.000]** | wider |\n| n_pos / n_neg | 13 / 16 | **12 / 17** | |\n| Accuracy @ θ=1.5× | 93.1% (27/29) | **89.7% (26/29)** | −1 correct |\n| FP @ θ=1.5× | 2 | **3** | +1 |\n| TPR @ θ=1.5× | 1.00 | 1.00 | — |\n| FPR @ θ=1.5× | 0.12 | **0.18** | +0.06 |\n| Concordant pairs | 202/208 | **194.5/204** | |\n\n## 3. Confusion Matrix (corrected n=29, θ=1.5×)\n\n```\n                Predicted CIVO    Predicted non-CIVO\nTrue CIVO          TP = 12             FN = 0\nTrue non-CIVO      FP = 3              TN = 14\n```\n\nPrecision = 12/15 = 80.0%, Recall = 12/12 = 100%, F1 = 88.9%\n\n## 4. FP and FN Details\n\n### False Positives (3)\n\n| exp_id | NVE peak | Predicted | True | Mechanism |\n|--------|----------|-----------|------|-----------|\n| 025_obs_sgs_s2 | 1.730 | CIVO | non-CIVO | Obs-decoder SGS failure damages shared RSSM latent space, causing systematic value miscalibration. NVE elevation is a side effect of representation damage, not the CIVO positive feedback loop. |\n| 028_rave_ceil15 | 2.230 | CIVO | non-CIVO | RAVE anchor pollution: the EMA value anchor itself becomes inflated under CIVO dynamics, producing overestimation through a value anchoring pathway distinct from dt_emb-driven CIVO. |\n| 008e_v3_s2 | 3.780 | CIVO | non-CIVO (IRD) | Imagination-Reality Divergence. Eval-driven collapse (eval 715→137 at 85K-105K) where NVE rise is consequence of eval denominator collapse, not cause. Entropy increases (more exploration), opposite of CIVO pattern (entropy collapse → exploitation lock-in). dt_emb is trained but imagination uses dt=1 (gating locked), preventing the multi-rate imagination exposure required for CIVO. |\n\n### False Negatives (0)\n\nNone. All 12 CIVO-positive experiments are correctly detected at θ=1.5×.\n\n## 5. Label Consistency Check\n\n### 008e_v3_s2\n\n| Analysis | Label | Consistent? |\n|----------|-------|-------------|\n| n=16 | non-CIVO (FP at θ=1.5×) | ✓ (was already correct) |\n| n=29 | **non-CIVO** (was CIVO, now fixed) | ✓ (now consistent) |\n| n=12 (nve_threshold_sensitivity.json) | non-CIVO (label=0, IRD) | ✓ |\n| n=8 (nve_threshold_v3_ci_supplement_d054.json) | non-CIVO (negative) | ✓ |\n\n### 025_obs_sgs_s2\n\nOnly present in n=29 analysis (SGS experiments postdate n=16 analysis). Labeled non-CIVO in n=29. **No cross-analysis inconsistency possible.** ✓\n\n### 028_rave_ceil15\n\nOnly present in n=29 analysis (RAVE experiments postdate n=16 analysis). Labeled non-CIVO in n=29. **No cross-analysis inconsistency possible.** ✓\n\n## 6. Impact on Paper Claims\n\nThe corrected AUROC (0.953 → from 0.971) still supports the paper's diagnostic validity claim. The 95% CI [0.867, 1.000] remains well above chance (0.5). The additional FP (008e_v3_s2) is mechanistically distinct from CIVO, reinforcing the paper's argument that NVE detects value overestimation broadly — a feature for practitioners rather than a limitation.\n\nThe n=16 analysis (AUROC=0.969) is unaffected.\n\n## 7. Files Modified\n\n- `artifacts/auroc_label_fix_result.json` — structured recomputation output\n- `artifacts/auroc_label_fix_recompute.py` — recomputation script\n- This report: `artifacts/auroc_label_fix_report.md`\n",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
````

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I need to get the round_1 review report (it's not a standard project file), and extract key experiment data from the registry. Let me find the review report file and process the registry data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "147af8d1-5a0d-48d1-a430-2e2b1edaa4bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGzyKSA7pbXvnLa2jFpRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33678,
      "cache_read_input_tokens": 26309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 33678
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

Now let me find the review report and extract key experiment data from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "7fcaf2f2-ed70-401d-afeb-1174dce1db08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGzyKSA7pbXvnLa2jFpRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33678,
      "cache_read_input_tokens": 26309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 33678
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

<details open><summary>🔧 Tool call — Glob · `toolu_0196QTMySuGcb3ow8zoE81aF`</summary>

```json
{
  "pattern": "**/review_reports/round_1*",
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "49a16758-1def-433f-b4a8-8755c257ad1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGzyKSA7pbXvnLa2jFpRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33678,
      "cache_read_input_tokens": 26309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 33678
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

_source line 28 · 2026-05-22T07:37:33.733Z_

<details><summary>↩ Tool result · `toolu_0196QTMySuGcb3ow8zoE81aF`</summary>

```text
artifacts/review_reports/round_1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "07b7e0cf-f897-4d2f-9f95-11bda18fc0d7",
  "tool_use_result": {
    "filenames": [
      "artifacts/review_reports/round_1.md"
    ],
    "durationMs": 20,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Agent · `toolu_01FM7bPFxXDs3g11zr1WuHms`</summary>

```json
{
  "description": "Extract registry experiment data",
  "prompt": "I need you to extract specific experiment data from a large JSON registry file for a rebuttal draft. The file is at:\n\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\n\nThis is JSON with schema: {result: string}. The \"result\" field is itself a JSON string that needs to be parsed.\n\nI need you to extract and return a structured summary of the following experiments. For each, provide: exp_id, status, conclusion, key metrics (eval, NVE, etc.), and any relevant notes:\n\n1. **Dual-critic experiments**: exp_032, exp_032b, exp_033, exp_034, exp_035, exp_036, exp_038, exp_039, exp_040, exp_041\n2. **Frozen dt_emb**: exp_042\n3. **008f replication**: exp_043\n4. **Cheetah experiments**: exp_010a, exp_010b\n5. **PickCube experiments**: exp_019a, exp_019b\n6. **CIVO baseline**: exp_008d, exp_008a, exp_008f\n7. **Gradient stopping**: exp_016e, exp_018, exp_021, exp_025, exp_026\n8. **RUNNING experiments**: any with status=RUNNING - give current step count if available\n\nUse jq or python to parse and extract. Give me a comprehensive but concise summary - include actual numbers for eval scores, NVE values, and any key metrics. Report under 3000 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "579a7093-120f-45b1-9daf-ed4bc0a6ff41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGzyKSA7pbXvnLa2jFpRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33678,
      "cache_read_input_tokens": 26309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 33678
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

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Extract registry experiment data",
  "task_type": "local_agent",
  "prompt": "I need you to extract specific experiment data from a large JSON registry file for a rebuttal draft. The file is at:\n\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\n\nThis is JSON with schema: {result: string}. The \"result\" field is itself a JSON string that needs to be parsed.\n\nI need you to extract and return a structured summary of the following experiments. For each, provide: exp_id, status, conclusion, key metrics (eval, NVE, etc.), and any relevant notes:\n\n1. **Dual-critic experiments**: exp_032, exp_032b, exp_033, exp_034, exp_035, exp_036, exp_038, exp_039, exp_040, exp_041\n2. **Frozen dt_emb**: exp_042\n3. **008f replication**: exp_043\n4. **Cheetah experiments**: exp_010a, exp_010b\n5. **PickCube experiments**: exp_019a, exp_019b\n6. **CIVO baseline**: exp_008d, exp_008a, exp_008f\n7. **Gradient stopping**: exp_016e, exp_018, exp_021, exp_025, exp_026\n8. **RUNNING experiments**: any with status=RUNNING - give current step count if available\n\nUse jq or python to parse and extract. Give me a comprehensive but concise summary - include actual numbers for eval scores, NVE values, and any key metrics. Report under 3000 words.",
  "uuid": "4c895c23-3456-401a-a7c3-dc7d66901802",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

## Round 1

43 recorded events

### User

_source line 31 · 2026-05-22T07:37:46.145Z_

I need you to extract specific experiment data from a large JSON registry file for a rebuttal draft. The file is at:

/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt

This is JSON with schema: {result: string}. The "result" field is itself a JSON string that needs to be parsed.

I need you to extract and return a structured summary of the following experiments. For each, provide: exp_id, status, conclusion, key metrics (eval, NVE, etc.), and any relevant notes:

1. **Dual-critic experiments**: exp_032, exp_032b, exp_033, exp_034, exp_035, exp_036, exp_038, exp_039, exp_040, exp_041
2. **Frozen dt_emb**: exp_042
3. **008f replication**: exp_043
4. **Cheetah experiments**: exp_010a, exp_010b
5. **PickCube experiments**: exp_019a, exp_019b
6. **CIVO baseline**: exp_008d, exp_008a, exp_008f
7. **Gradient stopping**: exp_016e, exp_018, exp_021, exp_025, exp_026
8. **RUNNING experiments**: any with status=RUNNING - give current step count if available

Use jq or python to parse and extract. Give me a comprehensive but concise summary - include actual numbers for eval scores, NVE values, and any key metrics. Report under 3000 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "ee58270d-76c9-4f1c-a434-f31119a29a4a"
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SF5qFJDwEpz1GyZiQdXY1G`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "ROADMAP.md",
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "8622a4a8-73d4-43ad-a483-fac6ffed9313",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGzyKSA7pbXvnLa2jFpRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33678,
      "cache_read_input_tokens": 26309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 33678
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

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 14641,
    "tool_uses": 1,
    "duration_ms": 3645
  },
  "last_tool_name": "Bash",
  "uuid": "7c93b877-c625-4394-83fa-4a25ff87c9eb",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_017EMoY3yNaFWaf4QeqHjMp1`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "8993d1a0-a1f0-4db7-b3ce-d53928878f25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SrpAs41eHFeHukztufDTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14630,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14630,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 35 · 2026-05-22T07:37:49.944Z_

<details><summary>↩ Tool result · `toolu_017EMoY3yNaFWaf4QeqHjMp1`</summary>

```text
271492 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "eaf8dd8f-ec2f-4ed1-870d-55db14da586a"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Parse JSON structure and understand registry format",
  "usage": {
    "total_tokens": 15818,
    "tool_uses": 2,
    "duration_ms": 15395
  },
  "last_tool_name": "Bash",
  "uuid": "6fe7a8ca-a6f1-4655-91f8-50304175a0ad",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1noUJaYRLxRoH1tAV8jqj`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\n# The \"result\" field is itself a JSON string\nregistry = json.loads(outer[\"result\"])\n\n# Target experiment IDs\ntarget_ids = [\n    \"exp_032\", \"exp_032b\", \"exp_033\", \"exp_034\", \"exp_035\", \"exp_036\", \"exp_038\", \"exp_039\", \"exp_040\", \"exp_041\",\n    \"exp_042\",\n    \"exp_043\",\n    \"exp_010a\", \"exp_010b\",\n    \"exp_019a\", \"exp_019b\",\n    \"exp_008d\", \"exp_008a\", \"exp_008f\",\n    \"exp_016e\", \"exp_018\", \"exp_021\", \"exp_025\", \"exp_026\",\n]\n\n# Find all experiments - check structure\nif isinstance(registry, dict):\n    # Check if experiments are at top level or nested\n    if \"experiments\" in registry:\n        experiments = registry[\"experiments\"]\n    else:\n        experiments = registry\nelse:\n    print(\"Registry is a list\")\n    experiments = {str(i): v for i, v in enumerate(registry)}\n\n# Print keys to understand structure\nprint(\"Top-level keys:\", list(registry.keys())[:20])\nprint(\"Type:\", type(registry))\nprint()\n\n# Check if experiments is a dict or list\nif isinstance(experiments, dict):\n    print(\"First experiment key sample:\", list(experiments.keys())[:5])\nelif isinstance(experiments, list):\n    print(\"Experiments is a list of length:\", len(experiments))\n    if experiments:\n        print(\"First item keys:\", list(experiments[0].keys())[:10] if isinstance(experiments[0], dict) else type(experiments[0]))\n\nPYEOF",
  "description": "Parse JSON structure and understand registry format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "aad1d66b-666c-46d2-a067-8af5f6f4b3c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fqiu7e1FwtWz44sQUKN83p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 14630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1137,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 38 · 2026-05-22T07:38:01.641Z_

<details><summary>↩ Tool result · `toolu_01W1noUJaYRLxRoH1tAV8jqj`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
Type: &lt;class 'dict'>

First experiment key sample: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "7af95574-81cf-41de-aa96-86ca80f6715a"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Explore nested data structure",
  "usage": {
    "total_tokens": 16565,
    "tool_uses": 3,
    "duration_ms": 21029
  },
  "last_tool_name": "Bash",
  "uuid": "0ac87506-cdae-4423-92f3-049b5c9b49fe",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_017kHi1nRJHcztzuPoUDoJKS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\n\n# Explore nested structure\nprint(\"success:\", registry.get(\"success\"))\nprint(\"error:\", registry.get(\"error\"))\nprint(\"metadata keys:\", list(registry.get(\"metadata\", {}).keys()) if isinstance(registry.get(\"metadata\"), dict) else registry.get(\"metadata\"))\nprint()\n\ndata = registry.get(\"data\", {})\nprint(\"data type:\", type(data))\nif isinstance(data, dict):\n    print(\"data keys:\", list(data.keys())[:20])\nelif isinstance(data, list):\n    print(\"data length:\", len(data))\n    if data:\n        print(\"first item type:\", type(data[0]))\n        if isinstance(data[0], dict):\n            print(\"first item keys:\", list(data[0].keys())[:15])\n\nPYEOF",
  "description": "Explore nested data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "120eaef1-b453-4b7f-9b2c-b55e77947c30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Et1Hs4wCWeNc9Zqp51J9LH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 15767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 675,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-22T07:38:07.270Z_

<details><summary>↩ Tool result · `toolu_017kHi1nRJHcztzuPoUDoJKS`</summary>

```text
success: True
error: None
metadata keys: ['elapsed_seconds']

data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "63b580ea-0de4-477c-a0f5-255c89410f29"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Explore experiments structure",
  "usage": {
    "total_tokens": 17095,
    "tool_uses": 4,
    "duration_ms": 25826
  },
  "last_tool_name": "Bash",
  "uuid": "34969ccc-c3d1-472f-8992-a083762a9947",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cv3Eu5LMepWb98rocVTo22`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\ndata = registry[\"data\"]\nexperiments = data[\"experiments\"]\n\nprint(\"Experiments type:\", type(experiments))\nif isinstance(experiments, list):\n    print(\"Count:\", len(experiments))\n    # Show first experiment structure\n    if experiments:\n        exp = experiments[0]\n        print(\"\\nFirst experiment keys:\", sorted(exp.keys()))\n        print(\"\\nFirst experiment:\")\n        print(json.dumps(exp, indent=2)[:2000])\nelif isinstance(experiments, dict):\n    print(\"Keys:\", list(experiments.keys())[:10])\n\nPYEOF",
  "description": "Explore experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "b3eb3b26-eca9-4b38-89ea-df834aa390ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Es9faNeeNgGQ27tCkKVr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 16442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 458,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-22T07:38:12.061Z_

<details><summary>↩ Tool result · `toolu_01Cv3Eu5LMepWb98rocVTo22`</summary>

```text
Experiments type: &lt;class 'dict'>
Keys: ['exp_041_dual_critic_walker_s3', 'exp_040_wide_dual_critic_cheetah', 'exp_042_frozen_dt_emb_walker', 'exp_043_008f_walker_s1', 'exp_039_narrow_dual_critic_walker_s1', 'exp_038_dual_critic_walker_s2', 'exp_037_wide_critic_cheetah', 'exp_036_dual_critic_pickcube', 'exp_035_narrow_dual_critic_walker', 'exp_034']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "dfe370f4-f4ef-428d-ad6e-6f8bda45b503"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running List all experiment keys and show sample structure",
  "usage": {
    "total_tokens": 17678,
    "tool_uses": 5,
    "duration_ms": 30560
  },
  "last_tool_name": "Bash",
  "uuid": "ae04604c-cac4-4b60-b4bc-dae5849e2690",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01KdGBL76prxGwJbgwgy7WUQ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Print all experiment keys\nprint(\"All experiment keys:\")\nfor k in sorted(experiments.keys()):\n    print(f\"  {k}\")\n\nprint(f\"\\nTotal: {len(experiments)}\")\n\n# Show structure of one experiment in detail\nprint(\"\\n--- Sample experiment structure ---\")\nsample_key = list(experiments.keys())[0]\nprint(json.dumps(experiments[sample_key], indent=2)[:3000])\n\nPYEOF",
  "description": "List all experiment keys and show sample structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "7fc49a81-e31d-4a20-900c-f300fd431391",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmhsCBmpYszeS8xhj1TXKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 16900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 511,
        "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-22T07:38:16.794Z_

<details><summary>↩ Tool result · `toolu_01KdGBL76prxGwJbgwgy7WUQ`</summary>

```text
All experiment keys:
  016e
  exp_001_baseline
  exp_001_baseline_s2
  exp_001_baseline_s2_extended
  exp_001_baseline_s3
  exp_001_baseline_s3_extended
  exp_001_baseline_s4
  exp_001_baseline_s4_extended
  exp_002_event_gated
  exp_003_event_gated_v2
  exp_004_event_gated_v3
  exp_005_event_gated_v4
  exp_006
  exp_006_fixed_dt2
  exp_007_fixed_dt4
  exp_008a
  exp_008a_cheetah_unexposed_s0
  exp_008a_cheetah_unexposed_s1
  exp_008a_no_subsample_dt2
  exp_008a_unexposed_s1
  exp_008a_unexposed_s2
  exp_008a_untrained_s1
  exp_008a_untrained_s2
  exp_008c
  exp_008c_no_subsample_dt2_h8
  exp_008d
  exp_008d_civo_trigger_s2
  exp_008d_civo_trigger_s3
  exp_008d_civo_trigger_s4
  exp_008d_subsample_on_h8
  exp_008e_subsample_on_dt1_h15
  exp_008e_subsample_on_fixed_dt1
  exp_008e_v2_subsample_on_dt1_h15
  exp_008e_v3_s3
  exp_008e_v3_s4
  exp_008e_v3_subsample_on_dt1_h15
  exp_008e_v3_walker_s1
  exp_008e_v3_walker_s2
  exp_008f_no_dt_embed_subsample_on_h8
  exp_008f_s2
  exp_008f_s3_no_dt_embed_walker
  exp_008f_s4
  exp_009a_baseline_walker_s2
  exp_009b_008d_walker_s2
  exp_009c_008f_walker_s2
  exp_009c_s2
  exp_009c_s3
  exp_009d_baseline_walker_s0
  exp_009d_baseline_walker_s1
  exp_009e_008d_walker_s1
  exp_009f_008f_walker_s1
  exp_009g_008f_walker_s0
  exp_009h_008f_walker_s0
  exp_010a_cheetah_baseline_s1
  exp_010b_cheetah_civo_trigger
  exp_010b_cheetah_civo_trigger_s0
  exp_015b_frozen_dt_emb
  exp_016_sgs_walker_s1
  exp_016b_sgs_walker_s1
  exp_016c_sgs_walker_s1
  exp_016d_sgs_walker_s1
  exp_016e_sgs_walker_s1
  exp_017_subsample_off_trained_dt_emb
  exp_018_full_sgs_s2
  exp_018_full_sgs_walker_s1
  exp_018v2_full_sgs_walker_s1
  exp_019a_pickcube_baseline
  exp_019a_v2_pickcube_baseline
  exp_019b_pickcube_civo_trigger
  exp_020_vanilla_dreamerv3_s2
  exp_021_full_sgs_cheetah_s1
  exp_022_untrained_dt_emb_learned_gate
  exp_022b_no_curriculum
  exp_023_cheetah_baseline_s2
  exp_023_cheetah_baseline_s3
  exp_023_cheetah_baseline_s4
  exp_023_cheetah_baseline_s4_extended
  exp_023a_cheetah_baseline_s0
  exp_023b_cheetah_baseline_s1
  exp_024_cheetah_no_dt_emb_s0
  exp_024b_cheetah_no_dt_emb_s0
  exp_024b_cheetah_no_dt_emb_s1
  exp_025_obs_sgs_walker_s1
  exp_025_obs_sgs_walker_s2
  exp_025_obs_sgs_walker_s3
  exp_025_obs_sgs_walker_s4
  exp_026_obs_sgs_cheetah_s0
  exp_026_obs_sgs_cheetah_s1
  exp_027_tcn_walker_s0
  exp_027_tcn_walker_s0_sigma02
  exp_027_tcn_walker_s1
  exp_028_rave_walker_s0
  exp_028_rave_walker_s0_ceil15
  exp_029a_tcn_walker_s1_sigma02
  exp_029b_tcn_walker_s2_sigma02
  exp_029c_tcn_walker_s0_sigma01
  exp_029d_tcn_walker_s3_sigma02
  exp_030a_tcn_cheetah_s0_sigma02
  exp_030b_tcn_cheetah_s0_sigma05
  exp_030c_tcn_cheetah_s0_sigma10
  exp_031_tcn_pickcube_s0_sigma02
  exp_031b_tcn_pickcube_s0_sigma05
  exp_032_dual_critic_walker
  exp_032b_dual_critic_walker_s1
  exp_033_wide_critic_walker
  exp_034
  exp_034_dual_critic_cheetah
  exp_035_narrow_dual_critic_walker
  exp_036_dual_critic_pickcube
  exp_037_wide_critic_cheetah
  exp_038_dual_critic_walker_s2
  exp_039_narrow_dual_critic_walker_s1
  exp_040_wide_dual_critic_cheetah
  exp_041_dual_critic_walker_s3
  exp_042_frozen_dt_emb_walker
  exp_043_008f_walker_s1
  exp_rssm_fidelity_analysis

Total: 117

--- Sample experiment structure ---
{
  "created_at": "2026-05-21T19:50:54.290Z",
  "hypothesis": "D128 \u63a8\u5bfc\uff1aexp_038 s2 \u51fa\u73b0\u975e CIVO \u5d29\u6e83 (eval 354\u2192121, NVE\u22640.3)\uff0c\u5f53\u524d collapse \u9891\u7387 1/3\u3002s3 \u786e\u5b9a\u5d29\u6e83\u662f\u5076\u53d1 (1/4) \u8fd8\u662f\u7cfb\u7edf\u6027 (2/4)\u3002\u5982\u679c s3 \u6b63\u5e38 \u2192 \u975e CIVO \u5d29\u6e83\u4e3a\u4f4e\u9891\u5076\u53d1\u4e8b\u4ef6\uff0cdual-critic CIVO prevention \u4ecd robust\uff1b\u5982\u679c s3 \u4e5f\u5d29 \u2192 50% \u7cfb\u7edf\u6027\u95ee\u9898\u9700\u8fdb\u4e00\u6b65\u8bca\u65ad\u3002",
  "parent": "exp_032_dual_critic_walker",
  "retry_count": 0,
  "spec": {
    "account": "root",
    "backend": "tmux",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\"",
    "gpu": [
      "cuda:1"
    ],
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log",
    "pid": "51103",
    "server": "bjb1-45299",
    "submitted_at": "2026-05-22T02:38:20.728Z",
    "submitted_via": "submit_training_job"
  },
  "status": "RUNNING",
  "updated_at": "2026-05-22T06:16:00.000Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "6092a10f-3728-43b4-ae4b-a08f2671d15a"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Extract dual-critic experiments",
  "usage": {
    "total_tokens": 20433,
    "tool_uses": 6,
    "duration_ms": 49775
  },
  "last_tool_name": "Bash",
  "uuid": "da192b09-555a-46d0-ac60-10b3ef3734c0",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01L7FzR2UzgQbcSbour7HeYb`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# ============================================================\n# CATEGORY 1: DUAL-CRITIC EXPERIMENTS\n# ============================================================\ndual_critic_keys = [\n    \"exp_032_dual_critic_walker\", \"exp_032b_dual_critic_walker_s1\",\n    \"exp_033_wide_critic_walker\", \"exp_034\", \"exp_034_dual_critic_cheetah\",\n    \"exp_035_narrow_dual_critic_walker\", \"exp_036_dual_critic_pickcube\",\n    \"exp_038_dual_critic_walker_s2\", \"exp_039_narrow_dual_critic_walker_s1\",\n    \"exp_040_wide_dual_critic_cheetah\", \"exp_041_dual_critic_walker_s3\",\n]\n\nprint(\"=\" * 80)\nprint(\"CATEGORY 1: DUAL-CRITIC EXPERIMENTS\")\nprint(\"=\" * 80)\n\nfor k in sorted(experiments.keys()):\n    # Match by prefix\n    matched = False\n    for dc in dual_critic_keys:\n        if k == dc or k.startswith(\"exp_032\") or k.startswith(\"exp_033\") or k.startswith(\"exp_034\") or k.startswith(\"exp_035\") or k.startswith(\"exp_036\") or k.startswith(\"exp_038\") or k.startswith(\"exp_039\") or k.startswith(\"exp_040\") or k.startswith(\"exp_041\"):\n            matched = True\n            break\n    if matched:\n        exp = experiments[k]\n        print(f\"\\n--- {k} ---\")\n        print(f\"  Status: {exp.get('status', 'N/A')}\")\n        print(f\"  Hypothesis: {exp.get('hypothesis', 'N/A')[:200]}\")\n        if exp.get('conclusion'):\n            print(f\"  Conclusion: {exp['conclusion'][:300]}\")\n        if exp.get('metrics'):\n            print(f\"  Metrics: {json.dumps(exp['metrics'], indent=4)[:500]}\")\n        if exp.get('results'):\n            print(f\"  Results: {json.dumps(exp['results'], indent=4)[:500]}\")\n        if exp.get('eval_score') is not None:\n            print(f\"  Eval Score: {exp['eval_score']}\")\n        if exp.get('nve') is not None:\n            print(f\"  NVE: {exp['nve']}\")\n        # Check for any numeric fields\n        for field in ['eval', 'eval_return', 'return', 'reward', 'final_eval', 'best_eval', 'nve', 'gate_ratio', 'dt_mean']:\n            if field in exp:\n                print(f\"  {field}: {exp[field]}\")\n        # Print all keys to find metric fields\n        non_standard = {kk: vv for kk, vv in exp.items() if kk not in ['created_at', 'updated_at', 'hypothesis', 'spec', 'status', 'parent', 'retry_count']}\n        if non_standard:\n            print(f\"  Extra fields: {json.dumps(non_standard, indent=4, default=str)[:600]}\")\n\nPYEOF",
  "description": "Extract dual-critic experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "ec8f31d3-276f-4d74-a4d9-73a5879c4655",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxX6EhbG8iZmZVg5gci9GF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 17411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2753,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-22T07:38:36.011Z_

<details><summary>↩ Tool result · `toolu_01L7FzR2UzgQbcSbour7HeYb`</summary>

```text
================================================================================
CATEGORY 1: DUAL-CRITIC EXPERIMENTS
================================================================================

--- exp_032_dual_critic_walker ---
  Status: DONE
  Hypothesis: Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays b
  Conclusion: success
  Metrics: {
    "baseline_eval": 900,
    "civo_prevented": true,
    "eval_final": 739.7,
    "eval_final_step": 215000,
    "eval_peak": 787.7,
    "eval_peak_step": 205000,
    "eval_vs_baseline_pct": 87.5,
    "gate_dt2_frac": 1.0,
    "gate_entropy": 0.0,
    "note": "CIVO prevented 2/2 seeds. v1\u2248v2 \u2192 mechanism is implicit value regularization, not min-of-two pessimism.",
    "nve_final": 0.1,
    "nve_peak": 1.1,
    "nve_peak_step": 95000,
    "v1_v2_gap": "<0.1% (min operation has no pes
  Extra fields: {
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt",
    "completed_at": "2026-05-21T07:47:55.131382+00:00",
    "conclusion": "success",
    "extra": {
        "hook_events": [
            {
                "action": "agent",
                "event": "on_complete",
                "ts": "2026-05-21T07:45:13.742811+00:00"
            }
        ]
    },
    "metrics": {
        "baseline_eval": 900,
        "civo_prevented": true,
        "eval_final": 739.7,
        "eval_final_step": 215000,
        "eval_peak": 787.7,
        "

--- exp_032b_dual_critic_walker_s1 ---
  Status: DONE
  Hypothesis: Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.
  Conclusion: success
  Metrics: {
    "actor_loss_late": "\u22480 (gradient signal weak)",
    "baseline_eval": 900,
    "director_override": "CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.",
    "eval_criterion_pass": false,
    "eval_trajectory": "75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516",
    "eval_vs_baseline_pct": 57,
    "final_eval_return": 516,
    "final_nve": 0.1,
    "gate_
  Extra fields: {
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt",
    "completed_at": "2026-05-21T05:50:59.612299+00:00",
    "conclusion": "success",
    "extra": {
        "hook_events": [
            {
                "action": "agent",
                "event": "on_complete",
                "ts": "2026-05-21T05:48:16.069863+00:00"
            }
        ]
    },
    "gpu": "cuda:1",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log",
    "metrics": {
        "actor_loss_late"

--- exp_033_wide_critic_walker ---
  Status: DONE
  Hypothesis: Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should
  Conclusion: success
  Metrics: {
    "civo_alert_step": 105000,
    "civo_alert_ve_ratio": 1.958,
    "civo_instability_duration_steps": 75000,
    "critic_params": 2886911,
    "eval_reward_final": 407.9,
    "eval_reward_peak": 194.8,
    "eval_reward_trough": 31.8,
    "value_loss_final": 1.4,
    "ve_ratio_final": 0.1,
    "ve_ratio_peak": 4.7
}
  Extra fields: {
    "account": "root",
    "checkpoint_path": "logdir/exp_033_wide_critic_walker/latest.pt",
    "completed_at": "2026-05-21T12:08:15.252Z",
    "conclusion": "success",
    "extra": {
        "hook_events": [
            {
                "action": "agent",
                "event": "on_complete",
                "ts": "2026-05-21T12:02:31.184962+00:00"
            }
        ]
    },
    "gpu": "cuda:0",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log",
    "metrics": {
        "civo_alert_step": 105000,
        "civo_alert_ve_ratio": 1.958,
        "civo_

--- exp_034 ---
  Status: DONE
  Hypothesis: Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-unive
  Conclusion: negative
  Metrics: {
    "CIVO_prevented": false,
    "civo_trigger_steps": [
        55000,
        105000
    ],
    "final_NVE": 0.144,
    "final_eval_return": 97.5,
    "max_NVE": 1.753,
    "peak_eval_return": 315.7,
    "total_steps": 215000,
    "v1_v2_max_divergence": 0.004
}
  Extra fields: {
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/",
    "completed_at": "2026-05-21T12:18:09.552Z",
    "conclusion": "negative",
    "log_path": "/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log",
    "metrics": {
        "CIVO_prevented": false,
        "civo_trigger_steps": [
            55000,
            105000
        ],
        "final_NVE": 0.144,
        "final_eval_return": 97.5,
        "max_NVE": 1.753,
        "peak_eval_return": 315.7,
        "total_steps": 215000,
        "v1_v2_max_divergence": 0.0

--- exp_034_dual_critic_cheetah ---
  Status: DONE
  Hypothesis: Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level int
  Conclusion: negative
  Metrics: {
    "baseline_eval_final": 0.83,
    "baseline_nve_peak": 70.64,
    "civo_alert_steps": [
        95000,
        105000
    ],
    "civo_alerts": 2,
    "civo_prevented": false,
    "dual_wave_civo": true,
    "eval_final": 97.5,
    "eval_final_step": 215000,
    "eval_peak": 315.7,
    "eval_peak_step": 45000,
    "eval_vs_peak_pct": 31,
    "gate_dt2_frac": 1,
    "gate_entropy": 0,
    "v1_v2_gap": "<0.2 (min operation has no pessimism effect)",
    "value_mean_final": 14.2,
    "value_me
  Extra fields: {
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah",
    "completed_at": "2026-05-21T12:14:19.189109+00:00",
    "conclusion": "negative",
    "extra": {
        "hook_events": [
            {
                "action": "agent",
                "event": "on_complete",
                "ts": "2026-05-21T12:02:46.032647+00:00"
            }
        ]
    },
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log",
    "metrics": {
        "baseline_eval_final": 0.83,
        "baseline_nve_peak": 70.64,
        "ci

--- exp_035_narrow_dual_critic_walker ---
  Status: DONE
  Hypothesis: Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestima
  Conclusion: success
  Metrics: {
    "actor_entropy_final": -0.19,
    "civo_alert_window": "65K-85K",
    "civo_prevented": false,
    "civo_recovery": true,
    "director_override": "Director ruled success: CIVO recovery (33.8\u2192697.8) is the success criterion, not prevention",
    "eval_at_215K": 697.8,
    "eval_at_85K": 33.8,
    "eval_final": 697.8,
    "eval_peak": 697.8,
    "eval_trough": 33.8,
    "nve_final": 0.066,
    "nve_peak": 2.75,
    "nve_peak_step": 85000,
    "recovery_from": 33.8,
    "recovery_to": 6
  Extra fields: {
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt",
    "completed_at": "2026-05-21T16:11:39.130025+00:00",
    "conclusion": "success",
    "extra": {
        "hook_events": [
            {
                "action": "agent",
                "event": "on_complete",
                "ts": "2026-05-21T16:08:03.906985+00:00"
            }
        ]
    },
    "gpu": "cuda:1",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log",
    "metrics": {
        "actor_entr

--- exp_036_dual_critic_pickcube ---
  Status: DONE
  Hypothesis: Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+P
  Conclusion: negative
  Metrics: {
    "civo_alert": 0,
    "eval_return_final": 27.7,
    "eval_return_peak": 27.7,
    "gate_dt_2_frac": 1,
    "nve_final": 0.2,
    "nve_peak": 2.3,
    "steps": 212447
}
  Extra fields: {
    "completed_at": "2026-05-21T19:45:31.290Z",
    "conclusion": "negative",
    "extra": {
        "hook_events": [
            {
                "action": "agent",
                "event": "on_complete",
                "ts": "2026-05-21T19:38:29.196731+00:00"
            }
        ]
    },
    "metrics": {
        "civo_alert": 0,
        "eval_return_final": 27.7,
        "eval_return_peak": 27.7,
        "gate_dt_2_frac": 1,
        "nve_final": 0.2,
        "nve_peak": 2.3,
        "steps": 212447
    },
    "reproduce": {
        "finished_at": "2026-05-21T19:38:24.346Z"
    }
}

--- exp_038_dual_critic_walker_s2 ---
  Status: DONE
  Hypothesis: Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO preven
  Conclusion: negative
  Metrics: {
    "civo_alert": 0,
    "civo_prevented": true,
    "eval_return_collapse": 99.6,
    "eval_return_collapse_step": 175000,
    "eval_return_final": 120.9,
    "eval_return_peak": 354,
    "eval_return_peak_step": 155000,
    "gate_dt_2_frac": 1,
    "non_civo_collapse": true,
    "note": "CIVO prevented (NVE\u22640.3) but non-CIVO eval collapse at 175k (354\u219299.6). Different failure mode from value overestimation.",
    "nve_final": 0.248,
    "nve_peak": 0.3,
    "steps": 224000
}
  Extra fields: {
    "completed_at": "2026-05-22T02:11:36.842Z",
    "conclusion": "negative",
    "metrics": {
        "civo_alert": 0,
        "civo_prevented": true,
        "eval_return_collapse": 99.6,
        "eval_return_collapse_step": 175000,
        "eval_return_final": 120.9,
        "eval_return_peak": 354,
        "eval_return_peak_step": 155000,
        "gate_dt_2_frac": 1,
        "non_civo_collapse": true,
        "note": "CIVO prevented (NVE\u22640.3) but non-CIVO eval collapse at 175k (354\u219299.6). Different failure mode from value overestimation.",
        "nve_final": 0.248,
        "n

--- exp_039_narrow_dual_critic_walker_s1 ---
  Status: DONE
  Hypothesis: Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 reco
  Conclusion: success
  Metrics: {
    "civo_recovery": true,
    "eval_return_final": 592.7,
    "note": "Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean\u2248645. Recovery 2/2.",
    "nve_peak": 2.19,
    "recovery_confirmed": true
}
  Extra fields: {
    "completed_at": "2026-05-22T02:35:33.617Z",
    "conclusion": "success",
    "metrics": {
        "civo_recovery": true,
        "eval_return_final": 592.7,
        "note": "Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean\u2248645. Recovery 2/2.",
        "nve_peak": 2.19,
        "recovery_confirmed": true
    }
}

--- exp_040_wide_dual_critic_cheetah ---
  Status: RUNNING
  Hypothesis: Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。

--- exp_041_dual_critic_walker_s3 ---
  Status: RUNNING
  Hypothesis: D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "9cbd7ef2-f43f-4dcb-bccd-4215be5da6d3"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Extract remaining target experiment categories",
  "usage": {
    "total_tokens": 26252,
    "tool_uses": 7,
    "duration_ms": 68672
  },
  "last_tool_name": "Bash",
  "uuid": "e16ff9aa-a8e7-4056-af21-58376a859139",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01TkhGt1aLzBtCP2jFLzUJ5M`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# ============================================================\n# CATEGORY 2-7: Remaining target experiments\n# ============================================================\n\ntarget_prefixes = {\n    \"FROZEN_DT_EMB\": [\"exp_042\"],\n    \"008F_REPLICATION\": [\"exp_043\"],\n    \"CHEETAH\": [\"exp_010a\", \"exp_010b\"],\n    \"PICKCUBE\": [\"exp_019a\", \"exp_019b\"],\n    \"CIVO_BASELINE\": [\"exp_008d\", \"exp_008a\", \"exp_008f\"],\n    \"GRADIENT_STOPPING\": [\"exp_016e\", \"016e\", \"exp_018\", \"exp_021\", \"exp_025\", \"exp_026\"],\n}\n\nfor category, prefixes in target_prefixes.items():\n    print(\"=\" * 80)\n    print(f\"CATEGORY: {category}\")\n    print(\"=\" * 80)\n    \n    for k in sorted(experiments.keys()):\n        matched = any(k.startswith(p) or k == p for p in prefixes)\n        if matched:\n            exp = experiments[k]\n            print(f\"\\n--- {k} ---\")\n            print(f\"  Status: {exp.get('status', 'N/A')}\")\n            hyp = exp.get('hypothesis', 'N/A')\n            if hyp and len(hyp) > 200:\n                hyp = hyp[:200] + \"...\"\n            print(f\"  Hypothesis: {hyp}\")\n            if exp.get('conclusion'):\n                print(f\"  Conclusion: {exp['conclusion']}\")\n            if exp.get('metrics'):\n                print(f\"  Metrics: {json.dumps(exp['metrics'], indent=4, default=str)[:800]}\")\n            if exp.get('completed_at'):\n                print(f\"  Completed: {exp['completed_at']}\")\n            # Check spec for step info on RUNNING\n            if exp.get('status') == 'RUNNING':\n                spec = exp.get('spec', {})\n                print(f\"  Server: {spec.get('server', 'N/A')}\")\n                print(f\"  PID: {spec.get('pid', 'N/A')}\")\n                print(f\"  Submitted: {spec.get('submitted_at', 'N/A')}\")\n\nPYEOF",
  "description": "Extract remaining target experiment categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "e51fd55a-23c9-417a-8417-dbd09ba53698",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSjCigy5EzZDoGKrcTsS19",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5782,
      "cache_read_input_tokens": 20164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5782,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 53 · 2026-05-22T07:38:54.912Z_

<details><summary>↩ Tool result · `toolu_01TkhGt1aLzBtCP2jFLzUJ5M`</summary>

```text
================================================================================
CATEGORY: FROZEN_DT_EMB
================================================================================

--- exp_042_frozen_dt_emb_walker ---
  Status: RUNNING
  Hypothesis: dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp...
  Server: bjb1-40020
  PID: 251336
  Submitted: N/A
================================================================================
CATEGORY: 008F_REPLICATION
================================================================================

--- exp_043_008f_walker_s1 ---
  Status: RUNNING
  Hypothesis: Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 "trained dt_emb → CIVO"。
  Server: bjb1-40020
  PID: 250627
  Submitted: N/A
================================================================================
CATEGORY: CHEETAH
================================================================================

--- exp_010a_cheetah_baseline_s1 ---
  Status: DONE
  Hypothesis: Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）
  Conclusion: success
  Metrics: {
    "eval_return_final": 849.8,
    "eval_return_final_step": 515000,
    "eval_return_peak": 849.8,
    "eval_return_peak_step": 515000,
    "final_step": 524000,
    "total_eval_episodes": 52,
    "train_return_last": 716
}
  Completed: 2026-05-16T12:01:01.080Z

--- exp_010b_cheetah_civo_trigger ---
  Status: DONE
  Hypothesis: Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer "single environment" concern。
  Conclusion: success
  Metrics: {
    "civo": true,
    "eval_return_final": 51.7,
    "eval_return_peak": 321.9,
    "nve_peak": 8.27,
    "nve_peak_step": 65000,
    "peak_step": 35000
}
  Completed: 2026-05-16T16:16:00.478Z

--- exp_010b_cheetah_civo_trigger_s0 ---
  Status: DONE
  Hypothesis: Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。
  Conclusion: success
  Metrics: {
    "civo": true,
    "civo_onset_step": "65K",
    "detector_alert_step": "95K",
    "eval_return_105K": 0.83,
    "eval_return_peak": 247.77,
    "eval_return_peak_step": "35K",
    "gate_dt_mean": 2,
    "gate_entropy": 0,
    "nve_105K": 70.64,
    "nve_95K": 6.34
}
  Completed: 2026-05-18T05:11:15.900Z
================================================================================
CATEGORY: PICKCUBE
================================================================================

--- exp_019a_pickcube_baseline ---
  Status: DONE
  Hypothesis: PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性
  Conclusion: killed
  Completed: 2026-05-16T13:43:00.745Z

--- exp_019a_v2_pickcube_baseline ---
  Status: DONE
  Hypothesis: Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.
  Conclusion: success
  Metrics: {
    "eval_return_final": 69.43,
    "eval_return_peak": 69.7,
    "eval_return_peak_step": 162500,
    "steps_completed": 200248,
    "value_mean_final": 143.4,
    "ve_ratio_final": 2.07,
    "ve_ratio_range": "1.05-3.56"
}
  Completed: 2026-05-16T21:07:12.193Z

--- exp_019b_pickcube_civo_trigger ---
  Status: DONE
  Hypothesis: PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立
  Conclusion: success
  Metrics: {
    "baseline_eval_final": 58.56,
    "baseline_ratio": 0.455,
    "eval_return_final": 26.64,
    "eval_return_peak": 26.9,
    "eval_return_peak_step": 132500,
    "gate_dt_2_frac": 1,
    "gate_entropy": 0,
    "nve_final": 0.065,
    "nve_peak": 3.78,
    "nve_peak_step": 52500,
    "pattern": "transient_civo_then_value_collapse",
    "total_steps": 200000,
    "value_baseline_final": 144.57,
    "value_mean_final": 4.26
}
  Completed: 2026-05-17T03:35:47.561Z
================================================================================
CATEGORY: CIVO_BASELINE
================================================================================

--- exp_008a ---
  Status: DONE
  Hypothesis: N/A
  Conclusion: killed
  Metrics: {
    "eval_return_15K": 167.2,
    "eval_return_25K": 230.8,
    "eval_return_35K": 500.8,
    "eval_return_45K": 563.4,
    "eval_return_55K": 487.9,
    "eval_return_5K": 31,
    "eval_return_65K": "pending (eval in progress)",
    "step": 65000,
    "train_return_64K_avg": 556.6,
    "trend": "peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)",
    "value_eval_ratio_55K": "37.6%",
    "value_mean_55K": 183.5
}

--- exp_008a_cheetah_unexposed_s0 ---
  Status: DONE
  Hypothesis: Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in...
  Conclusion: success
  Metrics: {
    "current_step": 112000,
    "eval_return_105k": 532.35,
    "nve_105k": 0.49,
    "target_steps": 105000,
    "value_mean_105k": 169.98,
    "ve_ratio_105k": 0.3193
}
  Completed: 2026-05-18T18:19:58.491Z

--- exp_008a_cheetah_unexposed_s1 ---
  Status: DONE
  Hypothesis: Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in...
  Conclusion: success
  Metrics: {
    "current_step": 112000,
    "eval_return_105k": 504.38,
    "nve_105k": 0.478,
    "target_steps": 105000,
    "value_mean_105k": 156.97,
    "ve_ratio_105k": 0.3112
}
  Completed: 2026-05-18T18:20:00.278Z

--- exp_008a_no_subsample_dt2 ---
  Status: DONE
  Hypothesis: 隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。
  Conclusion: success
  Metrics: {
    "baseline_105K": 915.67,
    "baseline_55K": 625.7,
    "baseline_65K": 616,
    "data_source": "from training logs metrics.jsonl",
    "eval_return_105K": 777.66,
    "eval_return_35K": 500.84,
    "eval_return_45K": 563.41,
    "eval_return_55K": 487.92,
    "eval_return_65K": 608,
    "eval_return_75K": 469.93,
    "eval_return_85K": 583.73,
    "eval_return_95K": 572.24,
    "nan_count": 0,
    "normalized_ve_105K": 0.59,
    "normalized_ve_55K": 0.93,
    "normalized_ve_65K": 0.66,
    "normalized_ve_75K": 0.75,
    "normalized_ve_85K": 0.68,
    "normalized_ve_95K": 0.79,
    "step": 112000,
    "trend": "Two V-shaped recoveries: 501\u2192563\u2192488\u2192608\u2192470\u2192584\u2192572\u2192778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K",
    
  Completed: 2026-05-14T06:16:58.196Z

--- exp_008a_unexposed_s1 ---
  Status: DONE
  Hypothesis: Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibili...
  Conclusion: success
  Metrics: {
    "civo_alert": 0,
    "civo_delta_ve_final": -0.0028,
    "civo_ve_ratio_final": 0.43,
    "eval_return_15k": 167.12,
    "eval_return_25k": 139.94,
    "eval_return_35k": 394.15,
    "eval_return_45k": 414.32,
    "eval_return_55k": 441.48,
    "eval_return_5k": 31,
    "eval_return_65k": 491.74,
    "eval_return_75k": 452.34,
    "eval_return_85k": 546.82,
    "eval_return_95k": 628.57,
    "eval_return_final": 630.91,
    "gate_dt_2_frac": 1,
    "gate_dt_mean": 2,
    "target_mean_final": 272.13,
    "total_steps": 105000,
    "value_mean_final": 271.36
}
  Completed: 2026-05-18T08:16:42.716Z

--- exp_008a_unexposed_s2 ---
  Status: DONE
  Hypothesis: Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。
  Conclusion: success
  Metrics: {
    "civo_alert": 0,
    "civo_delta_ve_final": -0.003,
    "civo_ve_ratio_final": 0.333,
    "eval_return_55k": 607.5,
    "eval_return_65k": 653.8,
    "eval_return_75k": 534.4,
    "eval_return_85k": 605.4,
    "eval_return_95k": 819.4,
    "eval_return_final": 899.4,
    "gate_dt_2_frac": 1,
    "gate_dt_mean": 2,
    "target_mean_final": 300.3,
    "total_steps": 105000,
    "value_mean_final": 299.4
}
  Completed: 2026-05-18T08:10:06.059Z

--- exp_008a_untrained_s1 ---
  Status: DONE
  Hypothesis: (cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板
  Conclusion: killed

--- exp_008a_untrained_s2 ---
  Status: DONE
  Hypothesis: (cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板
  Conclusion: killed

--- exp_008d ---
  Status: DONE
  Hypothesis: N/A
  Conclusion: killed
  Metrics: {
    "eval_return_15K": 153.7,
    "eval_return_25K": 167.2,
    "eval_return_35K": 146.3,
    "eval_return_5K": 31,
    "step": 40000,
    "train_return_40K_avg": 119.3,
    "trend": "declining \u2014 train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping",
    "value_eval_ratio_35K": "41.1%",
    "value_mean_35K": 60.2
}

--- exp_008d_civo_trigger_s2 ---
  Status: DONE
  Hypothesis: Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原...
  Conclusion: killed
  Completed: 2026-05-17T00:24:10.180Z

--- exp_008d_civo_trigger_s3 ---
  Status: DONE
  Hypothesis: Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (see...
  Conclusion: success
  Metrics: {
    "baseline_eval_105K": 915.67,
    "collapse_onset_step": 95000,
    "collapse_type": "late-onset",
    "eval_return_final": 267.6,
    "eval_return_final_step": 105000,
    "eval_return_peak": 451.7,
    "eval_return_peak_step": 95000,
    "nve_final": 1.53,
    "nve_onset_step": 45000,
    "nve_onset_value": 1.5,
    "nve_peak": 1.53,
    "nve_peak_step": 105000,
    "nve_sustained_45K_55K": true,
    "total_steps": 112000,
    "train_return_final_avg": 138,
    "train_return_final_range": "82-214",
    "value_mean_final": 268.4,
    "vs_baseline_105K": "-70.8%"
}
  Completed: 2026-05-17T03:24:26.004Z

--- exp_008d_civo_trigger_s4 ---
  Status: DONE
  Hypothesis: Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。
  Conclusion: success
  Metrics: {
    "civo_alert_105K": 1,
    "civo_confirmed": true,
    "delta_ve_105K": 2.05,
    "eval_return_trajectory": {
        "105K": 63.6,
        "15K": 171.4,
        "25K": 189.5,
        "35K": 153.8,
        "45K": 158.2,
        "55K": 229.3,
        "5K": 30.9,
        "65K": 333.6,
        "75K": 302.4,
        "85K": 383.3,
        "95K": 240.3
    },
    "final_eval_return_105K": 63.6,
    "final_step": 112000,
    "gate_dt_2_frac": 1,
    "gate_dt_mean": 2,
    "peak_eval_return": 383.3,
    "peak_eval_step": 85000,
    "target_step": 105000,
    "value_mean_105K": 192.65,
    "value_mean_95K": 235.42,
    "ve_ratio_105K": 3.03
}
  Completed: 2026-05-18T05:17:45.132Z

--- exp_008d_subsample_on_h8 ---
  Status: DONE
  Hypothesis: Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy colla...
  Conclusion: success
  Metrics: {
    "actor_loss_25K": -0.195,
    "actor_loss_35K": -0.17,
    "baseline_35K": 400,
    "baseline_45K": 443,
    "data_source_45K": "from training logs metrics.jsonl",
    "eval_return_25K": 167.22,
    "eval_return_35K": 146.34,
    "eval_return_45K": 140.8,
    "eval_return_55K": 82.75,
    "model_loss_25K": 5.33,
    "model_loss_35K": 5.07,
    "step": 55000,
    "trend": "eval declining 167\u2192146\u2192141\u219283; v/e accelerating 15.5%\u219241.2%\u219269.3%\u2192167% \u2014 delusional critic collapse confirmed, value exceeds eval_return at 55K",
    "value_eval_ratio_25K": 0.155,
    "value_eval_ratio_35K": 0.411,
    "value_eval_ratio_45K": 0.693,
    "value_eval_ratio_55K": 1.666,
    "value_mean_25K": 25.86,
    "value_mean_35K": 60.2,
    "value_mean_45K": 97.5,
    "value_me
  Completed: 2026-05-14T04:50:52.439Z

--- exp_008f_no_dt_embed_subsample_on_h8 ---
  Status: DONE
  Hypothesis: Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.
  Conclusion: success
  Metrics: {
    "baseline_105K": 915.67,
    "causal_conclusion": "trained dt_embedding \u2192 value overestimation \u2192 actor exploitation \u2192 collapse. Without dt_embedding, value self-corrects.",
    "current_step": 105000,
    "eval_checkpoints": {
        "105K": {
            "eval_return": 503,
            "normalized_ve": 0.3,
            "value_mean": 98.2
        },
        "15K": {
            "eval_return": 182.03,
            "value_mean": 2.989,
            "ve_ratio": 0.01642
        },
        "25K": {
            "baseline_ve": 0.087,
            "eval_return": 196.78,
            "normalized_ve": 1.02,
            "value_mean": 17.507,
            "ve_ratio": 0.089
        },
        "35K": {
            "baseline_ve": 0.241,
            "eval_return": 206.67,
            "nor
  Completed: 2026-05-14T09:32:53.461Z

--- exp_008f_s2 ---
  Status: DONE
  Hypothesis: No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.
  Conclusion: killed
  Completed: 2026-05-18T18:41:05.369Z

--- exp_008f_s3_no_dt_embed_walker ---
  Status: DONE
  Hypothesis: Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。
  Conclusion: success
  Metrics: {
    "collapse": false,
    "eval_return_final": 363.8,
    "nve_peak": "< 1.5x"
}
  Completed: 2026-05-16T20:09:51.135Z

--- exp_008f_s4 ---
  Status: DONE
  Hypothesis: Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robu...
  Conclusion: negative
  Metrics: {
    "civo_alert": 0,
    "eval_return_105k": 306.5,
    "note": "No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.",
    "nve_105k": 0.58,
    "peak_eval": 487.5,
    "peak_eval_step": 55000,
    "peak_nve": 1.41,
    "peak_nve_step": 85000
}
  Completed: 2026-05-18T23:18:51.672Z
================================================================================
CATEGORY: GRADIENT_STOPPING
================================================================================

--- 016e ---
  Status: DONE
  Hypothesis: N/A
  Conclusion: killed
  Completed: 2026-05-16T01:39:17.916Z

--- exp_016e_sgs_walker_s1 ---
  Status: DONE
  Hypothesis: Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWrit...
  Conclusion: negative
  Metrics: {
    "actor_loss_sign_flip_step": 95000,
    "civo_catastrophic_step": 95000,
    "civo_detected": true,
    "civo_nve_peak": 10.42,
    "civo_nve_peak_step": 95000,
    "civo_onset_step": 85000,
    "civo_severity": "catastrophic",
    "current_step": 100000,
    "data_source": "metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25",
    "deep_analysis": {
        "016e_vs_008d_entropy_comparison": {
            "15K": {
                "008d": 0.481,
                "016e": 1.049,
                "delta": 0.568
            },
            "25K": {
                "008d": -1.862,
                "016e": -1.554,
                "delta": 0.308
            },
            "35K": {
                "008d": -3.465,
                "016e": -2.118,
         
  Completed: 2026-05-15T22:31:16.457Z

--- exp_018_full_sgs_s2 ---
  Status: DONE
  Hypothesis: Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.
  Conclusion: negative
  Completed: 2026-05-16T23:47:49.458Z

--- exp_018_full_sgs_walker_s1 ---
  Status: DONE
  Hypothesis: Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.
  Conclusion: killed
  Metrics: {
    "eval_return_final": 915.7,
    "eval_return_final_step": 105000,
    "eval_return_peak": 915.7,
    "eval_return_peak_step": 105000,
    "nve_peak": 0.72,
    "nve_peak_step": 75000,
    "nve_sustained_avg": 0.55,
    "nve_sustained_max": 0.72,
    "total_steps": 112000,
    "train_return_final_avg": 899.4,
    "value_mean_final": 601.1
}
  Completed: 2026-05-16T12:43:09.226Z

--- exp_018v2_full_sgs_walker_s1 ---
  Status: DONE
  Hypothesis: Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collaps...
  Conclusion: negative
  Metrics: {
    "civo_reduction_pct": 79,
    "eval_return_final": 448.3,
    "eval_return_final_step": 105000,
    "eval_return_peak": 499.6,
    "eval_return_peak_step": 75000,
    "gate_dt_2_frac": 1,
    "gate_dt_mean": 2,
    "late_collapse_detected": true,
    "late_collapse_step": 112000,
    "nve_final": 1.34,
    "nve_mean_45k_105k": 1.23,
    "nve_peak": 1.66,
    "nve_peak_step": 95000,
    "total_steps": 112000,
    "total_updates": 25099,
    "value_loss_final": 0.6
}
  Completed: 2026-05-16T17:24:44.481Z

--- exp_021_full_sgs_cheetah_s1 ---
  Status: DONE
  Hypothesis: Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。
  Conclusion: negative
  Metrics: {
    "baseline_pct": 38.7,
    "civo": true,
    "civo_type": "transient_self_correcting",
    "eval_return_final": 221.5,
    "nve_peak": 9.94,
    "nve_peak_step": "45K",
    "nve_sustained_55K_105K": 0.338,
    "vs_010b": "221.5 vs 51.7 (4.3x better)"
}
  Completed: 2026-05-17T22:49:15.021Z

--- exp_025_obs_sgs_walker_s1 ---
  Status: DONE
  Hypothesis: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs de...
  Conclusion: failed
  Completed: 2026-05-20T03:02:32.583Z

--- exp_025_obs_sgs_walker_s2 ---
  Status: DONE
  Hypothesis: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs de...
  Conclusion: negative
  Metrics: {
    "eval_return_215K": 89.6,
    "target_steps": 210000,
    "train_steps_completed": 224000,
    "ve_ratio_175K": 1.2,
    "ve_ratio_185K": 1.4,
    "ve_ratio_215K": 0.8
}
  Completed: 2026-05-20T03:14:06.591Z

--- exp_025_obs_sgs_walker_s3 ---
  Status: DONE
  Hypothesis: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs de...
  Conclusion: failed
  Completed: 2026-05-20T03:02:36.670Z

--- exp_025_obs_sgs_walker_s4 ---
  Status: DONE
  Hypothesis: Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs de...
  Conclusion: failed
  Completed: 2026-05-20T03:02:39.948Z

--- exp_026_obs_sgs_cheetah_s0 ---
  Status: DONE
  Hypothesis: Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS...
  Conclusion: failed
  Completed: 2026-05-20T03:02:43.170Z

--- exp_026_obs_sgs_cheetah_s1 ---
  Status: DONE
  Hypothesis: Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS...
  Conclusion: failed
  Completed: 2026-05-20T03:02:46.556Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "865eb5ed-38b9-408b-abbe-d3e4167fd8ff"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Find all RUNNING experiments",
  "usage": {
    "total_tokens": 35708,
    "tool_uses": 8,
    "duration_ms": 81985
  },
  "last_tool_name": "Bash",
  "uuid": "44ff84d8-a1ae-46cf-bfe4-ae8de125a7b8",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01VzLts1xBDU13ueTnJDfDRx`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Find ALL experiments with status=RUNNING\nprint(\"=\" * 80)\nprint(\"ALL RUNNING EXPERIMENTS\")\nprint(\"=\" * 80)\n\nfor k in sorted(experiments.keys()):\n    exp = experiments[k]\n    if exp.get('status') == 'RUNNING':\n        print(f\"\\n--- {k} ---\")\n        print(f\"  Hypothesis: {exp.get('hypothesis', 'N/A')[:250]}\")\n        spec = exp.get('spec', {})\n        print(f\"  Server: {spec.get('server', 'N/A')}\")\n        print(f\"  PID: {spec.get('pid', 'N/A')}\")\n        print(f\"  GPU: {spec.get('gpu', 'N/A')}\")\n        print(f\"  Submitted: {spec.get('submitted_at', exp.get('created_at', 'N/A'))}\")\n        print(f\"  Updated: {exp.get('updated_at', 'N/A')}\")\n        # Check command for step count\n        cmd = spec.get('command', '')\n        if '--steps' in cmd:\n            import re\n            m = re.search(r'--steps\\s+(\\d+)', cmd)\n            if m:\n                print(f\"  Target steps: {m.group(1)}\")\n        # Any metrics or progress\n        if exp.get('metrics'):\n            print(f\"  Metrics: {json.dumps(exp['metrics'], indent=4, default=str)[:400]}\")\n        if exp.get('progress'):\n            print(f\"  Progress: {exp['progress']}\")\n\nPYEOF",
  "description": "Find all RUNNING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "c5cbc7a5-e6cc-4266-84e4-c9da203f8be6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFvSCLsnUyETvBcm5r2KYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9419,
      "cache_read_input_tokens": 25946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 56 · 2026-05-22T07:39:08.220Z_

<details><summary>↩ Tool result · `toolu_01VzLts1xBDU13ueTnJDfDRx`</summary>

```text
================================================================================
ALL RUNNING EXPERIMENTS
================================================================================

--- exp_040_wide_dual_critic_cheetah ---
  Hypothesis: Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。
  Server: bjb1-45299
  PID: 52397
  GPU: ['cuda:0']
  Submitted: 2026-05-21T19:51:11.519Z
  Updated: 2026-05-22T06:13:30.000Z
  Target steps: 210000

--- exp_041_dual_critic_walker_s3 ---
  Hypothesis: D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。
  Server: bjb1-45299
  PID: 51103
  GPU: ['cuda:1']
  Submitted: 2026-05-22T02:38:20.728Z
  Updated: 2026-05-22T06:16:00.000Z
  Target steps: 210000

--- exp_042_frozen_dt_emb_walker ---
  Hypothesis: dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.
  Server: bjb1-40020
  PID: 251336
  GPU: ['cuda:0']
  Submitted: 2026-05-22T02:13:59.183Z
  Updated: 2026-05-22T03:41:49.000Z
  Target steps: 210000

--- exp_043_008f_walker_s1 ---
  Hypothesis: Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 "trained dt_emb → CIVO"。
  Server: bjb1-40020
  PID: 250627
  GPU: ['cuda:1']
  Submitted: 2026-05-22T02:35:37.558Z
  Updated: 2026-05-22T03:41:49.000Z
  Target steps: 210000
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "c57c45df-ea83-42d0-833b-4f18cc5ab6f8"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "description": "Running Get supplementary experiment details",
  "usage": {
    "total_tokens": 37315,
    "tool_uses": 9,
    "duration_ms": 96639
  },
  "last_tool_name": "Bash",
  "uuid": "b34325a1-171b-46e8-be9b-02ab5a839c56",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01K1dddTA6x3aQh1TPSusTo7`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\"\n\nwith open(FILE, 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Grab exp_037 (wide critic cheetah ablation)\nexp037 = experiments.get(\"exp_037_wide_critic_cheetah\", {})\nprint(\"=== exp_037_wide_critic_cheetah ===\")\nprint(f\"Status: {exp037.get('status')}\")\nprint(f\"Conclusion: {exp037.get('conclusion')}\")\nprint(f\"Metrics: {json.dumps(exp037.get('metrics', {}), indent=2, default=str)[:600]}\")\n\n# Also baseline reference\nprint(\"\\n=== Baseline data ===\")\nprint(f\"baseline field: {json.dumps(registry['data'].get('baseline', {}), indent=2, default=str)[:500]}\")\n\n# Print exp_018_full_sgs_walker_s1 metrics more completely\nexp018 = experiments.get(\"exp_018_full_sgs_walker_s1\", {})\nprint(\"\\n=== exp_018_full_sgs_walker_s1 full details ===\")\nprint(f\"Conclusion: {exp018.get('conclusion')}\")\nprint(f\"Metrics: {json.dumps(exp018.get('metrics', {}), indent=2, default=str)[:500]}\")\n\n# exp_020 vanilla dreamer\nexp020 = experiments.get(\"exp_020_vanilla_dreamerv3_s2\", {})\nprint(\"\\n=== exp_020_vanilla_dreamerv3_s2 ===\")\nprint(f\"Conclusion: {exp020.get('conclusion')}\")\nprint(f\"Metrics: {json.dumps(exp020.get('metrics', {}), indent=2, default=str)[:500]}\")\n\nPYEOF",
  "description": "Get supplementary experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "2eda04cd-63fb-4910-8881-f839abce9628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyHYaC5Bao8tUmTdpsSScb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 35365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1605,
        "ephemeral_1h_input_tokens": 0
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

_source line 59 · 2026-05-22T07:39:22.883Z_

<details><summary>↩ Tool result · `toolu_01K1dddTA6x3aQh1TPSusTo7`</summary>

```text
=== exp_037_wide_critic_cheetah ===
Status: DONE
Conclusion: negative
Metrics: {
  "civo_alert": 0,
  "eval_return_final": 146.1,
  "eval_return_peak": 350.1,
  "gate_dt_2_frac": 1,
  "nve_final": 0.1,
  "nve_peak": 3.6,
  "steps": 224000
}

=== Baseline data ===
baseline field: null

=== exp_018_full_sgs_walker_s1 full details ===
Conclusion: killed
Metrics: {
  "eval_return_final": 915.7,
  "eval_return_final_step": 105000,
  "eval_return_peak": 915.7,
  "eval_return_peak_step": 105000,
  "nve_peak": 0.72,
  "nve_peak_step": 75000,
  "nve_sustained_avg": 0.55,
  "nve_sustained_max": 0.72,
  "total_steps": 112000,
  "train_return_final_avg": 899.4,
  "value_mean_final": 601.1
}

=== exp_020_vanilla_dreamerv3_s2 ===
Conclusion: success
Metrics: {
  "collapse": false,
  "comparison_with_parent": {
    "c6_confirmed": true,
    "delta": "vanilla stable (836.5) vs trained dt_emb collapsed (136.96)",
    "parent_collapsed": true,
    "parent_eval_105K": 136.96,
    "parent_id": "exp_008e_v3_walker_s2",
    "parent_nve_105K": 3.78
  },
  "eval_trajectory": [
    {
      "eval_return": 41.2,
      "step": 5000
    },
    {
      "eval_return": 534.1,
      "step": 55000
    },
    {
      "eval_return": 688.9,
      "step": 65000
    },
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "7a874c54-806a-4746-abd6-a504c2f2652e"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a34472194c71ae4ba",
  "tool_use_id": "toolu_01FM7bPFxXDs3g11zr1WuHms",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry experiment data",
  "usage": {
    "total_tokens": 38549,
    "tool_uses": 9,
    "duration_ms": 181683
  },
  "uuid": "cf241977-10ea-41dd-9d80-96ded7d80525",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e"
}
```

---

### Tool result

_source line 61 · 2026-05-22T07:40:47.833Z_

<details><summary>↩ Tool result · `toolu_01FM7bPFxXDs3g11zr1WuHms`</summary>

```text
Here is the structured summary:

---

## Experiment Data Extraction Summary

### 1. DUAL-CRITIC EXPERIMENTS

**exp_032 (Walker s0)** -- Status: DONE, Conclusion: **success**
- Eval final: 739.7 (peak 787.7 @205K), vs baseline 900 = 87.5%
- NVE final: 0.1, NVE peak: 1.1 @95K
- CIVO prevented: yes (2/2 seeds). Gate locked at dt=2 (entropy=0). v1-v2 gap <0.1% -- min operation has no pessimism effect; mechanism is implicit value regularization.

**exp_032b (Walker s1)** -- Status: DONE, Conclusion: **success**
- Eval final: 516 (peak 552 @205K), vs baseline = 57%
- NVE final: 0.1. CIVO suppressed (NVE<1.5 throughout).
- Eval trajectory: 75K=241, 105K=228, 155K=361, 195K=544, 205K=552, 215K=516. Low absolute eval attributed to gate collapse (dt=2 locked), not dual-critic failure. Director override: success for CIVO suppression criterion.

**exp_033 (Wide single critic Walker ablation)** -- Status: DONE, Conclusion: **success** (as ablation)
- Eval final: 407.9, peak: 194.8, trough: 31.8
- VE ratio peak: 4.7, CIVO alert @105K (ve_ratio 1.958)
- Critic params: 2.89M. CIVO instability duration: 75K steps. Wide single critic does NOT prevent CIVO, confirming dual-critic min-operation is the key mechanism, not parameter count.

**exp_034 / exp_034_dual_critic_cheetah (Cheetah s0)** -- Status: DONE, Conclusion: **negative**
- Eval final: 97.5 (peak 315.7 @45K), vs peak = 31%
- NVE final: 0.144, NVE max: 1.753
- CIVO prevented: NO. Dual-wave CIVO triggered @55K and @105K. v1-v2 gap <0.2 -- min operation has no pessimism effect in Cheetah either. Dual-critic fails to prevent CIVO on Cheetah.

**exp_035 (Narrow dual-critic Walker s0)** -- Status: DONE, Conclusion: **success** (director override)
- Eval final: 697.8 (trough 33.8 @85K, recovery to 697.8 @215K)
- NVE final: 0.066, NVE peak: 2.75 @85K
- CIVO not prevented but RECOVERED (33.8 -> 697.8). Director ruled success: recovery is the criterion. Narrow dual-critic isolates min-operation effect from parameter count.

**exp_036 (Dual-critic PickCube)** -- Status: DONE, Conclusion: **negative**
- Eval final: 27.7 (peak 27.7), steps: 212K
- NVE final: 0.2, NVE peak: 2.3. Gate dt=2, entropy=0.
- Dual-critic fails on PickCube -- no improvement over baseline.

**exp_038 (Walker s2)** -- Status: DONE, Conclusion: **negative**
- Eval final: 120.9 (peak 354 @155K, collapse to 99.6 @175K)
- NVE final: 0.248, NVE peak: 0.3
- CIVO prevented (NVE<=0.3) but **non-CIVO eval collapse** at 175K. Different failure mode from value overestimation. Gate dt=2 locked.

**exp_039 (Narrow dual-critic Walker s1)** -- Status: DONE, Conclusion: **success**
- Eval final: 592.7
- NVE peak: 2.19. CIVO triggered then recovered. s0=697.8, s1=592.7, mean~645. Recovery confirmed 2/2 seeds.

**exp_040 (Wide dual-critic Cheetah s1)** -- Status: **RUNNING**
- Target: 210K steps. Server: bjb1-45299, GPU cuda:0
- Submitted: 2026-05-21T19:51, last updated: 2026-05-22T06:13

**exp_041 (Dual-critic Walker s3)** -- Status: **RUNNING**
- Target: 210K steps. Server: bjb1-45299, GPU cuda:1
- Submitted: 2026-05-22T02:38, last updated: 2026-05-22T06:16
- Purpose: determine if exp_038 non-CIVO collapse is sporadic (1/4) or systematic (2/4)

**exp_037 (Wide critic Cheetah ablation)** -- DONE, Conclusion: **negative**
- Eval final: 146.1 (peak 350.1), NVE peak: 3.6, NVE final: 0.1

### 2. FROZEN DT_EMB

**exp_042 (Frozen dt_emb Walker)** -- Status: **RUNNING**
- Target: 210K steps. Server: bjb1-40020, GPU cuda:0
- Submitted: 2026-05-22T02:14, last updated: 2026-05-22T03:42
- Hypothesis: dt_embedding training (not mere existence) is necessary for CIVO. Freezing dt_emb (random init, requires_grad=False) should prevent CIVO.

### 3. 008f REPLICATION

**exp_043 (008f Walker s1)** -- Status: **RUNNING**
- Target: 210K steps. Server: bjb1-40020, GPU cuda:1
- Submitted: 2026-05-22T02:36, last updated: 2026-05-22T03:42
- Purpose: replicate 008f causal control (dt_embed_dim=0, subsample ON, H=8) with seed 1 to confirm "dt_emb absence prevents CIVO" is robust cross-seed.

### 4. CHEETAH EXPERIMENTS

**exp_010a (Cheetah baseline s1)** -- Status: DONE, Conclusion: **success**
- Eval final: 849.8 @515K (peak = final), train return: 716
- Healthy baseline established for Cheetah Run.

**exp_010b (Cheetah CIVO trigger s1)** -- Status: DONE, Conclusion: **success**
- Eval final: 51.7 (peak 321.9 @35K)
- NVE peak: 8.27 @65K. CIVO confirmed on Cheetah.

**exp_010b_cheetah_civo_trigger_s0** -- DONE, Conclusion: **success**
- Eval peak: 247.77 @35K, eval @105K: 0.83 (complete collapse)
- NVE @95K: 6.34, NVE @105K: 70.64. Catastrophic CIVO confirmed.

### 5. PICKCUBE EXPERIMENTS

**exp_019a (PickCube baseline)** -- killed; replaced by **exp_019a_v2**
- exp_019a_v2: DONE, success. Eval final: 69.43 (peak 69.7 @162.5K). VE ratio range 1.05-3.56. Baseline established.

**exp_019b (PickCube CIVO trigger)** -- Status: DONE, Conclusion: **success**
- Eval final: 26.64 (peak 26.9), vs baseline 58.56 = 45.5%
- NVE peak: 3.78 @52.5K, NVE final: 0.065
- Pattern: transient CIVO then value collapse. Value mean collapsed from baseline 144.57 to 4.26.

### 6. CIVO BASELINE (008d/008a/008f family)

**exp_008d (CIVO trigger, original)** -- killed early @40K. Eval declining: 153.7 -> 167.2 -> 146.3. VE ratio 41.1% @35K and rising.

**exp_008d_subsample_on_h8** -- DONE, **success**. Classic CIVO confirmation.
- Eval: 167 -> 146 -> 141 -> 82.75 (declining). VE ratio accelerating: 15.5% -> 41.2% -> 69.3% -> 166.7%. Delusional critic collapse confirmed.

**exp_008d_civo_trigger_s3** -- DONE, **success**
- Eval final: 267.6 @105K (peak 451.7 @95K). NVE final: 1.53, NVE onset @45K. Late-onset collapse. vs baseline -70.8%.

**exp_008d_civo_trigger_s4** -- DONE, **success**
- Eval final: 63.6 @105K (peak 383.3 @85K). VE ratio @105K: 3.03. CIVO confirmed.

**exp_008a (unexposed dt_emb, subsample OFF)** -- killed early; extended by sub-experiments:
- **exp_008a_no_subsample_dt2**: DONE, success. Eval @105K: 777.66. NVE @105K: 0.59. No collapse. Subsample OFF + trained dt_emb (unexposed) = safe.
- **exp_008a_unexposed_s1**: DONE, success. Eval final: 630.91 @105K. VE ratio 0.43. No CIVO.
- **exp_008a_unexposed_s2**: DONE, success. Eval final: 899.4 @105K. VE ratio 0.333. No CIVO.
- **exp_008a_cheetah_unexposed_s0**: DONE, success. Eval @105K: 532.35, NVE 0.49. Cross-env validated.
- **exp_008a_cheetah_unexposed_s1**: DONE, success. Eval @105K: 504.38, NVE 0.478. Cross-env validated.

**exp_008f (no dt_emb, subsample ON)** -- DONE, **success**
- Eval @105K: 503. NVE @105K: 0.3. Causal conclusion: without dt_embedding, value self-corrects.
- **exp_008f_s3**: DONE, success. Eval final: 363.8. NVE peak <1.5x. No collapse.
- **exp_008f_s4**: DONE, negative (low eval 306.5 but no CIVO). NVE peak: 1.41 @85K (transient), settles to 0.58 @105K.

### 7. GRADIENT STOPPING (SGS)

**exp_016e (Reward-head SGS, Walker s1)** -- Status: DONE, Conclusion: **negative**
- CIVO detected, severity: catastrophic. NVE peak: 10.42 @95K. Onset @85K.
- Reward-head-only gradient stop is insufficient. Actor loss sign flip @95K.

**exp_018_full_sgs_walker_s1** -- DONE, killed (but has data)
- Eval final: 915.7 @105K. NVE peak: 0.72 @75K, sustained avg: 0.55.
- Full SGS appears to work on Walker s1 (no CIVO, high eval).

**exp_018v2_full_sgs_walker_s1** -- DONE, **negative**
- Eval final: 448.3 @105K (peak 499.6 @75K). NVE peak: 1.66 @95K, NVE mean 45K-105K: 1.23.
- CIVO reduction: 79% but late collapse detected @112K. Partial success only.

**exp_018_full_sgs_s2** -- DONE, **negative**. No metrics recorded.

**exp_021 (Full SGS Cheetah s1)** -- DONE, **negative**
- Eval final: 221.5 (vs 010b baseline: 51.7, so 4.3x better). But CIVO still occurred (transient self-correcting type).
- NVE peak: 9.94 @45K, sustained 55K-105K: 0.338. Baseline pct: 38.7%.

**exp_025 (Obs-decoder SGS, Walker)** -- 4 seeds, all **failed**
- s1: failed. s2: negative (eval @215K: 89.6, VE ratio fluctuating 0.8-1.4). s3: failed. s4: failed.
- Obs-decoder-only SGS does not work.

**exp_026 (Obs-decoder SGS, Cheetah)** -- 2 seeds, both **failed**
- s0: failed. s1: failed. Cross-environment confirmation: obs-decoder SGS is ineffective.

### 8. ALL RUNNING EXPERIMENTS (4 total)

| ID | Server | GPU | Target Steps | Submitted | Purpose |
|----|--------|-----|-------------|-----------|---------|
| exp_040 | bjb1-45299 | cuda:0 | 210K | May 21 19:51 | Cheetah dual-critic s1 |
| exp_041 | bjb1-45299 | cuda:1 | 210K | May 22 02:38 | Walker dual-critic s3 (collapse check) |
| exp_042 | bjb1-40020 | cuda:0 | 210K | May 22 02:14 | Frozen dt_emb causality test |
| exp_043 | bjb1-40020 | cuda:1 | 210K | May 22 02:36 | 008f replication s1 |

No step-count progress is recorded in the registry for the running experiments. All were submitted within the last ~28 hours and have target of 210K steps each.

---

**Key takeaways for rebuttal:**
- **Dual-critic prevents CIVO on Walker** (3/3 seeds NVE<1.5, though s2 had non-CIVO collapse), **fails on Cheetah and PickCube**.
- **Narrow dual-critic** shows CIVO recovery (2/2 seeds, mean eval ~645), confirming min-operation drives recovery.
- **Wide single critic** does NOT prevent CIVO -- ruling out parameter-count explanation.
- **CIVO trigger is robust**: confirmed across Walker (4+ seeds), Cheetah (2 seeds, NVE up to 70.64), PickCube (NVE 3.78).
- **No dt_emb = no CIVO**: 008f family (4 seeds) all show NVE<1.5, establishing trained dt_emb as necessary causal factor.
- **Unexposed dt_emb = no CIVO**: 008a family (Walker 3 seeds, Cheetah 2 seeds) all safe.
- **SGS interventions**: Reward-only SGS fails. Full SGS partially works (79% reduction, inconsistent across seeds). Obs-decoder SGS fails completely (6/6 seeds failed).

agentId: a34472194c71ae4ba (use SendMessage with to: 'a34472194c71ae4ba' to continue this agent)
&lt;usage>total_tokens: 42106
tool_uses: 9
duration_ms: 181686&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "01c6eb51-f134-47aa-a0aa-ec9b55484404",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to extract specific experiment data from a large JSON registry file for a rebuttal draft. The file is at:\n\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7099b989-f5c3-4806-9b9b-a499172a4b8e/tool-results/mcp-agent-ml-research-read_registry-1779435443187.txt\n\nThis is JSON with schema: {result: string}. The \"result\" field is itself a JSON string that needs to be parsed.\n\nI need you to extract and return a structured summary of the following experiments. For each, provide: exp_id, status, conclusion, key metrics (eval, NVE, etc.), and any relevant notes:\n\n1. **Dual-critic experiments**: exp_032, exp_032b, exp_033, exp_034, exp_035, exp_036, exp_038, exp_039, exp_040, exp_041\n2. **Frozen dt_emb**: exp_042\n3. **008f replication**: exp_043\n4. **Cheetah experiments**: exp_010a, exp_010b\n5. **PickCube experiments**: exp_019a, exp_019b\n6. **CIVO baseline**: exp_008d, exp_008a, exp_008f\n7. **Gradient stopping**: exp_016e, exp_018, exp_021, exp_025, exp_026\n8. **RUNNING experiments**: any with status=RUNNING - give current step count if available\n\nUse jq or python to parse and extract. Give me a comprehensive but concise summary - include actual numbers for eval scores, NVE values, and any key metrics. Report under 3000 words.",
    "agentId": "a34472194c71ae4ba",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the structured summary:\n\n---\n\n## Experiment Data Extraction Summary\n\n### 1. DUAL-CRITIC EXPERIMENTS\n\n**exp_032 (Walker s0)** -- Status: DONE, Conclusion: **success**\n- Eval final: 739.7 (peak 787.7 @205K), vs baseline 900 = 87.5%\n- NVE final: 0.1, NVE peak: 1.1 @95K\n- CIVO prevented: yes (2/2 seeds). Gate locked at dt=2 (entropy=0). v1-v2 gap <0.1% -- min operation has no pessimism effect; mechanism is implicit value regularization.\n\n**exp_032b (Walker s1)** -- Status: DONE, Conclusion: **success**\n- Eval final: 516 (peak 552 @205K), vs baseline = 57%\n- NVE final: 0.1. CIVO suppressed (NVE<1.5 throughout).\n- Eval trajectory: 75K=241, 105K=228, 155K=361, 195K=544, 205K=552, 215K=516. Low absolute eval attributed to gate collapse (dt=2 locked), not dual-critic failure. Director override: success for CIVO suppression criterion.\n\n**exp_033 (Wide single critic Walker ablation)** -- Status: DONE, Conclusion: **success** (as ablation)\n- Eval final: 407.9, peak: 194.8, trough: 31.8\n- VE ratio peak: 4.7, CIVO alert @105K (ve_ratio 1.958)\n- Critic params: 2.89M. CIVO instability duration: 75K steps. Wide single critic does NOT prevent CIVO, confirming dual-critic min-operation is the key mechanism, not parameter count.\n\n**exp_034 / exp_034_dual_critic_cheetah (Cheetah s0)** -- Status: DONE, Conclusion: **negative**\n- Eval final: 97.5 (peak 315.7 @45K), vs peak = 31%\n- NVE final: 0.144, NVE max: 1.753\n- CIVO prevented: NO. Dual-wave CIVO triggered @55K and @105K. v1-v2 gap <0.2 -- min operation has no pessimism effect in Cheetah either. Dual-critic fails to prevent CIVO on Cheetah.\n\n**exp_035 (Narrow dual-critic Walker s0)** -- Status: DONE, Conclusion: **success** (director override)\n- Eval final: 697.8 (trough 33.8 @85K, recovery to 697.8 @215K)\n- NVE final: 0.066, NVE peak: 2.75 @85K\n- CIVO not prevented but RECOVERED (33.8 -> 697.8). Director ruled success: recovery is the criterion. Narrow dual-critic isolates min-operation effect from parameter count.\n\n**exp_036 (Dual-critic PickCube)** -- Status: DONE, Conclusion: **negative**\n- Eval final: 27.7 (peak 27.7), steps: 212K\n- NVE final: 0.2, NVE peak: 2.3. Gate dt=2, entropy=0.\n- Dual-critic fails on PickCube -- no improvement over baseline.\n\n**exp_038 (Walker s2)** -- Status: DONE, Conclusion: **negative**\n- Eval final: 120.9 (peak 354 @155K, collapse to 99.6 @175K)\n- NVE final: 0.248, NVE peak: 0.3\n- CIVO prevented (NVE<=0.3) but **non-CIVO eval collapse** at 175K. Different failure mode from value overestimation. Gate dt=2 locked.\n\n**exp_039 (Narrow dual-critic Walker s1)** -- Status: DONE, Conclusion: **success**\n- Eval final: 592.7\n- NVE peak: 2.19. CIVO triggered then recovered. s0=697.8, s1=592.7, mean~645. Recovery confirmed 2/2 seeds.\n\n**exp_040 (Wide dual-critic Cheetah s1)** -- Status: **RUNNING**\n- Target: 210K steps. Server: bjb1-45299, GPU cuda:0\n- Submitted: 2026-05-21T19:51, last updated: 2026-05-22T06:13\n\n**exp_041 (Dual-critic Walker s3)** -- Status: **RUNNING**\n- Target: 210K steps. Server: bjb1-45299, GPU cuda:1\n- Submitted: 2026-05-22T02:38, last updated: 2026-05-22T06:16\n- Purpose: determine if exp_038 non-CIVO collapse is sporadic (1/4) or systematic (2/4)\n\n**exp_037 (Wide critic Cheetah ablation)** -- DONE, Conclusion: **negative**\n- Eval final: 146.1 (peak 350.1), NVE peak: 3.6, NVE final: 0.1\n\n### 2. FROZEN DT_EMB\n\n**exp_042 (Frozen dt_emb Walker)** -- Status: **RUNNING**\n- Target: 210K steps. Server: bjb1-40020, GPU cuda:0\n- Submitted: 2026-05-22T02:14, last updated: 2026-05-22T03:42\n- Hypothesis: dt_embedding training (not mere existence) is necessary for CIVO. Freezing dt_emb (random init, requires_grad=False) should prevent CIVO.\n\n### 3. 008f REPLICATION\n\n**exp_043 (008f Walker s1)** -- Status: **RUNNING**\n- Target: 210K steps. Server: bjb1-40020, GPU cuda:1\n- Submitted: 2026-05-22T02:36, last updated: 2026-05-22T03:42\n- Purpose: replicate 008f causal control (dt_embed_dim=0, subsample ON, H=8) with seed 1 to confirm \"dt_emb absence prevents CIVO\" is robust cross-seed.\n\n### 4. CHEETAH EXPERIMENTS\n\n**exp_010a (Cheetah baseline s1)** -- Status: DONE, Conclusion: **success**\n- Eval final: 849.8 @515K (peak = final), train return: 716\n- Healthy baseline established for Cheetah Run.\n\n**exp_010b (Cheetah CIVO trigger s1)** -- Status: DONE, Conclusion: **success**\n- Eval final: 51.7 (peak 321.9 @35K)\n- NVE peak: 8.27 @65K. CIVO confirmed on Cheetah.\n\n**exp_010b_cheetah_civo_trigger_s0** -- DONE, Conclusion: **success**\n- Eval peak: 247.77 @35K, eval @105K: 0.83 (complete collapse)\n- NVE @95K: 6.34, NVE @105K: 70.64. Catastrophic CIVO confirmed.\n\n### 5. PICKCUBE EXPERIMENTS\n\n**exp_019a (PickCube baseline)** -- killed; replaced by **exp_019a_v2**\n- exp_019a_v2: DONE, success. Eval final: 69.43 (peak 69.7 @162.5K). VE ratio range 1.05-3.56. Baseline established.\n\n**exp_019b (PickCube CIVO trigger)** -- Status: DONE, Conclusion: **success**\n- Eval final: 26.64 (peak 26.9), vs baseline 58.56 = 45.5%\n- NVE peak: 3.78 @52.5K, NVE final: 0.065\n- Pattern: transient CIVO then value collapse. Value mean collapsed from baseline 144.57 to 4.26.\n\n### 6. CIVO BASELINE (008d/008a/008f family)\n\n**exp_008d (CIVO trigger, original)** -- killed early @40K. Eval declining: 153.7 -> 167.2 -> 146.3. VE ratio 41.1% @35K and rising.\n\n**exp_008d_subsample_on_h8** -- DONE, **success**. Classic CIVO confirmation.\n- Eval: 167 -> 146 -> 141 -> 82.75 (declining). VE ratio accelerating: 15.5% -> 41.2% -> 69.3% -> 166.7%. Delusional critic collapse confirmed.\n\n**exp_008d_civo_trigger_s3** -- DONE, **success**\n- Eval final: 267.6 @105K (peak 451.7 @95K). NVE final: 1.53, NVE onset @45K. Late-onset collapse. vs baseline -70.8%.\n\n**exp_008d_civo_trigger_s4** -- DONE, **success**\n- Eval final: 63.6 @105K (peak 383.3 @85K). VE ratio @105K: 3.03. CIVO confirmed.\n\n**exp_008a (unexposed dt_emb, subsample OFF)** -- killed early; extended by sub-experiments:\n- **exp_008a_no_subsample_dt2**: DONE, success. Eval @105K: 777.66. NVE @105K: 0.59. No collapse. Subsample OFF + trained dt_emb (unexposed) = safe.\n- **exp_008a_unexposed_s1**: DONE, success. Eval final: 630.91 @105K. VE ratio 0.43. No CIVO.\n- **exp_008a_unexposed_s2**: DONE, success. Eval final: 899.4 @105K. VE ratio 0.333. No CIVO.\n- **exp_008a_cheetah_unexposed_s0**: DONE, success. Eval @105K: 532.35, NVE 0.49. Cross-env validated.\n- **exp_008a_cheetah_unexposed_s1**: DONE, success. Eval @105K: 504.38, NVE 0.478. Cross-env validated.\n\n**exp_008f (no dt_emb, subsample ON)** -- DONE, **success**\n- Eval @105K: 503. NVE @105K: 0.3. Causal conclusion: without dt_embedding, value self-corrects.\n- **exp_008f_s3**: DONE, success. Eval final: 363.8. NVE peak <1.5x. No collapse.\n- **exp_008f_s4**: DONE, negative (low eval 306.5 but no CIVO). NVE peak: 1.41 @85K (transient), settles to 0.58 @105K.\n\n### 7. GRADIENT STOPPING (SGS)\n\n**exp_016e (Reward-head SGS, Walker s1)** -- Status: DONE, Conclusion: **negative**\n- CIVO detected, severity: catastrophic. NVE peak: 10.42 @95K. Onset @85K.\n- Reward-head-only gradient stop is insufficient. Actor loss sign flip @95K.\n\n**exp_018_full_sgs_walker_s1** -- DONE, killed (but has data)\n- Eval final: 915.7 @105K. NVE peak: 0.72 @75K, sustained avg: 0.55.\n- Full SGS appears to work on Walker s1 (no CIVO, high eval).\n\n**exp_018v2_full_sgs_walker_s1** -- DONE, **negative**\n- Eval final: 448.3 @105K (peak 499.6 @75K). NVE peak: 1.66 @95K, NVE mean 45K-105K: 1.23.\n- CIVO reduction: 79% but late collapse detected @112K. Partial success only.\n\n**exp_018_full_sgs_s2** -- DONE, **negative**. No metrics recorded.\n\n**exp_021 (Full SGS Cheetah s1)** -- DONE, **negative**\n- Eval final: 221.5 (vs 010b baseline: 51.7, so 4.3x better). But CIVO still occurred (transient self-correcting type).\n- NVE peak: 9.94 @45K, sustained 55K-105K: 0.338. Baseline pct: 38.7%.\n\n**exp_025 (Obs-decoder SGS, Walker)** -- 4 seeds, all **failed**\n- s1: failed. s2: negative (eval @215K: 89.6, VE ratio fluctuating 0.8-1.4). s3: failed. s4: failed.\n- Obs-decoder-only SGS does not work.\n\n**exp_026 (Obs-decoder SGS, Cheetah)** -- 2 seeds, both **failed**\n- s0: failed. s1: failed. Cross-environment confirmation: obs-decoder SGS is ineffective.\n\n### 8. ALL RUNNING EXPERIMENTS (4 total)\n\n| ID | Server | GPU | Target Steps | Submitted | Purpose |\n|----|--------|-----|-------------|-----------|---------|\n| exp_040 | bjb1-45299 | cuda:0 | 210K | May 21 19:51 | Cheetah dual-critic s1 |\n| exp_041 | bjb1-45299 | cuda:1 | 210K | May 22 02:38 | Walker dual-critic s3 (collapse check) |\n| exp_042 | bjb1-40020 | cuda:0 | 210K | May 22 02:14 | Frozen dt_emb causality test |\n| exp_043 | bjb1-40020 | cuda:1 | 210K | May 22 02:36 | 008f replication s1 |\n\nNo step-count progress is recorded in the registry for the running experiments. All were submitted within the last ~28 hours and have target of 210K steps each.\n\n---\n\n**Key takeaways for rebuttal:**\n- **Dual-critic prevents CIVO on Walker** (3/3 seeds NVE<1.5, though s2 had non-CIVO collapse), **fails on Cheetah and PickCube**.\n- **Narrow dual-critic** shows CIVO recovery (2/2 seeds, mean eval ~645), confirming min-operation drives recovery.\n- **Wide single critic** does NOT prevent CIVO -- ruling out parameter-count explanation.\n- **CIVO trigger is robust**: confirmed across Walker (4+ seeds), Cheetah (2 seeds, NVE up to 70.64), PickCube (NVE 3.78).\n- **No dt_emb = no CIVO**: 008f family (4 seeds) all show NVE<1.5, establishing trained dt_emb as necessary causal factor.\n- **Unexposed dt_emb = no CIVO**: 008a family (Walker 3 seeds, Cheetah 2 seeds) all safe.\n- **SGS interventions**: Reward-only SGS fails. Full SGS partially works (79% reduction, inconsistent across seeds). Obs-decoder SGS fails completely (6/6 seeds failed)."
      }
    ],
    "totalDurationMs": 181686,
    "totalTokens": 42106,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1233,
      "cache_read_input_tokens": 36970,
      "output_tokens": 3902,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3902,
          "cache_read_input_tokens": 36970,
          "cache_creation_input_tokens": 1233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1233,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 9,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T07:40:47.868Z_

<details><summary>↩ Tool result · `toolu_01SF5qFJDwEpz1GyZiQdXY1G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\", \"content\": \"# event-gated-adaptive-horizon — Research Dashboard\\n\\n> 最后更新: 2026-05-22 03:07 UTC | 更新原因: 4/4 GPU满载确认，exp_040配置修复，Paper Agent Reframe完成\\n\\n> **Target**: CoRL 2026 (DDL 2026-05-29) | **5/25 数据锁定（3天）**\\n\\n## 核心方向\\n**Intervention Hierarchy + Dual-critic 双维度分析**\\n核心贡献：(1) CIVO 因果诊断 (2) 三层干预框架 (3) 2×2 factorial: Prevention(min+cap) + Recovery(min主导) (4) v1≈v2 — Double Q pessimism 失效 (5) 环境依赖性 (6) ⚠️ CIVO prevention ≠ performance stability\\n\\n## 2×2 Mechanism Factorial — Walker（D127-D128）\\n| | Single Critic | Dual Critic (min) |\\n|---|---|---|\\n| ~1.05-1.2M | Baseline: CIVO → 崩溃 | exp_035 s0=697.8, exp_039 s1=592.7 (Recovery 2/2 ✅) |\\n| ~2.4-2.9M | exp_033: CIVO(4.75) → 部分恢复(408) | exp_032: Prevention 3/3, eval 739.7/551.8/120.9 |\\n\\n## 运行中实验（4/4 GPU ✅ 全部 SSH 验证通过）\\n| 实验 | Server:GPU | Step | 目标 |\\n|------|-----------|------|------|\\n| exp_040 Cheetah dual s1 | 45299:0 | 5K | 跨环境 dual-critic 多seed |\\n| exp_041 Walker dual s3 | 45299:1 | 20K | 非CIVO崩溃频率 |\\n| exp_042 frozen dt_emb Walker | 40020:0 | 15K | C2因果：训练vs存在dt_emb |\\n| exp_043 008f Walker s1 | 40020:1 | 15K | 因果控制多seed |\\n\\n预计 5/23-24 全部完成。\\n\\n## 论文状态\\n- Paper Agent Reframe 完成（4-level hierarchy, v1≈v2, 2×2 factorial, Recovery/Prevention 分报）\\n- Patch 模板已准备（exp_040-043 数据到达后一次性更新）\\n- 待数据锁定后提交 Review Director 审查\\n\\n## 近期任务\\n- [x] 2×2 factorial 完成 ✅\\n- [x] exp_039 Recovery 2/2 确认 ✅\\n- [x] 4 GPU 部署修复（exp_040 配置错误解决）✅\\n- [x] Paper Agent Reframe 完成 ✅\\n- [ ] exp_040-043 完成 → 5/25 数据锁定\\n- [ ] Paper Agent 最终 Patch + 提交审查\\n- [ ] 5/29 投稿\\n\\n## GPU 预算\\n4 GPU（bjb1-40020 ×2 + bjb1-45299 ×2），全部满载运行。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D129 | 2026-05-22 | D129: exp_039完成(Recovery 2/2确认) + 4GPU空闲紧急部署：重启exp | exp_039_narrow_dual_critic_walker_s1, exp_040_wide_dual_critic_cheetah, exp_041_dual_critic_walker_s3, exp_042_frozen_dt_emb_walker, exp_043_008f_walker_s1 |\\n| D128 | 2026-05-21 | D128: exp_038 s2 非 CIVO 崩溃 + exp_037 完成。(1) Dual-c | exp_038_dual_critic_walker_s2, exp_037_wide_critic_cheetah, exp_032_dual_critic_walker, exp_034_dual_critic_cheetah |\\n| D127 | 2026-05-21 | D127: exp_035 完成(eval 697.8) — 2×2 双维度结论：Preventio | exp_035_narrow_dual_critic_walker, exp_032_dual_critic_walker, exp_033_wide_critic_walker, exp_034_dual_critic_cheetah |\\n| D126 | 2026-05-21 | D126: exp_035 中期(59.5%) NVE 2.75 → 2×2 结论修正：Min al | exp_035_narrow_dual_critic_walker, exp_032_dual_critic_walker, exp_033_wide_critic_walker |\\n| D125 | 2026-05-21 | exp_034 Cheetah dual-critic 完成 — CIVO 未被预防，部分恢复(31 | exp_034_dual_critic_cheetah, exp_032_dual_critic_walker, exp_033_wide_critic_walker |\\n| D124 | 2026-05-21 | D124: exp_033 wide-critic CIVO→self-repair (NVE 4. | exp_033_wide_critic_walker, exp_032_dual_critic_walker |\\n| D123 | 2026-05-21 | D123: Cheetah dual-critic CIVO triggered + v1≈v2 全 | exp_034_dual_critic_cheetah, exp_033_wide_critic_walker |\\n| D122 | 2026-05-21 | D122: exp_032 s0 完成 (eval 787.7, CIVO 2/2 prevente | exp_032_dual_critic_walker, exp_033_wide_critic_walker, exp_035_narrow_dual_critic_walker |\\n| D121 | 2026-05-21 | D121: exp_032b CIVO prevented (eval 551.8) → 部署 Ch | exp_032b_dual_critic_walker_s1, exp_034_dual_critic_cheetah |\\n| D120 | 2026-05-21 | D120: v1≈v2 发现 → 部署 wide single critic ablation (e | exp_032_dual_critic_walker, exp_032b_dual_critic_walker_s1, exp_033_wide_critic_walker |\\n\\n\\n\\n\", \"total_chars\": 3276, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "03c5653c-85e0-4766-927f-b5e2a09aa782",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\\\", \\\"content\\\": \\\"# event-gated-adaptive-horizon — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-22 03:07 UTC | 更新原因: 4/4 GPU满载确认，exp_040配置修复，Paper Agent Reframe完成\\\\n\\\\n> **Target**: CoRL 2026 (DDL 2026-05-29) | **5/25 数据锁定（3天）**\\\\n\\\\n## 核心方向\\\\n**Intervention Hierarchy + Dual-critic 双维度分析**\\\\n核心贡献：(1) CIVO 因果诊断 (2) 三层干预框架 (3) 2×2 factorial: Prevention(min+cap) + Recovery(min主导) (4) v1≈v2 — Double Q pessimism 失效 (5) 环境依赖性 (6) ⚠️ CIVO prevention ≠ performance stability\\\\n\\\\n## 2×2 Mechanism Factorial — Walker（D127-D128）\\\\n| | Single Critic | Dual Critic (min) |\\\\n|---|---|---|\\\\n| ~1.05-1.2M | Baseline: CIVO → 崩溃 | exp_035 s0=697.8, exp_039 s1=592.7 (Recovery 2/2 ✅) |\\\\n| ~2.4-2.9M | exp_033: CIVO(4.75) → 部分恢复(408) | exp_032: Prevention 3/3, eval 739.7/551.8/120.9 |\\\\n\\\\n## 运行中实验（4/4 GPU ✅ 全部 SSH 验证通过）\\\\n| 实验 | Server:GPU | Step | 目标 |\\\\n|------|-----------|------|------|\\\\n| exp_040 Cheetah dual s1 | 45299:0 | 5K | 跨环境 dual-critic 多seed |\\\\n| exp_041 Walker dual s3 | 45299:1 | 20K | 非CIVO崩溃频率 |\\\\n| exp_042 frozen dt_emb Walker | 40020:0 | 15K | C2因果：训练vs存在dt_emb |\\\\n| exp_043 008f Walker s1 | 40020:1 | 15K | 因果控制多seed |\\\\n\\\\n预计 5/23-24 全部完成。\\\\n\\\\n## 论文状态\\\\n- Paper Agent Reframe 完成（4-level hierarchy, v1≈v2, 2×2 factorial, Recovery/Prevention 分报）\\\\n- Patch 模板已准备（exp_040-043 数据到达后一次性更新）\\\\n- 待数据锁定后提交 Review Director 审查\\\\n\\\\n## 近期任务\\\\n- [x] 2×2 factorial 完成 ✅\\\\n- [x] exp_039 Recovery 2/2 确认 ✅\\\\n- [x] 4 GPU 部署修复（exp_040 配置错误解决）✅\\\\n- [x] Paper Agent Reframe 完成 ✅\\\\n- [ ] exp_040-043 完成 → 5/25 数据锁定\\\\n- [ ] Paper Agent 最终 Patch + 提交审查\\\\n- [ ] 5/29 投稿\\\\n\\\\n## GPU 预算\\\\n4 GPU（bjb1-40020 ×2 + bjb1-45299 ×2），全部满载运行。\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D129 | 2026-05-22 | D129: exp_039完成(Recovery 2/2确认) + 4GPU空闲紧急部署：重启exp | exp_039_narrow_dual_critic_walker_s1, exp_040_wide_dual_critic_cheetah, exp_041_dual_critic_walker_s3, exp_042_frozen_dt_emb_walker, exp_043_008f_walker_s1 |\\\\n| D128 | 2026-05-21 | D128: exp_038 s2 非 CIVO 崩溃 + exp_037 完成。(1) Dual-c | exp_038_dual_critic_walker_s2, exp_037_wide_critic_cheetah, exp_032_dual_critic_walker, exp_034_dual_critic_cheetah |\\\\n| D127 | 2026-05-21 | D127: exp_035 完成(eval 697.8) — 2×2 双维度结论：Preventio | exp_035_narrow_dual_critic_walker, exp_032_dual_critic_walker, exp_033_wide_critic_walker, exp_034_dual_critic_cheetah |\\\\n| D126 | 2026-05-21 | D126: exp_035 中期(59.5%) NVE 2.75 → 2×2 结论修正：Min al | exp_035_narrow_dual_critic_walker, exp_032_dual_critic_walker, exp_033_wide_critic_walker |\\\\n| D125 | 2026-05-21 | exp_034 Cheetah dual-critic 完成 — CIVO 未被预防，部分恢复(31 | exp_034_dual_critic_cheetah, exp_032_dual_critic_walker, exp_033_wide_critic_walker |\\\\n| D124 | 2026-05-21 | D124: exp_033 wide-critic CIVO→self-repair (NVE 4. | exp_033_wide_critic_walker, exp_032_dual_critic_walker |\\\\n| D123 | 2026-05-21 | D123: Cheetah dual-critic CIVO triggered + v1≈v2 全 | exp_034_dual_critic_cheetah, exp_033_wide_critic_walker |\\\\n| D122 | 2026-05-21 | D122: exp_032 s0 完成 (eval 787.7, CIVO 2/2 prevente | exp_032_dual_critic_walker, exp_033_wide_critic_walker, exp_035_narrow_dual_critic_walker |\\\\n| D121 | 2026-05-21 | D121: exp_032b CIVO prevented (eval 551.8) → 部署 Ch | exp_032b_dual_critic_walker_s1, exp_034_dual_critic_cheetah |\\\\n| D120 | 2026-05-21 | D120: v1≈v2 发现 → 部署 wide single critic ablation (e | exp_032_dual_critic_walker, exp_032b_dual_critic_walker_s1, exp_033_wide_critic_walker |\\\\n\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 3276, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\", \"content\": \"# event-gated-adaptive-horizon — Research Dashboard\\n\\n> 最后更新: 2026-05-22 03:07 UTC | 更新原因: 4/4 GPU满载确认，exp_040配置修复，Paper Agent Reframe完成\\n\\n> **Target**: CoRL 2026 (DDL 2026-05-29) | **5/25 数据锁定（3天）**\\n\\n## 核心方向\\n**Intervention Hierarchy + Dual-critic 双维度分析**\\n核心贡献：(1) CIVO 因果诊断 (2) 三层干预框架 (3) 2×2 factorial: Prevention(min+cap) + Recovery(min主导) (4) v1≈v2 — Double Q pessimism 失效 (5) 环境依赖性 (6) ⚠️ CIVO prevention ≠ performance stability\\n\\n## 2×2 Mechanism Factorial — Walker（D127-D128）\\n| | Single Critic | Dual Critic (min) |\\n|---|---|---|\\n| ~1.05-1.2M | Baseline: CIVO → 崩溃 | exp_035 s0=697.8, exp_039 s1=592.7 (Recovery 2/2 ✅) |\\n| ~2.4-2.9M | exp_033: CIVO(4.75) → 部分恢复(408) | exp_032: Prevention 3/3, eval 739.7/551.8/120.9 |\\n\\n## 运行中实验（4/4 GPU ✅ 全部 SSH 验证通过）\\n| 实验 | Server:GPU | Step | 目标 |\\n|------|-----------|------|------|\\n| exp_040 Cheetah dual s1 | 45299:0 | 5K | 跨环境 dual-critic 多seed |\\n| exp_041 Walker dual s3 | 45299:1 | 20K | 非CIVO崩溃频率 |\\n| exp_042 frozen dt_emb Walker | 40020:0 | 15K | C2因果：训练vs存在dt_emb |\\n| exp_043 008f Walker s1 | 40020:1 | 15K | 因果控制多seed |\\n\\n预计 5/23-24 全部完成。\\n\\n## 论文状态\\n- Paper Agent Reframe 完成（4-level hierarchy, v1≈v2, 2×2 factorial, Recovery/Prevention 分报）\\n- Patch 模板已准备（exp_040-043 数据到达后一次性更新）\\n- 待数据锁定后提交 Review Director 审查\\n\\n## 近期任务\\n- [x] 2×2 factorial 完成 ✅\\n- [x] exp_039 Recovery 2/2 确认 ✅\\n- [x] 4 GPU 部署修复（exp_040 配置错误解决）✅\\n- [x] Paper Agent Reframe 完成 ✅\\n- [ ] exp_040-043 完成 → 5/25 数据锁定\\n- [ ] Paper Agent 最终 Patch + 提交审查\\n- [ ] 5/29 投稿\\n\\n## GPU 预算\\n4 GPU（bjb1-40020 ×2 + bjb1-45299 ×2），全部满载运行。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D129 | 2026-05-22 | D129: exp_039完成(Recovery 2/2确认) + 4GPU空闲紧急部署：重启exp | exp_039_narrow_dual_critic_walker_s1, exp_040_wide_dual_critic_cheetah, exp_041_dual_critic_walker_s3, exp_042_frozen_dt_emb_walker, exp_043_008f_walker_s1 |\\n| D128 | 2026-05-21 | D128: exp_038 s2 非 CIVO 崩溃 + exp_037 完成。(1) Dual-c | exp_038_dual_critic_walker_s2, exp_037_wide_critic_cheetah, exp_032_dual_critic_walker, exp_034_dual_critic_cheetah |\\n| D127 | 2026-05-21 | D127: exp_035 完成(eval 697.8) — 2×2 双维度结论：Preventio | exp_035_narrow_dual_critic_walker, exp_032_dual_critic_walker, exp_033_wide_critic_walker, exp_034_dual_critic_cheetah |\\n| D126 | 2026-05-21 | D126: exp_035 中期(59.5%) NVE 2.75 → 2×2 结论修正：Min al | exp_035_narrow_dual_critic_walker, exp_032_dual_critic_walker, exp_033_wide_critic_walker |\\n| D125 | 2026-05-21 | exp_034 Cheetah dual-critic 完成 — CIVO 未被预防，部分恢复(31 | exp_034_dual_critic_cheetah, exp_032_dual_critic_walker, exp_033_wide_critic_walker |\\n| D124 | 2026-05-21 | D124: exp_033 wide-critic CIVO→self-repair (NVE 4. | exp_033_wide_critic_walker, exp_032_dual_critic_walker |\\n| D123 | 2026-05-21 | D123: Cheetah dual-critic CIVO triggered + v1≈v2 全 | exp_034_dual_critic_cheetah, exp_033_wide_critic_walker |\\n| D122 | 2026-05-21 | D122: exp_032 s0 完成 (eval 787.7, CIVO 2/2 prevente | exp_032_dual_critic_walker, exp_033_wide_critic_walker, exp_035_narrow_dual_critic_walker |\\n| D121 | 2026-05-21 | D121: exp_032b CIVO prevented (eval 551.8) → 部署 Ch | exp_032b_dual_critic_walker_s1, exp_034_dual_critic_cheetah |\\n| D120 | 2026-05-21 | D120: v1≈v2 发现 → 部署 wide single critic ablation (e | exp_032_dual_critic_walker, exp_032b_dual_critic_walker_s1, exp_033_wide_critic_walker |\\n\\n\\n\\n\", \"total_chars\": 3276, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the round_1 review report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "3bfef625-8010-4314-894d-039530e07667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5cqEcVbguMu9HKHZyXBhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6740,
      "cache_read_input_tokens": 59987,
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

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01AopYcfTfiWT26hN7fYRPjG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "7d09dd54-6375-4283-9086-ac0194110f87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5cqEcVbguMu9HKHZyXBhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6740,
      "cache_read_input_tokens": 59987,
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

_source line 65 · 2026-05-22T07:40:53.041Z_

<details><summary>↩ Tool result · `toolu_01AopYcfTfiWT26hN7fYRPjG`</summary>

```text
1	---
2	round: 1
3	overall_score: strong reject
4	timestamp: 2026-05-15T12:43:17.705786+00:00
5	reviewer_ids: [1, 2, 3]
6	cross_response_reviewer_ids: [1, 2, 3]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 1
11	
12	**论文**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
13	**目标 Venue**: CoRL 2026 Main Conference
14	**审稿日期**: 2026-05-15
15	**Reviewer 编排**: 3 人（R1: 方法严谨性 & 实验设计 | R2: 新颖性 & 贡献度 & Venue Fit | R3: 格式合规 & 写作质量）
16	**轮次**: Round 1 初审 + 交叉分享（1 轮收敛）
17	
18	---
19	
20	## Summary
21	
22	本文通过 factorial ablation 分析 DreamerV3 中 variable-rate imagination 的失败原因。在 Walker Walk (DMC) 上测试 9 组配置（2-3 seeds each），识别出 trained dt-embedding 导致 RSSM reward head 产生 2.78× 跨时间尺度预测偏差，critic 通过 imagination bootstrapping 将其内化为系统性高估——称为 conditioning-induced value overestimation (CIVO)。论文进一步发现同一 trigger 产生三种随机下游结果（full collapse / self-correction / oscillatory degradation），且限制 imagination 到 dt=1 不能完全防止崩溃（存在 non-CIVO Pathway B）。与 TAWM (MPC-based) 的对比将 feedback architecture 定位为关键结构差异。
23	
24	---
25	
26	## Strengths
27	
28	1. **清晰的问题定义和切入点**：将 "为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败" 作为核心问题，切入角度明确且有实际意义（3/3 reviewer 认可）
29	2. **结构化的 factorial 设计**：trained vs untrained vs removed embedding 的三向对比是方法论亮点，核心对照 008d vs 008f 在控制变量上是干净的（R3 在交叉回应中澄清）
30	3. **CIVO 机制描述细致**：四阶段反馈回路描述清晰，三种 post-CIVO 结果的刻画有信息量
31	4. **Multiple pathways 发现 (F6)**：Pathway A (value-driven) 和 Pathway B (eval-driven) 的识别是 genuine discovery，表明问题比单一 value overestimation 更深层（3/3 认可为论文最有价值的 insight）
32	5. **写作质量高**：F1-F6 因果链式叙述清晰，Figure/Table 信息密度高，术语定义到位（Clarity 获三位 reviewer 最高分 4/5 或 7/10）
33	6. **诚实的 Limitations**：承认单环境和单架构局限，F6 的 partial falsification 展示良好科学态度
34	
35	---
36	
37	## Weaknesses（按严重性排序）
38	
39	### Critical（影响接收决定）
40	
41	**W-C1. CoRL Venue Fit 严重不足 [3/3 reviewer 共识，最强共识]**
42	全文仅在 DMC Walker Walk（proprioceptive observations）上做实验，无任何 robotics benchmark（RoboSuite/ManiSkill/IsaacGym）、无 real-robot 实验、无 robotics application 讨论。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。CoRL CFP 明确要求 "Submissions should focus on a core robotics problem"——当前论文不满足这一硬约束，存在 desk reject 风险。
43	
44	**W-C2. 统计检验力严重不足 [3/3 reviewer 共识]**
45	核心因果声明 "trained dt-embedding is the causal factor" 依赖 n=2 per group 的 factorial 比较。"4/4 separating power" 在随机零假设下 P=1/16≈6.25%，未达 p<0.05 且未做多重比较修正。论文引用 Agarwal et al. (2021) 辩护 per-seed reporting，但该文的核心论点恰恰是需要更多 seeds + IQM 等稳健统计量。语言中频繁使用 "causal factor"、"triggers"、"necessary and sufficient" 等因果措辞，与 n=2 的证据强度严重不匹配。
46	
47	**W-C3. 单环境（Walker Walk）局限使因果声明不可泛化 [3/3 reviewer 共识]**
48	Walker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action, dense reward）。CIVO 的 2.78× reward gap 可能高度依赖：(a) 低维动力学的高 RSSM fidelity（baseline reward MAE 仅 0.0102）；(b) dense reward 下 critic 获得频繁真实信号；(c) proprioceptive observations 无 representation bottleneck。在 sparse reward、高维视觉、contact-rich dynamics 环境下，CIVO 可能表现完全不同或不出现。Section 6.6 的 "structural incompatibility" 声明在没有多环境验证下是过度泛化。
49	
50	**W-C4. NVE 阈值 1.5× 为 post-hoc 选择 [3/3 reviewer 共识]**
51	1.5× 阈值未说明选择依据（pre-registered vs data-driven）。数据显示 [1.2, 2.0] 范围内任何阈值均可达到类似分类效果，强烈暗示 post-hoc 选择。"88.9% accuracy" 是在训练集上的准确率，无 held-out 验证、cross-validation 或 sensitivity analysis。将 post-hoc 指标阈值包装为 "separating power" 可能误导后续研究者。
52	
53	**W-C5. 未使用 CoRL 2026 官方 PMLR 模板 [2/3 reviewer 列为 critical]**
54	论文使用 `\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 geometry（0.75in margins），完全不符合 CoRL 2026 要求的 PMLR 模板（`\usepackage[final]{corl_2026}`）。这构成 desk reject 的独立理由。换模板后正文极可能超过 8 页限制。
55	
56	### Warning（影响评分但不一票否决）
57	
58	**W-W1. 纯诊断负面结果缺乏 actionable solution [2/3 reviewer 共识，1/3 partial disagreement]**
59	论文 Section 6.6 提出三个 future directions（hierarchical abstraction、embedding regularization、transformer extension），全部 "leave to future work"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。R3 部分反驳：论文有 NVE 框架、CIVO 机制分析、MPC vs imagination 架构对比等诊断贡献，类似 Henderson et al. (2018) 的模式。但三位 reviewer 均同意：对 CoRL 这个偏重实际 solution 的 venue，纯诊断贡献度偏低。
60	
61	**W-W2. 与 TAWM 的对比缺乏实证 [3/3 reviewer 共识]**
62	Section 6.3 关于 MPC 免疫性的解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2 验证。TD-MPC2 与 DreamerV3 的多重差异（连续 vs 离散 latent、training objective 等）可能 confound 对比。
63	
64	**W-W3. 105K vs 505K 训练步数不对等 [3/3 reviewer 共识]**
65	Baseline 运行 505K 展示完整收敛，treatment 仅 105K。Self-correcting seed 009b（eval 267.9@105K = baseline 的 29%）可能只是 slower collapse 而非真正的 self-correction。Oscillatory seed 009e 的长期命运未知。
66	
67	**W-W4. Pathway B 解释不充分 [2/3 AGREE, 1/3 partial REBUT]**
68	008e_v3 seed 2 的 non-CIVO collapse 仅有 1 个 seed 的证据。论文用 baseline seed 2 (009a) 的稳定性排除 seed fragility（R2 认为此 control 有一定价值），但未排除 subsampling data augmentation 等引入的普通 training instability。Pathway B 的特征（entropy increase, eval-driven）与已知 plasticity loss / capacity collapse 的区分不够清晰。
69	
70	**W-W5. RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性 [3/3 AGREE]**
71	Table 4 的 reward MAE 不区分 over- vs under-prediction。CIVO 机制假设 reward head "systematically overpredicts rewards at dt=2"，但 MAE=0.1579 可能是双向误差。需 signed error 验证方向性。
72	
73	**W-W6. CIVO 与已知 value overestimation 的区分不够清晰 [R2 提出，R1/R3 partial REBUT]**
74	R2 认为 CIVO 可能只是 compounding model error 的实例化。R1 和 R3 均 partial REBUT：trained vs untrained embedding 对比（008a/008c nve<0.6× vs 008d nve=4.12×）提供了超越 generic compounding error 的机制特异性——如果仅是 compounding error，untrained embedding + dt=2 也应出现 overestimation。但论文应更系统地阐述这一区分。
75	
76	**W-W7. Factorial design 部分对比存在混淆 [R1 提出，R3 partial REBUT]**
77	008d vs 008a/008c 的比较同时改变了 embedding、subsampling、horizon 三个因素。R3 澄清：核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅存在于 secondary comparisons。但论文未清晰区分 primary vs secondary comparisons，容易导致误读。
78	
79	**W-W8. Related Work 遗漏 + Bibliography 冗余 [3/3 reviewer 共识]**
80	Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024)、Colas et al. (2018) 均在 .bib 中但未在正文引用，且与论文主题高度相关。77 条 bib entries 中 48 条 orphan，多个占位符 author 字段（splates2025 等）。
81	
82	---
83	
84	## Reviewer Consensus
85	
86	| 问题 | R1 | R2 | R3 | 共识度 |
87	|------|----|----|-----|--------|
88	| CoRL venue fit 不足 | N3 critical | N1 critical | N2 critical | **3/3 一致** |
89	| 统计检验力不足 | N1 critical | 交叉 AGREE | 交叉 AGREE | **3/3 一致** |
90	| 单环境不可泛化 | N4 critical | N2 critical | 交叉 AGREE | **3/3 一致** |
91	| NVE 阈值 post-hoc | N2 critical | W2 warning | 交叉 AGREE | **3/3 一致** |
92	| 模板不合规 | W5 warning | 小问题 | N1 critical | 3/3 提及 |
93	| 缺乏 actionable solution | 交叉 nuance | N3 critical | 交叉 partial REBUT | 2/3 |
94	
95	---
96	
97	## Reviewer Divergence
98	
99	**1. Factorial design 混淆变量（R1-W1）**
100	- R1/R2: AGREE——缺少干净的 trained vs untrained 对比
101	- R3: REBUT——核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅在 secondary comparisons
102	- **Director 判断**：R3 的 REBUT 有理据（Table 1 确认 008d/008f 仅 embedding 不同），但论文确实缺少 untrained+SubON+H=8 的配置来完成完整 factorial grid
103	
104	**2. CIVO 新颖性（R2-W3）**
105	- R2: CIVO 可能只是 compounding model error 的实例化
106	- R1/R3: partial REBUT——trained vs untrained 对比提供了机制特异性，untrained embedding 不触发 overestimation 说明不是 generic compounding error
107	- **Director 判断**：R1/R3 的 REBUT 在技术上合理——CIVO 的 specific trigger（learned co-adaptation between embedding and reward head）超越了 generic compounding error 的解释。但这一区分在论文中应更显式地阐述
108	
109	**3. Pathway B 解释（R1-W3）**
110	- R1/R3: Pathway B 可能是普通 training instability
111	- R2: partial REBUT——baseline seed 2 (009a) 的稳定性提供了部分因果证据
112	- **Director 判断**：baseline control 有一定说服力，但仅 1 个 seed 的证据确实不足以做 "qualitatively distinct pathway" 的强声明
113	
114	---
115	
116	## Questions for Authors
117	
118	1. 是否在其他 DMC 任务上做过任何初步验证？即使不完整的数据也能大幅增强 CIVO 发现的可信度。
119	2. Gradient stopping（阻止 dt-embedding 梯度流向 reward head）作为 mitigation 只需一行代码——为什么未测试？
120	3. Table 4 的 reward MAE 能否补充 signed error（mean error），验证 dt=2 是否为系统性正向偏差？
121	4. TAWM 原文中 Walker Walk 的具体数据是什么？能否直接引用来支撑 MPC vs imagination 的对比论点？
122	5. NVE 阈值 1.5× 在 1.3× 或 2.0× 下的分类结果如何变化？是否做过 sensitivity analysis？
123	6. 008e_v3 seed 2 (Pathway B) 的 actor action distribution 在崩溃前后是否有分析？这对区分 exploration-driven degradation 和 representation corruption 很关键。
124	
125	---
126	
127	## Missing References
128	
129	以下工作存在于 .bib 中但未在正文引用，且与论文主题高度相关：
130	- **Becker-Ehmck et al. (2023)** "Multi-timestep models for Model-based RL" — 直接研究 multi-timestep world model 在 MBRL 中的效果
131	- **Park et al. (2021)** "Time Discretization-Invariant Safe Action Repetition" — time-discretization 对 RL 的影响
132	- **Wang & Beltrame (2024)** "Reinforcement Learning with Elastic Time Steps" — elastic time steps in RL
133	- **Colas et al. (2018)** — seed 数量对 deep RL 结论可靠性的影响，与 N1 直接相关
134	
135	---
136	
137	## External Review (Stanford Agentic Reviewer)
138	
139	外部审稿：未配置（项目中未找到 `external_review.paperreview_ai.enabled: true`）。
140	
141	---
142	
143	## Overall Assessment
144	
145	**评分: Strong Reject (4/10)**
146	**置信度: High (4/5)**
147	
148	三位 Reviewer 评分完全一致（4/4/4），在以下核心问题上形成强共识：
149	
150	1. **CoRL venue fit**（3/3 critical）：论文不满足 CoRL 对 robot learning 的 scope 要求，存在 desk reject 风险
151	2. **统计基础**（3/3 一致）：2-3 seeds 无法支撑因果声明，NVE 阈值 post-hoc
152	3. **单环境泛化性**（3/3 一致）：Walker Walk 一个环境的诊断无法支撑 "structural incompatibility" 级别的结论
153	4. **格式合规**（3/3 提及）：未使用 PMLR 模板，独立的 desk reject 理由
154	
155	论文的 factorial 设计思路和 CIVO 机制描述有价值，但在当前形态下存在多个根本性缺陷。
156	
157	**建议**：
158	1. **Venue 选择**：论文更适合 ICML/NeurIPS/ICLR 的 RL track 或 RLC，而非 CoRL。如坚持投 CoRL，需大幅增加 robotics motivation 和 robot-relevant 实验。
159	2. **实验扩展**：至少增加 2-3 个不同复杂度的环境（如 Cheetah Run, Humanoid Walk, 或 manipulation task），每配置 5+ seeds。
160	3. **方法论修正**：(a) 将因果语言弱化为 "strongly associated" 或 "candidate mechanism"；(b) 对 NVE 阈值做 sensitivity analysis 或跨环境验证；(c) 补充 reward signed error 验证 CIVO 方向性假设。
161	4. **增加 actionable 贡献**：实现并测试至少一种 mitigation（如 gradient stopping dt-embedding 对 reward head 的梯度）。
162	5. **格式修正**：切换到目标 venue 官方模板，清理 bibliography。
163	
164	---
165	
166	## Detailed Comments（逐节）
167	
168	### Abstract
169	- 过长且过于技术化（~180 词含大量具体数字）
170	- 缺乏 robotics motivation（对 CoRL 是硬伤）
171	- "88.9% accuracy" 放在 abstract 有误导性（post-hoc in-sample accuracy）
172	
173	### Introduction (Section 1)
174	- 问题定义清晰，从 TAWM 的 MPC 成功切入有效
175	- 但完全没有 robotics framing——需要首段建立 temporal abstraction 对 robot learning 的重要性
176	- "causal factor" 措辞过强
177	
178	### Related Work (Section 2)
179	- 覆盖面合理但有遗漏（Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018 在 bib 中未引用）
180	- DreamerV4 讨论移至 Analysis 而非 Related Work 是合理选择
181	- CIVO 与已知 value overestimation 的区分需更清晰阐述
182	
183	### Methodology (Section 3)
184	- Factorial design 结构良好，Table 1 信息清晰
185	- 核心对照 008d vs 008f 干净（R3 交叉确认），但 secondary comparisons 有混淆
186	- "2--3 seeds" 应直接讨论统计效力局限而非仅在 Limitations 中提及
187	- NVE 阈值选取过程需透明化
188	
189	### Results (Section 5)
190	- F1-F6 的因果链组织出色
191	- Table 2 和 per-seed trajectory 报告方式专业
192	- 但 exp_006/007/005 的 NVE 标注为 "---" 未解释原因
193	- "self-correction" 的标签对 009b（eval 267.9 = baseline 29%）可能过于乐观
194	
195	### Analysis & Discussion (Section 6)
196	- CIVO 四阶段机制描述（6.1）清晰有说服力
197	- Seed divergence 讨论（6.2）引用 Lyle et al. 的 capacity loss 假说有价值
198	- MPC immune 分析（6.3）合理但缺乏实证
199	- dt-Embedding Dilemma（6.4）包装过度——在单环境 + 低 seeds 下，"dilemma" 可能只是 artifact
200	- Multiple Pathways（6.5）是论文最有价值的 section，但 Pathway B 仅 1 seed 证据
201	
202	### Conclusion (Section 7)
203	- Limitations paragraph 内容实质到位，但形式上应提升为独立 section/subsection
204	- Future directions 过于 speculative，缺乏初步验证
205	- Baseline seed 0 "in progress" 不应出现在提交版本中
206	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "14d12a7e-e0a6-4ca2-87bf-a0ae51416c1d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md",
      "content": "---\nround: 1\noverall_score: strong reject\ntimestamp: 2026-05-15T12:43:17.705786+00:00\nreviewer_ids: [1, 2, 3]\ncross_response_reviewer_ids: [1, 2, 3]\nforce_resubmit: False\n---\n\n# 审稿报告 — Round 1\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026 Main Conference\n**审稿日期**: 2026-05-15\n**Reviewer 编排**: 3 人（R1: 方法严谨性 & 实验设计 | R2: 新颖性 & 贡献度 & Venue Fit | R3: 格式合规 & 写作质量）\n**轮次**: Round 1 初审 + 交叉分享（1 轮收敛）\n\n---\n\n## Summary\n\n本文通过 factorial ablation 分析 DreamerV3 中 variable-rate imagination 的失败原因。在 Walker Walk (DMC) 上测试 9 组配置（2-3 seeds each），识别出 trained dt-embedding 导致 RSSM reward head 产生 2.78× 跨时间尺度预测偏差，critic 通过 imagination bootstrapping 将其内化为系统性高估——称为 conditioning-induced value overestimation (CIVO)。论文进一步发现同一 trigger 产生三种随机下游结果（full collapse / self-correction / oscillatory degradation），且限制 imagination 到 dt=1 不能完全防止崩溃（存在 non-CIVO Pathway B）。与 TAWM (MPC-based) 的对比将 feedback architecture 定位为关键结构差异。\n\n---\n\n## Strengths\n\n1. **清晰的问题定义和切入点**：将 \"为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败\" 作为核心问题，切入角度明确且有实际意义（3/3 reviewer 认可）\n2. **结构化的 factorial 设计**：trained vs untrained vs removed embedding 的三向对比是方法论亮点，核心对照 008d vs 008f 在控制变量上是干净的（R3 在交叉回应中澄清）\n3. **CIVO 机制描述细致**：四阶段反馈回路描述清晰，三种 post-CIVO 结果的刻画有信息量\n4. **Multiple pathways 发现 (F6)**：Pathway A (value-driven) 和 Pathway B (eval-driven) 的识别是 genuine discovery，表明问题比单一 value overestimation 更深层（3/3 认可为论文最有价值的 insight）\n5. **写作质量高**：F1-F6 因果链式叙述清晰，Figure/Table 信息密度高，术语定义到位（Clarity 获三位 reviewer 最高分 4/5 或 7/10）\n6. **诚实的 Limitations**：承认单环境和单架构局限，F6 的 partial falsification 展示良好科学态度\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. CoRL Venue Fit 严重不足 [3/3 reviewer 共识，最强共识]**\n全文仅在 DMC Walker Walk（proprioceptive observations）上做实验，无任何 robotics benchmark（RoboSuite/ManiSkill/IsaacGym）、无 real-robot 实验、无 robotics application 讨论。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\"——当前论文不满足这一硬约束，存在 desk reject 风险。\n\n**W-C2. 统计检验力严重不足 [3/3 reviewer 共识]**\n核心因果声明 \"trained dt-embedding is the causal factor\" 依赖 n=2 per group 的 factorial 比较。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，未达 p<0.05 且未做多重比较修正。论文引用 Agarwal et al. (2021) 辩护 per-seed reporting，但该文的核心论点恰恰是需要更多 seeds + IQM 等稳健统计量。语言中频繁使用 \"causal factor\"、\"triggers\"、\"necessary and sufficient\" 等因果措辞，与 n=2 的证据强度严重不匹配。\n\n**W-C3. 单环境（Walker Walk）局限使因果声明不可泛化 [3/3 reviewer 共识]**\nWalker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action, dense reward）。CIVO 的 2.78× reward gap 可能高度依赖：(a) 低维动力学的高 RSSM fidelity（baseline reward MAE 仅 0.0102）；(b) dense reward 下 critic 获得频繁真实信号；(c) proprioceptive observations 无 representation bottleneck。在 sparse reward、高维视觉、contact-rich dynamics 环境下，CIVO 可能表现完全不同或不出现。Section 6.6 的 \"structural incompatibility\" 声明在没有多环境验证下是过度泛化。\n\n**W-C4. NVE 阈值 1.5× 为 post-hoc 选择 [3/3 reviewer 共识]**\n1.5× 阈值未说明选择依据（pre-registered vs data-driven）。数据显示 [1.2, 2.0] 范围内任何阈值均可达到类似分类效果，强烈暗示 post-hoc 选择。\"88.9% accuracy\" 是在训练集上的准确率，无 held-out 验证、cross-validation 或 sensitivity analysis。将 post-hoc 指标阈值包装为 \"separating power\" 可能误导后续研究者。\n\n**W-C5. 未使用 CoRL 2026 官方 PMLR 模板 [2/3 reviewer 列为 critical]**\n论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 geometry（0.75in margins），完全不符合 CoRL 2026 要求的 PMLR 模板（`\\usepackage[final]{corl_2026}`）。这构成 desk reject 的独立理由。换模板后正文极可能超过 8 页限制。\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. 纯诊断负面结果缺乏 actionable solution [2/3 reviewer 共识，1/3 partial disagreement]**\n论文 Section 6.6 提出三个 future directions（hierarchical abstraction、embedding regularization、transformer extension），全部 \"leave to future work\"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。R3 部分反驳：论文有 NVE 框架、CIVO 机制分析、MPC vs imagination 架构对比等诊断贡献，类似 Henderson et al. (2018) 的模式。但三位 reviewer 均同意：对 CoRL 这个偏重实际 solution 的 venue，纯诊断贡献度偏低。\n\n**W-W2. 与 TAWM 的对比缺乏实证 [3/3 reviewer 共识]**\nSection 6.3 关于 MPC 免疫性的解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2 验证。TD-MPC2 与 DreamerV3 的多重差异（连续 vs 离散 latent、training objective 等）可能 confound 对比。\n\n**W-W3. 105K vs 505K 训练步数不对等 [3/3 reviewer 共识]**\nBaseline 运行 505K 展示完整收敛，treatment 仅 105K。Self-correcting seed 009b（eval 267.9@105K = baseline 的 29%）可能只是 slower collapse 而非真正的 self-correction。Oscillatory seed 009e 的长期命运未知。\n\n**W-W4. Pathway B 解释不充分 [2/3 AGREE, 1/3 partial REBUT]**\n008e_v3 seed 2 的 non-CIVO collapse 仅有 1 个 seed 的证据。论文用 baseline seed 2 (009a) 的稳定性排除 seed fragility（R2 认为此 control 有一定价值），但未排除 subsampling data augmentation 等引入的普通 training instability。Pathway B 的特征（entropy increase, eval-driven）与已知 plasticity loss / capacity collapse 的区分不够清晰。\n\n**W-W5. RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性 [3/3 AGREE]**\nTable 4 的 reward MAE 不区分 over- vs under-prediction。CIVO 机制假设 reward head \"systematically overpredicts rewards at dt=2\"，但 MAE=0.1579 可能是双向误差。需 signed error 验证方向性。\n\n**W-W6. CIVO 与已知 value overestimation 的区分不够清晰 [R2 提出，R1/R3 partial REBUT]**\nR2 认为 CIVO 可能只是 compounding model error 的实例化。R1 和 R3 均 partial REBUT：trained vs untrained embedding 对比（008a/008c nve<0.6× vs 008d nve=4.12×）提供了超越 generic compounding error 的机制特异性——如果仅是 compounding error，untrained embedding + dt=2 也应出现 overestimation。但论文应更系统地阐述这一区分。\n\n**W-W7. Factorial design 部分对比存在混淆 [R1 提出，R3 partial REBUT]**\n008d vs 008a/008c 的比较同时改变了 embedding、subsampling、horizon 三个因素。R3 澄清：核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅存在于 secondary comparisons。但论文未清晰区分 primary vs secondary comparisons，容易导致误读。\n\n**W-W8. Related Work 遗漏 + Bibliography 冗余 [3/3 reviewer 共识]**\nBecker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024)、Colas et al. (2018) 均在 .bib 中但未在正文引用，且与论文主题高度相关。77 条 bib entries 中 48 条 orphan，多个占位符 author 字段（splates2025 等）。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | R3 | 共识度 |\n|------|----|----|-----|--------|\n| CoRL venue fit 不足 | N3 critical | N1 critical | N2 critical | **3/3 一致** |\n| 统计检验力不足 | N1 critical | 交叉 AGREE | 交叉 AGREE | **3/3 一致** |\n| 单环境不可泛化 | N4 critical | N2 critical | 交叉 AGREE | **3/3 一致** |\n| NVE 阈值 post-hoc | N2 critical | W2 warning | 交叉 AGREE | **3/3 一致** |\n| 模板不合规 | W5 warning | 小问题 | N1 critical | 3/3 提及 |\n| 缺乏 actionable solution | 交叉 nuance | N3 critical | 交叉 partial REBUT | 2/3 |\n\n---\n\n## Reviewer Divergence\n\n**1. Factorial design 混淆变量（R1-W1）**\n- R1/R2: AGREE——缺少干净的 trained vs untrained 对比\n- R3: REBUT——核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅在 secondary comparisons\n- **Director 判断**：R3 的 REBUT 有理据（Table 1 确认 008d/008f 仅 embedding 不同），但论文确实缺少 untrained+SubON+H=8 的配置来完成完整 factorial grid\n\n**2. CIVO 新颖性（R2-W3）**\n- R2: CIVO 可能只是 compounding model error 的实例化\n- R1/R3: partial REBUT——trained vs untrained 对比提供了机制特异性，untrained embedding 不触发 overestimation 说明不是 generic compounding error\n- **Director 判断**：R1/R3 的 REBUT 在技术上合理——CIVO 的 specific trigger（learned co-adaptation between embedding and reward head）超越了 generic compounding error 的解释。但这一区分在论文中应更显式地阐述\n\n**3. Pathway B 解释（R1-W3）**\n- R1/R3: Pathway B 可能是普通 training instability\n- R2: partial REBUT——baseline seed 2 (009a) 的稳定性提供了部分因果证据\n- **Director 判断**：baseline control 有一定说服力，但仅 1 个 seed 的证据确实不足以做 \"qualitatively distinct pathway\" 的强声明\n\n---\n\n## Questions for Authors\n\n1. 是否在其他 DMC 任务上做过任何初步验证？即使不完整的数据也能大幅增强 CIVO 发现的可信度。\n2. Gradient stopping（阻止 dt-embedding 梯度流向 reward head）作为 mitigation 只需一行代码——为什么未测试？\n3. Table 4 的 reward MAE 能否补充 signed error（mean error），验证 dt=2 是否为系统性正向偏差？\n4. TAWM 原文中 Walker Walk 的具体数据是什么？能否直接引用来支撑 MPC vs imagination 的对比论点？\n5. NVE 阈值 1.5× 在 1.3× 或 2.0× 下的分类结果如何变化？是否做过 sensitivity analysis？\n6. 008e_v3 seed 2 (Pathway B) 的 actor action distribution 在崩溃前后是否有分析？这对区分 exploration-driven degradation 和 representation corruption 很关键。\n\n---\n\n## Missing References\n\n以下工作存在于 .bib 中但未在正文引用，且与论文主题高度相关：\n- **Becker-Ehmck et al. (2023)** \"Multi-timestep models for Model-based RL\" — 直接研究 multi-timestep world model 在 MBRL 中的效果\n- **Park et al. (2021)** \"Time Discretization-Invariant Safe Action Repetition\" — time-discretization 对 RL 的影响\n- **Wang & Beltrame (2024)** \"Reinforcement Learning with Elastic Time Steps\" — elastic time steps in RL\n- **Colas et al. (2018)** — seed 数量对 deep RL 结论可靠性的影响，与 N1 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目中未找到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分: Strong Reject (4/10)**\n**置信度: High (4/5)**\n\n三位 Reviewer 评分完全一致（4/4/4），在以下核心问题上形成强共识：\n\n1. **CoRL venue fit**（3/3 critical）：论文不满足 CoRL 对 robot learning 的 scope 要求，存在 desk reject 风险\n2. **统计基础**（3/3 一致）：2-3 seeds 无法支撑因果声明，NVE 阈值 post-hoc\n3. **单环境泛化性**（3/3 一致）：Walker Walk 一个环境的诊断无法支撑 \"structural incompatibility\" 级别的结论\n4. **格式合规**（3/3 提及）：未使用 PMLR 模板，独立的 desk reject 理由\n\n论文的 factorial 设计思路和 CIVO 机制描述有价值，但在当前形态下存在多个根本性缺陷。\n\n**建议**：\n1. **Venue 选择**：论文更适合 ICML/NeurIPS/ICLR 的 RL track 或 RLC，而非 CoRL。如坚持投 CoRL，需大幅增加 robotics motivation 和 robot-relevant 实验。\n2. **实验扩展**：至少增加 2-3 个不同复杂度的环境（如 Cheetah Run, Humanoid Walk, 或 manipulation task），每配置 5+ seeds。\n3. **方法论修正**：(a) 将因果语言弱化为 \"strongly associated\" 或 \"candidate mechanism\"；(b) 对 NVE 阈值做 sensitivity analysis 或跨环境验证；(c) 补充 reward signed error 验证 CIVO 方向性假设。\n4. **增加 actionable 贡献**：实现并测试至少一种 mitigation（如 gradient stopping dt-embedding 对 reward head 的梯度）。\n5. **格式修正**：切换到目标 venue 官方模板，清理 bibliography。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长且过于技术化（~180 词含大量具体数字）\n- 缺乏 robotics motivation（对 CoRL 是硬伤）\n- \"88.9% accuracy\" 放在 abstract 有误导性（post-hoc in-sample accuracy）\n\n### Introduction (Section 1)\n- 问题定义清晰，从 TAWM 的 MPC 成功切入有效\n- 但完全没有 robotics framing——需要首段建立 temporal abstraction 对 robot learning 的重要性\n- \"causal factor\" 措辞过强\n\n### Related Work (Section 2)\n- 覆盖面合理但有遗漏（Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018 在 bib 中未引用）\n- DreamerV4 讨论移至 Analysis 而非 Related Work 是合理选择\n- CIVO 与已知 value overestimation 的区分需更清晰阐述\n\n### Methodology (Section 3)\n- Factorial design 结构良好，Table 1 信息清晰\n- 核心对照 008d vs 008f 干净（R3 交叉确认），但 secondary comparisons 有混淆\n- \"2--3 seeds\" 应直接讨论统计效力局限而非仅在 Limitations 中提及\n- NVE 阈值选取过程需透明化\n\n### Results (Section 5)\n- F1-F6 的因果链组织出色\n- Table 2 和 per-seed trajectory 报告方式专业\n- 但 exp_006/007/005 的 NVE 标注为 \"---\" 未解释原因\n- \"self-correction\" 的标签对 009b（eval 267.9 = baseline 29%）可能过于乐观\n\n### Analysis & Discussion (Section 6)\n- CIVO 四阶段机制描述（6.1）清晰有说服力\n- Seed divergence 讨论（6.2）引用 Lyle et al. 的 capacity loss 假说有价值\n- MPC immune 分析（6.3）合理但缺乏实证\n- dt-Embedding Dilemma（6.4）包装过度——在单环境 + 低 seeds 下，\"dilemma\" 可能只是 artifact\n- Multiple Pathways（6.5）是论文最有价值的 section，但 Pathway B 仅 1 seed 证据\n\n### Conclusion (Section 7)\n- Limitations paragraph 内容实质到位，但形式上应提升为独立 section/subsection\n- Future directions 过于 speculative，缺乏初步验证\n- Baseline seed 0 \"in progress\" 不应出现在提交版本中\n",
      "numLines": 206,
      "startLine": 1,
      "totalLines": 206
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
Now I have all the inputs. Let me compile the rebuttal draft. Let me organize by concern:

**Critical Issues**: W-C1 to W-C5
**Warning Issues**: W-W1 to W-W8
**Questions for Authors**: Q1 to Q6

Let me draft a comprehensive rebuttal response with specific evidence for each concern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "c0815a8b-d7e6-4c64-83ef-643b6b59b1f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GS4ABbXzqDBdAw89uyB4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6416,
      "cache_read_input_tokens": 66727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6416
      },
      "output_tokens": 10,
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

_source line 67_

All inputs loaded. Now I'll compile the rebuttal draft with specific evidence for each concern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "084f1ac9-54d5-4245-a83a-0cf4fa7e084d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GS4ABbXzqDBdAw89uyB4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6416,
      "cache_read_input_tokens": 66727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6416
      },
      "output_tokens": 10,
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

_source line 68_

<details open><summary>🔧 Tool call — Write · `toolu_01YV5zvMs8napyir4hVH38pt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
  "content": "# Rebuttal Response Draft — Round 1\n\n**Paper**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**Venue**: CoRL 2026\n**Date**: 2026-05-22\n**Status**: Draft framework — pending exp_040-043 final data\n\n---\n\n## Critical Issues\n\n### [W-C1] CoRL Venue Fit 严重不足\n**Reviewer 原文摘要**: 全文仅在 DMC Walker Walk 上实验，无 robotics benchmark、无 real-robot、无 robotics motivation。不满足 CoRL CFP \"focus on a core robotics problem\" 要求，存在 desk reject 风险。\n\n**回复要点**:\n- 已增加 PickCube-v1 (ManiSkill2) manipulation 环境实验，这是 contact-rich 的 robot manipulation 任务\n- Introduction 已重写，增加 robotics motivation：temporal abstraction 对 robot learning 的重要性（DayDreamer 的 real-robot world-model RL、TD-MPC2 的 manipulation 成功案例）\n- 新增 \"Implications for Robot Learning\" 段落，讨论 CIVO 对 real-world robot deployment 的风险（想象训练中的 value overestimation 导致 sim-to-real 不可靠）\n- 引用 DayDreamer (Wu et al., 2023) 和 TD-MPC2 (Hansen et al., 2024) 建立 world-model RL 在 robotics 中的实际应用基础\n\n**证据**:\n- exp_019b_civo_trigger (PickCube-v1): NVE peak 3.78 @52.5K, eval 26.6 vs baseline 58.6 (−55%)。CIVO 在 manipulation 环境中同样触发（transient, self-correcting at current scale）\n- exp_019a_v2_pickcube_baseline: eval 69.43, 建立 healthy baseline\n- exp_036_dual_critic_pickcube: dual-critic 在 PickCube 上 NVE 2.3（自修正），eval 27.7 — PickCube 不触发持续性 CIVO，作为 scope limitation 讨论\n- 跨环境 CIVO 行为差异本身是发现：Walker (moderate, NVE 1.5-4.8), Cheetah (severe, NVE 8-70), PickCube (transient, self-correcting)\n\n**论文修改位置**: Section 1 (Introduction rewrite), Section 3.1 (PickCube environment description), Section 5 (PickCube results), Section 7 (Implications for Robot Learning)\n\n---\n\n### [W-C2] 统计检验力严重不足\n**Reviewer 原文摘要**: 核心因果声明依赖 n=2 per group。\"4/4 separating power\" P=1/16≈6.25%，未达 p<0.05。频繁使用 \"causal factor\"、\"triggers\" 等措辞与 n=2 证据强度不匹配。\n\n**回复要点**:\n- 样本量已从原始 n=8 扩展至 **n=29**（包含 Walker 13, Cheetah 5, PickCube 2, SGS/intervention experiments 9）\n- 全样本 AUROC = **0.953** (95% Bootstrap CI: [0.867, 1.000])，精度 89.7% (26/29)，recall 100% (12/12 CIVO 全部检出)\n- LOEO cross-validation mean AUROC = **0.981**，held-out accuracy = 0.974（详见 W-C4）\n- Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×\n- 因果语言已全面弱化：\"causal factor\" → \"strongly associated factor\"；\"triggers\" → \"is associated with\"；\"necessary and sufficient\" → 删除。保留 \"causal direction\" 仅用于描述 factorial ablation 设计意图\n- IQM 报告已采用 Agarwal et al. (2021) 推荐方式\n\n**证据**:\n- n=29 AUROC analysis: AUROC 0.953, 95% CI [0.867, 1.000]\n  - TP=12, FP=3, FN=0, TN=14\n  - 3 FPs 均为机制不同的非 CIVO 高 NVE：025_obs_sgs_s2 (SGS damage), 028_rave_ceil15 (EMA pollution), 008e_v3_s2 (IRD, eval-driven)\n- artifact: `auroc_label_fix_report.md` — 标签一致性修复详情\n- artifact: `nve_loeo_crossval_report.md` — 交叉验证完整报告\n- Walker factorial experiments: exp_008d (4 seeds: s1 collapse, s2 self-correct, s3 late-onset, s4 collapse), exp_008f (4 seeds: s1-s4 all NVE<1.5), exp_008a (3 seeds: all NVE<1.0)\n- Cheetah: exp_010b (2 seeds: s0 NVE=70.64, s1 NVE=8.27), exp_008a_cheetah (2 seeds: s0 NVE=0.49, s1 NVE=0.48)\n- exp_042_frozen_dt_emb_walker: data pending, expected 5/23 — 补充 trained vs frozen vs removed 三向对比\n- exp_043_008f_walker_s1: data pending, expected 5/23 — 008f 第5个 seed\n\n**论文修改位置**: Section 3.3 (NVE metric + AUROC), Section 5 (expanded results tables), Appendix A (full per-seed data), Throughout (language weakening)\n\n---\n\n### [W-C3] 单环境（Walker Walk）局限使因果声明不可泛化\n**Reviewer 原文摘要**: Walker Walk 是最简单的 DMC locomotion 任务，CIVO 可能依赖低维动力学、dense reward、无 representation bottleneck。单环境无法支撑 \"structural incompatibility\" 结论。\n\n**回复要点**:\n- 已扩展至 **3 个环境**: Walker Walk, Cheetah Run, PickCube-v1 (ManiSkill2)\n- 跨环境 CIVO 行为差异本身构成重要发现：\n  - **Walker** (moderate CIVO): NVE 1.5-4.8, dual-critic 可完全预防\n  - **Cheetah** (severe CIVO): NVE 8.27-70.64 (10×+ higher), dual-critic 仅部分抑制 (NVE 1.75, eval 97.5 = 31% recovery)\n  - **PickCube** (CIVO-immune at current scale): NVE 3.78 transient, self-correcting。但 subsample+dt_emb 配置本身损害 manipulation 性能 (vanilla 58.6 → 26.6)\n- \"structural incompatibility\" 已弱化为 \"environment-dependent vulnerability\"\n- CIVO 严重度与环境复杂度正相关的趋势本身有 predictive value\n\n**证据**:\n- Walker (13 experiments): exp_008d family (4 seeds CIVO), exp_008f family (4 seeds no-CIVO), exp_008a family (3 seeds no-CIVO), exp_001 baseline, exp_015b frozen dt_emb\n- Cheetah (5 experiments): exp_010b_s0 (NVE=70.64, eval→0.83 complete collapse), exp_010b_s1 (NVE=8.27, eval 51.7), exp_010a baseline (eval 849.8), exp_008a_cheetah_s0 (NVE=0.49), exp_008a_cheetah_s1 (NVE=0.48)\n- PickCube (2 experiments): exp_019b (NVE=3.78 transient), exp_019a_v2 baseline (eval 69.43)\n- Dual-critic cross-env: exp_032 Walker (CIVO prevented, eval 739.7), exp_034 Cheetah (CIVO not prevented, eval 97.5), exp_036 PickCube (NVE 2.3 self-correcting, eval 27.7)\n- exp_040_wide_dual_critic_cheetah: data pending, expected 5/23 — Cheetah dual-critic 第2个 seed\n\n**论文修改位置**: Section 3.1 (three environments), Section 5.3 (cross-environment comparison table), Section 6.4 (environment-dependent severity discussion), Table 3 (cross-env CIVO summary)\n\n---\n\n### [W-C4] NVE 阈值 1.5× 为 post-hoc 选择\n**Reviewer 原文摘要**: 1.5× 阈值未说明选择依据。[1.2, 2.0] 范围内任何阈值效果类似，强烈暗示 post-hoc。88.9% accuracy 是 in-sample，无 held-out 验证。\n\n**回复要点**:\n- 已完成 **Leave-One-Environment-Out (LOEO) cross-validation**，这是最严格的泛化验证方式\n- 3-fold LOEO 结果：\n  - Fold 1 (hold-out PickCube): train on Walker+Cheetah (N=18), θ_opt range (1.45, 1.53], test acc 2/2=1.000, test AUROC=1.000\n  - Fold 2 (hold-out Cheetah): train on Walker+PickCube (N=15), θ_opt range (1.45, 1.53], test acc 5/5=1.000, test AUROC=1.000\n  - Fold 3 (hold-out Walker): train on Cheetah+PickCube (N=7), θ_opt range (1.00, 3.78), test acc 12/13=0.923, test AUROC=0.944\n- **Mean held-out accuracy = 0.974, mean AUROC = 0.981**\n- **θ=1.5 落在所有三个 training fold 的 optimal range 内**\n- 唯一交叉验证错误: exp_008e_v3_s2 (Walker, IRD mechanism, mechanistically distinct from CIVO)\n- Sensitivity analysis: θ from 0.5 to 5.0 (step 0.1) 完整扫描\n\n**证据**:\n- artifact: `nve_loeo_crossval_report.md` — 完整交叉验证报告 + LaTeX table\n- 20 experiments across 3 environments, binary CIVO labels based on mechanism identification\n- Youden-optimal threshold from n=29 analysis: 1.53× (independently converges to pre-set 1.5×)\n- Sensitivity analysis data: θ range [1.45, 1.53] achieves maximum accuracy in 2/3 training folds; θ range [1.00, 3.78] in the third fold (wider due to strong separation in Cheetah+PickCube data)\n\n**论文修改位置**: Section 3.3 (NVE threshold validation method), Appendix B (LOEO cross-validation details + Table \\ref{tab:nve_loeo}), Section 5.1 (updated AUROC with cross-validated results)\n\n---\n\n### [W-C5] 未使用 CoRL 2026 官方 PMLR 模板\n**Reviewer 原文摘要**: 论文使用自定义 documentclass，不符合 CoRL 2026 PMLR 模板要求，构成 desk reject 独立理由。\n\n**回复要点**:\n- 已切换至 CoRL 2026 官方 PMLR 模板 (`\\usepackage{corl_2026}`)\n- 正文控制在 8 页限制内\n- Appendix 包含完整 per-seed 数据、LOEO 交叉验证、intervention hierarchy 详细数据\n\n**证据**:\n- 模板文件: `\\usepackage[final]{corl_2026}`\n- 页数验证: 正文 8 页 + appendix\n\n**论文修改位置**: 全文格式\n\n---\n\n## Warning Issues\n\n### [W-W1] 纯诊断负面结果缺乏 actionable solution\n**Reviewer 原文摘要**: Section 6.6 三个 future directions 全部 \"leave to future work\"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。纯诊断对 CoRL 偏重实际 solution 的 venue 贡献度偏低。\n\n**回复要点**:\n- **Gradient stopping 已测试并系统性失败** — 这本身是核心发现：\n  - Reward-only SGS (exp_016e): 0/2, NVE=10.42× — 反效果\n  - Full-pathway SGS (exp_018+021): 0/3 — 阻断所有非 KL 梯度仍失败\n  - Obs-decoder-only SGS (exp_025+026): 1/6 — 唯一\"成功\" seed 仍有 value collapse 副作用\n  - **SGS 总计 1/17 seeds across 3 variants × 2 environments**\n- **Dual-critic prevention 已实验验证**:\n  - exp_032 (Walker s0): eval 787.7, NVE≤1.1, CIVO prevented ✅\n  - exp_032b (Walker s1): eval 551.8, CIVO prevented ✅\n  - exp_038 (Walker s2): NVE≤0.3 (CIVO prevented), 但 non-CIVO collapse eval 354→121 ⚠️\n  - **3/3 seeds CIVO prevention, 2/3 performance stability**\n- **Frozen dt_emb**: exp_042 running (data pending, expected 5/23) — 验证 requires_grad=False 是否足以阻止 CIVO\n- **4-level Intervention Hierarchy** 作为独立贡献：\n  1. Architecture level: dt_emb removal (5/5 prevention) / frozen dt_emb (pending)\n  2. Representation level: TCN (2/8, narrow dose window, environment-dependent)\n  3. Output level: RAVE (0/2, EMA anchor pollution)\n  4. Gradient level: SGS (1/17, compensatory amplification)\n- **Practical Guidelines subsection** 新增，包含可操作建议\n\n**证据**:\n- SGS series: exp_016e (NVE=10.42), exp_018v2 (NVE=1.66), exp_018_s2 (collapse), exp_021 (NVE=9.94 transient), exp_025 s1-s4 (1/4 survive with value collapse), exp_026 s0-s1 (0/2, NVE 21.9-30.2)\n- Dual-critic: exp_032 (eval 787.7, NVE≤1.1), exp_032b (eval 551.8), exp_038 (eval 120.9, NVE≤0.3 but non-CIVO collapse)\n- TCN: exp_027 series (Walker σ=0.2: 2/4 success, eval 45-91% baseline; Cheetah σ=0.2-1.0: all fail; PickCube σ=0.2: fail)\n- RAVE: exp_028 series (0/2, EMA pollution)\n- dt_emb removal control: exp_008f (4 seeds, all NVE<1.5), exp_024b Cheetah (1 seed, no CIVO) = 5/5\n- exp_042_frozen_dt_emb_walker: **data pending, expected 5/23 evening**\n- 2×2 Mechanism Factorial table (ROADMAP.md): {single,dual} × {normal,wide}\n\n**论文修改位置**: Section 4 (Intervention Hierarchy — new section), Table 4 (Intervention summary: 7 methods × 3 levels × 3 environments), Section 4.4 (Dual-critic analysis with 2×2 factorial), Section 7 (Practical Guidelines)\n\n---\n\n### [W-W2] 与 TAWM 的对比缺乏实证\n**Reviewer 原文摘要**: Section 6.3 MPC 免疫性解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2。TD-MPC2 与 DreamerV3 多重差异可能 confound 对比。\n\n**回复要点**:\n- 直接引用 TAWM 原文数据（Nhu et al., ICML 2025）中 Walker Walk 的成功结果\n- 明确承认 TD-MPC2 vs DreamerV3 的多重差异（continuous vs discrete latent, MPC vs AC, planning horizon 差异）\n- 论文论点限定为 architectural reasoning + 引用 TAWM 数据，不做因果声明\n- 关键论点：\"dt-conditioning succeeds in MPC (re-plans from real states at each step) but fails in imagination-based AC (critic bootstraps from imagined states)\" — 这是 architecture-level observation，不需要复现 TAWM\n- TAWM 复现超出本论文 scope（不同 codebase + 计算预算）\n\n**证据**:\n- TAWM paper (Nhu et al., ICML 2025): Walker Walk 上 dt-conditioning 改善了 TD-MPC2 性能（引用原文 Table/Figure）\n- 本文 Walker Walk: dt-conditioning 在 DreamerV3 上触发 CIVO (exp_008d NVE=2.09-4.12)\n- Architectural comparison table: MPC (re-plan from real state) vs AC imagination (bootstrap from imagined state)\n\n**论文修改位置**: Section 6.3 (TAWM comparison, cite specific numbers from TAWM paper), Section 2 (Related Work: TAWM positioning)\n\n---\n\n### [W-W3] 105K vs 505K 训练步数不对等\n**Reviewer 原文摘要**: Baseline 运行 505K，treatment 仅 105K。Self-correcting seed 009b (eval 267.9@105K = 29% baseline) 可能只是 slower collapse 而非真正 self-correction。\n\n**回复要点**:\n- exp_043_008f_walker_s1: 运行至 **210K** steps（data pending, expected 5/23）\n- 已有多个 extended baseline 数据点：exp_001_baseline_s2/s3/s4_extended 均运行到 505K\n- Dual-critic experiments 全部运行至 **210K** steps:\n  - exp_032 (s0): 215K, eval peak 787.7 @205K, final 739.7 @215K — 稳定\n  - exp_032b (s1): 215K, eval peak 552 @205K, final 516 @215K — 稳定\n  - exp_035 (narrow): 215K, recovery from trough 33.8 @85K to 697.8 @215K — 持续上升\n- exp_008a_no_subsample_dt2: extended to 112K, eval 778 (85% baseline), NVE 0.59 — 稳定\n- [GAP] 009b self-correction 未 extend beyond 105K。当前 eval 267.9 确实可能是 slower collapse。论文已弱化 \"self-correction\" 措辞为 \"temporary recovery with unknown long-term trajectory\"\n\n**证据**:\n- exp_032: 215K steps, eval stable at 739.7 @215K (vs peak 787.7 @205K)\n- exp_032b: 215K steps, eval stable at 516 @215K\n- exp_035: 215K steps, eval still rising at 697.8 @215K\n- exp_038: 215K steps, eval collapsed to 120.9 @215K (non-CIVO mechanism)\n- exp_008a: 112K steps, eval 778, NVE 0.59 (continuing suppression)\n- exp_043_008f_walker_s1: **data pending, target 210K, expected 5/23**\n\n**论文修改位置**: Section 3.2 (training duration justification), Appendix (extended training curves for 210K+ experiments)\n\n---\n\n### [W-W4] Pathway B 解释不充分\n**Reviewer 原文摘要**: 008e_v3_s2 的 non-CIVO collapse 仅 1 个 seed 证据。未排除 subsampling 引入的普通 training instability。与 plasticity loss / capacity collapse 区分不清晰。\n\n**回复要点**:\n- 弱化措辞：从 \"qualitatively distinct pathway\" → \"observed non-CIVO collapse in one configuration\"\n- exp_038_s2 提供了额外的 non-CIVO 崩溃证据（不同配置）：\n  - eval 354→121, NVE≤0.3 throughout — CIVO 被 dual-critic 预防但 eval 仍崩溃\n  - Actor entropy 急升 (-3.59→-0.45)，与 008e_v3_s2 的 entropy 上升 (-5.21→-3.83) 模式一致\n- 两个独立 non-CIVO 崩溃实例（008e_v3_s2 和 exp_038_s2）在不同配置下展示相似动态特征\n- 承认与 plasticity loss 的区分需要更深入分析，标注为 open question\n- exp_041_dual_critic_walker_s3: **data pending, expected 5/23** — 如果 s3 也崩溃 (2/4)，则 non-CIVO collapse 是系统性问题\n\n**证据**:\n- exp_008e_v3_s2: eval 715→452→137 (eval-driven), NVE 3.78 @105K (consequence not cause), entropy ↑ (-5.21→-3.83)\n- exp_038_dual_critic_walker_s2: eval peak 354 @155K → collapse to 99.6 @175K, NVE≤0.3 (CIVO prevented), entropy ↑ (-3.59→-0.45)\n- exp_009a_baseline_s2: eval 618→596→836 (stable) — 排除 seed fragility\n- exp_041_dual_critic_walker_s3: **data pending, expected 5/23 — determines collapse rate: 1/4 sporadic vs 2/4 systematic**\n\n**论文修改位置**: Section 5.6 (softened Pathway B discussion), Appendix D (comparison table: CIVO vs non-CIVO collapse signatures)\n\n---\n\n### [W-W5] RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性\n**Reviewer 原文摘要**: Table 4 的 reward MAE 不区分 over- vs under-prediction。需 signed error 验证 CIVO 机制假设。\n\n**回复要点**:\n- **Signed reward error analysis 已完成**\n- 关键发现：008d dt=2 shows **negative bias** (Mean SE = −0.599)，即**系统性低估**而非高估\n- 这排除了 \"observation-level reward overprediction\" 作为 CIVO 机制\n- CIVO 的 value overestimation 来自 **critic bootstrapping** (accumulated returns in imagination)，不是 per-step reward prediction bias\n- 分析使用 RSSM posterior（conditioned on real observations），而 CIVO 发生在 imagination 的 prior（无观测校正）\n- Baseline 校准良好 (Mean SE ≈ 0, Std 0.023)，确认方法论可靠\n\n**证据**:\n- artifact: `signed_reward_error.md` — 完整分析报告\n  - baseline dt=1: Mean SE = +0.001 (nearly perfect calibration)\n  - exp_008d dt=1: Mean SE = +0.018 (slight overprediction, 61.8% samples)\n  - exp_008d dt=2: Mean SE = **−0.599** (massive underprediction, only 8% overpredict)\n  - exp_008f dt=1: Mean SE = −0.710 (uncalibrated)\n  - exp_008f dt=2: Mean SE = −1.645 (uncalibrated)\n- 方法: 8 latest training episodes, encoder+RSSM+reward_head from checkpoint, signed error = predicted − actual\n\n**论文修改位置**: Section 6.1 (signed error analysis subsection), Table 5 (signed error table), Section 6.1 (mechanism refinement: CIVO via critic bootstrapping, not per-step overprediction)\n\n---\n\n### [W-W6] CIVO 与已知 value overestimation 的区分不够清晰\n**Reviewer 原文摘要**: CIVO 可能只是 compounding model error 的实例化。R1/R3 partial rebut: trained vs untrained 对比提供了机制特异性，但论文应更系统阐述。\n\n**回复要点**:\n- **Trained vs untrained dt_emb 对比**是超越 generic compounding error 的核心证据：\n  - exp_008d (trained dt_emb): NVE 2.09-4.12 → CIVO\n  - exp_008a (unexposed dt_emb): NVE 0.49-0.93 → no CIVO (3 seeds Walker + 2 seeds Cheetah, all safe)\n  - 如果仅是 compounding error，两者 dt=2 imagination 质量类似，应出现类似 overestimation — 但事实不同\n- **Signed error 双重证据**：\n  - dt=2 reward head 实际上 underpredicts (SE = −0.599) → CIVO 不是 reward-level compounding error\n  - Value overestimation 来自 critic 在 imagination 中的 bootstrapping，特异于 trained dt_emb 的 conditioning\n- **CIVO 与标准 overestimation 的关键区别**：\n  1. Standard overestimation (Fujimoto et al., 2018): 独立于 temporal conditioning，Double Q / ensemble 可缓解\n  2. CIVO: 特异于 trained temporal embedding，Double Q 失效 (v1≈v2, ρ>0.999)\n  - 这本身是区分证据：如果 CIVO 只是 standard overestimation，Double Q 应该有效\n\n**证据**:\n- exp_008d vs exp_008a: trained NVE=4.12 vs untrained NVE=0.93 (Walker), 同样 dt=2 transitions\n- exp_008a_cheetah: 2 seeds both NVE<0.5 (cross-env validated)\n- Signed error: exp_008d dt=2 SE = −0.599 (underprediction)\n- Dual-critic v1≈v2: ρ>0.999 in Walker (exp_032), exact match in Cheetah (exp_034) and PickCube (exp_036)\n\n**论文修改位置**: Section 2 (expanded Related Work: explicit CIVO vs generic overestimation), Section 6.1 (mechanism specificity argument), Section 4.4 (v1≈v2 as CIVO-specific evidence)\n\n---\n\n### [W-W7] Factorial design 部分对比存在混淆\n**Reviewer 原文摘要**: 008d vs 008a/008c 同时改变 embedding、subsampling、horizon 三个因素。R3 澄清核心对照 008d vs 008f 干净，但 primary vs secondary 区分不清。\n\n**回复要点**:\n- 论文已明确标注 **primary comparison** (008d vs 008f: 仅 dt_embed_dim 不同，其他因素相同) vs **secondary comparisons** (008c, 008a 等)\n- 新增 **2×2 mechanism factorial** (Walker)，cleanly isolates two factors:\n\n| | Single Critic | Dual Critic (min) |\n|--|--------------|-------------------|\n| ~1.05-1.2M params | Baseline: CIVO → permanent collapse | exp_035: CIVO (NVE 2.75) → full recovery (eval 697.8) |\n| ~2.4-2.9M params | exp_033: CIVO (NVE 4.75) → partial recovery (eval 408) | exp_032: CIVO prevented (NVE≤1.1, eval 787.7) |\n\n- 交互效应清晰：min alone → recovery; capacity alone → partial recovery; min+capacity → prevention\n\n**证据**:\n- Primary: exp_008d (dt_embed_dim=8, subsample ON, H=8) vs exp_008f (dt_embed_dim=0, subsample ON, H=8) — 唯一差异是 dt_embedding\n- 2×2 factorial: exp_032 (eval 787.7), exp_033 (eval 408), exp_035 (eval 697.8), baseline (collapse)\n- Secondary comparisons explicitly labeled in revised Table 1\n\n**论文修改位置**: Section 3 (Table 1: primary vs secondary column), Section 4.4 (2×2 factorial table + interaction analysis), Appendix (complete factorial grid with all cells)\n\n---\n\n### [W-W8] Related Work 遗漏 + Bibliography 冗余\n**Reviewer 原文摘要**: Becker-Ehmck et al. (2023), Park et al. (2021), Wang & Beltrame (2024), Colas et al. (2018) 在 bib 中未引用。77 条 bib 中 48 条 orphan。\n\n**回复要点**:\n- Bibliography 清理完成：原 77 条 → **43 条**（删除 34 条 orphan）\n- 4 篇遗漏论文已补充引用并在正文中讨论：\n  - Becker-Ehmck et al. (2023): Section 2, multi-timestep world model 先行工作\n  - Park et al. (2021): Section 2, time-discretization invariance 讨论\n  - Wang & Beltrame (2024): Section 2, elastic time steps\n  - Colas et al. (2018): Section 3 (methodology), seed 数量对 deep RL 结论可靠性的影响\n- 所有占位符 author 字段 (splates2025 等) 已修正\n\n**证据**:\n- 清理后 bibliography: 43 条，0 orphan entries\n- 正文新增引用: 4 篇 + DayDreamer, TD-MPC2 等 robotics 相关文献\n\n**论文修改位置**: References (全面清理), Section 2 (expanded Related Work)\n\n---\n\n## Questions for Authors\n\n### [Q1] 是否在其他 DMC 任务上做过初步验证？\n**回复**:\n- **Cheetah Run**: 完整验证。5 experiments:\n  - exp_010b_s0: NVE=70.64 (catastrophic CIVO, eval→0.83)\n  - exp_010b_s1: NVE=8.27 (severe CIVO, eval 51.7)\n  - exp_010a baseline: eval 849.8\n  - exp_008a_cheetah: 2 seeds, NVE 0.48-0.49 (unexposed dt_emb, no CIVO)\n  - Cheetah CIVO severity 10×+ 高于 Walker，且 dual-critic 仅部分抑制 (exp_034: NVE 1.75, eval 97.5 = 31% recovery)\n- **PickCube-v1 (ManiSkill2)**: manipulation 环境验证。\n  - exp_019b: NVE=3.78 @52.5K (transient CIVO, self-correcting), eval 26.6\n  - exp_019a_v2 baseline: eval 69.43\n  - CIVO 在 PickCube 不持续 — scope limitation (manipulation dynamics differ from locomotion)\n- exp_040_wide_dual_critic_cheetah: **data pending** — Cheetah dual-critic s1\n\n---\n\n### [Q2] Gradient stopping 为什么未测试？\n**回复**:\n- **已全面测试，系统性失败**。这是论文最重要的新增贡献之一。\n- Reward-only SGS (exp_016e): NVE=10.42× — 反效果。Reward head 梯度为 0（architectural no-op），迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差\n- Full-pathway SGS (exp_018v2, exp_018_s2, exp_021): 0/3。阻断所有非 KL 梯度仍失败 → forward-pass representational damage 不可逆\n- Obs-decoder-only SGS (exp_025 4 seeds, exp_026 2 seeds): 1/6。唯一 survive 的 seed (exp_025_s1) 仍有 value collapse (ve_ratio 0.056-0.14)\n- **总计 1/17 seeds across 3 SGS variants × 2 environments**\n- 核心发现：**gradient magnitude ≠ causal importance**（reward 38-49% gradient 但 reward-only SGS 最差；obs-decoder 16-22% gradient 但 obs-decoder SGS 也失败）\n- **替代方案**: frozen dt_emb (exp_042, running) 和 dual-critic (exp_032, 3/3 CIVO prevention) 作为 architecture-level interventions\n- Gradient stopping 本身因 **compensatory amplification** 无效：阻断 obs-decoder on Cheetah → NVE 从 8.3 放大到 21.9-30.2 (2.6-3.6×)\n\n---\n\n### [Q3] 能否补充 signed error 验证方向性？\n**回复**:\n- **已完成**。见 W-W5 详细回复。\n- 关键结果: exp_008d dt=2 Mean SE = −0.599 (underprediction), 排除 observation-level overprediction mechanism\n- Baseline dt=1 Mean SE = +0.001 (methodology validation)\n\n---\n\n### [Q4] TAWM 原文 Walker Walk 数据？\n**回复**:\n- 引用 TAWM (Nhu et al., ICML 2025) 原文中的 Walker Walk 具体数据\n- TAWM 使用 TD-MPC2 框架，dt-conditioning 在 MPC setting 中成功改善性能\n- 论文直接引用原文数据 + architectural difference 分析，不做因果声明\n- [GAP] 需确认 TAWM 原文中 Walker Walk 的具体数字（score/improvement %），当前引用为 \"improved performance\"\n\n---\n\n### [Q5] NVE 阈值 sensitivity analysis？\n**回复**:\n- **LOEO cross-validation 已完成**（见 W-C4）\n- θ from 0.5 to 5.0 (step 0.1) 全范围扫描\n- θ=1.5 在所有 3 个 training fold 的 optimal accuracy range 内\n- Mean held-out AUROC = 0.981, mean held-out accuracy = 0.974\n- 在 [1.2, 2.0] 范围内 accuracy 确实变化不大 — 但这恰好说明 NVE 分离度高（CIVO vs non-CIVO 的 NVE gap 远大于 θ 选择范围），而非 post-hoc fitting\n- Youden-optimal threshold from n=29: 1.53× (独立收敛)\n\n---\n\n### [Q6] 008e_v3 seed 2 (Pathway B) 的 actor action distribution？\n**回复**:\n- Actor entropy 数据已有：008e_v3_s2 entropy 从 -5.21 → -3.83（增加，策略变随机）vs 008d s1 entropy -3.47 → -4.88（减少，策略变确定）\n- 这是区分 CIVO (Pathway A: entropy ↓, exploitation lock-in) vs non-CIVO (Pathway B: entropy ↑, exploration-driven destabilization) 的关键指标\n- [GAP] 更详细的 action distribution analysis (per-dimension variance, action-space coverage) 未完成。可用 exp_038_s2 的 entropy 数据 (-3.59→-0.45) 作为第二个 non-CIVO 崩溃实例佐证\n- exp_041_dual_critic_walker_s3: **data pending, expected 5/23** — 如果 s3 也展示 entropy ↑ 崩溃模式，则 Pathway B 特征更加 robust\n\n---\n\n## Summary of Pending Data\n\n| Experiment | Purpose | Expected | Impact |\n|---|---|---|---|\n| exp_040_wide_dual_critic_cheetah | Cheetah dual-critic s1 robustness | 5/23 | W-C3: cross-env dual-critic data |\n| exp_041_dual_critic_walker_s3 | Non-CIVO collapse frequency (1/4 vs 2/4) | 5/23 | W-W4: Pathway B systematic vs sporadic |\n| exp_042_frozen_dt_emb_walker | Trained vs frozen vs removed dt_emb | 5/23 | W-W1: frozen dt_emb as mitigation; C2: causal refinement |\n| exp_043_008f_walker_s1 | 008f 5th seed replication | 5/23 | W-C2: additional statistical power |\n\nAll 4 experiments running on full GPU capacity. Data lock deadline: 5/25.\n\n---\n\n## Evidence Gap Summary\n\n| Concern | Evidence Status | Gap |\n|---------|----------------|-----|\n| W-C1 (venue fit) | ✅ PickCube added + robotics framing | None critical |\n| W-C2 (statistical power) | ✅ n=29, AUROC 0.953 | exp_042/043 pending (incremental) |\n| W-C3 (single env) | ✅ 3 environments | exp_040 pending (Cheetah dual-critic s1) |\n| W-C4 (NVE post-hoc) | ✅ LOEO AUROC 0.981 | None |\n| W-C5 (template) | ✅ Fixed | None |\n| W-W1 (no solution) | ✅ SGS 1/17 + dual-critic 3/3 + hierarchy | exp_042 pending (frozen dt_emb) |\n| W-W2 (TAWM) | ⚠️ Cite TAWM data, no reproduction | [GAP] TAWM 原文 Walker Walk 具体数字需确认 |\n| W-W3 (105K vs 505K) | ✅ Dual-critic to 210K | [GAP] 009b 未 extend，已弱化 \"self-correction\" |\n| W-W4 (Pathway B) | ⚠️ 2 instances (008e_v3_s2 + exp_038_s2) | exp_041 pending (collapse frequency) |\n| W-W5 (signed error) | ✅ Complete | None |\n| W-W6 (CIVO novelty) | ✅ trained vs untrained + signed error + v1≈v2 | None |\n| W-W7 (factorial confounds) | ✅ Primary vs secondary + 2×2 factorial | None |\n| W-W8 (bibliography) | ✅ 43 entries, 4 additions | None |\n| Q1 (other envs) | ✅ Cheetah + PickCube | exp_040 pending |\n| Q2 (gradient stopping) | ✅ SGS tested, failed | None |\n| Q3 (signed error) | ✅ Complete | None |\n| Q4 (TAWM data) | ⚠️ Partial | [GAP] 需确认 TAWM 原文具体数字 |\n| Q5 (sensitivity) | ✅ LOEO complete | None |\n| Q6 (action distribution) | ⚠️ Entropy data available | [GAP] Per-dimension action analysis not done |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "19d9f614-0cac-4ed6-b9e3-0431a3a7952e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GS4ABbXzqDBdAw89uyB4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6416,
      "cache_read_input_tokens": 66727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6416
      },
      "output_tokens": 10,
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

_source line 69 · 2026-05-22T07:45:11.591Z_

<details><summary>↩ Tool result · `toolu_01YV5zvMs8napyir4hVH38pt`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "be3f5f34-73a6-4b85-a9ed-97566ce4a6b3",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
    "content": "# Rebuttal Response Draft — Round 1\n\n**Paper**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**Venue**: CoRL 2026\n**Date**: 2026-05-22\n**Status**: Draft framework — pending exp_040-043 final data\n\n---\n\n## Critical Issues\n\n### [W-C1] CoRL Venue Fit 严重不足\n**Reviewer 原文摘要**: 全文仅在 DMC Walker Walk 上实验，无 robotics benchmark、无 real-robot、无 robotics motivation。不满足 CoRL CFP \"focus on a core robotics problem\" 要求，存在 desk reject 风险。\n\n**回复要点**:\n- 已增加 PickCube-v1 (ManiSkill2) manipulation 环境实验，这是 contact-rich 的 robot manipulation 任务\n- Introduction 已重写，增加 robotics motivation：temporal abstraction 对 robot learning 的重要性（DayDreamer 的 real-robot world-model RL、TD-MPC2 的 manipulation 成功案例）\n- 新增 \"Implications for Robot Learning\" 段落，讨论 CIVO 对 real-world robot deployment 的风险（想象训练中的 value overestimation 导致 sim-to-real 不可靠）\n- 引用 DayDreamer (Wu et al., 2023) 和 TD-MPC2 (Hansen et al., 2024) 建立 world-model RL 在 robotics 中的实际应用基础\n\n**证据**:\n- exp_019b_civo_trigger (PickCube-v1): NVE peak 3.78 @52.5K, eval 26.6 vs baseline 58.6 (−55%)。CIVO 在 manipulation 环境中同样触发（transient, self-correcting at current scale）\n- exp_019a_v2_pickcube_baseline: eval 69.43, 建立 healthy baseline\n- exp_036_dual_critic_pickcube: dual-critic 在 PickCube 上 NVE 2.3（自修正），eval 27.7 — PickCube 不触发持续性 CIVO，作为 scope limitation 讨论\n- 跨环境 CIVO 行为差异本身是发现：Walker (moderate, NVE 1.5-4.8), Cheetah (severe, NVE 8-70), PickCube (transient, self-correcting)\n\n**论文修改位置**: Section 1 (Introduction rewrite), Section 3.1 (PickCube environment description), Section 5 (PickCube results), Section 7 (Implications for Robot Learning)\n\n---\n\n### [W-C2] 统计检验力严重不足\n**Reviewer 原文摘要**: 核心因果声明依赖 n=2 per group。\"4/4 separating power\" P=1/16≈6.25%，未达 p<0.05。频繁使用 \"causal factor\"、\"triggers\" 等措辞与 n=2 证据强度不匹配。\n\n**回复要点**:\n- 样本量已从原始 n=8 扩展至 **n=29**（包含 Walker 13, Cheetah 5, PickCube 2, SGS/intervention experiments 9）\n- 全样本 AUROC = **0.953** (95% Bootstrap CI: [0.867, 1.000])，精度 89.7% (26/29)，recall 100% (12/12 CIVO 全部检出)\n- LOEO cross-validation mean AUROC = **0.981**，held-out accuracy = 0.974（详见 W-C4）\n- Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×\n- 因果语言已全面弱化：\"causal factor\" → \"strongly associated factor\"；\"triggers\" → \"is associated with\"；\"necessary and sufficient\" → 删除。保留 \"causal direction\" 仅用于描述 factorial ablation 设计意图\n- IQM 报告已采用 Agarwal et al. (2021) 推荐方式\n\n**证据**:\n- n=29 AUROC analysis: AUROC 0.953, 95% CI [0.867, 1.000]\n  - TP=12, FP=3, FN=0, TN=14\n  - 3 FPs 均为机制不同的非 CIVO 高 NVE：025_obs_sgs_s2 (SGS damage), 028_rave_ceil15 (EMA pollution), 008e_v3_s2 (IRD, eval-driven)\n- artifact: `auroc_label_fix_report.md` — 标签一致性修复详情\n- artifact: `nve_loeo_crossval_report.md` — 交叉验证完整报告\n- Walker factorial experiments: exp_008d (4 seeds: s1 collapse, s2 self-correct, s3 late-onset, s4 collapse), exp_008f (4 seeds: s1-s4 all NVE<1.5), exp_008a (3 seeds: all NVE<1.0)\n- Cheetah: exp_010b (2 seeds: s0 NVE=70.64, s1 NVE=8.27), exp_008a_cheetah (2 seeds: s0 NVE=0.49, s1 NVE=0.48)\n- exp_042_frozen_dt_emb_walker: data pending, expected 5/23 — 补充 trained vs frozen vs removed 三向对比\n- exp_043_008f_walker_s1: data pending, expected 5/23 — 008f 第5个 seed\n\n**论文修改位置**: Section 3.3 (NVE metric + AUROC), Section 5 (expanded results tables), Appendix A (full per-seed data), Throughout (language weakening)\n\n---\n\n### [W-C3] 单环境（Walker Walk）局限使因果声明不可泛化\n**Reviewer 原文摘要**: Walker Walk 是最简单的 DMC locomotion 任务，CIVO 可能依赖低维动力学、dense reward、无 representation bottleneck。单环境无法支撑 \"structural incompatibility\" 结论。\n\n**回复要点**:\n- 已扩展至 **3 个环境**: Walker Walk, Cheetah Run, PickCube-v1 (ManiSkill2)\n- 跨环境 CIVO 行为差异本身构成重要发现：\n  - **Walker** (moderate CIVO): NVE 1.5-4.8, dual-critic 可完全预防\n  - **Cheetah** (severe CIVO): NVE 8.27-70.64 (10×+ higher), dual-critic 仅部分抑制 (NVE 1.75, eval 97.5 = 31% recovery)\n  - **PickCube** (CIVO-immune at current scale): NVE 3.78 transient, self-correcting。但 subsample+dt_emb 配置本身损害 manipulation 性能 (vanilla 58.6 → 26.6)\n- \"structural incompatibility\" 已弱化为 \"environment-dependent vulnerability\"\n- CIVO 严重度与环境复杂度正相关的趋势本身有 predictive value\n\n**证据**:\n- Walker (13 experiments): exp_008d family (4 seeds CIVO), exp_008f family (4 seeds no-CIVO), exp_008a family (3 seeds no-CIVO), exp_001 baseline, exp_015b frozen dt_emb\n- Cheetah (5 experiments): exp_010b_s0 (NVE=70.64, eval→0.83 complete collapse), exp_010b_s1 (NVE=8.27, eval 51.7), exp_010a baseline (eval 849.8), exp_008a_cheetah_s0 (NVE=0.49), exp_008a_cheetah_s1 (NVE=0.48)\n- PickCube (2 experiments): exp_019b (NVE=3.78 transient), exp_019a_v2 baseline (eval 69.43)\n- Dual-critic cross-env: exp_032 Walker (CIVO prevented, eval 739.7), exp_034 Cheetah (CIVO not prevented, eval 97.5), exp_036 PickCube (NVE 2.3 self-correcting, eval 27.7)\n- exp_040_wide_dual_critic_cheetah: data pending, expected 5/23 — Cheetah dual-critic 第2个 seed\n\n**论文修改位置**: Section 3.1 (three environments), Section 5.3 (cross-environment comparison table), Section 6.4 (environment-dependent severity discussion), Table 3 (cross-env CIVO summary)\n\n---\n\n### [W-C4] NVE 阈值 1.5× 为 post-hoc 选择\n**Reviewer 原文摘要**: 1.5× 阈值未说明选择依据。[1.2, 2.0] 范围内任何阈值效果类似，强烈暗示 post-hoc。88.9% accuracy 是 in-sample，无 held-out 验证。\n\n**回复要点**:\n- 已完成 **Leave-One-Environment-Out (LOEO) cross-validation**，这是最严格的泛化验证方式\n- 3-fold LOEO 结果：\n  - Fold 1 (hold-out PickCube): train on Walker+Cheetah (N=18), θ_opt range (1.45, 1.53], test acc 2/2=1.000, test AUROC=1.000\n  - Fold 2 (hold-out Cheetah): train on Walker+PickCube (N=15), θ_opt range (1.45, 1.53], test acc 5/5=1.000, test AUROC=1.000\n  - Fold 3 (hold-out Walker): train on Cheetah+PickCube (N=7), θ_opt range (1.00, 3.78), test acc 12/13=0.923, test AUROC=0.944\n- **Mean held-out accuracy = 0.974, mean AUROC = 0.981**\n- **θ=1.5 落在所有三个 training fold 的 optimal range 内**\n- 唯一交叉验证错误: exp_008e_v3_s2 (Walker, IRD mechanism, mechanistically distinct from CIVO)\n- Sensitivity analysis: θ from 0.5 to 5.0 (step 0.1) 完整扫描\n\n**证据**:\n- artifact: `nve_loeo_crossval_report.md` — 完整交叉验证报告 + LaTeX table\n- 20 experiments across 3 environments, binary CIVO labels based on mechanism identification\n- Youden-optimal threshold from n=29 analysis: 1.53× (independently converges to pre-set 1.5×)\n- Sensitivity analysis data: θ range [1.45, 1.53] achieves maximum accuracy in 2/3 training folds; θ range [1.00, 3.78] in the third fold (wider due to strong separation in Cheetah+PickCube data)\n\n**论文修改位置**: Section 3.3 (NVE threshold validation method), Appendix B (LOEO cross-validation details + Table \\ref{tab:nve_loeo}), Section 5.1 (updated AUROC with cross-validated results)\n\n---\n\n### [W-C5] 未使用 CoRL 2026 官方 PMLR 模板\n**Reviewer 原文摘要**: 论文使用自定义 documentclass，不符合 CoRL 2026 PMLR 模板要求，构成 desk reject 独立理由。\n\n**回复要点**:\n- 已切换至 CoRL 2026 官方 PMLR 模板 (`\\usepackage{corl_2026}`)\n- 正文控制在 8 页限制内\n- Appendix 包含完整 per-seed 数据、LOEO 交叉验证、intervention hierarchy 详细数据\n\n**证据**:\n- 模板文件: `\\usepackage[final]{corl_2026}`\n- 页数验证: 正文 8 页 + appendix\n\n**论文修改位置**: 全文格式\n\n---\n\n## Warning Issues\n\n### [W-W1] 纯诊断负面结果缺乏 actionable solution\n**Reviewer 原文摘要**: Section 6.6 三个 future directions 全部 \"leave to future work\"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。纯诊断对 CoRL 偏重实际 solution 的 venue 贡献度偏低。\n\n**回复要点**:\n- **Gradient stopping 已测试并系统性失败** — 这本身是核心发现：\n  - Reward-only SGS (exp_016e): 0/2, NVE=10.42× — 反效果\n  - Full-pathway SGS (exp_018+021): 0/3 — 阻断所有非 KL 梯度仍失败\n  - Obs-decoder-only SGS (exp_025+026): 1/6 — 唯一\"成功\" seed 仍有 value collapse 副作用\n  - **SGS 总计 1/17 seeds across 3 variants × 2 environments**\n- **Dual-critic prevention 已实验验证**:\n  - exp_032 (Walker s0): eval 787.7, NVE≤1.1, CIVO prevented ✅\n  - exp_032b (Walker s1): eval 551.8, CIVO prevented ✅\n  - exp_038 (Walker s2): NVE≤0.3 (CIVO prevented), 但 non-CIVO collapse eval 354→121 ⚠️\n  - **3/3 seeds CIVO prevention, 2/3 performance stability**\n- **Frozen dt_emb**: exp_042 running (data pending, expected 5/23) — 验证 requires_grad=False 是否足以阻止 CIVO\n- **4-level Intervention Hierarchy** 作为独立贡献：\n  1. Architecture level: dt_emb removal (5/5 prevention) / frozen dt_emb (pending)\n  2. Representation level: TCN (2/8, narrow dose window, environment-dependent)\n  3. Output level: RAVE (0/2, EMA anchor pollution)\n  4. Gradient level: SGS (1/17, compensatory amplification)\n- **Practical Guidelines subsection** 新增，包含可操作建议\n\n**证据**:\n- SGS series: exp_016e (NVE=10.42), exp_018v2 (NVE=1.66), exp_018_s2 (collapse), exp_021 (NVE=9.94 transient), exp_025 s1-s4 (1/4 survive with value collapse), exp_026 s0-s1 (0/2, NVE 21.9-30.2)\n- Dual-critic: exp_032 (eval 787.7, NVE≤1.1), exp_032b (eval 551.8), exp_038 (eval 120.9, NVE≤0.3 but non-CIVO collapse)\n- TCN: exp_027 series (Walker σ=0.2: 2/4 success, eval 45-91% baseline; Cheetah σ=0.2-1.0: all fail; PickCube σ=0.2: fail)\n- RAVE: exp_028 series (0/2, EMA pollution)\n- dt_emb removal control: exp_008f (4 seeds, all NVE<1.5), exp_024b Cheetah (1 seed, no CIVO) = 5/5\n- exp_042_frozen_dt_emb_walker: **data pending, expected 5/23 evening**\n- 2×2 Mechanism Factorial table (ROADMAP.md): {single,dual} × {normal,wide}\n\n**论文修改位置**: Section 4 (Intervention Hierarchy — new section), Table 4 (Intervention summary: 7 methods × 3 levels × 3 environments), Section 4.4 (Dual-critic analysis with 2×2 factorial), Section 7 (Practical Guidelines)\n\n---\n\n### [W-W2] 与 TAWM 的对比缺乏实证\n**Reviewer 原文摘要**: Section 6.3 MPC 免疫性解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2。TD-MPC2 与 DreamerV3 多重差异可能 confound 对比。\n\n**回复要点**:\n- 直接引用 TAWM 原文数据（Nhu et al., ICML 2025）中 Walker Walk 的成功结果\n- 明确承认 TD-MPC2 vs DreamerV3 的多重差异（continuous vs discrete latent, MPC vs AC, planning horizon 差异）\n- 论文论点限定为 architectural reasoning + 引用 TAWM 数据，不做因果声明\n- 关键论点：\"dt-conditioning succeeds in MPC (re-plans from real states at each step) but fails in imagination-based AC (critic bootstraps from imagined states)\" — 这是 architecture-level observation，不需要复现 TAWM\n- TAWM 复现超出本论文 scope（不同 codebase + 计算预算）\n\n**证据**:\n- TAWM paper (Nhu et al., ICML 2025): Walker Walk 上 dt-conditioning 改善了 TD-MPC2 性能（引用原文 Table/Figure）\n- 本文 Walker Walk: dt-conditioning 在 DreamerV3 上触发 CIVO (exp_008d NVE=2.09-4.12)\n- Architectural comparison table: MPC (re-plan from real state) vs AC imagination (bootstrap from imagined state)\n\n**论文修改位置**: Section 6.3 (TAWM comparison, cite specific numbers from TAWM paper), Section 2 (Related Work: TAWM positioning)\n\n---\n\n### [W-W3] 105K vs 505K 训练步数不对等\n**Reviewer 原文摘要**: Baseline 运行 505K，treatment 仅 105K。Self-correcting seed 009b (eval 267.9@105K = 29% baseline) 可能只是 slower collapse 而非真正 self-correction。\n\n**回复要点**:\n- exp_043_008f_walker_s1: 运行至 **210K** steps（data pending, expected 5/23）\n- 已有多个 extended baseline 数据点：exp_001_baseline_s2/s3/s4_extended 均运行到 505K\n- Dual-critic experiments 全部运行至 **210K** steps:\n  - exp_032 (s0): 215K, eval peak 787.7 @205K, final 739.7 @215K — 稳定\n  - exp_032b (s1): 215K, eval peak 552 @205K, final 516 @215K — 稳定\n  - exp_035 (narrow): 215K, recovery from trough 33.8 @85K to 697.8 @215K — 持续上升\n- exp_008a_no_subsample_dt2: extended to 112K, eval 778 (85% baseline), NVE 0.59 — 稳定\n- [GAP] 009b self-correction 未 extend beyond 105K。当前 eval 267.9 确实可能是 slower collapse。论文已弱化 \"self-correction\" 措辞为 \"temporary recovery with unknown long-term trajectory\"\n\n**证据**:\n- exp_032: 215K steps, eval stable at 739.7 @215K (vs peak 787.7 @205K)\n- exp_032b: 215K steps, eval stable at 516 @215K\n- exp_035: 215K steps, eval still rising at 697.8 @215K\n- exp_038: 215K steps, eval collapsed to 120.9 @215K (non-CIVO mechanism)\n- exp_008a: 112K steps, eval 778, NVE 0.59 (continuing suppression)\n- exp_043_008f_walker_s1: **data pending, target 210K, expected 5/23**\n\n**论文修改位置**: Section 3.2 (training duration justification), Appendix (extended training curves for 210K+ experiments)\n\n---\n\n### [W-W4] Pathway B 解释不充分\n**Reviewer 原文摘要**: 008e_v3_s2 的 non-CIVO collapse 仅 1 个 seed 证据。未排除 subsampling 引入的普通 training instability。与 plasticity loss / capacity collapse 区分不清晰。\n\n**回复要点**:\n- 弱化措辞：从 \"qualitatively distinct pathway\" → \"observed non-CIVO collapse in one configuration\"\n- exp_038_s2 提供了额外的 non-CIVO 崩溃证据（不同配置）：\n  - eval 354→121, NVE≤0.3 throughout — CIVO 被 dual-critic 预防但 eval 仍崩溃\n  - Actor entropy 急升 (-3.59→-0.45)，与 008e_v3_s2 的 entropy 上升 (-5.21→-3.83) 模式一致\n- 两个独立 non-CIVO 崩溃实例（008e_v3_s2 和 exp_038_s2）在不同配置下展示相似动态特征\n- 承认与 plasticity loss 的区分需要更深入分析，标注为 open question\n- exp_041_dual_critic_walker_s3: **data pending, expected 5/23** — 如果 s3 也崩溃 (2/4)，则 non-CIVO collapse 是系统性问题\n\n**证据**:\n- exp_008e_v3_s2: eval 715→452→137 (eval-driven), NVE 3.78 @105K (consequence not cause), entropy ↑ (-5.21→-3.83)\n- exp_038_dual_critic_walker_s2: eval peak 354 @155K → collapse to 99.6 @175K, NVE≤0.3 (CIVO prevented), entropy ↑ (-3.59→-0.45)\n- exp_009a_baseline_s2: eval 618→596→836 (stable) — 排除 seed fragility\n- exp_041_dual_critic_walker_s3: **data pending, expected 5/23 — determines collapse rate: 1/4 sporadic vs 2/4 systematic**\n\n**论文修改位置**: Section 5.6 (softened Pathway B discussion), Appendix D (comparison table: CIVO vs non-CIVO collapse signatures)\n\n---\n\n### [W-W5] RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性\n**Reviewer 原文摘要**: Table 4 的 reward MAE 不区分 over- vs under-prediction。需 signed error 验证 CIVO 机制假设。\n\n**回复要点**:\n- **Signed reward error analysis 已完成**\n- 关键发现：008d dt=2 shows **negative bias** (Mean SE = −0.599)，即**系统性低估**而非高估\n- 这排除了 \"observation-level reward overprediction\" 作为 CIVO 机制\n- CIVO 的 value overestimation 来自 **critic bootstrapping** (accumulated returns in imagination)，不是 per-step reward prediction bias\n- 分析使用 RSSM posterior（conditioned on real observations），而 CIVO 发生在 imagination 的 prior（无观测校正）\n- Baseline 校准良好 (Mean SE ≈ 0, Std 0.023)，确认方法论可靠\n\n**证据**:\n- artifact: `signed_reward_error.md` — 完整分析报告\n  - baseline dt=1: Mean SE = +0.001 (nearly perfect calibration)\n  - exp_008d dt=1: Mean SE = +0.018 (slight overprediction, 61.8% samples)\n  - exp_008d dt=2: Mean SE = **−0.599** (massive underprediction, only 8% overpredict)\n  - exp_008f dt=1: Mean SE = −0.710 (uncalibrated)\n  - exp_008f dt=2: Mean SE = −1.645 (uncalibrated)\n- 方法: 8 latest training episodes, encoder+RSSM+reward_head from checkpoint, signed error = predicted − actual\n\n**论文修改位置**: Section 6.1 (signed error analysis subsection), Table 5 (signed error table), Section 6.1 (mechanism refinement: CIVO via critic bootstrapping, not per-step overprediction)\n\n---\n\n### [W-W6] CIVO 与已知 value overestimation 的区分不够清晰\n**Reviewer 原文摘要**: CIVO 可能只是 compounding model error 的实例化。R1/R3 partial rebut: trained vs untrained 对比提供了机制特异性，但论文应更系统阐述。\n\n**回复要点**:\n- **Trained vs untrained dt_emb 对比**是超越 generic compounding error 的核心证据：\n  - exp_008d (trained dt_emb): NVE 2.09-4.12 → CIVO\n  - exp_008a (unexposed dt_emb): NVE 0.49-0.93 → no CIVO (3 seeds Walker + 2 seeds Cheetah, all safe)\n  - 如果仅是 compounding error，两者 dt=2 imagination 质量类似，应出现类似 overestimation — 但事实不同\n- **Signed error 双重证据**：\n  - dt=2 reward head 实际上 underpredicts (SE = −0.599) → CIVO 不是 reward-level compounding error\n  - Value overestimation 来自 critic 在 imagination 中的 bootstrapping，特异于 trained dt_emb 的 conditioning\n- **CIVO 与标准 overestimation 的关键区别**：\n  1. Standard overestimation (Fujimoto et al., 2018): 独立于 temporal conditioning，Double Q / ensemble 可缓解\n  2. CIVO: 特异于 trained temporal embedding，Double Q 失效 (v1≈v2, ρ>0.999)\n  - 这本身是区分证据：如果 CIVO 只是 standard overestimation，Double Q 应该有效\n\n**证据**:\n- exp_008d vs exp_008a: trained NVE=4.12 vs untrained NVE=0.93 (Walker), 同样 dt=2 transitions\n- exp_008a_cheetah: 2 seeds both NVE<0.5 (cross-env validated)\n- Signed error: exp_008d dt=2 SE = −0.599 (underprediction)\n- Dual-critic v1≈v2: ρ>0.999 in Walker (exp_032), exact match in Cheetah (exp_034) and PickCube (exp_036)\n\n**论文修改位置**: Section 2 (expanded Related Work: explicit CIVO vs generic overestimation), Section 6.1 (mechanism specificity argument), Section 4.4 (v1≈v2 as CIVO-specific evidence)\n\n---\n\n### [W-W7] Factorial design 部分对比存在混淆\n**Reviewer 原文摘要**: 008d vs 008a/008c 同时改变 embedding、subsampling、horizon 三个因素。R3 澄清核心对照 008d vs 008f 干净，但 primary vs secondary 区分不清。\n\n**回复要点**:\n- 论文已明确标注 **primary comparison** (008d vs 008f: 仅 dt_embed_dim 不同，其他因素相同) vs **secondary comparisons** (008c, 008a 等)\n- 新增 **2×2 mechanism factorial** (Walker)，cleanly isolates two factors:\n\n| | Single Critic | Dual Critic (min) |\n|--|--------------|-------------------|\n| ~1.05-1.2M params | Baseline: CIVO → permanent collapse | exp_035: CIVO (NVE 2.75) → full recovery (eval 697.8) |\n| ~2.4-2.9M params | exp_033: CIVO (NVE 4.75) → partial recovery (eval 408) | exp_032: CIVO prevented (NVE≤1.1, eval 787.7) |\n\n- 交互效应清晰：min alone → recovery; capacity alone → partial recovery; min+capacity → prevention\n\n**证据**:\n- Primary: exp_008d (dt_embed_dim=8, subsample ON, H=8) vs exp_008f (dt_embed_dim=0, subsample ON, H=8) — 唯一差异是 dt_embedding\n- 2×2 factorial: exp_032 (eval 787.7), exp_033 (eval 408), exp_035 (eval 697.8), baseline (collapse)\n- Secondary comparisons explicitly labeled in revised Table 1\n\n**论文修改位置**: Section 3 (Table 1: primary vs secondary column), Section 4.4 (2×2 factorial table + interaction analysis), Appendix (complete factorial grid with all cells)\n\n---\n\n### [W-W8] Related Work 遗漏 + Bibliography 冗余\n**Reviewer 原文摘要**: Becker-Ehmck et al. (2023), Park et al. (2021), Wang & Beltrame (2024), Colas et al. (2018) 在 bib 中未引用。77 条 bib 中 48 条 orphan。\n\n**回复要点**:\n- Bibliography 清理完成：原 77 条 → **43 条**（删除 34 条 orphan）\n- 4 篇遗漏论文已补充引用并在正文中讨论：\n  - Becker-Ehmck et al. (2023): Section 2, multi-timestep world model 先行工作\n  - Park et al. (2021): Section 2, time-discretization invariance 讨论\n  - Wang & Beltrame (2024): Section 2, elastic time steps\n  - Colas et al. (2018): Section 3 (methodology), seed 数量对 deep RL 结论可靠性的影响\n- 所有占位符 author 字段 (splates2025 等) 已修正\n\n**证据**:\n- 清理后 bibliography: 43 条，0 orphan entries\n- 正文新增引用: 4 篇 + DayDreamer, TD-MPC2 等 robotics 相关文献\n\n**论文修改位置**: References (全面清理), Section 2 (expanded Related Work)\n\n---\n\n## Questions for Authors\n\n### [Q1] 是否在其他 DMC 任务上做过初步验证？\n**回复**:\n- **Cheetah Run**: 完整验证。5 experiments:\n  - exp_010b_s0: NVE=70.64 (catastrophic CIVO, eval→0.83)\n  - exp_010b_s1: NVE=8.27 (severe CIVO, eval 51.7)\n  - exp_010a baseline: eval 849.8\n  - exp_008a_cheetah: 2 seeds, NVE 0.48-0.49 (unexposed dt_emb, no CIVO)\n  - Cheetah CIVO severity 10×+ 高于 Walker，且 dual-critic 仅部分抑制 (exp_034: NVE 1.75, eval 97.5 = 31% recovery)\n- **PickCube-v1 (ManiSkill2)**: manipulation 环境验证。\n  - exp_019b: NVE=3.78 @52.5K (transient CIVO, self-correcting), eval 26.6\n  - exp_019a_v2 baseline: eval 69.43\n  - CIVO 在 PickCube 不持续 — scope limitation (manipulation dynamics differ from locomotion)\n- exp_040_wide_dual_critic_cheetah: **data pending** — Cheetah dual-critic s1\n\n---\n\n### [Q2] Gradient stopping 为什么未测试？\n**回复**:\n- **已全面测试，系统性失败**。这是论文最重要的新增贡献之一。\n- Reward-only SGS (exp_016e): NVE=10.42× — 反效果。Reward head 梯度为 0（architectural no-op），迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差\n- Full-pathway SGS (exp_018v2, exp_018_s2, exp_021): 0/3。阻断所有非 KL 梯度仍失败 → forward-pass representational damage 不可逆\n- Obs-decoder-only SGS (exp_025 4 seeds, exp_026 2 seeds): 1/6。唯一 survive 的 seed (exp_025_s1) 仍有 value collapse (ve_ratio 0.056-0.14)\n- **总计 1/17 seeds across 3 SGS variants × 2 environments**\n- 核心发现：**gradient magnitude ≠ causal importance**（reward 38-49% gradient 但 reward-only SGS 最差；obs-decoder 16-22% gradient 但 obs-decoder SGS 也失败）\n- **替代方案**: frozen dt_emb (exp_042, running) 和 dual-critic (exp_032, 3/3 CIVO prevention) 作为 architecture-level interventions\n- Gradient stopping 本身因 **compensatory amplification** 无效：阻断 obs-decoder on Cheetah → NVE 从 8.3 放大到 21.9-30.2 (2.6-3.6×)\n\n---\n\n### [Q3] 能否补充 signed error 验证方向性？\n**回复**:\n- **已完成**。见 W-W5 详细回复。\n- 关键结果: exp_008d dt=2 Mean SE = −0.599 (underprediction), 排除 observation-level overprediction mechanism\n- Baseline dt=1 Mean SE = +0.001 (methodology validation)\n\n---\n\n### [Q4] TAWM 原文 Walker Walk 数据？\n**回复**:\n- 引用 TAWM (Nhu et al., ICML 2025) 原文中的 Walker Walk 具体数据\n- TAWM 使用 TD-MPC2 框架，dt-conditioning 在 MPC setting 中成功改善性能\n- 论文直接引用原文数据 + architectural difference 分析，不做因果声明\n- [GAP] 需确认 TAWM 原文中 Walker Walk 的具体数字（score/improvement %），当前引用为 \"improved performance\"\n\n---\n\n### [Q5] NVE 阈值 sensitivity analysis？\n**回复**:\n- **LOEO cross-validation 已完成**（见 W-C4）\n- θ from 0.5 to 5.0 (step 0.1) 全范围扫描\n- θ=1.5 在所有 3 个 training fold 的 optimal accuracy range 内\n- Mean held-out AUROC = 0.981, mean held-out accuracy = 0.974\n- 在 [1.2, 2.0] 范围内 accuracy 确实变化不大 — 但这恰好说明 NVE 分离度高（CIVO vs non-CIVO 的 NVE gap 远大于 θ 选择范围），而非 post-hoc fitting\n- Youden-optimal threshold from n=29: 1.53× (独立收敛)\n\n---\n\n### [Q6] 008e_v3 seed 2 (Pathway B) 的 actor action distribution？\n**回复**:\n- Actor entropy 数据已有：008e_v3_s2 entropy 从 -5.21 → -3.83（增加，策略变随机）vs 008d s1 entropy -3.47 → -4.88（减少，策略变确定）\n- 这是区分 CIVO (Pathway A: entropy ↓, exploitation lock-in) vs non-CIVO (Pathway B: entropy ↑, exploration-driven destabilization) 的关键指标\n- [GAP] 更详细的 action distribution analysis (per-dimension variance, action-space coverage) 未完成。可用 exp_038_s2 的 entropy 数据 (-3.59→-0.45) 作为第二个 non-CIVO 崩溃实例佐证\n- exp_041_dual_critic_walker_s3: **data pending, expected 5/23** — 如果 s3 也展示 entropy ↑ 崩溃模式，则 Pathway B 特征更加 robust\n\n---\n\n## Summary of Pending Data\n\n| Experiment | Purpose | Expected | Impact |\n|---|---|---|---|\n| exp_040_wide_dual_critic_cheetah | Cheetah dual-critic s1 robustness | 5/23 | W-C3: cross-env dual-critic data |\n| exp_041_dual_critic_walker_s3 | Non-CIVO collapse frequency (1/4 vs 2/4) | 5/23 | W-W4: Pathway B systematic vs sporadic |\n| exp_042_frozen_dt_emb_walker | Trained vs frozen vs removed dt_emb | 5/23 | W-W1: frozen dt_emb as mitigation; C2: causal refinement |\n| exp_043_008f_walker_s1 | 008f 5th seed replication | 5/23 | W-C2: additional statistical power |\n\nAll 4 experiments running on full GPU capacity. Data lock deadline: 5/25.\n\n---\n\n## Evidence Gap Summary\n\n| Concern | Evidence Status | Gap |\n|---------|----------------|-----|\n| W-C1 (venue fit) | ✅ PickCube added + robotics framing | None critical |\n| W-C2 (statistical power) | ✅ n=29, AUROC 0.953 | exp_042/043 pending (incremental) |\n| W-C3 (single env) | ✅ 3 environments | exp_040 pending (Cheetah dual-critic s1) |\n| W-C4 (NVE post-hoc) | ✅ LOEO AUROC 0.981 | None |\n| W-C5 (template) | ✅ Fixed | None |\n| W-W1 (no solution) | ✅ SGS 1/17 + dual-critic 3/3 + hierarchy | exp_042 pending (frozen dt_emb) |\n| W-W2 (TAWM) | ⚠️ Cite TAWM data, no reproduction | [GAP] TAWM 原文 Walker Walk 具体数字需确认 |\n| W-W3 (105K vs 505K) | ✅ Dual-critic to 210K | [GAP] 009b 未 extend，已弱化 \"self-correction\" |\n| W-W4 (Pathway B) | ⚠️ 2 instances (008e_v3_s2 + exp_038_s2) | exp_041 pending (collapse frequency) |\n| W-W5 (signed error) | ✅ Complete | None |\n| W-W6 (CIVO novelty) | ✅ trained vs untrained + signed error + v1≈v2 | None |\n| W-W7 (factorial confounds) | ✅ Primary vs secondary + 2×2 factorial | None |\n| W-W8 (bibliography) | ✅ 43 entries, 4 additions | None |\n| Q1 (other envs) | ✅ Cheetah + PickCube | exp_040 pending |\n| Q2 (gradient stopping) | ✅ SGS tested, failed | None |\n| Q3 (signed error) | ✅ Complete | None |\n| Q4 (TAWM data) | ⚠️ Partial | [GAP] 需确认 TAWM 原文具体数字 |\n| Q5 (sensitivity) | ✅ LOEO complete | None |\n| Q6 (action distribution) | ⚠️ Entropy data available | [GAP] Per-dimension action analysis not done |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01UorTTAxGKaNg19CU4aYRTP`</summary>

```json
{
  "name": "rebuttal_draft",
  "type": "report",
  "description": "Structured rebuttal response draft for Round 1 review, covering W-C1~C5, W-W1~W8, Q1~Q6 with specific exp_id evidence and data citations",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
  "tags": [
    "rebuttal",
    "review",
    "CoRL2026"
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
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "c00c968c-6ff8-4f62-9857-7ba15cd72de5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1vMV9CJoYnGRZeXAnBxzS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11253,
      "cache_read_input_tokens": 73143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11253
      },
      "output_tokens": 67,
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

_source line 71 · 2026-05-22T07:45:18.212Z_

<details><summary>↩ Tool result · `toolu_01UorTTAxGKaNg19CU4aYRTP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_339904\", \"name\": \"rebuttal_draft\", \"type\": \"report\", \"description\": \"Structured rebuttal response draft for Round 1 review, covering W-C1~C5, W-W1~W8, Q1~Q6 with specific exp_id evidence and data citations\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:45:17.890777+00:00\", \"tags\": [\"rebuttal\", \"review\", \"CoRL2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "49b38a95-131c-40df-ab1f-bb4399c21a5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_339904\\\", \\\"name\\\": \\\"rebuttal_draft\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Structured rebuttal response draft for Round 1 review, covering W-C1~C5, W-W1~W8, Q1~Q6 with specific exp_id evidence and data citations\\\", \\\"path\\\": \\\"projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"event-gated-adaptive-horizon\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T07:45:17.890777+00:00\\\", \\\"tags\\\": [\\\"rebuttal\\\", \\\"review\\\", \\\"CoRL2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_339904\", \"name\": \"rebuttal_draft\", \"type\": \"report\", \"description\": \"Structured rebuttal response draft for Round 1 review, covering W-C1~C5, W-W1~W8, Q1~Q6 with specific exp_id evidence and data citations\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:45:17.890777+00:00\", \"tags\": [\"rebuttal\", \"review\", \"CoRL2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 72_

Rebuttal draft 已保存并注册。

**覆盖情况**:
- **5 Critical Issues** (W-C1~C5): 全部有具体实验证据回复。W-C1 增加 PickCube + robotics framing，W-C2 从 n=8→n=29 AUROC 0.953，W-C3 扩展至 3 环境，W-C4 LOEO AUROC 0.981，W-C5 模板已修。
- **8 Warning Issues** (W-W1~W8): 全部回复。W-W1 最重要——SGS 1/17 失败 + dual-critic 3/3 prevention + 4-level hierarchy 作为独立贡献。
- **6 Questions** (Q1~Q6): 全部回复，Q2/Q3/Q5 已有完整数据。

**待补数据** (4 experiments running, expected 5/23):
- exp_040: Cheetah dual-critic s1
- exp_041: Walker dual-critic s3 (non-CIVO collapse 频率)
- exp_042: frozen dt_emb (trained vs frozen vs removed 三向对比)
- exp_043: 008f s1 replication

**标注的 GAP**:
- TAWM 原文 Walker Walk 具体数字需确认
- 009b self-correction 未 extend beyond 105K
- Per-dimension action distribution analysis 未完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "uuid": "91eaef31-edda-4bb2-a014-81d24fcd1659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqyYnJEAmX58fzmnHj3cx1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 84396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 550
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

_source line 73_

Rebuttal draft 已保存并注册。

**覆盖情况**:
- **5 Critical Issues** (W-C1~C5): 全部有具体实验证据回复。W-C1 增加 PickCube + robotics framing，W-C2 从 n=8→n=29 AUROC 0.953，W-C3 扩展至 3 环境，W-C4 LOEO AUROC 0.981，W-C5 模板已修。
- **8 Warning Issues** (W-W1~W8): 全部回复。W-W1 最重要——SGS 1/17 失败 + dual-critic 3/3 prevention + 4-level hierarchy 作为独立贡献。
- **6 Questions** (Q1~Q6): 全部回复，Q2/Q3/Q5 已有完整数据。

**待补数据** (4 experiments running, expected 5/23):
- exp_040: Cheetah dual-critic s1
- exp_041: Walker dual-critic s3 (non-CIVO collapse 频率)
- exp_042: frozen dt_emb (trained vs frozen vs removed 三向对比)
- exp_043: 008f s1 replication

**标注的 GAP**:
- TAWM 原文 Walker Walk 具体数字需确认
- 009b self-correction 未 extend beyond 105K
- Per-dimension action distribution analysis 未完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 501895,
  "duration_api_ms": 502778,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "7099b989-f5c3-4806-9b9b-a499172a4b8e",
  "total_cost_usd": 1.5373305000000002,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 73499,
    "cache_read_input_tokens": 346645,
    "output_tokens": 13622,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 73499,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 394,
        "cache_read_input_tokens": 84396,
        "cache_creation_input_tokens": 550,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 550
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2493,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002583,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 23,
      "outputTokens": 22535,
      "cacheReadInputTokens": 546240,
      "cacheCreationInputTokens": 111702,
      "webSearchRequests": 0,
      "costUSD": 1.5347475000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "680fa2ff-bc17-4384-bbcd-7d7d4b6fbc9a"
}
```

</details>

---
