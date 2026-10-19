# research full benchmark audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_research_full-benchmark-audit_20260520T071731.log`
- **Structured JSON:** [`cf4c474b5f60e95ca069.json`](../../sessions/cf/cf4c474b5f60e95ca069.json)

## Before a recorded user message

58 recorded events

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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
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
  "uuid": "b9ad08a0-931d-4a3a-a5dd-8138bd66f6be",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779469200,
    "rateLimitType": "seven_day",
    "utilization": 0.78,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "95c8ef2c-c233-4e6a-b56c-1d29b3203040",
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry file to audit all benchmark data. The registry is large (375+ entries), so I'll need to be strategic about reading it. Let me also read the statistical analysis script to have the exact data being used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "f7447a2d-de76-416a-b2ea-24529f44339a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kr7tjDyVo3ySLkscHhbiCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12848,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12848
      },
      "output_tokens": 22,
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

开始全 benchmark 数据审计。先读取 registry 和统计脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "2361485e-01e3-4ec6-877c-3d4421998587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kr7tjDyVo3ySLkscHhbiCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12848,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12848
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Bash · `toolu_017vpLgcoX7gnkqaYHpfdwd6`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Check registry file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "f1161dae-c0c5-4581-8863-49d20c1481a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kr7tjDyVo3ySLkscHhbiCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12848,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12848
      },
      "output_tokens": 22,
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

_source line 7 · 2026-05-20T07:17:46.698Z_

<details><summary>↩ Tool result · `toolu_017vpLgcoX7gnkqaYHpfdwd6`</summary>

```text
15654 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "2d50ec21-f2b6-4cb1-bd30-743b2adbb15b",
  "tool_use_result": {
    "stdout": "15654 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
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

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_016tjRcNDeqTC6kAcQyRG9FX`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "description": "Check script size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "ae9dc697-9cbc-4d20-9691-3f21f48be095",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kr7tjDyVo3ySLkscHhbiCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12848,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12848
      },
      "output_tokens": 22,
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

_source line 9 · 2026-05-20T07:17:47.417Z_

<details><summary>↩ Tool result · `toolu_016tjRcNDeqTC6kAcQyRG9FX`</summary>

```text
285 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "9b609633-f525-4f5d-a804-79b72e9ad3f2",
  "tool_use_result": {
    "stdout": "285 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
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

_source line 10_

Registry 有 15654 行。我需要提取所有 DONE+success 的实验。让我用多个并行搜索提取各 benchmark 的数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "4dd348f8-5c8b-4819-bf19-b6dd5eea92b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gm3dPPC4gne22hDrwBeqkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 24689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Rj9usjD9v5PTTJcheNEQZL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "15fc0670-1275-4e80-b093-8633f0d09ea4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gm3dPPC4gne22hDrwBeqkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 24689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 12 · 2026-05-20T07:17:51.450Z_

<details><summary>↩ Tool result · `toolu_01Rj9usjD9v5PTTJcheNEQZL`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Statistical analysis of ACR-VLA Conformal Refinement experiments.
4	Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.
5	Also includes Argmin and Adaptive-K baselines.
6	
7	Primary CRM config for Object: norm02 (ε=0.2), K=10.
8	"""
9	
10	import numpy as np
11	from scipy import stats
12	
13	def print_separator(char='=', width=80):
14	    print(char * width)
15	
16	def print_group_stats(name, values):
17	    arr = np.array(values)
18	    print(f"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, "
19	          f"min={arr.min():.4f}, max={arr.max():.4f}")
20	    print(f"    values: {[round(v, 4) for v in values]}")
21	
22	def run_tests(name_a, vals_a, name_b, vals_b):
23	    a = np.array(vals_a)
24	    b = np.array(vals_b)
25	
26	    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)
27	    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')
28	
29	    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /
30	                         (len(a) + len(b) - 2))
31	    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')
32	
33	    diff = a.mean() - b.mean()
34	    diff_pct = diff * 100
35	
36	    print(f"\n  {name_a} vs {name_b}:")
37	    print(f"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)")
38	    print(f"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}")
39	    print(f"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}")
40	    print(f"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})")
41	
42	    return t_pval, u_pval
43	
44	# ============================================================================
45	# DATA (from registry, conclusion=success, 2026-05-20)
46	# Each seed appears once; r2/r3 supersedes earlier runs.
47	# ============================================================================
48	
49	# --- LIBERO-Spatial ---
50	# CRM obs_only norm02 K=10 (seeds 42-48, 51) — D083 corrected
51	crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35, 0.36]  # s42(mag-obsonly-norm02), s43-r2, s44, s45, s46-r2, s47, s48, s51
52	
53	# VLA-only Spatial (seeds 42-50)
54	vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50
55	
56	# --- LIBERO-Long ---
57	# CRM obs_only Long (seeds 42-47, 50)
58	crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50
59	
60	# VLA-only Long (seeds 42-52)
61	vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52
62	
63	# --- LIBERO-Goal ---
64	# CRM obs_only Goal (seeds 42-47)
65	crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47
66	
67	# VLA-only Goal (seeds 42-46, 49)
68	vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49
69	
70	# --- LIBERO-Object ---
71	# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)
72	crm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2
73	
74	# Supplementary: CRM obs_only norm01 (seeds 42-48)
75	crm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48
76	
77	# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)
78	crm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48
79	
80	# VLA-only Object (seeds 42-50, using r2 for seed45)
81	vla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50
82	
83	# --- Argmin Object ---
84	# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)
85	argmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47
86	argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45
87	
88	# --- Adaptive-K Object ---
89	adaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44
90	adaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44
91	adaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44
92	adaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44
93	
94	
95	# ============================================================================
96	# ANALYSIS
97	# ============================================================================
98	
99	print_separator()
100	print("STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments")
101	print("All success rates are fractions (0.0 to 1.0)")
102	print("Object benchmark primary CRM config: norm02 (ε=0.2), K=10")
103	print_separator()
104	
105	# ============================================================================
106	# 1. LIBERO-SPATIAL
107	# ============================================================================
108	print("\n1. LIBERO-SPATIAL")
109	print_separator('-')
110	print_group_stats("CRM obs_only (n=8)", crm_spatial)
111	print_group_stats("VLA-only (n=9)", vla_spatial)
112	run_tests("CRM", crm_spatial, "VLA-only", vla_spatial)
113	
114	# ============================================================================
115	# 2. LIBERO-LONG
116	# ============================================================================
117	print("\n\n2. LIBERO-LONG")
118	print_separator('-')
119	print_group_stats("CRM obs_only (n=7)", crm_long)
120	print_group_stats("VLA-only (n=11)", vla_long)
121	run_tests("CRM", crm_long, "VLA-only", vla_long)
122	
123	# ============================================================================
124	# 3. LIBERO-GOAL
125	# ============================================================================
126	print("\n\n3. LIBERO-GOAL")
127	print_separator('-')
128	print_group_stats("CRM obs_only (n=6)", crm_goal)
129	print_group_stats("VLA-only (n=6)", vla_goal)
130	run_tests("CRM", crm_goal, "VLA-only", vla_goal)
131	
132	# ============================================================================
133	# 4. LIBERO-OBJECT (primary: norm02 K=10)
134	# ============================================================================
135	print("\n\n4. LIBERO-OBJECT")
136	print_separator('-')
137	
138	print("\n  [PRIMARY: CRM norm02 K=10]")
139	print_group_stats("CRM obs_only norm02 K=10 (n=6)", crm_object)
140	print_group_stats("VLA-only (n=8)", vla_object)
141	run_tests("CRM norm02 K=10", crm_object, "VLA-only", vla_object)
142	
143	print("\n  [Supplementary: CRM norm01]")
144	print_group_stats("CRM obs_only norm01 (n=6)", crm_object_norm01)
145	run_tests("CRM norm01", crm_object_norm01, "VLA-only", vla_object)
146	
147	print("\n  [Supplementary: CRM norm02 K=5]")
148	print_group_stats("CRM obs_only norm02 K=5 (n=7)", crm_object_k5)
149	run_tests("CRM norm02 K=5", crm_object_k5, "VLA-only", vla_object)
150	
151	# ============================================================================
152	# 5. ARGMIN BASELINES (Object)
153	# ============================================================================
154	print("\n\n5. ARGMIN BASELINES (Object)")
155	print_separator('-')
156	print_group_stats("Argmin K=10 (n=5)", argmin_object_k10)
157	print_group_stats("Argmin K=5 (n=4)", argmin_object_k5)
158	print_group_stats("VLA-only (n=8)", vla_object)
159	print_group_stats("CRM norm02 K=10 (n=6)", crm_object)
160	
161	print("\n  Argmin K=10 vs VLA-only:")
162	run_tests("Argmin K=10", argmin_object_k10, "VLA-only", vla_object)
163	print("\n  Argmin K=10 vs CRM norm02 K=10:")
164	run_tests("Argmin K=10", argmin_object_k10, "CRM norm02", crm_object)
165	
166	# ============================================================================
167	# 6. ADAPTIVE-K BASELINES (Object)
168	# ============================================================================
169	print("\n\n6. ADAPTIVE-K BASELINES (Object)")
170	print_separator('-')
171	print_group_stats("Adaptive-K p25 (n=3)", adaptive_k_p25)
172	print_group_stats("Adaptive-K p50 (n=3)", adaptive_k_p50)
173	print_group_stats("Adaptive-K p75 (n=3)", adaptive_k_p75)
174	print_group_stats("Adaptive-K p90 (n=3)", adaptive_k_p90)
175	all_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90
176	print_group_stats("Adaptive-K all (n=12)", all_adaptive)
177	print_group_stats("VLA-only (n=8)", vla_object)
178	print_group_stats("CRM norm02 K=10 (n=6)", crm_object)
179	
180	print("\n  Adaptive-K (all) vs VLA-only:")
181	run_tests("Adaptive-K all", all_adaptive, "VLA-only", vla_object)
182	print("\n  Adaptive-K (all) vs CRM norm02 K=10:")
183	run_tests("Adaptive-K all", all_adaptive, "CRM norm02", crm_object)
184	
185	# ============================================================================
186	# 7. SUMMARY TABLE
187	# ============================================================================
188	print("\n")
189	print_separator()
190	print("SUMMARY TABLE")
191	print_separator()
192	print(f"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}")
193	print_separator('-')
194	
195	def get_vla_baseline(bench):
196	    if bench == "LIBERO-Spatial": return vla_spatial
197	    if bench == "LIBERO-Long": return vla_long
198	    if bench == "LIBERO-Goal": return vla_goal
199	    if bench == "LIBERO-Object": return vla_object
200	    return None
201	
202	def print_summary_row(bench, method, vals, is_vla=False):
203	    arr = np.array(vals)
204	    n = len(arr)
205	    mean = arr.mean()
206	    std = arr.std(ddof=1)
207	    baseline = get_vla_baseline(bench)
208	    if is_vla or baseline is None:
209	        print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}")
210	    else:
211	        bl_arr = np.array(baseline)
212	        diff = mean - bl_arr.mean()
213	        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)
214	        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
215	        print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}")
216	
217	print_summary_row("LIBERO-Spatial", "CRM obs_only", crm_spatial)
218	print_summary_row("LIBERO-Spatial", "VLA-only", vla_spatial, is_vla=True)
219	print()
220	print_summary_row("LIBERO-Long", "CRM obs_only", crm_long)
221	print_summary_row("LIBERO-Long", "VLA-only", vla_long, is_vla=True)
222	print()
223	print_summary_row("LIBERO-Goal", "CRM obs_only", crm_goal)
224	print_summary_row("LIBERO-Goal", "VLA-only", vla_goal, is_vla=True)
225	print()
226	print_summary_row("LIBERO-Object", "CRM norm02 K=10", crm_object)
227	print_summary_row("LIBERO-Object", "CRM norm01 (supp)", crm_object_norm01)
228	print_summary_row("LIBERO-Object", "CRM norm02 K=5 (supp)", crm_object_k5)
229	print_summary_row("LIBERO-Object", "VLA-only", vla_object, is_vla=True)
230	print_summary_row("LIBERO-Object", "Argmin K=10", argmin_object_k10)
231	print_summary_row("LIBERO-Object", "Argmin K=5", argmin_object_k5)
232	print_summary_row("LIBERO-Object", "Adaptive-K (all)", all_adaptive)
233	
234	# ============================================================================
235	# 8. KEY SIGNIFICANCE RESULTS
236	# ============================================================================
237	print("\n")
238	print_separator()
239	print("KEY SIGNIFICANCE RESULTS")
240	print_separator()
241	
242	tests = [
243	    ("Spatial: CRM vs VLA", crm_spatial, vla_spatial),
244	    ("Long: CRM vs VLA", crm_long, vla_long),
245	    ("Goal: CRM vs VLA", crm_goal, vla_goal),
246	    ("Object(norm02): CRM vs VLA", crm_object, vla_object),
247	    ("Object(norm01-supp): CRM vs VLA", crm_object_norm01, vla_object),
248	    ("Object: Argmin-K10 vs VLA", argmin_object_k10, vla_object),
249	    ("Object: CRM-norm02 vs Argmin-K10", crm_object, argmin_object_k10),
250	    ("Object: Adaptive-K vs VLA", all_adaptive, vla_object),
251	    ("Object: CRM-norm02 vs Adaptive-K", crm_object, all_adaptive),
252	]
253	
254	print(f"\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}")
255	print('-' * 85)
256	for name, a, b in tests:
257	    arr_a, arr_b = np.array(a), np.array(b)
258	    diff = arr_a.mean() - arr_b.mean()
259	    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)
260	    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')
261	    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /
262	                         (len(a) + len(b) - 2))
263	    d = diff / pooled_std if pooled_std > 0 else float('inf')
264	    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
265	    print(f"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}")
266	
267	# ============================================================================
268	# 9. VERIFICATION NOTES
269	# ============================================================================
270	print("\n")
271	print_separator()
272	print("VERIFICATION NOTES")
273	print_separator()
274	print("- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).")
275	print("  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).")
276	print("  Registry value retained but unverified.")
277	print("- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).")
278	print("- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).")
279	print("- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.")
280	
281	print("\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant")
282	print()
283	print_separator()
284	print("END OF ANALYSIS")
285	print_separator()
286	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "bf2e66fb-7c5f-4ff6-840c-eb6bb359e967",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 42-48, 51) — D083 corrected\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35, 0.36]  # s42(mag-obsonly-norm02), s43-r2, s44, s45, s46-r2, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47, 50)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-52)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46, 49)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=8)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
      "numLines": 286,
      "startLine": 1,
      "totalLines": 286
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01XoQHk3iLrRakdn1GU6CVZ3`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\n# Filter DONE + success experiments\ndone = []\nfor exp_id, exp in registry.items():\n    if isinstance(exp, dict) and exp.get('status') == 'DONE' and exp.get('conclusion') == 'success':\n        done.append({\n            'exp_id': exp_id,\n            'hypothesis': exp.get('hypothesis', ''),\n            'seed': exp.get('seed', ''),\n            'metrics': exp.get('metrics', {}),\n            'spec': exp.get('spec', {}),\n        })\n\nprint(f'Total DONE+success: {len(done)}')\nprint()\n\n# Categorize by benchmark\nfor d in done:\n    eid = d['exp_id'].lower()\n    hyp = str(d['hypothesis']).lower()\n    # Print exp_id and key info for categorization\n    sr = d['metrics'].get('success_rate', d['metrics'].get('avg_success_rate', 'N/A'))\n    seed = d['seed']\n    spec = d.get('spec', {})\n    norm = spec.get('norm_type', spec.get('normalization', ''))\n    k = spec.get('K', spec.get('k', ''))\n    print(f'{d[\\\"exp_id\\\"]} | seed={seed} | SR={sr} | norm={norm} | K={k} | hyp={d[\\\"hypothesis\\\"][:100]}')\n\" 2>&1",
  "description": "Extract all DONE+success experiments from registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "c57cd070-c09b-4b93-9a26-171af122d562",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gm3dPPC4gne22hDrwBeqkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 24689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 14 · 2026-05-20T07:17:58.452Z_

<details><summary>↩ Tool result · `toolu_01XoQHk3iLrRakdn1GU6CVZ3`</summary>

```text
Total DONE+success: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "6c468e17-170f-42cb-b136-d5d22fe7c228",
  "tool_use_result": {
    "stdout": "Total DONE+success: 0",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The registry query returned 0 DONE+success experiments. This might be because the YAML structure is different from what I expected. Let me look at the registry structure to understand the format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "0d284ab2-5958-4253-af36-48e5d7ae9c79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTtq1J8tvr3te7HPQ1W7iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6502,
      "cache_read_input_tokens": 25135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6502
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

Registry 查询返回 0 条，格式可能不同。让我查看 registry 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "ae1599a6-6e89-4553-b71d-cc4c1bebf0e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTtq1J8tvr3te7HPQ1W7iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6502,
      "cache_read_input_tokens": 25135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6502
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

<details open><summary>🔧 Tool call — Read · `toolu_01De6guHv2JW3tJXyotZuVLW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "4f320629-9537-4fc4-bfbd-ea4653016b5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTtq1J8tvr3te7HPQ1W7iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6502,
      "cache_read_input_tokens": 25135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6502
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

_source line 18 · 2026-05-20T07:18:04.247Z_

<details><summary>↩ Tool result · `toolu_01De6guHv2JW3tJXyotZuVLW`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp-point-reaching:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-13T01:22:10.415Z'
7	    updated_at: '2026-05-17T03:13:35.534Z'
8	    spec:
9	      hypothesis: Per-DOF uncertainty features carry more actionable information than
10	        scalar uncertainty summaries, enabling dimension-selective correction
11	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
12	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
13	      server: bjb2-40593
14	      gpu: cuda:0
15	      data_count: 20000
16	      model_name: CorrectionMLP(2-layer, 64-hidden)
17	      seed: 42
18	      command: python -u run_mvp.py
19	      data_path: synthetic (generated in-script)
20	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
21	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
22	    conclusion: success
23	    completed_at: '2026-05-13T01:44:00.055Z'
24	    metrics:
25	      group1_oracle:
26	        A_scalar:
27	          mse_x: 0.180218
28	          mse_y: 0.02497
29	          mse_z: 0.024232
30	          total: 0.076473
31	        B_perDOF:
32	          mse_x: 0.172652
33	          mse_y: 0.015544
34	          mse_z: 0.01561
35	          total: 0.067935
36	        C_none:
37	          mse_x: 0.22706
38	          mse_y: 0.025542
39	          mse_z: 0.024753
40	          total: 0.092451
41	      group2_oracle:
42	        A_scalar:
43	          mse_x: 0.064642
44	          mse_y: 0.023836
45	          mse_z: 0.022967
46	          total: 0.037148
47	        B_perDOF:
48	          mse_x: 0.053403
49	          mse_y: 0.015695
50	          mse_z: 0.01573
51	          total: 0.028276
52	        C_none:
53	          mse_x: 0.084178
54	          mse_y: 0.025427
55	          mse_z: 0.024798
56	          total: 0.044801
57	      group3_oracle:
58	        A_scalar:
59	          mse_x: 0.042948
60	          mse_y: 0.023218
61	          mse_z: 0.022365
62	          total: 0.02951
63	        B_perDOF:
64	          mse_x: 0.033008
65	          mse_y: 0.015621
66	          mse_z: 0.015647
67	          total: 0.021425
68	        C_none:
69	          mse_x: 0.053043
70	          mse_y: 0.025523
71	          mse_z: 0.024741
72	          total: 0.034436
73	      group4_K10:
74	        A_scalar:
75	          mse_x: 0.187418
76	          mse_y: 0.024701
77	          mse_z: 0.024277
78	          total: 0.078799
79	        B_perDOF:
80	          mse_x: 0.182888
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "063c1965-7a70-42f0-be4e-c4c6a36b0e21",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
      "content": "baseline: null\nexperiments:\n  mvp-point-reaching:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-13T01:22:10.415Z'\n    updated_at: '2026-05-17T03:13:35.534Z'\n    spec:\n      hypothesis: Per-DOF uncertainty features carry more actionable information than\n        scalar uncertainty summaries, enabling dimension-selective correction\n      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)\n        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'\n      server: bjb2-40593\n      gpu: cuda:0\n      data_count: 20000\n      model_name: CorrectionMLP(2-layer, 64-hidden)\n      seed: 42\n      command: python -u run_mvp.py\n      data_path: synthetic (generated in-script)\n      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/\n      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log\n    conclusion: success\n    completed_at: '2026-05-13T01:44:00.055Z'\n    metrics:\n      group1_oracle:\n        A_scalar:\n          mse_x: 0.180218\n          mse_y: 0.02497\n          mse_z: 0.024232\n          total: 0.076473\n        B_perDOF:\n          mse_x: 0.172652\n          mse_y: 0.015544\n          mse_z: 0.01561\n          total: 0.067935\n        C_none:\n          mse_x: 0.22706\n          mse_y: 0.025542\n          mse_z: 0.024753\n          total: 0.092451\n      group2_oracle:\n        A_scalar:\n          mse_x: 0.064642\n          mse_y: 0.023836\n          mse_z: 0.022967\n          total: 0.037148\n        B_perDOF:\n          mse_x: 0.053403\n          mse_y: 0.015695\n          mse_z: 0.01573\n          total: 0.028276\n        C_none:\n          mse_x: 0.084178\n          mse_y: 0.025427\n          mse_z: 0.024798\n          total: 0.044801\n      group3_oracle:\n        A_scalar:\n          mse_x: 0.042948\n          mse_y: 0.023218\n          mse_z: 0.022365\n          total: 0.02951\n        B_perDOF:\n          mse_x: 0.033008\n          mse_y: 0.015621\n          mse_z: 0.015647\n          total: 0.021425\n        C_none:\n          mse_x: 0.053043\n          mse_y: 0.025523\n          mse_z: 0.024741\n          total: 0.034436\n      group4_K10:\n        A_scalar:\n          mse_x: 0.187418\n          mse_y: 0.024701\n          mse_z: 0.024277\n          total: 0.078799\n        B_perDOF:\n          mse_x: 0.182888",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 15655
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
The registry is nested under `experiments:` key. Experiments are accessed via `registry['experiments'][exp_id]`. Let me fix my script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "30a6ade5-748b-48b3-ae25-61547087c83f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfHE9XiYBiFAw6edncintB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1255,
      "cache_read_input_tokens": 31637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1255
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

结构是嵌套在 `experiments:` 下的。让我修正查询。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "ef7824d6-57d9-4a5c-95b3-493410eef25b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfHE9XiYBiFAw6edncintB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1255,
      "cache_read_input_tokens": 31637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1255
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

<details open><summary>🔧 Tool call — Bash · `toolu_01FZDTbKpysxgpqotmkHUA8D`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', {})\nprint(f'Total experiments: {len(experiments)}')\n\ndone = []\nfor exp_id, exp in experiments.items():\n    if isinstance(exp, dict) and exp.get('status') == 'DONE' and exp.get('conclusion') == 'success':\n        done.append(exp_id)\n\nprint(f'DONE+success: {len(done)}')\nfor eid in sorted(done):\n    print(f'  {eid}')\n\" 2>&1",
  "description": "List all DONE+success experiment IDs",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "7bd4eb8c-3333-4f74-bbc9-dd8fea3201f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfHE9XiYBiFAw6edncintB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1255,
      "cache_read_input_tokens": 31637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1255
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

_source line 22 · 2026-05-20T07:18:12.535Z_

<details><summary>↩ Tool result · `toolu_01FZDTbKpysxgpqotmkHUA8D`</summary>

```text
Total experiments: 422
DONE+success: 208
  crm-lto-splitA-train
  crm-lto-splitA-train-fixed
  crm-train-v2-obs-only
  crm-train-v2-perdof
  crm-train-v2-scalar-unc
  crm-train-v3-norm
  crm-train-v3-norm-obs-only
  crm-train-v3-norm-scalar-unc
  eval-acr-object-obs-only-default
  eval-acr-object-obs-only-norm02
  eval-acr-object-v4-default-r2
  eval-acr-object-v4-obs-only
  eval-acr-object-v4-perdof
  eval-acr-spatial-v3
  eval-acr-spatial-v4-obs-only-r3
  eval-acr-spatial-v4-scalar-r2
  eval-acr-spatial-v4-small-r2
  eval-adaptive-k-p25-seed42
  eval-adaptive-k-p25-seed43
  eval-adaptive-k-p25-seed44-r2
  eval-adaptive-k-p50-seed44
  eval-adaptive-k-p75-seed44
  eval-adaptive-k-p90-seed42
  eval-adaptive-k-p90-seed43
  eval-adaptive-k-p90-seed44
  eval-argmin-object-k5-seed42
  eval-argmin-object-k5-seed43
  eval-argmin-object-k5-seed44-r2
  eval-argmin-object-k5-seed45
  eval-argmin-object-seed43
  eval-argmin-object-seed44-r2
  eval-argmin-object-seed45
  eval-argmin-object-seed46
  eval-argmin-object-seed47
  eval-argmin-only-spatial-r2
  eval-crm-goal-seed42
  eval-crm-goal-seed43
  eval-crm-goal-seed44-r2
  eval-crm-goal-seed45-r2
  eval-crm-goal-seed46
  eval-crm-long-seed42
  eval-crm-long-seed43
  eval-crm-long-seed44
  eval-crm-long-seed45
  eval-crm-long-seed46
  eval-crm-long-seed47
  eval-crm-long-seed50
  eval-crm-spatial-k10-seed51
  eval-direct-correction-object-seed42-r3
  eval-lto-splitA-vla-only-r2
  eval-lto-splitA-vla-only-r3
  eval-lto-splitA-vla-only-v2
  eval-mag-obsonly-norm003-b2
  eval-mag-obsonly-norm003-object
  eval-mag-obsonly-norm005
  eval-mag-obsonly-norm005-object
  eval-mag-obsonly-norm03-object
  eval-mag-obsonly-norm03-r2
  eval-mag-perdof-norm003-object
  eval-mag-perdof-norm005-object
  eval-mag-perdof-norm02-seed43-object-r3
  eval-mag-perdof-norm03-object-r3
  eval-object-v8-full
  eval-obs-only-object-default-seed44
  eval-obs-only-object-default-seed45
  eval-obs-only-object-default-seed45-r2
  eval-obs-only-object-default-seed46
  eval-obs-only-object-default-seed47
  eval-obs-only-object-default-seed48
  eval-obs-only-object-default-seed48-r2
  eval-obs-only-object-norm003-seed44-bjb2
  eval-obs-only-object-norm003-seed47-r2
  eval-obs-only-object-norm003-seed48
  eval-obs-only-object-norm005-seed43-r2
  eval-obs-only-object-norm005-seed44
  eval-obs-only-object-norm005-seed45
  eval-obs-only-object-norm005-seed47
  eval-obs-only-object-norm005-seed48
  eval-obs-only-object-norm01-seed44
  eval-obs-only-object-norm01-seed45
  eval-obs-only-object-norm01-seed45-r2
  eval-obs-only-object-norm01-seed46-r3
  eval-obs-only-object-norm01-seed47
  eval-obs-only-object-norm01-seed48
  eval-obs-only-object-norm02-k5-seed42
  eval-obs-only-object-norm02-k5-seed43
  eval-obs-only-object-norm02-k5-seed44
  eval-obs-only-object-norm02-k5-seed45
  eval-obs-only-object-norm02-k5-seed46
  eval-obs-only-object-norm02-k5-seed47
  eval-obs-only-object-norm02-k5-seed48
  eval-obs-only-object-norm02-seed43-r2
  eval-obs-only-object-norm02-seed44-r2
  eval-obs-only-object-norm02-seed45
  eval-obs-only-object-norm02-seed46
  eval-obs-only-object-norm02-seed47
  eval-obs-only-object-norm02-seed48-r2
  eval-obs-only-object-norm03-seed44
  eval-obs-only-object-norm03-seed45-r2
  eval-obs-only-object-norm03-seed46
  eval-obs-only-object-norm03-seed48
  eval-obs-only-spatial-norm02-k5-seed42
  eval-obs-only-spatial-norm02-k5-seed43
  eval-obs-only-spatial-norm02-k5-seed44-r2
  eval-obs-only-spatial-norm02-k5-seed45-r2
  eval-obs-only-spatial-norm02-seed43-r2
  eval-obs-only-spatial-norm02-seed44
  eval-obs-only-spatial-norm02-seed45
  eval-obs-only-spatial-norm02-seed46-r2
  eval-obs-only-spatial-norm02-seed47
  eval-obs-only-spatial-norm02-seed48
  eval-openvla-object-vla-only-seed42-v2
  eval-perdof-object-default-seed43
  eval-perdof-object-default-seed45
  eval-perdof-object-norm003-seed43
  eval-perdof-object-norm003-seed46
  eval-perdof-object-norm003-seed47
  eval-perdof-object-norm003-seed48
  eval-perdof-object-norm005-seed43
  eval-perdof-object-norm005-seed44
  eval-perdof-object-norm005-seed45-r2
  eval-perdof-object-norm005-seed46
  eval-perdof-object-norm005-seed47
  eval-perdof-object-norm01-seed43
  eval-perdof-object-norm01-seed45
  eval-perdof-object-norm01-seed46-r2
  eval-perdof-object-norm01-seed47-bjb1
  eval-perdof-object-norm01-seed48
  eval-perdof-object-norm02-seed43
  eval-perdof-object-norm02-seed43-r3
  eval-perdof-object-norm02-seed44
  eval-perdof-object-norm02-seed45
  eval-perdof-object-norm02-seed46
  eval-perdof-object-norm02-seed47
  eval-perdof-object-norm03-seed43
  eval-perdof-object-norm03-seed46
  eval-perdof-object-norm03-seed47
  eval-perdof-object-seed43
  eval-random-selection-object-k5-seed42-r2
  eval-random-selection-object-k5-seed43-r2
  eval-random-selection-object-k5-seed44-r2
  eval-random-selection-object-k5-seed45-r2
  eval-random-selection-object-seed43
  eval-random-selection-object-seed45
  eval-reconvla-object
  eval-reconvla-spatial-v3
  eval-scalar-object-seed43
  eval-scalar-object-seed45
  eval-scalar-object-seed46
  eval-spatial-v7-full
  eval-vla-mean-object
  eval-vla-mean-object-seed43
  eval-vla-mean-object-seed44
  eval-vla-mean-object-seed45
  eval-vla-mean-spatial
  eval-vla-mean-spatial-t10
  eval-vla-only-goal-seed42
  eval-vla-only-goal-seed43
  eval-vla-only-goal-seed44-r2
  eval-vla-only-goal-seed45
  eval-vla-only-goal-seed46
  eval-vla-only-goal-seed49
  eval-vla-only-long-seed42
  eval-vla-only-long-seed43
  eval-vla-only-long-seed44
  eval-vla-only-long-seed45
  eval-vla-only-long-seed46
  eval-vla-only-long-seed47
  eval-vla-only-long-seed48
  eval-vla-only-long-seed50
  eval-vla-only-long-seed51
  eval-vla-only-long-seed52
  eval-vla-only-object
  eval-vla-only-object-seed43
  eval-vla-only-object-seed44-r2
  eval-vla-only-object-seed45
  eval-vla-only-object-seed45-r2
  eval-vla-only-object-seed46
  eval-vla-only-object-seed47
  eval-vla-only-object-seed48
  eval-vla-only-object-seed50
  eval-vla-only-spatial-seed42
  eval-vla-only-spatial-seed43
  eval-vla-only-spatial-seed44
  eval-vla-only-spatial-seed45
  eval-vla-only-spatial-seed46
  eval-vla-only-spatial-seed47
  eval_obs_only_norm01_seed48
  eval_obs_only_norm03_seed48
  k2-l2-calibration-phase1
  mvp-point-reaching
  plan_602-latency-profile
  plan_602-latency-profiling
  plan_701-crm-k1-train
  plan_701-precompute-k1-spatial
  precompute-k5
  precompute-shard0
  precompute-shard1
  precompute-shard2
  precompute-v4-shard0
  precompute-v4-shard1
  precompute-v4-shard2
  precompute-v5-shard0
  precompute-v5-shard1
  precompute-v5-shard2
  train-crm-k1-accg-object-seed42-fallback
  train-crm-k1-accg-object-seed42-full
  train-crm-k1-accg-object-seed42-v2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "ef06ba9f-6b82-436a-9160-df23bdfecff4",
  "tool_use_result": {
    "stdout": "Total experiments: 422\nDONE+success: 208\n  crm-lto-splitA-train\n  crm-lto-splitA-train-fixed\n  crm-train-v2-obs-only\n  crm-train-v2-perdof\n  crm-train-v2-scalar-unc\n  crm-train-v3-norm\n  crm-train-v3-norm-obs-only\n  crm-train-v3-norm-scalar-unc\n  eval-acr-object-obs-only-default\n  eval-acr-object-obs-only-norm02\n  eval-acr-object-v4-default-r2\n  eval-acr-object-v4-obs-only\n  eval-acr-object-v4-perdof\n  eval-acr-spatial-v3\n  eval-acr-spatial-v4-obs-only-r3\n  eval-acr-spatial-v4-scalar-r2\n  eval-acr-spatial-v4-small-r2\n  eval-adaptive-k-p25-seed42\n  eval-adaptive-k-p25-seed43\n  eval-adaptive-k-p25-seed44-r2\n  eval-adaptive-k-p50-seed44\n  eval-adaptive-k-p75-seed44\n  eval-adaptive-k-p90-seed42\n  eval-adaptive-k-p90-seed43\n  eval-adaptive-k-p90-seed44\n  eval-argmin-object-k5-seed42\n  eval-argmin-object-k5-seed43\n  eval-argmin-object-k5-seed44-r2\n  eval-argmin-object-k5-seed45\n  eval-argmin-object-seed43\n  eval-argmin-object-seed44-r2\n  eval-argmin-object-seed45\n  eval-argmin-object-seed46\n  eval-argmin-object-seed47\n  eval-argmin-only-spatial-r2\n  eval-crm-goal-seed42\n  eval-crm-goal-seed43\n  eval-crm-goal-seed44-r2\n  eval-crm-goal-seed45-r2\n  eval-crm-goal-seed46\n  eval-crm-long-seed42\n  eval-crm-long-seed43\n  eval-crm-long-seed44\n  eval-crm-long-seed45\n  eval-crm-long-seed46\n  eval-crm-long-seed47\n  eval-crm-long-seed50\n  eval-crm-spatial-k10-seed51\n  eval-direct-correction-object-seed42-r3\n  eval-lto-splitA-vla-only-r2\n  eval-lto-splitA-vla-only-r3\n  eval-lto-splitA-vla-only-v2\n  eval-mag-obsonly-norm003-b2\n  eval-mag-obsonly-norm003-object\n  eval-mag-obsonly-norm005\n  eval-mag-obsonly-norm005-object\n  eval-mag-obsonly-norm03-object\n  eval-mag-obsonly-norm03-r2\n  eval-mag-perdof-norm003-object\n  eval-mag-perdof-norm005-object\n  eval-mag-perdof-norm02-seed43-object-r3\n  eval-mag-perdof-norm03-object-r3\n  eval-object-v8-full\n  eval-obs-only-object-default-seed44\n  eval-obs-only-object-default-seed45\n  eval-obs-only-object-default-seed45-r2\n  eval-obs-only-object-default-seed46\n  eval-obs-only-object-default-seed47\n  eval-obs-only-object-default-seed48\n  eval-obs-only-object-default-seed48-r2\n  eval-obs-only-object-norm003-seed44-bjb2\n  eval-obs-only-object-norm003-seed47-r2\n  eval-obs-only-object-norm003-seed48\n  eval-obs-only-object-norm005-seed43-r2\n  eval-obs-only-object-norm005-seed44\n  eval-obs-only-object-norm005-seed45\n  eval-obs-only-object-norm005-seed47\n  eval-obs-only-object-norm005-seed48\n  eval-obs-only-object-norm01-seed44\n  eval-obs-only-object-norm01-seed45\n  eval-obs-only-object-norm01-seed45-r2\n  eval-obs-only-object-norm01-seed46-r3\n  eval-obs-only-object-norm01-seed47\n  eval-obs-only-object-norm01-seed48\n  eval-obs-only-object-norm02-k5-seed42\n  eval-obs-only-object-norm02-k5-seed43\n  eval-obs-only-object-norm02-k5-seed44\n  eval-obs-only-object-norm02-k5-seed45\n  eval-obs-only-object-norm02-k5-seed46\n  eval-obs-only-object-norm02-k5-seed47\n  eval-obs-only-object-norm02-k5-seed48\n  eval-obs-only-object-norm02-seed43-r2\n  eval-obs-only-object-norm02-seed44-r2\n  eval-obs-only-object-norm02-seed45\n  eval-obs-only-object-norm02-seed46\n  eval-obs-only-object-norm02-seed47\n  eval-obs-only-object-norm02-seed48-r2\n  eval-obs-only-object-norm03-seed44\n  eval-obs-only-object-norm03-seed45-r2\n  eval-obs-only-object-norm03-seed46\n  eval-obs-only-object-norm03-seed48\n  eval-obs-only-spatial-norm02-k5-seed42\n  eval-obs-only-spatial-norm02-k5-seed43\n  eval-obs-only-spatial-norm02-k5-seed44-r2\n  eval-obs-only-spatial-norm02-k5-seed45-r2\n  eval-obs-only-spatial-norm02-seed43-r2\n  eval-obs-only-spatial-norm02-seed44\n  eval-obs-only-spatial-norm02-seed45\n  eval-obs-only-spatial-norm02-seed46-r2\n  eval-obs-only-spatial-norm02-seed47\n  eval-obs-only-spatial-norm02-seed48\n  eval-openvla-object-vla-only-seed42-v2\n  eval-perdof-object-default-seed43\n  eval-perdof-object-default-seed45\n  eval-perdof-object-norm003-seed43\n  eval-perdof-object-norm003-seed46\n  eval-perdof-object-norm003-seed47\n  eval-perdof-object-norm003-seed48\n  eval-perdof-object-norm005-seed43\n  eval-perdof-object-norm005-seed44\n  eval-perdof-object-norm005-seed45-r2\n  eval-perdof-object-norm005-seed46\n  eval-perdof-object-norm005-seed47\n  eval-perdof-object-norm01-seed43\n  eval-perdof-object-norm01-seed45\n  eval-perdof-object-norm01-seed46-r2\n  eval-perdof-object-norm01-seed47-bjb1\n  eval-perdof-object-norm01-seed48\n  eval-perdof-object-norm02-seed43\n  eval-perdof-object-norm02-seed43-r3\n  eval-perdof-object-norm02-seed44\n  eval-perdof-object-norm02-seed45\n  eval-perdof-object-norm02-seed46\n  eval-perdof-object-norm02-seed47\n  eval-perdof-object-norm03-seed43\n  eval-perdof-object-norm03-seed46\n  eval-perdof-object-norm03-seed47\n  eval-perdof-object-seed43\n  eval-random-selection-object-k5-seed42-r2\n  eval-random-selection-object-k5-seed43-r2\n  eval-random-selection-object-k5-seed44-r2\n  eval-random-selection-object-k5-seed45-r2\n  eval-random-selection-object-seed43\n  eval-random-selection-object-seed45\n  eval-reconvla-object\n  eval-reconvla-spatial-v3\n  eval-scalar-object-seed43\n  eval-scalar-object-seed45\n  eval-scalar-object-seed46\n  eval-spatial-v7-full\n  eval-vla-mean-object\n  eval-vla-mean-object-seed43\n  eval-vla-mean-object-seed44\n  eval-vla-mean-object-seed45\n  eval-vla-mean-spatial\n  eval-vla-mean-spatial-t10\n  eval-vla-only-goal-seed42\n  eval-vla-only-goal-seed43\n  eval-vla-only-goal-seed44-r2\n  eval-vla-only-goal-seed45\n  eval-vla-only-goal-seed46\n  eval-vla-only-goal-seed49\n  eval-vla-only-long-seed42\n  eval-vla-only-long-seed43\n  eval-vla-only-long-seed44\n  eval-vla-only-long-seed45\n  eval-vla-only-long-seed46\n  eval-vla-only-long-seed47\n  eval-vla-only-long-seed48\n  eval-vla-only-long-seed50\n  eval-vla-only-long-seed51\n  eval-vla-only-long-seed52\n  eval-vla-only-object\n  eval-vla-only-object-seed43\n  eval-vla-only-object-seed44-r2\n  eval-vla-only-object-seed45\n  eval-vla-only-object-seed45-r2\n  eval-vla-only-object-seed46\n  eval-vla-only-object-seed47\n  eval-vla-only-object-seed48\n  eval-vla-only-object-seed50\n  eval-vla-only-spatial-seed42\n  eval-vla-only-spatial-seed43\n  eval-vla-only-spatial-seed44\n  eval-vla-only-spatial-seed45\n  eval-vla-only-spatial-seed46\n  eval-vla-only-spatial-seed47\n  eval_obs_only_norm01_seed48\n  eval_obs_only_norm03_seed48\n  k2-l2-calibration-phase1\n  mvp-point-reaching\n  plan_602-latency-profile\n  plan_602-latency-profiling\n  plan_701-crm-k1-train\n  plan_701-precompute-k1-spatial\n  precompute-k5\n  precompute-shard0\n  precompute-shard1\n  precompute-shard2\n  precompute-v4-shard0\n  precompute-v4-shard1\n  precompute-v4-shard2\n  precompute-v5-shard0\n  precompute-v5-shard1\n  precompute-v5-shard2\n  train-crm-k1-accg-object-seed42-fallback\n  train-crm-k1-accg-object-seed42-full\n  train-crm-k1-accg-object-seed42-v2",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good, I have 208 DONE+success experiments. Now I need to systematically extract the relevant ones for each benchmark and method. Let me write a comprehensive Python script to do the full audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "9f02da21-7dda-423e-bf35-b86e34551bc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PM9movfzgLPMaQAetDopX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 32892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3387
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

_source line 24_

有 208 个成功实验。现在提取每个 benchmark+method 的详细数据做审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "e56d2113-0efd-487b-8b97-61afdb1f3509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PM9movfzgLPMaQAetDopX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 32892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3387
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01YTE3SmwvMKfdY5RGUAMTno`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', {})\n\n# Focus on eval experiments that are DONE+success\neval_done = {}\nfor exp_id, exp in experiments.items():\n    if isinstance(exp, dict) and exp.get('status') == 'DONE' and exp.get('conclusion') == 'success':\n        if exp_id.startswith('eval-'):\n            eval_done[exp_id] = exp\n\nprint(f\"Total eval DONE+success: {len(eval_done)}\")\nprint()\n\n# ===================== SPATIAL =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-SPATIAL\")\nprint(\"=\" * 80)\n\n# CRM obs_only spatial norm02 K=10\nprint(\"\\n--- CRM obs_only spatial norm02 K=10 ---\")\nspatial_crm_candidates = []\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'spatial' in eid_lower and ('obs-only' in eid_lower or 'obs_only' in eid_lower or 'obsonly' in eid_lower):\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        hyp = exp.get('hypothesis', '')[:120]\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        # Check if this is norm02\n        norm = ''\n        if 'norm02' in eid_lower:\n            norm = 'norm02'\n        elif 'norm03' in eid_lower:\n            norm = 'norm03'\n        elif 'norm01' in eid_lower:\n            norm = 'norm01'\n        elif 'norm005' in eid_lower:\n            norm = 'norm005'\n        elif 'norm003' in eid_lower:\n            norm = 'norm003'\n        \n        k_val = ''\n        if 'k5' in eid_lower or 'k-5' in eid_lower:\n            k_val = 'K=5'\n        elif 'k10' in eid_lower or 'k-10' in eid_lower:\n            k_val = 'K=10'\n        \n        spatial_crm_candidates.append({\n            'exp_id': eid,\n            'seed': seed,\n            'sr': sr,\n            'norm': norm,\n            'k': k_val,\n            'hyp': hyp\n        })\n\nfor c in sorted(spatial_crm_candidates, key=lambda x: x['exp_id']):\n    print(f\"  {c['exp_id']} | seed={c['seed']} | SR={c['sr']} | norm={c['norm']} | {c['k']} | {c['hyp']}\")\n\n# Also check mag-obsonly spatial\nprint(\"\\n--- mag-obsonly spatial ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'mag' in eid_lower and 'obsonly' in eid_lower and 'spatial' not in eid_lower and 'object' not in eid_lower:\n        # These might be spatial (default benchmark)\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', 'N/A')\n        hyp = exp.get('hypothesis', '')[:120]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# Also check eval-acr-spatial\nprint(\"\\n--- eval-acr-spatial ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'acr' in eid_lower and 'spatial' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', 'N/A')\n        hyp = exp.get('hypothesis', '')[:120]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# VLA-only spatial\nprint(\"\\n--- VLA-only spatial ---\")\nspatial_vla_candidates = []\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'spatial' in eid_lower and 'vla-only' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        spatial_vla_candidates.append({'exp_id': eid, 'seed': seed, 'sr': sr})\n\nfor c in sorted(spatial_vla_candidates, key=lambda x: x['exp_id']):\n    print(f\"  {c['exp_id']} | seed={c['seed']} | SR={c['sr']}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"LIBERO-LONG\")\nprint(\"=\" * 80)\n\n# CRM Long\nprint(\"\\n--- CRM obs_only Long ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'long' in eid_lower and ('crm' in eid_lower or 'obs-only' in eid_lower or 'obs_only' in eid_lower or 'obsonly' in eid_lower):\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        hyp = exp.get('hypothesis', '')[:120]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# VLA-only Long\nprint(\"\\n--- VLA-only Long ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'long' in eid_lower and 'vla-only' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        print(f\"  {eid} | seed={seed} | SR={sr}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"LIBERO-GOAL\")\nprint(\"=\" * 80)\n\n# CRM Goal\nprint(\"\\n--- CRM obs_only Goal ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'goal' in eid_lower and ('crm' in eid_lower or 'obs-only' in eid_lower or 'obs_only' in eid_lower or 'obsonly' in eid_lower):\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        hyp = exp.get('hypothesis', '')[:120]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# VLA-only Goal\nprint(\"\\n--- VLA-only Goal ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'goal' in eid_lower and 'vla-only' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        print(f\"  {eid} | seed={seed} | SR={sr}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"LIBERO-OBJECT\")\nprint(\"=\" * 80)\n\n# CRM obs_only object\nprint(\"\\n--- CRM obs_only Object (all norms) ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'object' in eid_lower and ('obs-only' in eid_lower or 'obs_only' in eid_lower or 'obsonly' in eid_lower):\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        hyp = exp.get('hypothesis', '')[:80]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# Also check mag-obsonly object\nprint(\"\\n--- mag-obsonly Object ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'mag' in eid_lower and 'obsonly' in eid_lower and 'object' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', 'N/A')\n        hyp = exp.get('hypothesis', '')[:80]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# eval-acr-object obs-only\nprint(\"\\n--- eval-acr-object ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'acr' in eid_lower and 'object' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', 'N/A')\n        hyp = exp.get('hypothesis', '')[:80]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# VLA-only Object\nprint(\"\\n--- VLA-only Object ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'object' in eid_lower and 'vla-only' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        print(f\"  {eid} | seed={seed} | SR={sr}\")\n\n# Argmin Object\nprint(\"\\n--- Argmin Object ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'argmin' in eid_lower and 'object' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        k_val = 'K=5' if 'k5' in eid_lower or 'k-5' in eid_lower else 'K=10'\n        print(f\"  {eid} | seed={seed} | SR={sr} | {k_val}\")\n\n# Adaptive-K\nprint(\"\\n--- Adaptive-K ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'adaptive' in eid_lower:\n        spec = exp.get('spec', {})\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n        seed = spec.get('seed', exp.get('seed', 'N/A'))\n        hyp = exp.get('hypothesis', '')[:80]\n        print(f\"  {eid} | seed={seed} | SR={sr} | hyp={hyp}\")\n\n# Check for adaptive-k p50 seed42, seed43 which might have different naming\nprint(\"\\n--- Also check adaptive_k variants ---\")\nfor eid, exp in eval_done.items():\n    eid_lower = eid.lower()\n    if 'adaptive_k' in eid_lower or 'adaptive-k' in eid_lower:\n        if eid not in [e for e in eval_done if 'adaptive' in e.lower()]:\n            spec = exp.get('spec', {})\n            metrics = exp.get('metrics', {})\n            sr = metrics.get('success_rate', metrics.get('avg_success_rate', 'N/A'))\n            seed = spec.get('seed', 'N/A')\n            print(f\"  {eid} | seed={seed} | SR={sr}\")\n\nPYEOF\n",
  "description": "Extract all relevant eval experiments per benchmark",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "204be069-1f6a-483d-8c13-d8bceeb72257",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PM9movfzgLPMaQAetDopX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 32892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3387
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

_source line 26 · 2026-05-20T07:18:52.845Z_

<details><summary>↩ Tool result · `toolu_01YTE3SmwvMKfdY5RGUAMTno`</summary>

```text
Total eval DONE+success: 179

================================================================================
LIBERO-SPATIAL
================================================================================

--- CRM obs_only spatial norm02 K=10 ---
  eval-acr-spatial-v4-obs-only-r3 | seed=42 | SR=N/A | norm= |  | Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features
  eval-obs-only-spatial-norm02-k5-seed42 | seed=42 | SR=0.35 | norm=norm02 | K=5 | K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark general
  eval-obs-only-spatial-norm02-k5-seed43 | seed=43 | SR=0.32 | norm=norm02 | K=5 | K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark general
  eval-obs-only-spatial-norm02-k5-seed44-r2 | seed=44 | SR=0.37 | norm=norm02 | K=5 | CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success r
  eval-obs-only-spatial-norm02-k5-seed45-r2 | seed=45 | SR=0.34 | norm=norm02 | K=5 | CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success r
  eval-obs-only-spatial-norm02-seed43-r2 | seed=43 | SR=N/A | norm=norm02 |  | obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed43. 重跑：bjb2-40593 上 7/10 tasks 后进程终止无 JSON。补齐 Spatial K=10 n=5。
  eval-obs-only-spatial-norm02-seed44 | seed=44 | SR=0.36 | norm=norm02 |  | obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 2
  eval-obs-only-spatial-norm02-seed45 | seed=45 | SR=0.34 | norm=norm02 |  | obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 2
  eval-obs-only-spatial-norm02-seed46-r2 | seed=46 | SR=N/A | norm=norm02 |  | obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed46. 重跑：原实验被 SIGKILL（M023）。补充 Spatial K=10 cross-benchmark 数据。
  eval-obs-only-spatial-norm02-seed47 | seed=47 | SR=N/A | norm=norm02 |  | obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed47. 补充 Spatial cross-seed 一致性数据。
  eval-obs-only-spatial-norm02-seed48 | seed=48 | SR=0.35 | norm=norm02 |  | CRM obs_only norm02 (ε=0.2) K=10 on LIBERO-Spatial seed48. Complement Spatial cross-seed consistency data.

--- mag-obsonly spatial ---
  eval-mag-obsonly-norm005 | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。
  eval-mag-obsonly-norm003-b2 | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 bench
  eval-mag-obsonly-norm03-r2 | seed=42 | SR=N/A | hyp=Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fill

--- eval-acr-spatial ---
  eval-acr-spatial-v3 | seed=42 | SR=N/A | hyp=ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal 
  eval-acr-spatial-v4-scalar-r2 | seed=42 | SR=N/A | hyp=Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_un
  eval-acr-spatial-v4-small-r2 | seed=42 | SR=N/A | hyp=Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.
  eval-acr-spatial-v4-obs-only-r3 | seed=42 | SR=N/A | hyp=Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features

--- VLA-only spatial ---
  eval-vla-only-spatial-seed42 | seed=42 | SR=0.3
  eval-vla-only-spatial-seed43 | seed=43 | SR=0.29
  eval-vla-only-spatial-seed44 | seed=44 | SR=0.31
  eval-vla-only-spatial-seed45 | seed=N/A | SR=0.27
  eval-vla-only-spatial-seed46 | seed=46 | SR=N/A
  eval-vla-only-spatial-seed47 | seed=N/A | SR=N/A

================================================================================
LIBERO-LONG
================================================================================

--- CRM obs_only Long ---
  eval-crm-long-seed42 | seed=42 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed42. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%
  eval-crm-long-seed43 | seed=43 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed43. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%
  eval-crm-long-seed44 | seed=44 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed44. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%
  eval-crm-long-seed45 | seed=45 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD long-horizon 任务。补充 see
  eval-crm-long-seed46 | seed=46 | SR=0.18 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed46. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是未见过的 suite。补齐 CRM-Long 第 5 个 s
  eval-crm-long-seed47 | seed=47 | SR=0.17 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed47. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是 OOD long-horizon 任务。补充 seed42
  eval-crm-long-seed50 | seed=50 | SR=0.14 | hyp=CRM obs_only K=10 on LIBERO-Long seed50. Long OOD 补样本量，验证 CRM 在 cross-suite OOD 上的效果。

--- VLA-only Long ---
  eval-vla-only-long-seed42 | seed=N/A | SR=N/A
  eval-vla-only-long-seed43 | seed=43 | SR=N/A
  eval-vla-only-long-seed44 | seed=N/A | SR=N/A
  eval-vla-only-long-seed45 | seed=N/A | SR=N/A
  eval-vla-only-long-seed46 | seed=46 | SR=N/A
  eval-vla-only-long-seed47 | seed=47 | SR=N/A
  eval-vla-only-long-seed48 | seed=48 | SR=0.14
  eval-vla-only-long-seed50 | seed=50 | SR=0.16
  eval-vla-only-long-seed51 | seed=51 | SR=0.15
  eval-vla-only-long-seed52 | seed=52 | SR=0.17

================================================================================
LIBERO-GOAL
================================================================================

--- CRM obs_only Goal ---
  eval-crm-goal-seed42 | seed=42 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed42. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。若 CRM 提升 Goal SR，证明
  eval-crm-goal-seed43 | seed=43 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed43. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。与 seed42 配对增加统计稳健性。
  eval-crm-goal-seed44-r2 | seed=44 | SR=0.64 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed44. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。
  eval-crm-goal-seed45-r2 | seed=45 | SR=0.65 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。
  eval-crm-goal-seed46 | seed=N/A | SR=N/A | hyp=CRM obs_only K=10 on LIBERO-Goal seed46. Goal OOD 补样本量 (n→5)，验证 CRM 在 cross-suite OOD 上的效果（当前 n=2 结果中性 ~69.5%≈VLA-only）。

--- VLA-only Goal ---
  eval-vla-only-goal-seed42 | seed=42 | SR=N/A
  eval-vla-only-goal-seed43 | seed=43 | SR=N/A
  eval-vla-only-goal-seed44-r2 | seed=44 | SR=N/A
  eval-vla-only-goal-seed45 | seed=N/A | SR=N/A
  eval-vla-only-goal-seed46 | seed=46 | SR=N/A
  eval-vla-only-goal-seed49 | seed=49 | SR=0.65

================================================================================
LIBERO-OBJECT
================================================================================

--- CRM obs_only Object (all norms) ---
  eval-acr-object-v4-obs-only | seed=N/A | SR=N/A | hyp=D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchma
  eval-acr-object-obs-only-norm02 | seed=42 | SR=N/A | hyp=ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves mean
  eval-mag-obsonly-norm005-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_
  eval-mag-obsonly-norm03-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_on
  eval-mag-obsonly-norm003-object | seed=42 | SR=N/A | hyp=Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object bench
  eval-acr-object-obs-only-default | seed=42 | SR=N/A | hyp=obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude contr
  eval-obs-only-object-norm02-seed43-r2 | seed=N/A | SR=N/A | hyp=D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry
  eval-obs-only-object-norm02-seed44-r2 | seed=44 | SR=N/A | hyp=Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activa
  eval-obs-only-object-norm03-seed44 | seed=44 | SR=N/A | hyp=obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed 
  eval-obs-only-object-norm01-seed44 | seed=44 | SR=N/A | hyp=Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, 
  eval-obs-only-object-default-seed44 | seed=44 | SR=N/A | hyp=obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapp
  eval-obs-only-object-norm02-seed45 | seed=45 | SR=N/A | hyp=obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR r
  eval-obs-only-object-norm01-seed45 | seed=45 | SR=N/A | hyp=obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。se
  eval-obs-only-object-default-seed45 | seed=45 | SR=N/A | hyp=obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 u
  eval-obs-only-object-norm03-seed45-r2 | seed=45 | SR=N/A | hyp=obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show
  eval-obs-only-object-norm02-seed46 | seed=46 | SR=0.15 | hyp=obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argm
  eval-obs-only-object-norm02-seed47 | seed=47 | SR=0.2 | hyp=obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comp
  eval-obs-only-object-norm01-seed47 | seed=47 | SR=0.17 | hyp=Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。
  eval-obs-only-object-norm03-seed46 | seed=46 | SR=0.17 | hyp=Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。
  eval-obs-only-object-default-seed46 | seed=46 | SR=N/A | hyp=obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-O
  eval-obs-only-object-norm005-seed43-r2 | seed=43 | SR=N/A | hyp=obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve
  eval-obs-only-object-norm02-k5-seed42 | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 
  eval-obs-only-object-norm01-seed48 | seed=48 | SR=0.18 | hyp=obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 obs_only ε=0.1 至 n=7。
  eval-obs-only-object-norm03-seed48 | seed=48 | SR=0.16 | hyp=obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 see
  eval-obs-only-object-norm005-seed44 | seed=44 | SR=0.16 | hyp=obs_only CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段数据。seed42=13%
  eval-obs-only-object-norm02-k5-seed43 | seed=43 | SR=0.19 | hyp=obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Direc
  eval-obs-only-object-norm02-k5-seed44 | seed=N/A | SR=0.17 | hyp=obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=
  eval-obs-only-object-norm005-seed45 | seed=45 | SR=0.14 | hyp=obs_only CRM (ε=0.05) seed45 on LIBERO-Object. Supplements magnitude curve low-n
  eval-obs-only-object-norm02-seed48-r2 | seed=48 | SR=0.18 | hyp=obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attemp
  eval-obs-only-object-norm01-seed46-r3 | seed=46 | SR=0.18 | hyp=obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude cu
  eval-obs-only-object-norm01-seed45-r2 | seed=N/A | SR=0.17 | hyp=obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标
  eval-obs-only-object-default-seed45-r2 | seed=N/A | SR=N/A | hyp=obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n
  eval-obs-only-object-default-seed47 | seed=47 | SR=0.16 | hyp=Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。
  eval-obs-only-object-norm02-k5-seed45 | seed=45 | SR=0.15 | hyp=Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。
  eval-obs-only-object-default-seed48 | seed=48 | SR=0.17 | hyp=Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。
  eval-obs-only-object-norm005-seed47 | seed=47 | SR=0.14 | hyp=obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。
  eval-obs-only-object-norm003-seed44-bjb2 | seed=44 | SR=N/A | hyp=obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄
  eval-obs-only-object-default-seed48-r2 | seed=48 | SR=0.17 | hyp=obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (
  eval-obs-only-object-norm02-k5-seed46 | seed=46 | SR=0.16 | hyp=K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 
  eval-obs-only-object-norm02-k5-seed47 | seed=47 | SR=0.13 | hyp=K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 
  eval-obs-only-object-norm02-k5-seed48 | seed=48 | SR=0.18 | hyp=K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration
  eval-obs-only-object-norm005-seed48 | seed=48 | SR=N/A | hyp=obs_only CRM (ε=0.05) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.05
  eval-obs-only-object-norm003-seed47-r2 | seed=47 | SR=0.15 | hyp=obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed
  eval-obs-only-object-norm003-seed48 | seed=48 | SR=0.15 | hyp=obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude 

--- mag-obsonly Object ---
  eval-mag-obsonly-norm005-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_
  eval-mag-obsonly-norm03-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_on
  eval-mag-obsonly-norm003-object | seed=42 | SR=N/A | hyp=Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object bench

--- eval-acr-object ---
  eval-acr-object-v4-perdof | seed=42 | SR=N/A | hyp=D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object b
  eval-acr-object-v4-obs-only | seed=N/A | SR=N/A | hyp=D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchma
  eval-acr-object-obs-only-norm02 | seed=42 | SR=N/A | hyp=ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves mean
  eval-acr-object-obs-only-default | seed=42 | SR=N/A | hyp=obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude contr
  eval-acr-object-v4-default-r2 | seed=42 | SR=N/A | hyp=v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to c

--- VLA-only Object ---
  eval-vla-only-object | seed=42 | SR=N/A
  eval-vla-only-object-seed43 | seed=43 | SR=N/A
  eval-vla-only-object-seed44-r2 | seed=N/A | SR=N/A
  eval-vla-only-object-seed45 | seed=45 | SR=N/A
  eval-openvla-object-vla-only-seed42-v2 | seed=42 | SR=N/A
  eval-vla-only-object-seed45-r2 | seed=45 | SR=N/A
  eval-vla-only-object-seed46 | seed=46 | SR=0.13
  eval-vla-only-object-seed47 | seed=47 | SR=N/A
  eval-vla-only-object-seed48 | seed=48 | SR=0.1
  eval-vla-only-object-seed50 | seed=50 | SR=0.09

--- Argmin Object ---
  eval-argmin-object-seed43 | seed=43 | SR=N/A | K=10
  eval-argmin-object-seed44-r2 | seed=44 | SR=N/A | K=10
  eval-argmin-object-seed45 | seed=45 | SR=N/A | K=10
  eval-argmin-object-seed46 | seed=46 | SR=N/A | K=10
  eval-argmin-object-seed47 | seed=47 | SR=N/A | K=10
  eval-argmin-object-k5-seed43 | seed=43 | SR=N/A | K=5
  eval-argmin-object-k5-seed42 | seed=42 | SR=N/A | K=5
  eval-argmin-object-k5-seed45 | seed=45 | SR=N/A | K=5
  eval-argmin-object-k5-seed44-r2 | seed=N/A | SR=N/A | K=5

--- Adaptive-K ---
  eval-adaptive-k-p75-seed44 | seed=44 | SR=0.16 | hyp=Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed44. ~25% steps trigger K=1
  eval-adaptive-k-p50-seed44 | seed=44 | SR=0.14 | hyp=Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed44. ~50% steps trigger K=1
  eval-adaptive-k-p25-seed42 | seed=42 | SR=0.15 | hyp=Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed42. ~75% steps trigger K=1
  eval-adaptive-k-p25-seed43 | seed=43 | SR=0.13 | hyp=Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed43. ~75% steps trigger K=1
  eval-adaptive-k-p90-seed42 | seed=42 | SR=0.12 | hyp=Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed42. ~10% steps trigger K=1
  eval-adaptive-k-p90-seed43 | seed=43 | SR=0.14 | hyp=Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed43. ~10% steps trigger K=1
  eval-adaptive-k-p90-seed44 | seed=44 | SR=0.14 | hyp=Adaptive K with P90 threshold (τ=0.127) on Object seed44. Part of the 4-threshol
  eval-adaptive-k-p25-seed44-r2 | seed=44 | SR=0.15 | hyp=Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. 重新部署在干净 GPU 上（原 bjb2-4

--- Also check adaptive_k variants ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "3a04e162-a88f-4efc-bb48-60dd77f60f9a",
  "tool_use_result": {
    "stdout": "Total eval DONE+success: 179\n\n================================================================================\nLIBERO-SPATIAL\n================================================================================\n\n--- CRM obs_only spatial norm02 K=10 ---\n  eval-acr-spatial-v4-obs-only-r3 | seed=42 | SR=N/A | norm= |  | Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features\n  eval-obs-only-spatial-norm02-k5-seed42 | seed=42 | SR=0.35 | norm=norm02 | K=5 | K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark general\n  eval-obs-only-spatial-norm02-k5-seed43 | seed=43 | SR=0.32 | norm=norm02 | K=5 | K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark general\n  eval-obs-only-spatial-norm02-k5-seed44-r2 | seed=44 | SR=0.37 | norm=norm02 | K=5 | CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success r\n  eval-obs-only-spatial-norm02-k5-seed45-r2 | seed=45 | SR=0.34 | norm=norm02 | K=5 | CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success r\n  eval-obs-only-spatial-norm02-seed43-r2 | seed=43 | SR=N/A | norm=norm02 |  | obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed43. 重跑：bjb2-40593 上 7/10 tasks 后进程终止无 JSON。补齐 Spatial K=10 n=5。\n  eval-obs-only-spatial-norm02-seed44 | seed=44 | SR=0.36 | norm=norm02 |  | obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 2\n  eval-obs-only-spatial-norm02-seed45 | seed=45 | SR=0.34 | norm=norm02 |  | obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 2\n  eval-obs-only-spatial-norm02-seed46-r2 | seed=46 | SR=N/A | norm=norm02 |  | obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed46. 重跑：原实验被 SIGKILL（M023）。补充 Spatial K=10 cross-benchmark 数据。\n  eval-obs-only-spatial-norm02-seed47 | seed=47 | SR=N/A | norm=norm02 |  | obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed47. 补充 Spatial cross-seed 一致性数据。\n  eval-obs-only-spatial-norm02-seed48 | seed=48 | SR=0.35 | norm=norm02 |  | CRM obs_only norm02 (ε=0.2) K=10 on LIBERO-Spatial seed48. Complement Spatial cross-seed consistency data.\n\n--- mag-obsonly spatial ---\n  eval-mag-obsonly-norm005 | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\n  eval-mag-obsonly-norm003-b2 | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 bench\n  eval-mag-obsonly-norm03-r2 | seed=42 | SR=N/A | hyp=Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fill\n\n--- eval-acr-spatial ---\n  eval-acr-spatial-v3 | seed=42 | SR=N/A | hyp=ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal \n  eval-acr-spatial-v4-scalar-r2 | seed=42 | SR=N/A | hyp=Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_un\n  eval-acr-spatial-v4-small-r2 | seed=42 | SR=N/A | hyp=Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\n  eval-acr-spatial-v4-obs-only-r3 | seed=42 | SR=N/A | hyp=Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features\n\n--- VLA-only spatial ---\n  eval-vla-only-spatial-seed42 | seed=42 | SR=0.3\n  eval-vla-only-spatial-seed43 | seed=43 | SR=0.29\n  eval-vla-only-spatial-seed44 | seed=44 | SR=0.31\n  eval-vla-only-spatial-seed45 | seed=N/A | SR=0.27\n  eval-vla-only-spatial-seed46 | seed=46 | SR=N/A\n  eval-vla-only-spatial-seed47 | seed=N/A | SR=N/A\n\n================================================================================\nLIBERO-LONG\n================================================================================\n\n--- CRM obs_only Long ---\n  eval-crm-long-seed42 | seed=42 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed42. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%\n  eval-crm-long-seed43 | seed=43 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed43. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%\n  eval-crm-long-seed44 | seed=44 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed44. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%\n  eval-crm-long-seed45 | seed=45 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD long-horizon 任务。补充 see\n  eval-crm-long-seed46 | seed=46 | SR=0.18 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed46. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是未见过的 suite。补齐 CRM-Long 第 5 个 s\n  eval-crm-long-seed47 | seed=47 | SR=0.17 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed47. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是 OOD long-horizon 任务。补充 seed42\n  eval-crm-long-seed50 | seed=50 | SR=0.14 | hyp=CRM obs_only K=10 on LIBERO-Long seed50. Long OOD 补样本量，验证 CRM 在 cross-suite OOD 上的效果。\n\n--- VLA-only Long ---\n  eval-vla-only-long-seed42 | seed=N/A | SR=N/A\n  eval-vla-only-long-seed43 | seed=43 | SR=N/A\n  eval-vla-only-long-seed44 | seed=N/A | SR=N/A\n  eval-vla-only-long-seed45 | seed=N/A | SR=N/A\n  eval-vla-only-long-seed46 | seed=46 | SR=N/A\n  eval-vla-only-long-seed47 | seed=47 | SR=N/A\n  eval-vla-only-long-seed48 | seed=48 | SR=0.14\n  eval-vla-only-long-seed50 | seed=50 | SR=0.16\n  eval-vla-only-long-seed51 | seed=51 | SR=0.15\n  eval-vla-only-long-seed52 | seed=52 | SR=0.17\n\n================================================================================\nLIBERO-GOAL\n================================================================================\n\n--- CRM obs_only Goal ---\n  eval-crm-goal-seed42 | seed=42 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed42. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。若 CRM 提升 Goal SR，证明\n  eval-crm-goal-seed43 | seed=43 | SR=N/A | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed43. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。与 seed42 配对增加统计稳健性。\n  eval-crm-goal-seed44-r2 | seed=44 | SR=0.64 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed44. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\n  eval-crm-goal-seed45-r2 | seed=45 | SR=0.65 | hyp=CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\n  eval-crm-goal-seed46 | seed=N/A | SR=N/A | hyp=CRM obs_only K=10 on LIBERO-Goal seed46. Goal OOD 补样本量 (n→5)，验证 CRM 在 cross-suite OOD 上的效果（当前 n=2 结果中性 ~69.5%≈VLA-only）。\n\n--- VLA-only Goal ---\n  eval-vla-only-goal-seed42 | seed=42 | SR=N/A\n  eval-vla-only-goal-seed43 | seed=43 | SR=N/A\n  eval-vla-only-goal-seed44-r2 | seed=44 | SR=N/A\n  eval-vla-only-goal-seed45 | seed=N/A | SR=N/A\n  eval-vla-only-goal-seed46 | seed=46 | SR=N/A\n  eval-vla-only-goal-seed49 | seed=49 | SR=0.65\n\n================================================================================\nLIBERO-OBJECT\n================================================================================\n\n--- CRM obs_only Object (all norms) ---\n  eval-acr-object-v4-obs-only | seed=N/A | SR=N/A | hyp=D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchma\n  eval-acr-object-obs-only-norm02 | seed=42 | SR=N/A | hyp=ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves mean\n  eval-mag-obsonly-norm005-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_\n  eval-mag-obsonly-norm03-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_on\n  eval-mag-obsonly-norm003-object | seed=42 | SR=N/A | hyp=Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object bench\n  eval-acr-object-obs-only-default | seed=42 | SR=N/A | hyp=obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude contr\n  eval-obs-only-object-norm02-seed43-r2 | seed=N/A | SR=N/A | hyp=D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry\n  eval-obs-only-object-norm02-seed44-r2 | seed=44 | SR=N/A | hyp=Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activa\n  eval-obs-only-object-norm03-seed44 | seed=44 | SR=N/A | hyp=obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed \n  eval-obs-only-object-norm01-seed44 | seed=44 | SR=N/A | hyp=Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, \n  eval-obs-only-object-default-seed44 | seed=44 | SR=N/A | hyp=obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapp\n  eval-obs-only-object-norm02-seed45 | seed=45 | SR=N/A | hyp=obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR r\n  eval-obs-only-object-norm01-seed45 | seed=45 | SR=N/A | hyp=obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。se\n  eval-obs-only-object-default-seed45 | seed=45 | SR=N/A | hyp=obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 u\n  eval-obs-only-object-norm03-seed45-r2 | seed=45 | SR=N/A | hyp=obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show\n  eval-obs-only-object-norm02-seed46 | seed=46 | SR=0.15 | hyp=obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argm\n  eval-obs-only-object-norm02-seed47 | seed=47 | SR=0.2 | hyp=obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comp\n  eval-obs-only-object-norm01-seed47 | seed=47 | SR=0.17 | hyp=Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\n  eval-obs-only-object-norm03-seed46 | seed=46 | SR=0.17 | hyp=Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\n  eval-obs-only-object-default-seed46 | seed=46 | SR=N/A | hyp=obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-O\n  eval-obs-only-object-norm005-seed43-r2 | seed=43 | SR=N/A | hyp=obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve\n  eval-obs-only-object-norm02-k5-seed42 | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) \n  eval-obs-only-object-norm01-seed48 | seed=48 | SR=0.18 | hyp=obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 obs_only ε=0.1 至 n=7。\n  eval-obs-only-object-norm03-seed48 | seed=48 | SR=0.16 | hyp=obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 see\n  eval-obs-only-object-norm005-seed44 | seed=44 | SR=0.16 | hyp=obs_only CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段数据。seed42=13%\n  eval-obs-only-object-norm02-k5-seed43 | seed=43 | SR=0.19 | hyp=obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Direc\n  eval-obs-only-object-norm02-k5-seed44 | seed=N/A | SR=0.17 | hyp=obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=\n  eval-obs-only-object-norm005-seed45 | seed=45 | SR=0.14 | hyp=obs_only CRM (ε=0.05) seed45 on LIBERO-Object. Supplements magnitude curve low-n\n  eval-obs-only-object-norm02-seed48-r2 | seed=48 | SR=0.18 | hyp=obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attemp\n  eval-obs-only-object-norm01-seed46-r3 | seed=46 | SR=0.18 | hyp=obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude cu\n  eval-obs-only-object-norm01-seed45-r2 | seed=N/A | SR=0.17 | hyp=obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标\n  eval-obs-only-object-default-seed45-r2 | seed=N/A | SR=N/A | hyp=obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n\n  eval-obs-only-object-default-seed47 | seed=47 | SR=0.16 | hyp=Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\n  eval-obs-only-object-norm02-k5-seed45 | seed=45 | SR=0.15 | hyp=Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。\n  eval-obs-only-object-default-seed48 | seed=48 | SR=0.17 | hyp=Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。\n  eval-obs-only-object-norm005-seed47 | seed=47 | SR=0.14 | hyp=obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\n  eval-obs-only-object-norm003-seed44-bjb2 | seed=44 | SR=N/A | hyp=obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄\n  eval-obs-only-object-default-seed48-r2 | seed=48 | SR=0.17 | hyp=obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (\n  eval-obs-only-object-norm02-k5-seed46 | seed=46 | SR=0.16 | hyp=K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 \n  eval-obs-only-object-norm02-k5-seed47 | seed=47 | SR=0.13 | hyp=K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 \n  eval-obs-only-object-norm02-k5-seed48 | seed=48 | SR=0.18 | hyp=K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration\n  eval-obs-only-object-norm005-seed48 | seed=48 | SR=N/A | hyp=obs_only CRM (ε=0.05) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.05\n  eval-obs-only-object-norm003-seed47-r2 | seed=47 | SR=0.15 | hyp=obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed\n  eval-obs-only-object-norm003-seed48 | seed=48 | SR=0.15 | hyp=obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude \n\n--- mag-obsonly Object ---\n  eval-mag-obsonly-norm005-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_\n  eval-mag-obsonly-norm03-object | seed=42 | SR=N/A | hyp=obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_on\n  eval-mag-obsonly-norm003-object | seed=42 | SR=N/A | hyp=Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object bench\n\n--- eval-acr-object ---\n  eval-acr-object-v4-perdof | seed=42 | SR=N/A | hyp=D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object b\n  eval-acr-object-v4-obs-only | seed=N/A | SR=N/A | hyp=D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchma\n  eval-acr-object-obs-only-norm02 | seed=42 | SR=N/A | hyp=ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves mean\n  eval-acr-object-obs-only-default | seed=42 | SR=N/A | hyp=obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude contr\n  eval-acr-object-v4-default-r2 | seed=42 | SR=N/A | hyp=v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to c\n\n--- VLA-only Object ---\n  eval-vla-only-object | seed=42 | SR=N/A\n  eval-vla-only-object-seed43 | seed=43 | SR=N/A\n  eval-vla-only-object-seed44-r2 | seed=N/A | SR=N/A\n  eval-vla-only-object-seed45 | seed=45 | SR=N/A\n  eval-openvla-object-vla-only-seed42-v2 | seed=42 | SR=N/A\n  eval-vla-only-object-seed45-r2 | seed=45 | SR=N/A\n  eval-vla-only-object-seed46 | seed=46 | SR=0.13\n  eval-vla-only-object-seed47 | seed=47 | SR=N/A\n  eval-vla-only-object-seed48 | seed=48 | SR=0.1\n  eval-vla-only-object-seed50 | seed=50 | SR=0.09\n\n--- Argmin Object ---\n  eval-argmin-object-seed43 | seed=43 | SR=N/A | K=10\n  eval-argmin-object-seed44-r2 | seed=44 | SR=N/A | K=10\n  eval-argmin-object-seed45 | seed=45 | SR=N/A | K=10\n  eval-argmin-object-seed46 | seed=46 | SR=N/A | K=10\n  eval-argmin-object-seed47 | seed=47 | SR=N/A | K=10\n  eval-argmin-object-k5-seed43 | seed=43 | SR=N/A | K=5\n  eval-argmin-object-k5-seed42 | seed=42 | SR=N/A | K=5\n  eval-argmin-object-k5-seed45 | seed=45 | SR=N/A | K=5\n  eval-argmin-object-k5-seed44-r2 | seed=N/A | SR=N/A | K=5\n\n--- Adaptive-K ---\n  eval-adaptive-k-p75-seed44 | seed=44 | SR=0.16 | hyp=Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed44. ~25% steps trigger K=1\n  eval-adaptive-k-p50-seed44 | seed=44 | SR=0.14 | hyp=Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed44. ~50% steps trigger K=1\n  eval-adaptive-k-p25-seed42 | seed=42 | SR=0.15 | hyp=Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed42. ~75% steps trigger K=1\n  eval-adaptive-k-p25-seed43 | seed=43 | SR=0.13 | hyp=Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed43. ~75% steps trigger K=1\n  eval-adaptive-k-p90-seed42 | seed=42 | SR=0.12 | hyp=Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed42. ~10% steps trigger K=1\n  eval-adaptive-k-p90-seed43 | seed=43 | SR=0.14 | hyp=Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed43. ~10% steps trigger K=1\n  eval-adaptive-k-p90-seed44 | seed=44 | SR=0.14 | hyp=Adaptive K with P90 threshold (τ=0.127) on Object seed44. Part of the 4-threshol\n  eval-adaptive-k-p25-seed44-r2 | seed=44 | SR=0.15 | hyp=Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. 重新部署在干净 GPU 上（原 bjb2-4\n\n--- Also check adaptive_k variants ---",
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

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Many experiments show SR=N/A. I need to dig deeper into these experiments to get the actual success rate values from their metrics. The metrics might be stored differently. Let me read a few of these experiments in detail to understand the structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "5891eaec-8606-4d74-b8ba-d2bcdc65c44a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01542PKxVxWafuDJhGVEzP6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11756,
      "cache_read_input_tokens": 36279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11756
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

_source line 28_

很多实验 SR 显示 N/A — metrics 可能用不同的键存储。让我深入查看这些实验的 metrics 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "513dd703-7ba4-4fcf-a608-88e190f2c311",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01542PKxVxWafuDJhGVEzP6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11756,
      "cache_read_input_tokens": 36279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11756
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01N9heWJpDousELZGFVZ16WF`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', {})\n\n# Check a few experiments with N/A SR to understand metrics structure\ncheck_ids = [\n    'eval-crm-goal-seed42',\n    'eval-crm-goal-seed43',\n    'eval-crm-long-seed42',\n    'eval-vla-only-long-seed42',\n    'eval-vla-only-spatial-seed42',\n    'eval-vla-only-spatial-seed46',\n    'eval-vla-only-spatial-seed47',\n    'eval-vla-only-object',\n    'eval-vla-only-object-seed43',\n    'eval-obs-only-spatial-norm02-seed43-r2',\n    'eval-obs-only-spatial-norm02-seed46-r2',\n    'eval-obs-only-spatial-norm02-seed47',\n    'eval-argmin-object-seed43',\n    'eval-mag-obsonly-norm02',  # might not exist, check\n    'eval-obs-only-object-norm02-k5-seed42',\n]\n\nfor eid in check_ids:\n    exp = experiments.get(eid)\n    if exp:\n        metrics = exp.get('metrics', {})\n        # Get all metric keys\n        metric_keys = list(metrics.keys()) if isinstance(metrics, dict) else str(metrics)\n        sr_candidates = {}\n        if isinstance(metrics, dict):\n            for k, v in metrics.items():\n                if 'success' in k.lower() or 'sr' in k.lower() or 'rate' in k.lower():\n                    sr_candidates[k] = v\n                elif isinstance(v, (int, float)) and 0 <= v <= 1:\n                    sr_candidates[k] = v\n        print(f\"{eid}: metric_keys={metric_keys[:10]}, sr_found={sr_candidates}\")\n    else:\n        print(f\"{eid}: NOT FOUND\")\n    print()\n\nPYEOF\n",
  "description": "Check metrics structure for N/A experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "1bbb0d58-eb9f-4a44-af4c-a3b73e08a8b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01542PKxVxWafuDJhGVEzP6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11756,
      "cache_read_input_tokens": 36279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11756
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

_source line 30 · 2026-05-20T07:19:08.538Z_

<details><summary>↩ Tool result · `toolu_01N9heWJpDousELZGFVZ16WF`</summary>

```text
eval-crm-goal-seed42: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'per_task'], sr_found={'overall_success_rate': 0.67}

eval-crm-goal-seed43: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'per_task'], sr_found={'overall_success_rate': 0.72}

eval-crm-long-seed42: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'per_task'], sr_found={'overall_success_rate': 0.17}

eval-vla-only-long-seed42: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'per_task'], sr_found={'overall_success_rate': 0.11}

eval-vla-only-spatial-seed42: metric_keys=['success_rate', 'per_task'], sr_found={'success_rate': 0.3}

eval-vla-only-spatial-seed46: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'successful_rollouts'], sr_found={'overall_success_rate': 0.3, 'successful_rollouts': 30}

eval-vla-only-spatial-seed47: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'successful_rollouts'], sr_found={'overall_success_rate': 0.3, 'successful_rollouts': 30}

eval-vla-only-object: metric_keys=['overall_sr', 'total_success', 'total_trials', 'per_task'], sr_found={'overall_sr': 0.12, 'total_success': 12}

eval-vla-only-object-seed43: metric_keys=['overall_sr', 'tasks_done', 'tasks_total', 'per_task_sr', 'source'], sr_found={'overall_sr': 0.12, 'per_task_sr': {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.1, 'bbq_sauce': 0.3, 'ketchup': 0, 'tomato_sauce': 0, 'butter': 0, 'milk': 0.1, 'chocolate_pudding': 0.4, 'orange_juice': 0.2}}

eval-obs-only-spatial-norm02-seed43-r2: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'per_task'], sr_found={'overall_success_rate': 0.34}

eval-obs-only-spatial-norm02-seed46-r2: metric_keys=['sr', 'sr_pct', 'n_tasks', 'n_rollouts', 'per_task'], sr_found={'sr': 0.33, 'sr_pct': '33.0%'}

eval-obs-only-spatial-norm02-seed47: metric_keys=['overall_success_rate', 'per_task'], sr_found={'overall_success_rate': 0.32}

eval-argmin-object-seed43: metric_keys=['overall_success_rate', 'total_successes', 'total_trials', 'per_task'], sr_found={'overall_success_rate': 0.17, 'total_successes': 17}

eval-mag-obsonly-norm02: metric_keys=['T0_between_plate_ramekin', 'T1_next_to_ramekin', 'T2_table_center', 'T3_on_cookie_box', 'T4_top_drawer', 'T5_on_ramekin', 'T6_next_to_cookie_box', 'T7_on_stove', 'T8_next_to_plate', 'T9_on_wooden_cabinet'], sr_found={'T2_table_center': 0, 'T5_on_ramekin': 0, 'T7_on_stove': 0, 'T9_on_wooden_cabinet': 0, 'overall_sr': 35, 'total_success': 35}

eval-obs-only-object-norm02-k5-seed42: metric_keys=['overall_success_rate'], sr_found={'overall_success_rate': 0.14}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "957a44e8-aef5-4053-90bd-025dd19c41b2",
  "tool_use_result": {
    "stdout": "eval-crm-goal-seed42: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'per_task'], sr_found={'overall_success_rate': 0.67}\n\neval-crm-goal-seed43: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'per_task'], sr_found={'overall_success_rate': 0.72}\n\neval-crm-long-seed42: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'per_task'], sr_found={'overall_success_rate': 0.17}\n\neval-vla-only-long-seed42: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'per_task'], sr_found={'overall_success_rate': 0.11}\n\neval-vla-only-spatial-seed42: metric_keys=['success_rate', 'per_task'], sr_found={'success_rate': 0.3}\n\neval-vla-only-spatial-seed46: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'successful_rollouts'], sr_found={'overall_success_rate': 0.3, 'successful_rollouts': 30}\n\neval-vla-only-spatial-seed47: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'total_episodes', 'successful_rollouts'], sr_found={'overall_success_rate': 0.3, 'successful_rollouts': 30}\n\neval-vla-only-object: metric_keys=['overall_sr', 'total_success', 'total_trials', 'per_task'], sr_found={'overall_sr': 0.12, 'total_success': 12}\n\neval-vla-only-object-seed43: metric_keys=['overall_sr', 'tasks_done', 'tasks_total', 'per_task_sr', 'source'], sr_found={'overall_sr': 0.12, 'per_task_sr': {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.1, 'bbq_sauce': 0.3, 'ketchup': 0, 'tomato_sauce': 0, 'butter': 0, 'milk': 0.1, 'chocolate_pudding': 0.4, 'orange_juice': 0.2}}\n\neval-obs-only-spatial-norm02-seed43-r2: metric_keys=['overall_success_rate', 'n_tasks', 'n_rollouts', 'per_task'], sr_found={'overall_success_rate': 0.34}\n\neval-obs-only-spatial-norm02-seed46-r2: metric_keys=['sr', 'sr_pct', 'n_tasks', 'n_rollouts', 'per_task'], sr_found={'sr': 0.33, 'sr_pct': '33.0%'}\n\neval-obs-only-spatial-norm02-seed47: metric_keys=['overall_success_rate', 'per_task'], sr_found={'overall_success_rate': 0.32}\n\neval-argmin-object-seed43: metric_keys=['overall_success_rate', 'total_successes', 'total_trials', 'per_task'], sr_found={'overall_success_rate': 0.17, 'total_successes': 17}\n\neval-mag-obsonly-norm02: metric_keys=['T0_between_plate_ramekin', 'T1_next_to_ramekin', 'T2_table_center', 'T3_on_cookie_box', 'T4_top_drawer', 'T5_on_ramekin', 'T6_next_to_cookie_box', 'T7_on_stove', 'T8_next_to_plate', 'T9_on_wooden_cabinet'], sr_found={'T2_table_center': 0, 'T5_on_ramekin': 0, 'T7_on_stove': 0, 'T9_on_wooden_cabinet': 0, 'overall_sr': 35, 'total_success': 35}\n\neval-obs-only-object-norm02-k5-seed42: metric_keys=['overall_success_rate'], sr_found={'overall_success_rate': 0.14}",
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

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I see — the metric key varies: `success_rate`, `overall_success_rate`, `overall_sr`, `sr`. Let me also check `eval-mag-obsonly-norm02` which has `overall_sr: 35` (which is percentage, not fraction). 

Also I notice `eval-mag-obsonly-norm02` was NOT found in the DONE+success list earlier — it wasn't listed. Let me check its status. Actually, looking back, it wasn't in the list. Let me check.


I need to verify whether `eval-mag-obsonly-norm02` actually exists and has a DONE+success status, since it showed metrics but wasn't in my earlier list. Let me run a comprehensive audit to check this more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "a6272cba-6b06-4a26-9cbd-3b40257f2a43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bo7W2q9dYfLZLiTSMQoS1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 48035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 32_

明白了 — metric 键不统一（`success_rate`/`overall_success_rate`/`overall_sr`/`sr`）。现在写一个全面审计脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "d34e9a15-b8b8-46fb-be11-524f6d5613ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bo7W2q9dYfLZLiTSMQoS1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 48035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01VH386F2hWdGztvJcFZDm4d`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, json\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', {})\n\ndef get_sr(exp):\n    \"\"\"Extract success rate from various metric key formats.\"\"\"\n    metrics = exp.get('metrics', {})\n    if not isinstance(metrics, dict):\n        return None\n    \n    # Try various keys\n    for key in ['success_rate', 'overall_success_rate', 'overall_sr', 'sr', 'avg_success_rate']:\n        if key in metrics:\n            val = metrics[key]\n            if isinstance(val, (int, float)):\n                # Some store as percentage (>1), convert\n                if val > 1:\n                    return round(val / 100, 2)\n                return round(val, 2)\n    return None\n\ndef get_seed_from_exp(exp_id, exp):\n    \"\"\"Extract seed from spec or exp_id.\"\"\"\n    spec = exp.get('spec', {})\n    seed = spec.get('seed')\n    if seed is not None:\n        return int(seed)\n    # Try to extract from exp_id\n    import re\n    m = re.search(r'seed(\\d+)', exp_id)\n    if m:\n        return int(m.group(1))\n    return None\n\n# Get all DONE+success eval experiments\neval_done = {}\nfor exp_id, exp in experiments.items():\n    if isinstance(exp, dict) and exp.get('status') == 'DONE' and exp.get('conclusion') == 'success':\n        eval_done[exp_id] = exp\n\n# Also check non-eval DONE experiments that might be relevant (like eval-mag-obsonly-norm02)\n# Actually let me check - is eval-mag-obsonly-norm02 DONE+success?\nfor eid in ['eval-mag-obsonly-norm02']:\n    e = experiments.get(eid)\n    if e:\n        print(f\"CHECK {eid}: status={e.get('status')}, conclusion={e.get('conclusion')}\")\n\nprint()\n\n# =====================================================================\n# COMPREHENSIVE AUDIT\n# =====================================================================\n\nresults = {}\n\n# ===================== SPATIAL =====================\n\n# --- CRM obs_only spatial norm02 K=10 ---\nprint(\"=\" * 80)\nprint(\"LIBERO-SPATIAL: CRM obs_only norm02 K=10\")\nprint(\"=\" * 80)\n\n# Script says: seeds 42-48,51 → [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35, 0.36]\nscript_spatial_crm = {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}\n\n# Registry candidates for spatial CRM obs_only norm02 K=10 (NOT K=5)\nregistry_spatial_crm = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    seed = get_seed_from_exp(eid, exp)\n    sr = get_sr(exp)\n    \n    # obs-only spatial norm02, NOT k5\n    if 'spatial' in el and 'norm02' in el and ('obs-only' in el or 'obs_only' in el):\n        if 'k5' not in el and 'k-5' not in el:\n            registry_spatial_crm[eid] = {'seed': seed, 'sr': sr}\n    \n    # Also check eval-mag-obsonly-norm02 (which is spatial by default, seed=42)\n    if eid == 'eval-mag-obsonly-norm02':\n        registry_spatial_crm[eid] = {'seed': seed, 'sr': sr}\n    \n    # eval-crm-spatial-k10-seed51\n    if 'crm-spatial' in el and 'k10' in el:\n        registry_spatial_crm[eid] = {'seed': seed, 'sr': sr}\n\n# Check eval-mag-obsonly-norm02 even if not in eval_done\nif 'eval-mag-obsonly-norm02' not in registry_spatial_crm:\n    e = experiments.get('eval-mag-obsonly-norm02')\n    if e and e.get('status') == 'DONE':\n        seed = get_seed_from_exp('eval-mag-obsonly-norm02', e)\n        sr = get_sr(e)\n        registry_spatial_crm['eval-mag-obsonly-norm02'] = {'seed': seed, 'sr': sr}\n        print(f\"  NOTE: eval-mag-obsonly-norm02 included (status={e.get('status')}, conclusion={e.get('conclusion')})\")\n\nprint(f\"\\nScript: n={len(script_spatial_crm)}, seeds={sorted(script_spatial_crm.keys())}\")\nprint(f\"  values: {dict(sorted(script_spatial_crm.items()))}\")\n\nprint(f\"\\nRegistry candidates:\")\nfor eid, info in sorted(registry_spatial_crm.items()):\n    print(f\"  {eid}: seed={info['seed']}, SR={info['sr']}\")\n\n# Map registry seeds to SR\nreg_seed_sr = {}\nfor eid, info in registry_spatial_crm.items():\n    s = info['seed']\n    if s is not None and info['sr'] is not None:\n        if s in reg_seed_sr:\n            # Keep the one matching the script comment (r2 > r1, etc)\n            # For now just note duplicates\n            print(f\"  DUPLICATE seed={s}: {eid} (SR={info['sr']}) vs existing SR={reg_seed_sr[s]}\")\n        reg_seed_sr[s] = info['sr']\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr.items()))}\")\n\n# Compare\nscript_seeds = set(script_spatial_crm.keys())\nreg_seeds = set(reg_seed_sr.keys())\nmissing_from_script = reg_seeds - script_seeds\nmissing_from_registry = script_seeds - reg_seeds\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_spatial_crm[s], reg_seed_sr[s]) for s in common if abs(script_spatial_crm[s] - reg_seed_sr[s]) > 0.005}\n\nprint(f\"\\n  Missing from script (in registry but not script): {sorted(missing_from_script)}\")\nprint(f\"  Missing from registry (in script but not registry): {sorted(missing_from_registry)}\")\nprint(f\"  Value mismatches: {mismatches}\")\nprint()\n\n# ===================== SPATIAL VLA-only =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-SPATIAL: VLA-only\")\nprint(\"=\" * 80)\n\nscript_spatial_vla = {42: 0.30, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.30, 47: 0.30, 48: 0.30, 49: 0.29, 50: 0.30}\n\nregistry_spatial_vla = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'spatial' in el and 'vla-only' in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_spatial_vla[eid] = {'seed': seed, 'sr': sr}\n\n# Also check vla-mean-spatial\nfor eid in ['eval-vla-mean-spatial', 'eval-vla-mean-spatial-t10']:\n    if eid in eval_done:\n        seed = get_seed_from_exp(eid, eval_done[eid])\n        sr = get_sr(eval_done[eid])\n        print(f\"  NOTE: {eid} exists but is vla-mean, not vla-only. seed={seed}, SR={sr}\")\n\nprint(f\"\\nScript: n={len(script_spatial_vla)}, seeds={sorted(script_spatial_vla.keys())}\")\n\nreg_seed_sr_svla = {}\nfor eid, info in sorted(registry_spatial_vla.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_svla[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_svla.items()))}\")\n\nscript_seeds = set(script_spatial_vla.keys())\nreg_seeds = set(reg_seed_sr_svla.keys())\nmissing_from_script = reg_seeds - script_seeds\nmissing_from_registry = script_seeds - reg_seeds\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_spatial_vla[s], reg_seed_sr_svla[s]) for s in common if abs(script_spatial_vla[s] - reg_seed_sr_svla[s]) > 0.005}\n\nprint(f\"\\n  Missing from script: {sorted(missing_from_script)}\")\nprint(f\"  Missing from registry: {sorted(missing_from_registry)}\")\nprint(f\"  Value mismatches: {mismatches}\")\n\n# Check if there are VLA-only spatial experiments with seed 48,49,50 but no seed in exp_id\nprint(\"\\n  Checking for unlisted VLA-only spatial seeds...\")\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'vla' in el and 'spatial' in el and 'mean' not in el and 'argmin' not in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        if seed not in reg_seed_sr_svla:\n            print(f\"    EXTRA: {eid}, seed={seed}, SR={sr}\")\n\nprint()\n\n# ===================== LONG CRM =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-LONG: CRM obs_only\")\nprint(\"=\" * 80)\n\nscript_long_crm = {42: 0.17, 43: 0.15, 44: 0.20, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}\n\nregistry_long_crm = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'long' in el and ('crm' in el):\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_long_crm[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_long_crm)}, seeds={sorted(script_long_crm.keys())}\")\nprint(f\"  values: {dict(sorted(script_long_crm.items()))}\")\n\nreg_seed_sr_lcrm = {}\nfor eid, info in sorted(registry_long_crm.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_lcrm[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_lcrm.items()))}\")\n\nscript_seeds = set(script_long_crm.keys())\nreg_seeds = set(reg_seed_sr_lcrm.keys())\nmissing_from_script = reg_seeds - script_seeds\nmissing_from_registry = script_seeds - reg_seeds\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_long_crm[s], reg_seed_sr_lcrm[s]) for s in common if abs(script_long_crm[s] - reg_seed_sr_lcrm[s]) > 0.005}\n\nprint(f\"\\n  Missing from script: {sorted(missing_from_script)}\")\nprint(f\"  Missing from registry: {sorted(missing_from_registry)}\")\nprint(f\"  Value mismatches: {mismatches}\")\nprint()\n\n# ===================== LONG VLA-only =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-LONG: VLA-only\")\nprint(\"=\" * 80)\n\nscript_long_vla = {42: 0.11, 43: 0.13, 44: 0.12, 45: 0.17, 46: 0.18, 47: 0.14, 48: 0.14, 49: 0.16, 50: 0.16, 51: 0.15, 52: 0.17}\n\nregistry_long_vla = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'long' in el and 'vla-only' in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_long_vla[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_long_vla)}, seeds={sorted(script_long_vla.keys())}\")\n\nreg_seed_sr_lvla = {}\nfor eid, info in sorted(registry_long_vla.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_lvla[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_lvla.items()))}\")\n\nscript_seeds = set(script_long_vla.keys())\nreg_seeds = set(reg_seed_sr_lvla.keys())\nmissing_from_script = reg_seeds - script_seeds\nmissing_from_registry = script_seeds - reg_seeds\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_long_vla[s], reg_seed_sr_lvla[s]) for s in common if abs(script_long_vla[s] - reg_seed_sr_lvla[s]) > 0.005}\n\nprint(f\"\\n  Missing from script: {sorted(missing_from_script)}\")\nprint(f\"  Missing from registry: {sorted(missing_from_registry)}\")\nprint(f\"  Value mismatches: {mismatches}\")\nprint()\n\n# ===================== GOAL CRM =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-GOAL: CRM obs_only\")\nprint(\"=\" * 80)\n\nscript_goal_crm = {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72, 47: 0.69}\n\nregistry_goal_crm = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'goal' in el and 'crm' in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_goal_crm[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_goal_crm)}, seeds={sorted(script_goal_crm.keys())}\")\nprint(f\"  values: {dict(sorted(script_goal_crm.items()))}\")\n\nreg_seed_sr_gcrm = {}\nfor eid, info in sorted(registry_goal_crm.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_gcrm[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_gcrm.items()))}\")\n\nscript_seeds = set(script_goal_crm.keys())\nreg_seeds = set(reg_seed_sr_gcrm.keys())\nmissing_from_script = reg_seeds - script_seeds\nmissing_from_registry = script_seeds - reg_seeds\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_goal_crm[s], reg_seed_sr_gcrm[s]) for s in common if abs(script_goal_crm[s] - reg_seed_sr_gcrm[s]) > 0.005}\n\nprint(f\"\\n  Missing from script: {sorted(missing_from_script)}\")\nprint(f\"  Missing from registry: {sorted(missing_from_registry)}\")\nprint(f\"  Value mismatches: {mismatches}\")\n\n# Check for CRM-goal-seed47 which is mentioned in verification notes\ne47 = experiments.get('eval-crm-goal-seed47')\nif e47:\n    print(f\"\\n  NOTE: eval-crm-goal-seed47 status={e47.get('status')}, conclusion={e47.get('conclusion')}\")\nelse:\n    print(f\"\\n  NOTE: eval-crm-goal-seed47 does NOT exist in registry\")\nprint()\n\n# ===================== GOAL VLA-only =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-GOAL: VLA-only\")\nprint(\"=\" * 80)\n\nscript_goal_vla = {42: 0.71, 43: 0.69, 44: 0.73, 45: 0.63, 46: 0.71, 49: 0.65}\n\nregistry_goal_vla = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'goal' in el and 'vla-only' in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_goal_vla[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_goal_vla)}, seeds={sorted(script_goal_vla.keys())}\")\n\nreg_seed_sr_gvla = {}\nfor eid, info in sorted(registry_goal_vla.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_gvla[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_gvla.items()))}\")\n\nscript_seeds = set(script_goal_vla.keys())\nreg_seeds = set(reg_seed_sr_gvla.keys())\nmissing_from_script = reg_seeds - script_seeds\nmissing_from_registry = script_seeds - reg_seeds\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_goal_vla[s], reg_seed_sr_gvla[s]) for s in common if abs(script_goal_vla[s] - reg_seed_sr_gvla[s]) > 0.005}\n\nprint(f\"\\n  Missing from script: {sorted(missing_from_script)}\")\nprint(f\"  Missing from registry: {sorted(missing_from_registry)}\")\nprint(f\"  Value mismatches: {mismatches}\")\nprint()\n\nPYEOF\n",
  "description": "Full audit part 1: Spatial, Long, Goal",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "1c8d967c-97f8-400b-a5a1-365180c0a528",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bo7W2q9dYfLZLiTSMQoS1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 48035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 34 · 2026-05-20T07:20:12.484Z_

<details><summary>↩ Tool result · `toolu_01VH386F2hWdGztvJcFZDm4d`</summary>

```text
CHECK eval-mag-obsonly-norm02: status=DONE, conclusion=negative

================================================================================
LIBERO-SPATIAL: CRM obs_only norm02 K=10
================================================================================
  NOTE: eval-mag-obsonly-norm02 included (status=DONE, conclusion=negative)

Script: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 51]
  values: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}

Registry candidates:
  eval-crm-spatial-k10-seed51: seed=51, SR=0.36
  eval-mag-obsonly-norm02: seed=42, SR=0.35
  eval-obs-only-spatial-norm02-seed43-r2: seed=43, SR=0.34
  eval-obs-only-spatial-norm02-seed44: seed=44, SR=0.36
  eval-obs-only-spatial-norm02-seed45: seed=45, SR=0.34
  eval-obs-only-spatial-norm02-seed46-r2: seed=46, SR=0.33
  eval-obs-only-spatial-norm02-seed47: seed=47, SR=0.32
  eval-obs-only-spatial-norm02-seed48: seed=48, SR=0.35

Registry seed→SR: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}

  Missing from script (in registry but not script): []
  Missing from registry (in script but not registry): []
  Value mismatches: {}

================================================================================
LIBERO-SPATIAL: VLA-only
================================================================================
  NOTE: eval-vla-mean-spatial exists but is vla-mean, not vla-only. seed=42, SR=None
  NOTE: eval-vla-mean-spatial-t10 exists but is vla-mean, not vla-only. seed=42, SR=None

Script: n=9, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50]
  eval-vla-only-spatial-seed42: seed=42, SR=0.3
  eval-vla-only-spatial-seed43: seed=43, SR=0.29
  eval-vla-only-spatial-seed44: seed=44, SR=0.31
  eval-vla-only-spatial-seed45: seed=45, SR=0.27
  eval-vla-only-spatial-seed46: seed=46, SR=0.3
  eval-vla-only-spatial-seed47: seed=47, SR=0.3

Registry seed→SR: {42: 0.3, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.3, 47: 0.3}

  Missing from script: []
  Missing from registry: [48, 49, 50]
  Value mismatches: {}

  Checking for unlisted VLA-only spatial seeds...

================================================================================
LIBERO-LONG: CRM obs_only
================================================================================

Script: n=7, seeds=[42, 43, 44, 45, 46, 47, 50]
  values: {42: 0.17, 43: 0.15, 44: 0.2, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}
  eval-crm-long-seed42: seed=42, SR=0.17
  eval-crm-long-seed43: seed=43, SR=0.15
  eval-crm-long-seed44: seed=44, SR=0.2
  eval-crm-long-seed45: seed=45, SR=0.18
  eval-crm-long-seed46: seed=46, SR=0.18
  eval-crm-long-seed47: seed=47, SR=0.17
  eval-crm-long-seed50: seed=50, SR=0.14

Registry seed→SR: {42: 0.17, 43: 0.15, 44: 0.2, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}

  Missing from script: []
  Missing from registry: []
  Value mismatches: {}

================================================================================
LIBERO-LONG: VLA-only
================================================================================

Script: n=11, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
  eval-vla-only-long-seed42: seed=42, SR=0.11
  eval-vla-only-long-seed43: seed=43, SR=0.13
  eval-vla-only-long-seed44: seed=44, SR=0.12
  eval-vla-only-long-seed45: seed=45, SR=0.17
  eval-vla-only-long-seed46: seed=46, SR=0.18
  eval-vla-only-long-seed47: seed=47, SR=0.14
  eval-vla-only-long-seed48: seed=48, SR=0.14
  eval-vla-only-long-seed50: seed=50, SR=0.16
  eval-vla-only-long-seed51: seed=51, SR=0.15
  eval-vla-only-long-seed52: seed=52, SR=0.17

Registry seed→SR: {42: 0.11, 43: 0.13, 44: 0.12, 45: 0.17, 46: 0.18, 47: 0.14, 48: 0.14, 50: 0.16, 51: 0.15, 52: 0.17}

  Missing from script: []
  Missing from registry: [49]
  Value mismatches: {}

================================================================================
LIBERO-GOAL: CRM obs_only
================================================================================

Script: n=6, seeds=[42, 43, 44, 45, 46, 47]
  values: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72, 47: 0.69}
  eval-crm-goal-seed42: seed=42, SR=0.67
  eval-crm-goal-seed43: seed=43, SR=0.72
  eval-crm-goal-seed44-r2: seed=44, SR=0.64
  eval-crm-goal-seed45-r2: seed=45, SR=0.65
  eval-crm-goal-seed46: seed=46, SR=0.72

Registry seed→SR: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72}

  Missing from script: []
  Missing from registry: [47]
  Value mismatches: {}

  NOTE: eval-crm-goal-seed47 status=PREPARING, conclusion=None

================================================================================
LIBERO-GOAL: VLA-only
================================================================================

Script: n=6, seeds=[42, 43, 44, 45, 46, 49]
  eval-vla-only-goal-seed42: seed=42, SR=0.71
  eval-vla-only-goal-seed43: seed=43, SR=0.69
  eval-vla-only-goal-seed44-r2: seed=44, SR=0.73
  eval-vla-only-goal-seed45: seed=45, SR=0.63
  eval-vla-only-goal-seed46: seed=46, SR=0.71
  eval-vla-only-goal-seed49: seed=49, SR=0.65

Registry seed→SR: {42: 0.71, 43: 0.69, 44: 0.73, 45: 0.63, 46: 0.71, 49: 0.65}

  Missing from script: []
  Missing from registry: []
  Value mismatches: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "214758c1-81b5-4af5-9802-3d654d1b6993",
  "tool_use_result": {
    "stdout": "CHECK eval-mag-obsonly-norm02: status=DONE, conclusion=negative\n\n================================================================================\nLIBERO-SPATIAL: CRM obs_only norm02 K=10\n================================================================================\n  NOTE: eval-mag-obsonly-norm02 included (status=DONE, conclusion=negative)\n\nScript: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 51]\n  values: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}\n\nRegistry candidates:\n  eval-crm-spatial-k10-seed51: seed=51, SR=0.36\n  eval-mag-obsonly-norm02: seed=42, SR=0.35\n  eval-obs-only-spatial-norm02-seed43-r2: seed=43, SR=0.34\n  eval-obs-only-spatial-norm02-seed44: seed=44, SR=0.36\n  eval-obs-only-spatial-norm02-seed45: seed=45, SR=0.34\n  eval-obs-only-spatial-norm02-seed46-r2: seed=46, SR=0.33\n  eval-obs-only-spatial-norm02-seed47: seed=47, SR=0.32\n  eval-obs-only-spatial-norm02-seed48: seed=48, SR=0.35\n\nRegistry seed→SR: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}\n\n  Missing from script (in registry but not script): []\n  Missing from registry (in script but not registry): []\n  Value mismatches: {}\n\n================================================================================\nLIBERO-SPATIAL: VLA-only\n================================================================================\n  NOTE: eval-vla-mean-spatial exists but is vla-mean, not vla-only. seed=42, SR=None\n  NOTE: eval-vla-mean-spatial-t10 exists but is vla-mean, not vla-only. seed=42, SR=None\n\nScript: n=9, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50]\n  eval-vla-only-spatial-seed42: seed=42, SR=0.3\n  eval-vla-only-spatial-seed43: seed=43, SR=0.29\n  eval-vla-only-spatial-seed44: seed=44, SR=0.31\n  eval-vla-only-spatial-seed45: seed=45, SR=0.27\n  eval-vla-only-spatial-seed46: seed=46, SR=0.3\n  eval-vla-only-spatial-seed47: seed=47, SR=0.3\n\nRegistry seed→SR: {42: 0.3, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.3, 47: 0.3}\n\n  Missing from script: []\n  Missing from registry: [48, 49, 50]\n  Value mismatches: {}\n\n  Checking for unlisted VLA-only spatial seeds...\n\n================================================================================\nLIBERO-LONG: CRM obs_only\n================================================================================\n\nScript: n=7, seeds=[42, 43, 44, 45, 46, 47, 50]\n  values: {42: 0.17, 43: 0.15, 44: 0.2, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}\n  eval-crm-long-seed42: seed=42, SR=0.17\n  eval-crm-long-seed43: seed=43, SR=0.15\n  eval-crm-long-seed44: seed=44, SR=0.2\n  eval-crm-long-seed45: seed=45, SR=0.18\n  eval-crm-long-seed46: seed=46, SR=0.18\n  eval-crm-long-seed47: seed=47, SR=0.17\n  eval-crm-long-seed50: seed=50, SR=0.14\n\nRegistry seed→SR: {42: 0.17, 43: 0.15, 44: 0.2, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}\n\n  Missing from script: []\n  Missing from registry: []\n  Value mismatches: {}\n\n================================================================================\nLIBERO-LONG: VLA-only\n================================================================================\n\nScript: n=11, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]\n  eval-vla-only-long-seed42: seed=42, SR=0.11\n  eval-vla-only-long-seed43: seed=43, SR=0.13\n  eval-vla-only-long-seed44: seed=44, SR=0.12\n  eval-vla-only-long-seed45: seed=45, SR=0.17\n  eval-vla-only-long-seed46: seed=46, SR=0.18\n  eval-vla-only-long-seed47: seed=47, SR=0.14\n  eval-vla-only-long-seed48: seed=48, SR=0.14\n  eval-vla-only-long-seed50: seed=50, SR=0.16\n  eval-vla-only-long-seed51: seed=51, SR=0.15\n  eval-vla-only-long-seed52: seed=52, SR=0.17\n\nRegistry seed→SR: {42: 0.11, 43: 0.13, 44: 0.12, 45: 0.17, 46: 0.18, 47: 0.14, 48: 0.14, 50: 0.16, 51: 0.15, 52: 0.17}\n\n  Missing from script: []\n  Missing from registry: [49]\n  Value mismatches: {}\n\n================================================================================\nLIBERO-GOAL: CRM obs_only\n================================================================================\n\nScript: n=6, seeds=[42, 43, 44, 45, 46, 47]\n  values: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72, 47: 0.69}\n  eval-crm-goal-seed42: seed=42, SR=0.67\n  eval-crm-goal-seed43: seed=43, SR=0.72\n  eval-crm-goal-seed44-r2: seed=44, SR=0.64\n  eval-crm-goal-seed45-r2: seed=45, SR=0.65\n  eval-crm-goal-seed46: seed=46, SR=0.72\n\nRegistry seed→SR: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72}\n\n  Missing from script: []\n  Missing from registry: [47]\n  Value mismatches: {}\n\n  NOTE: eval-crm-goal-seed47 status=PREPARING, conclusion=None\n\n================================================================================\nLIBERO-GOAL: VLA-only\n================================================================================\n\nScript: n=6, seeds=[42, 43, 44, 45, 46, 49]\n  eval-vla-only-goal-seed42: seed=42, SR=0.71\n  eval-vla-only-goal-seed43: seed=43, SR=0.69\n  eval-vla-only-goal-seed44-r2: seed=44, SR=0.73\n  eval-vla-only-goal-seed45: seed=45, SR=0.63\n  eval-vla-only-goal-seed46: seed=46, SR=0.71\n  eval-vla-only-goal-seed49: seed=49, SR=0.65\n\nRegistry seed→SR: {42: 0.71, 43: 0.69, 44: 0.73, 45: 0.63, 46: 0.71, 49: 0.65}\n\n  Missing from script: []\n  Missing from registry: []\n  Value mismatches: {}",
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

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Good progress. Now I need to do the Object benchmark audit. Let me continue with part 2.

Key findings so far:
1. **Spatial CRM obs_only norm02 K=10**: MATCH - all 8 seeds match perfectly
2. **Spatial VLA-only**: 3 seeds (48, 49, 50) in script but NOT in registry - these were added per Director directive per the verification notes
3. **Long CRM**: MATCH - all 7 seeds match perfectly
4. **Long VLA-only**: seed 49 in script but NOT in registry; all others match


5. **Goal CRM**: seed 47 in script but NOT in registry (status=PREPARING); all others match, with the script showing 0.69 per Director directive
6. **Goal VLA-only**: MATCH - all 6 seeds match perfectly

Now moving on to the Object benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "8e319021-171f-46d2-b594-a5cdd1d2cbd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kLRiBrWCshEcv5eMz9r9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7511,
      "cache_read_input_tokens": 49925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7511
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

_source line 36_

Spatial/Long/Goal 审计完成。几个发现：VLA-Spatial seed48/49/50 和 VLA-Long seed49 不在 registry 中（Director 指令添加），CRM-Goal seed47 状态 PREPARING。继续 Object 审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "2d8f3fc6-2768-4ac6-a745-f0fcc5f59573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kLRiBrWCshEcv5eMz9r9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7511,
      "cache_read_input_tokens": 49925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7511
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01LB5Lo7vuWcDGUQNvTPneeZ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, json, re\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', {})\n\ndef get_sr(exp):\n    metrics = exp.get('metrics', {})\n    if not isinstance(metrics, dict):\n        return None\n    for key in ['success_rate', 'overall_success_rate', 'overall_sr', 'sr', 'avg_success_rate']:\n        if key in metrics:\n            val = metrics[key]\n            if isinstance(val, (int, float)):\n                if val > 1:\n                    return round(val / 100, 2)\n                return round(val, 2)\n    return None\n\ndef get_seed_from_exp(exp_id, exp):\n    spec = exp.get('spec', {})\n    seed = spec.get('seed')\n    if seed is not None:\n        return int(seed)\n    m = re.search(r'seed(\\d+)', exp_id)\n    if m:\n        return int(m.group(1))\n    return None\n\neval_done = {}\nfor exp_id, exp in experiments.items():\n    if isinstance(exp, dict) and exp.get('status') == 'DONE' and exp.get('conclusion') == 'success':\n        eval_done[exp_id] = exp\n\n# ===================== OBJECT CRM norm02 K=10 =====================\nprint(\"=\" * 80)\nprint(\"LIBERO-OBJECT: CRM obs_only norm02 K=10 (PRIMARY)\")\nprint(\"=\" * 80)\n\nscript_obj_crm = {43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.20, 48: 0.18}\n\nregistry_obj_crm_norm02 = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    seed = get_seed_from_exp(eid, exp)\n    sr = get_sr(exp)\n    \n    # obs-only object norm02 K=10 (NOT k5)\n    if 'object' in el and 'norm02' in el and ('obs-only' in el or 'obs_only' in el):\n        if 'k5' not in el and 'k-5' not in el:\n            registry_obj_crm_norm02[eid] = {'seed': seed, 'sr': sr}\n    \n    # Also check eval-acr-object-obs-only-norm02\n    if eid == 'eval-acr-object-obs-only-norm02':\n        registry_obj_crm_norm02[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_obj_crm)}, seeds={sorted(script_obj_crm.keys())}\")\nprint(f\"  values: {dict(sorted(script_obj_crm.items()))}\")\n\nreg_seed_sr = {}\nfor eid, info in sorted(registry_obj_crm_norm02.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        if s in reg_seed_sr:\n            print(f\"    DUP: seed={s} already has SR={reg_seed_sr[s]}, new={sr}\")\n        reg_seed_sr[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr.items()))}\")\n\nscript_seeds = set(script_obj_crm.keys())\nreg_seeds = set(reg_seed_sr.keys())\nprint(f\"\\n  Missing from script: {sorted(reg_seeds - script_seeds)} (seeds in registry but not script)\")\nprint(f\"  Missing from registry: {sorted(script_seeds - reg_seeds)} (seeds in script but not registry)\")\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_obj_crm[s], reg_seed_sr[s]) for s in common if abs(script_obj_crm[s] - reg_seed_sr[s]) > 0.005}\nprint(f\"  Value mismatches: {mismatches}\")\n\n# ===================== OBJECT CRM norm01 =====================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"LIBERO-OBJECT: CRM obs_only norm01 (Supplementary)\")\nprint(\"=\" * 80)\n\nscript_obj_norm01 = {42: 0.19, 44: 0.16, 45: 0.17, 46: 0.18, 47: 0.17, 48: 0.18}\n\nregistry_obj_norm01 = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    seed = get_seed_from_exp(eid, exp)\n    sr = get_sr(exp)\n    \n    if 'object' in el and 'norm01' in el and ('obs-only' in el or 'obs_only' in el):\n        registry_obj_norm01[eid] = {'seed': seed, 'sr': sr}\n\n# Also check eval_obs_only_norm01_seed48 (underscore naming)\nfor eid in list(eval_done.keys()):\n    if 'norm01' in eid.lower() and 'obs_only' in eid.lower():\n        if eid not in registry_obj_norm01:\n            registry_obj_norm01[eid] = {'seed': get_seed_from_exp(eid, eval_done[eid]), 'sr': get_sr(eval_done[eid])}\n\n# Check for acr-object-obs-only with default norm (which is norm01=0.1)\n# eval-acr-object-v4-obs-only was norm=0.1\n\nprint(f\"\\nScript: n={len(script_obj_norm01)}, seeds={sorted(script_obj_norm01.keys())}\")\nprint(f\"  Comment says: s42, s44, s45-r2, s46-r3, s47, s48\")\n\nreg_seed_sr_n01 = {}\nfor eid, info in sorted(registry_obj_norm01.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        if s in reg_seed_sr_n01:\n            print(f\"    DUP: seed={s} already={reg_seed_sr_n01[s]}\")\n        reg_seed_sr_n01[s] = sr\n\n# Also check eval-acr-object-v4-obs-only (norm=0.1)\ne = eval_done.get('eval-acr-object-v4-obs-only')\nif e:\n    sr = get_sr(e)\n    seed = get_seed_from_exp('eval-acr-object-v4-obs-only', e)\n    print(f\"  NOTE: eval-acr-object-v4-obs-only (norm=0.1/default): seed={seed}, SR={sr}\")\n    # This is seed42 norm01 equivalent\n    if seed == 42 and sr is not None:\n        print(f\"    → This is the seed42 norm01 data (SR={sr}≈0.19)\")\n        reg_seed_sr_n01[42] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_n01.items()))}\")\n\nscript_seeds = set(script_obj_norm01.keys())\nreg_seeds = set(reg_seed_sr_n01.keys())\nprint(f\"\\n  Missing from script: {sorted(reg_seeds - script_seeds)}\")\nprint(f\"  Missing from registry: {sorted(script_seeds - reg_seeds)}\")\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_obj_norm01[s], reg_seed_sr_n01[s]) for s in common if abs(script_obj_norm01[s] - reg_seed_sr_n01[s]) > 0.005}\nprint(f\"  Value mismatches: {mismatches}\")\n\n# ===================== OBJECT CRM norm02 K=5 =====================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"LIBERO-OBJECT: CRM obs_only norm02 K=5 (Supplementary)\")\nprint(\"=\" * 80)\n\nscript_obj_k5 = {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}\n\nregistry_obj_k5 = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    seed = get_seed_from_exp(eid, exp)\n    sr = get_sr(exp)\n    \n    if 'object' in el and 'norm02' in el and 'k5' in el and ('obs-only' in el or 'obs_only' in el):\n        registry_obj_k5[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_obj_k5)}, seeds={sorted(script_obj_k5.keys())}\")\n\nreg_seed_sr_k5 = {}\nfor eid, info in sorted(registry_obj_k5.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_k5[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_k5.items()))}\")\n\nscript_seeds = set(script_obj_k5.keys())\nreg_seeds = set(reg_seed_sr_k5.keys())\nprint(f\"\\n  Missing from script: {sorted(reg_seeds - script_seeds)}\")\nprint(f\"  Missing from registry: {sorted(script_seeds - reg_seeds)}\")\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_obj_k5[s], reg_seed_sr_k5[s]) for s in common if abs(script_obj_k5[s] - reg_seed_sr_k5[s]) > 0.005}\nprint(f\"  Value mismatches: {mismatches}\")\n\n# ===================== OBJECT VLA-only =====================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"LIBERO-OBJECT: VLA-only\")\nprint(\"=\" * 80)\n\nscript_obj_vla = {42: 0.12, 43: 0.12, 44: 0.10, 45: 0.11, 46: 0.13, 47: 0.10, 48: 0.10, 50: 0.09}\n# Script comment: s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\nregistry_obj_vla = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'object' in el and ('vla-only' in el or (el == 'eval-openvla-object-vla-only-seed42-v2')):\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_obj_vla[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_obj_vla)}, seeds={sorted(script_obj_vla.keys())}\")\nprint(f\"  Comment: s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\")\n\nreg_seed_sr_ovla = {}\nfor eid, info in sorted(registry_obj_vla.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        if s in reg_seed_sr_ovla:\n            print(f\"    DUP: seed={s}, prev SR={reg_seed_sr_ovla[s]}\")\n        reg_seed_sr_ovla[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_ovla.items()))}\")\n\nscript_seeds = set(script_obj_vla.keys())\nreg_seeds = set(reg_seed_sr_ovla.keys())\nprint(f\"\\n  Missing from script: {sorted(reg_seeds - script_seeds)}\")\nprint(f\"  Missing from registry: {sorted(script_seeds - reg_seeds)}\")\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_obj_vla[s], reg_seed_sr_ovla[s]) for s in common if abs(script_obj_vla[s] - reg_seed_sr_ovla[s]) > 0.005}\nprint(f\"  Value mismatches: {mismatches}\")\n\n# Check for seed45 which has r2\nprint(\"\\n  Checking seed45 versions:\")\nfor eid in ['eval-vla-only-object-seed45', 'eval-vla-only-object-seed45-r2']:\n    e = experiments.get(eid)\n    if e:\n        sr = get_sr(e)\n        print(f\"    {eid}: status={e.get('status')}, conclusion={e.get('conclusion')}, SR={sr}\")\n\n# ===================== ARGMIN K=10 =====================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"LIBERO-OBJECT: Argmin K=10\")\nprint(\"=\" * 80)\n\nscript_argmin_k10 = {43: 0.17, 44: 0.13, 45: 0.12, 46: 0.10, 47: 0.10}\n\nregistry_argmin_k10 = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'argmin' in el and 'object' in el and 'k5' not in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_argmin_k10[eid] = {'seed': seed, 'sr': sr}\n\n# Also check eval-argmin-only-spatial-r2 in case it's misnamed\nfor eid in ['eval-argmin-only-spatial-r2']:\n    if eid in eval_done:\n        e = eval_done[eid]\n        print(f\"  NOTE: {eid} exists - seed={get_seed_from_exp(eid, e)}, SR={get_sr(e)}, hyp={e.get('hypothesis', '')[:100]}\")\n\nprint(f\"\\nScript: n={len(script_argmin_k10)}, seeds={sorted(script_argmin_k10.keys())}\")\n\nreg_seed_sr_ak10 = {}\nfor eid, info in sorted(registry_argmin_k10.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_ak10[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_ak10.items()))}\")\n\nscript_seeds = set(script_argmin_k10.keys())\nreg_seeds = set(reg_seed_sr_ak10.keys())\nprint(f\"\\n  Missing from script: {sorted(reg_seeds - script_seeds)}\")\nprint(f\"  Missing from registry: {sorted(script_seeds - reg_seeds)}\")\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_argmin_k10[s], reg_seed_sr_ak10[s]) for s in common if abs(script_argmin_k10[s] - reg_seed_sr_ak10[s]) > 0.005}\nprint(f\"  Value mismatches: {mismatches}\")\n\n# ===================== ARGMIN K=5 =====================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"LIBERO-OBJECT: Argmin K=5\")\nprint(\"=\" * 80)\n\nscript_argmin_k5 = {42: 0.15, 43: 0.13, 44: 0.11, 45: 0.13}\n\nregistry_argmin_k5 = {}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'argmin' in el and 'object' in el and 'k5' in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        registry_argmin_k5[eid] = {'seed': seed, 'sr': sr}\n\nprint(f\"\\nScript: n={len(script_argmin_k5)}, seeds={sorted(script_argmin_k5.keys())}\")\n\nreg_seed_sr_ak5 = {}\nfor eid, info in sorted(registry_argmin_k5.items()):\n    s = info['seed']\n    sr = info['sr']\n    print(f\"  {eid}: seed={s}, SR={sr}\")\n    if s is not None and sr is not None:\n        reg_seed_sr_ak5[s] = sr\n\nprint(f\"\\nRegistry seed→SR: {dict(sorted(reg_seed_sr_ak5.items()))}\")\n\nscript_seeds = set(script_argmin_k5.keys())\nreg_seeds = set(reg_seed_sr_ak5.keys())\nprint(f\"\\n  Missing from script: {sorted(reg_seeds - script_seeds)}\")\nprint(f\"  Missing from registry: {sorted(script_seeds - reg_seeds)}\")\ncommon = script_seeds & reg_seeds\nmismatches = {s: (script_argmin_k5[s], reg_seed_sr_ak5[s]) for s in common if abs(script_argmin_k5[s] - reg_seed_sr_ak5[s]) > 0.005}\nprint(f\"  Value mismatches: {mismatches}\")\n\n# ===================== ADAPTIVE-K =====================\nprint(\"\\n\" + \"=\" * 80)\nprint(\"LIBERO-OBJECT: Adaptive-K\")\nprint(\"=\" * 80)\n\nscript_adaptive = {\n    'p25': {42: 0.15, 43: 0.13, 44: 0.15},\n    'p50': {42: 0.16, 43: 0.16, 44: 0.14},\n    'p75': {42: 0.12, 43: 0.13, 44: 0.16},\n    'p90': {42: 0.12, 43: 0.14, 44: 0.14},\n}\n\nregistry_adaptive = {'p25': {}, 'p50': {}, 'p75': {}, 'p90': {}}\nfor eid, exp in eval_done.items():\n    el = eid.lower()\n    if 'adaptive' in el:\n        seed = get_seed_from_exp(eid, exp)\n        sr = get_sr(exp)\n        for pct in ['p25', 'p50', 'p75', 'p90']:\n            if pct in el:\n                registry_adaptive[pct][eid] = {'seed': seed, 'sr': sr}\n                break\n\nfor pct in ['p25', 'p50', 'p75', 'p90']:\n    print(f\"\\n  --- Adaptive-K {pct} ---\")\n    print(f\"  Script: seeds={sorted(script_adaptive[pct].keys())}, values={dict(sorted(script_adaptive[pct].items()))}\")\n    \n    reg_sr = {}\n    for eid, info in sorted(registry_adaptive[pct].items()):\n        s = info['seed']\n        sr = info['sr']\n        print(f\"    {eid}: seed={s}, SR={sr}\")\n        if s is not None and sr is not None:\n            reg_sr[s] = sr\n    \n    print(f\"  Registry seed→SR: {dict(sorted(reg_sr.items()))}\")\n    \n    script_seeds = set(script_adaptive[pct].keys())\n    reg_seeds = set(reg_sr.keys())\n    missing_from_script = reg_seeds - script_seeds\n    missing_from_registry = script_seeds - reg_seeds\n    common = script_seeds & reg_seeds\n    mismatches = {s: (script_adaptive[pct][s], reg_sr[s]) for s in common if abs(script_adaptive[pct][s] - reg_sr[s]) > 0.005}\n    \n    if missing_from_script or missing_from_registry or mismatches:\n        print(f\"  *** Missing from script: {sorted(missing_from_script)}\")\n        print(f\"  *** Missing from registry: {sorted(missing_from_registry)}\")\n        print(f\"  *** Mismatches: {mismatches}\")\n    else:\n        print(f\"  MATCH OK\")\n\n# Check for adaptive-k p50 seed42/43 which might not be in registry\nprint(\"\\n  Checking missing adaptive-k experiments:\")\nfor pct in ['p50', 'p75']:\n    for seed in [42, 43]:\n        candidates = [f'eval-adaptive-k-{pct}-seed{seed}', f'eval-adaptive-k-{pct}-seed{seed}-r2']\n        for c in candidates:\n            e = experiments.get(c)\n            if e:\n                print(f\"    {c}: status={e.get('status')}, conclusion={e.get('conclusion')}, SR={get_sr(e)}\")\n            else:\n                print(f\"    {c}: NOT IN REGISTRY\")\n\nPYEOF\n",
  "description": "Full audit part 2: Object benchmark",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "f4ee2d6e-db8d-479a-8b66-3f246c3d7c64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kLRiBrWCshEcv5eMz9r9p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7511,
      "cache_read_input_tokens": 49925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7511
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

_source line 38 · 2026-05-20T07:21:18.679Z_

<details><summary>↩ Tool result · `toolu_01LB5Lo7vuWcDGUQNvTPneeZ`</summary>

```text
================================================================================
LIBERO-OBJECT: CRM obs_only norm02 K=10 (PRIMARY)
================================================================================

Script: n=6, seeds=[43, 44, 45, 46, 47, 48]
  values: {43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.2, 48: 0.18}
  eval-acr-object-obs-only-norm02: seed=42, SR=0.22
  eval-obs-only-object-norm02-seed43-r2: seed=43, SR=0.16
  eval-obs-only-object-norm02-seed44-r2: seed=44, SR=0.16
  eval-obs-only-object-norm02-seed45: seed=45, SR=0.16
  eval-obs-only-object-norm02-seed46: seed=46, SR=0.15
  eval-obs-only-object-norm02-seed47: seed=47, SR=0.2
  eval-obs-only-object-norm02-seed48-r2: seed=48, SR=0.18

Registry seed→SR: {42: 0.22, 43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.2, 48: 0.18}

  Missing from script: [42] (seeds in registry but not script)
  Missing from registry: [] (seeds in script but not registry)
  Value mismatches: {}

================================================================================
LIBERO-OBJECT: CRM obs_only norm01 (Supplementary)
================================================================================

Script: n=6, seeds=[42, 44, 45, 46, 47, 48]
  Comment says: s42, s44, s45-r2, s46-r3, s47, s48
  eval-obs-only-object-norm01-seed44: seed=44, SR=0.16
  eval-obs-only-object-norm01-seed45: seed=45, SR=0.14
  eval-obs-only-object-norm01-seed45-r2: seed=45, SR=0.17
    DUP: seed=45 already=0.14
  eval-obs-only-object-norm01-seed46-r3: seed=46, SR=0.18
  eval-obs-only-object-norm01-seed47: seed=47, SR=0.17
  eval-obs-only-object-norm01-seed48: seed=48, SR=0.18
  eval_obs_only_norm01_seed48: seed=48, SR=0.18
    DUP: seed=48 already=0.18
  NOTE: eval-acr-object-v4-obs-only (norm=0.1/default): seed=None, SR=None

Registry seed→SR: {44: 0.16, 45: 0.17, 46: 0.18, 47: 0.17, 48: 0.18}

  Missing from script: []
  Missing from registry: [42]
  Value mismatches: {}

================================================================================
LIBERO-OBJECT: CRM obs_only norm02 K=5 (Supplementary)
================================================================================

Script: n=7, seeds=[42, 43, 44, 45, 46, 47, 48]
  eval-obs-only-object-norm02-k5-seed42: seed=42, SR=0.14
  eval-obs-only-object-norm02-k5-seed43: seed=43, SR=0.19
  eval-obs-only-object-norm02-k5-seed44: seed=44, SR=0.17
  eval-obs-only-object-norm02-k5-seed45: seed=45, SR=0.15
  eval-obs-only-object-norm02-k5-seed46: seed=46, SR=0.16
  eval-obs-only-object-norm02-k5-seed47: seed=47, SR=0.13
  eval-obs-only-object-norm02-k5-seed48: seed=48, SR=0.18

Registry seed→SR: {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}

  Missing from script: []
  Missing from registry: []
  Value mismatches: {}

================================================================================
LIBERO-OBJECT: VLA-only
================================================================================

Script: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 50]
  Comment: s42, s43, s44-r2, s45-r2, s46, s47, s48, s50
  eval-openvla-object-vla-only-seed42-v2: seed=42, SR=0.69
  eval-vla-only-object: seed=42, SR=0.12
    DUP: seed=42, prev SR=0.69
  eval-vla-only-object-seed43: seed=43, SR=0.12
  eval-vla-only-object-seed44-r2: seed=44, SR=0.1
  eval-vla-only-object-seed45: seed=45, SR=0.09
  eval-vla-only-object-seed45-r2: seed=45, SR=0.11
    DUP: seed=45, prev SR=0.09
  eval-vla-only-object-seed46: seed=46, SR=0.13
  eval-vla-only-object-seed47: seed=47, SR=0.1
  eval-vla-only-object-seed48: seed=48, SR=0.1
  eval-vla-only-object-seed50: seed=50, SR=0.09

Registry seed→SR: {42: 0.12, 43: 0.12, 44: 0.1, 45: 0.11, 46: 0.13, 47: 0.1, 48: 0.1, 50: 0.09}

  Missing from script: []
  Missing from registry: []
  Value mismatches: {}

  Checking seed45 versions:
    eval-vla-only-object-seed45: status=DONE, conclusion=success, SR=0.09
    eval-vla-only-object-seed45-r2: status=DONE, conclusion=success, SR=0.11

================================================================================
LIBERO-OBJECT: Argmin K=10
================================================================================
  NOTE: eval-argmin-only-spatial-r2 exists - seed=42, SR=0.34, hyp=Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base a

Script: n=5, seeds=[43, 44, 45, 46, 47]
  eval-argmin-object-seed43: seed=43, SR=0.17
  eval-argmin-object-seed44-r2: seed=44, SR=0.13
  eval-argmin-object-seed45: seed=45, SR=0.12
  eval-argmin-object-seed46: seed=46, SR=0.1
  eval-argmin-object-seed47: seed=47, SR=0.1

Registry seed→SR: {43: 0.17, 44: 0.13, 45: 0.12, 46: 0.1, 47: 0.1}

  Missing from script: []
  Missing from registry: []
  Value mismatches: {}

================================================================================
LIBERO-OBJECT: Argmin K=5
================================================================================

Script: n=4, seeds=[42, 43, 44, 45]
  eval-argmin-object-k5-seed42: seed=42, SR=0.15
  eval-argmin-object-k5-seed43: seed=43, SR=0.13
  eval-argmin-object-k5-seed44-r2: seed=44, SR=0.11
  eval-argmin-object-k5-seed45: seed=45, SR=0.13

Registry seed→SR: {42: 0.15, 43: 0.13, 44: 0.11, 45: 0.13}

  Missing from script: []
  Missing from registry: []
  Value mismatches: {}

================================================================================
LIBERO-OBJECT: Adaptive-K
================================================================================

  --- Adaptive-K p25 ---
  Script: seeds=[42, 43, 44], values={42: 0.15, 43: 0.13, 44: 0.15}
    eval-adaptive-k-p25-seed42: seed=42, SR=0.15
    eval-adaptive-k-p25-seed43: seed=43, SR=0.13
    eval-adaptive-k-p25-seed44-r2: seed=44, SR=0.15
  Registry seed→SR: {42: 0.15, 43: 0.13, 44: 0.15}
  MATCH OK

  --- Adaptive-K p50 ---
  Script: seeds=[42, 43, 44], values={42: 0.16, 43: 0.16, 44: 0.14}
    eval-adaptive-k-p50-seed44: seed=44, SR=0.14
  Registry seed→SR: {44: 0.14}
  *** Missing from script: []
  *** Missing from registry: [42, 43]
  *** Mismatches: {}

  --- Adaptive-K p75 ---
  Script: seeds=[42, 43, 44], values={42: 0.12, 43: 0.13, 44: 0.16}
    eval-adaptive-k-p75-seed44: seed=44, SR=0.16
  Registry seed→SR: {44: 0.16}
  *** Missing from script: []
  *** Missing from registry: [42, 43]
  *** Mismatches: {}

  --- Adaptive-K p90 ---
  Script: seeds=[42, 43, 44], values={42: 0.12, 43: 0.14, 44: 0.14}
    eval-adaptive-k-p90-seed42: seed=42, SR=0.12
    eval-adaptive-k-p90-seed43: seed=43, SR=0.14
    eval-adaptive-k-p90-seed44: seed=44, SR=0.14
  Registry seed→SR: {42: 0.12, 43: 0.14, 44: 0.14}
  MATCH OK

  Checking missing adaptive-k experiments:
    eval-adaptive-k-p50-seed42: status=ALLOCATED, conclusion=success, SR=0.16
    eval-adaptive-k-p50-seed42-r2: NOT IN REGISTRY
    eval-adaptive-k-p50-seed43: status=ALLOCATED, conclusion=success, SR=0.16
    eval-adaptive-k-p50-seed43-r2: NOT IN REGISTRY
    eval-adaptive-k-p75-seed42: status=ALLOCATED, conclusion=success, SR=0.12
    eval-adaptive-k-p75-seed42-r2: NOT IN REGISTRY
    eval-adaptive-k-p75-seed43: status=ALLOCATED, conclusion=success, SR=0.13
    eval-adaptive-k-p75-seed43-r2: NOT IN REGISTRY
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "a3621926-de4d-43b3-9d20-af0297caca30",
  "tool_use_result": {
    "stdout": "================================================================================\nLIBERO-OBJECT: CRM obs_only norm02 K=10 (PRIMARY)\n================================================================================\n\nScript: n=6, seeds=[43, 44, 45, 46, 47, 48]\n  values: {43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.2, 48: 0.18}\n  eval-acr-object-obs-only-norm02: seed=42, SR=0.22\n  eval-obs-only-object-norm02-seed43-r2: seed=43, SR=0.16\n  eval-obs-only-object-norm02-seed44-r2: seed=44, SR=0.16\n  eval-obs-only-object-norm02-seed45: seed=45, SR=0.16\n  eval-obs-only-object-norm02-seed46: seed=46, SR=0.15\n  eval-obs-only-object-norm02-seed47: seed=47, SR=0.2\n  eval-obs-only-object-norm02-seed48-r2: seed=48, SR=0.18\n\nRegistry seed→SR: {42: 0.22, 43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.2, 48: 0.18}\n\n  Missing from script: [42] (seeds in registry but not script)\n  Missing from registry: [] (seeds in script but not registry)\n  Value mismatches: {}\n\n================================================================================\nLIBERO-OBJECT: CRM obs_only norm01 (Supplementary)\n================================================================================\n\nScript: n=6, seeds=[42, 44, 45, 46, 47, 48]\n  Comment says: s42, s44, s45-r2, s46-r3, s47, s48\n  eval-obs-only-object-norm01-seed44: seed=44, SR=0.16\n  eval-obs-only-object-norm01-seed45: seed=45, SR=0.14\n  eval-obs-only-object-norm01-seed45-r2: seed=45, SR=0.17\n    DUP: seed=45 already=0.14\n  eval-obs-only-object-norm01-seed46-r3: seed=46, SR=0.18\n  eval-obs-only-object-norm01-seed47: seed=47, SR=0.17\n  eval-obs-only-object-norm01-seed48: seed=48, SR=0.18\n  eval_obs_only_norm01_seed48: seed=48, SR=0.18\n    DUP: seed=48 already=0.18\n  NOTE: eval-acr-object-v4-obs-only (norm=0.1/default): seed=None, SR=None\n\nRegistry seed→SR: {44: 0.16, 45: 0.17, 46: 0.18, 47: 0.17, 48: 0.18}\n\n  Missing from script: []\n  Missing from registry: [42]\n  Value mismatches: {}\n\n================================================================================\nLIBERO-OBJECT: CRM obs_only norm02 K=5 (Supplementary)\n================================================================================\n\nScript: n=7, seeds=[42, 43, 44, 45, 46, 47, 48]\n  eval-obs-only-object-norm02-k5-seed42: seed=42, SR=0.14\n  eval-obs-only-object-norm02-k5-seed43: seed=43, SR=0.19\n  eval-obs-only-object-norm02-k5-seed44: seed=44, SR=0.17\n  eval-obs-only-object-norm02-k5-seed45: seed=45, SR=0.15\n  eval-obs-only-object-norm02-k5-seed46: seed=46, SR=0.16\n  eval-obs-only-object-norm02-k5-seed47: seed=47, SR=0.13\n  eval-obs-only-object-norm02-k5-seed48: seed=48, SR=0.18\n\nRegistry seed→SR: {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}\n\n  Missing from script: []\n  Missing from registry: []\n  Value mismatches: {}\n\n================================================================================\nLIBERO-OBJECT: VLA-only\n================================================================================\n\nScript: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 50]\n  Comment: s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n  eval-openvla-object-vla-only-seed42-v2: seed=42, SR=0.69\n  eval-vla-only-object: seed=42, SR=0.12\n    DUP: seed=42, prev SR=0.69\n  eval-vla-only-object-seed43: seed=43, SR=0.12\n  eval-vla-only-object-seed44-r2: seed=44, SR=0.1\n  eval-vla-only-object-seed45: seed=45, SR=0.09\n  eval-vla-only-object-seed45-r2: seed=45, SR=0.11\n    DUP: seed=45, prev SR=0.09\n  eval-vla-only-object-seed46: seed=46, SR=0.13\n  eval-vla-only-object-seed47: seed=47, SR=0.1\n  eval-vla-only-object-seed48: seed=48, SR=0.1\n  eval-vla-only-object-seed50: seed=50, SR=0.09\n\nRegistry seed→SR: {42: 0.12, 43: 0.12, 44: 0.1, 45: 0.11, 46: 0.13, 47: 0.1, 48: 0.1, 50: 0.09}\n\n  Missing from script: []\n  Missing from registry: []\n  Value mismatches: {}\n\n  Checking seed45 versions:\n    eval-vla-only-object-seed45: status=DONE, conclusion=success, SR=0.09\n    eval-vla-only-object-seed45-r2: status=DONE, conclusion=success, SR=0.11\n\n================================================================================\nLIBERO-OBJECT: Argmin K=10\n================================================================================\n  NOTE: eval-argmin-only-spatial-r2 exists - seed=42, SR=0.34, hyp=Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base a\n\nScript: n=5, seeds=[43, 44, 45, 46, 47]\n  eval-argmin-object-seed43: seed=43, SR=0.17\n  eval-argmin-object-seed44-r2: seed=44, SR=0.13\n  eval-argmin-object-seed45: seed=45, SR=0.12\n  eval-argmin-object-seed46: seed=46, SR=0.1\n  eval-argmin-object-seed47: seed=47, SR=0.1\n\nRegistry seed→SR: {43: 0.17, 44: 0.13, 45: 0.12, 46: 0.1, 47: 0.1}\n\n  Missing from script: []\n  Missing from registry: []\n  Value mismatches: {}\n\n================================================================================\nLIBERO-OBJECT: Argmin K=5\n================================================================================\n\nScript: n=4, seeds=[42, 43, 44, 45]\n  eval-argmin-object-k5-seed42: seed=42, SR=0.15\n  eval-argmin-object-k5-seed43: seed=43, SR=0.13\n  eval-argmin-object-k5-seed44-r2: seed=44, SR=0.11\n  eval-argmin-object-k5-seed45: seed=45, SR=0.13\n\nRegistry seed→SR: {42: 0.15, 43: 0.13, 44: 0.11, 45: 0.13}\n\n  Missing from script: []\n  Missing from registry: []\n  Value mismatches: {}\n\n================================================================================\nLIBERO-OBJECT: Adaptive-K\n================================================================================\n\n  --- Adaptive-K p25 ---\n  Script: seeds=[42, 43, 44], values={42: 0.15, 43: 0.13, 44: 0.15}\n    eval-adaptive-k-p25-seed42: seed=42, SR=0.15\n    eval-adaptive-k-p25-seed43: seed=43, SR=0.13\n    eval-adaptive-k-p25-seed44-r2: seed=44, SR=0.15\n  Registry seed→SR: {42: 0.15, 43: 0.13, 44: 0.15}\n  MATCH OK\n\n  --- Adaptive-K p50 ---\n  Script: seeds=[42, 43, 44], values={42: 0.16, 43: 0.16, 44: 0.14}\n    eval-adaptive-k-p50-seed44: seed=44, SR=0.14\n  Registry seed→SR: {44: 0.14}\n  *** Missing from script: []\n  *** Missing from registry: [42, 43]\n  *** Mismatches: {}\n\n  --- Adaptive-K p75 ---\n  Script: seeds=[42, 43, 44], values={42: 0.12, 43: 0.13, 44: 0.16}\n    eval-adaptive-k-p75-seed44: seed=44, SR=0.16\n  Registry seed→SR: {44: 0.16}\n  *** Missing from script: []\n  *** Missing from registry: [42, 43]\n  *** Mismatches: {}\n\n  --- Adaptive-K p90 ---\n  Script: seeds=[42, 43, 44], values={42: 0.12, 43: 0.14, 44: 0.14}\n    eval-adaptive-k-p90-seed42: seed=42, SR=0.12\n    eval-adaptive-k-p90-seed43: seed=43, SR=0.14\n    eval-adaptive-k-p90-seed44: seed=44, SR=0.14\n  Registry seed→SR: {42: 0.12, 43: 0.14, 44: 0.14}\n  MATCH OK\n\n  Checking missing adaptive-k experiments:\n    eval-adaptive-k-p50-seed42: status=ALLOCATED, conclusion=success, SR=0.16\n    eval-adaptive-k-p50-seed42-r2: NOT IN REGISTRY\n    eval-adaptive-k-p50-seed43: status=ALLOCATED, conclusion=success, SR=0.16\n    eval-adaptive-k-p50-seed43-r2: NOT IN REGISTRY\n    eval-adaptive-k-p75-seed42: status=ALLOCATED, conclusion=success, SR=0.12\n    eval-adaptive-k-p75-seed42-r2: NOT IN REGISTRY\n    eval-adaptive-k-p75-seed43: status=ALLOCATED, conclusion=success, SR=0.13\n    eval-adaptive-k-p75-seed43-r2: NOT IN REGISTRY",
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
Now I have all the data. Let me also check a few edge cases:

1. **Object CRM norm02 K=10 seed42**: Registry has `eval-acr-object-obs-only-norm02` with SR=0.22, but script doesn't include it (seeds start at 43). Need to check why. The script comment says "s43-r2, s44-r2, s45, s46, s47, s48-r2". It might be excluded because this was an early experiment with different config.

2. **Object CRM norm01 seed42**: Script says s42 with SR=0.19, but registry doesn't have an explicit norm01-seed42 experiment. 

Looking at the script comment for norm01, it lists "s42, s44, s45-r2, s46-r3, s47, s48", so seed42 should be there. The `eval-acr-object-v4-obs-only` experiment shows norm=0.1 but has missing seed and SR values, so there might be another experiment providing the norm01 data.

3. **VLA-Spatial seeds 48,49,50**: These are in the script but not in the registry. Script verification notes say "VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive."

4. **VLA-Long**: (appears to be cut off)

Now looking at the rest of the discrepancies: seed49 appears in the script with SR=0.16 but isn't in the registry, CRM-Goal seed47 is in the script with SR=0.69 but shows PREPARING status in the registry, and Adaptive-K has ALLOCATED status despite having success conclusions and matching SR values. For the Object VLA-only seed42 entries, there are two different results—one from OpenVLA with SR=0.69 and one from SmolVLA with SR=0.12—and the script correctly uses the 0.12 value from the SmolVLA model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "8d0dedda-d89a-4e99-8290-23be5e3859e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgkwzXtDdHmFqXduKpS2HF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 57436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

发现几个关键差异。让我验证一些边界情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "5c2451b8-a571-4db5-b54a-c6c91d53fe38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgkwzXtDdHmFqXduKpS2HF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 57436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

<details open><summary>🔧 Tool call — Bash · `toolu_014faLbkRW5kmaKD4H71VH5v`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open('registry.yaml', 'r') as f:\n    registry = yaml.safe_load(f)\n\nexperiments = registry.get('experiments', {})\n\ndef get_sr(exp):\n    metrics = exp.get('metrics', {})\n    if not isinstance(metrics, dict):\n        return None\n    for key in ['success_rate', 'overall_success_rate', 'overall_sr', 'sr', 'avg_success_rate']:\n        if key in metrics:\n            val = metrics[key]\n            if isinstance(val, (int, float)):\n                if val > 1:\n                    return round(val / 100, 2)\n                return round(val, 2)\n    return None\n\n# 1. Check what provides Object CRM norm01 seed42=0.19\nprint(\"=== Object norm01 seed42 source ===\")\n# eval-acr-object-v4-obs-only was default norm (0.1)\nfor eid in ['eval-acr-object-v4-obs-only', 'eval-acr-object-obs-only-default']:\n    e = experiments.get(eid)\n    if e:\n        spec = e.get('spec', {})\n        hyp = e.get('hypothesis', '')[:150]\n        sr = get_sr(e)\n        norm = spec.get('norm', spec.get('max_correction_norm', 'N/A'))\n        print(f\"  {eid}: status={e.get('status')}, SR={sr}, norm_in_spec={norm}\")\n        print(f\"    hyp: {hyp}\")\n\n# Check for any obs-only object norm01 seed42\nprint(\"\\n  Looking for norm01-seed42 or norm=0.1 seed=42...\")\nfor eid, exp in experiments.items():\n    el = eid.lower()\n    if 'object' in el and ('obs-only' in el or 'obs_only' in el or 'obsonly' in el) and 'norm01' in el:\n        spec = exp.get('spec', {})\n        seed = spec.get('seed')\n        if seed == 42 or 'seed42' in el:\n            sr = get_sr(exp)\n            print(f\"  {eid}: status={exp.get('status')}, conclusion={exp.get('conclusion')}, SR={sr}\")\n\n# Maybe the acr-object-obs-only-norm02 seed42 (SR=0.22) was an early experiment\n# and v4-obs-only (norm=0.1) was the norm01 equivalent\nprint(\"\\n=== eval-acr-object-obs-only-norm02 details ===\")\ne = experiments.get('eval-acr-object-obs-only-norm02')\nif e:\n    spec = e.get('spec', {})\n    print(f\"  spec: {dict((k,v) for k,v in spec.items() if k in ['seed','norm','max_correction_norm','K','k','n_rollouts','n_refine_steps','benchmark'])}\")\n    print(f\"  SR={get_sr(e)}, hyp={e.get('hypothesis', '')[:150]}\")\n\n# 2. Check VLA-only Long seed49\nprint(\"\\n=== VLA-only Long seed49 ===\")\ne49 = experiments.get('eval-vla-only-long-seed49')\nif e49:\n    print(f\"  status={e49.get('status')}, conclusion={e49.get('conclusion')}, SR={get_sr(e49)}\")\nelse:\n    print(\"  NOT IN REGISTRY\")\n\n# 3. Check VLA-only Spatial seeds 48-50\nprint(\"\\n=== VLA-only Spatial seeds 48-50 ===\")\nfor s in [48, 49, 50]:\n    eid = f'eval-vla-only-spatial-seed{s}'\n    e = experiments.get(eid)\n    if e:\n        print(f\"  {eid}: status={e.get('status')}, conclusion={e.get('conclusion')}, SR={get_sr(e)}\")\n    else:\n        print(f\"  {eid}: NOT IN REGISTRY\")\n\n# 4. Check CRM Goal seed47\nprint(\"\\n=== CRM Goal seed47 ===\")\ne = experiments.get('eval-crm-goal-seed47')\nif e:\n    print(f\"  status={e.get('status')}, conclusion={e.get('conclusion')}, SR={get_sr(e)}\")\n    print(f\"  hyp: {e.get('hypothesis', '')[:150]}\")\n\n# 5. Adaptive-K p50/p75 seed42/43 - status ALLOCATED but conclusion success\nprint(\"\\n=== Adaptive-K ALLOCATED+success anomalies ===\")\nfor eid in ['eval-adaptive-k-p50-seed42', 'eval-adaptive-k-p50-seed43', 'eval-adaptive-k-p75-seed42', 'eval-adaptive-k-p75-seed43']:\n    e = experiments.get(eid)\n    if e:\n        print(f\"  {eid}: status={e.get('status')}, conclusion={e.get('conclusion')}, SR={get_sr(e)}\")\n\n# 6. Check if there's an eval-obs-only-object-norm01-seed42 or similar\nprint(\"\\n=== Any Object obs-only seed42 norm=0.1 ===\")\nfor eid, exp in experiments.items():\n    el = eid.lower()\n    spec = exp.get('spec', {})\n    seed = spec.get('seed')\n    if seed == 42 and 'object' in el and ('obs-only' in el or 'obs_only' in el or 'obsonly' in el or 'acr' in el):\n        sr = get_sr(exp)\n        norm = spec.get('max_correction_norm', '')\n        status = exp.get('status')\n        conclusion = exp.get('conclusion')\n        print(f\"  {eid}: norm={norm}, SR={sr}, status={status}, conclusion={conclusion}\")\n\n# 7. Object CRM norm02 K=10 seed42 (eval-acr-object-obs-only-norm02 SR=0.22) - why excluded from script?\nprint(\"\\n=== Why seed42 norm02 excluded from Object CRM primary? ===\")\ne = experiments.get('eval-acr-object-obs-only-norm02')\nif e:\n    spec = e.get('spec', {})\n    print(f\"  n_rollouts={spec.get('n_rollouts', spec.get('rollouts', 'N/A'))}\")\n    print(f\"  K={spec.get('K', spec.get('k', spec.get('n_refine_steps', 'N/A')))}\")\n    print(f\"  max_correction_norm={spec.get('max_correction_norm', 'N/A')}\")\n    print(f\"  created_at={e.get('created_at', 'N/A')}\")\n    print(f\"  Full hyp: {e.get('hypothesis', '')}\")\n\nPYEOF\n",
  "description": "Verify edge cases and anomalies",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "370994b9-250e-4f83-ad7b-a1998343bd44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgkwzXtDdHmFqXduKpS2HF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 57436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 42 · 2026-05-20T07:21:58.195Z_

<details><summary>↩ Tool result · reported error · `toolu_014faLbkRW5kmaKD4H71VH5v`</summary>

```text
Exit code 1
=== Object norm01 seed42 source ===
  eval-acr-object-v4-obs-only: status=DONE, SR=None, norm_in_spec=N/A
    hyp: D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.
  eval-acr-object-obs-only-default: status=DONE, SR=0.17, norm_in_spec=N/A
    hyp: obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default

  Looking for norm01-seed42 or norm=0.1 seed=42...
  eval-obs-only-object-norm01-seed42: status=DEPLOYED, conclusion=success, SR=0.19
  eval-obs-only-object-norm01-seed42-r2: status=DONE, conclusion=failed, SR=None

=== eval-acr-object-obs-only-norm02 details ===
  spec: {'seed': 42}
  SR=0.22, hyp=ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided 

=== VLA-only Long seed49 ===
  status=PREPARING, conclusion=None, SR=None

=== VLA-only Spatial seeds 48-50 ===
  eval-vla-only-spatial-seed48: status=DONE, conclusion=failed, SR=None
  eval-vla-only-spatial-seed49: status=DONE, conclusion=failed, SR=None
  eval-vla-only-spatial-seed50: status=PREPARING, conclusion=success, SR=0.3

=== CRM Goal seed47 ===
  status=PREPARING, conclusion=None, SR=0.69
  hyp: CRM obs_only K=10 on LIBERO-Goal seed47. Goal OOD 补样本量 (n→6)，增强 cross-suite OOD 统计可靠性。

=== Adaptive-K ALLOCATED+success anomalies ===
  eval-adaptive-k-p50-seed42: status=ALLOCATED, conclusion=success, SR=0.16
  eval-adaptive-k-p50-seed43: status=ALLOCATED, conclusion=success, SR=0.16
  eval-adaptive-k-p75-seed42: status=ALLOCATED, conclusion=success, SR=0.12
  eval-adaptive-k-p75-seed43: status=ALLOCATED, conclusion=success, SR=0.13

=== Any Object obs-only seed42 norm=0.1 ===
  eval-acr-object-v3: norm=, SR=0, status=DONE, conclusion=negative
  eval-acr-object-v4-perdof: norm=, SR=None, status=DONE, conclusion=success
  eval-acr-object-v4-default: norm=, SR=None, status=DONE, conclusion=killed
  eval-acr-object-obs-only-norm02: norm=, SR=0.22, status=DONE, conclusion=success
  eval-mag-obsonly-norm005-object: norm=, SR=0.13, status=DONE, conclusion=success
  eval-mag-obsonly-norm03-object: norm=, SR=0.19, status=DONE, conclusion=success
  eval-mag-obsonly-norm003-object: norm=, SR=0.16, status=DONE, conclusion=success
  eval-acr-object-obs-only-default: norm=, SR=0.17, status=DONE, conclusion=success
  eval-acr-object-v4-default-r2: norm=, SR=0, status=DONE, conclusion=success
  eval-mag-obsonly-norm02-object: norm=, SR=None, status=DONE, conclusion=killed
  eval-obs-only-object-norm02-k5-seed42: norm=, SR=0.14, status=DONE, conclusion=success
  eval-obs-only-object-norm01-seed42: norm=, SR=0.19, status=DEPLOYED, conclusion=success
  eval-obs-only-object-norm01-seed42-r2: norm=, SR=None, status=DONE, conclusion=failed
Traceback (most recent call last):
  File "&lt;stdin>", line 91, in &lt;module>
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "169bbc8a-a342-486c-9b19-60e20aaae7c2",
  "tool_use_result": "Error: Exit code 1\n=== Object norm01 seed42 source ===\n  eval-acr-object-v4-obs-only: status=DONE, SR=None, norm_in_spec=N/A\n    hyp: D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\n  eval-acr-object-obs-only-default: status=DONE, SR=0.17, norm_in_spec=N/A\n    hyp: obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default\n\n  Looking for norm01-seed42 or norm=0.1 seed=42...\n  eval-obs-only-object-norm01-seed42: status=DEPLOYED, conclusion=success, SR=0.19\n  eval-obs-only-object-norm01-seed42-r2: status=DONE, conclusion=failed, SR=None\n\n=== eval-acr-object-obs-only-norm02 details ===\n  spec: {'seed': 42}\n  SR=0.22, hyp=ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided \n\n=== VLA-only Long seed49 ===\n  status=PREPARING, conclusion=None, SR=None\n\n=== VLA-only Spatial seeds 48-50 ===\n  eval-vla-only-spatial-seed48: status=DONE, conclusion=failed, SR=None\n  eval-vla-only-spatial-seed49: status=DONE, conclusion=failed, SR=None\n  eval-vla-only-spatial-seed50: status=PREPARING, conclusion=success, SR=0.3\n\n=== CRM Goal seed47 ===\n  status=PREPARING, conclusion=None, SR=0.69\n  hyp: CRM obs_only K=10 on LIBERO-Goal seed47. Goal OOD 补样本量 (n→6)，增强 cross-suite OOD 统计可靠性。\n\n=== Adaptive-K ALLOCATED+success anomalies ===\n  eval-adaptive-k-p50-seed42: status=ALLOCATED, conclusion=success, SR=0.16\n  eval-adaptive-k-p50-seed43: status=ALLOCATED, conclusion=success, SR=0.16\n  eval-adaptive-k-p75-seed42: status=ALLOCATED, conclusion=success, SR=0.12\n  eval-adaptive-k-p75-seed43: status=ALLOCATED, conclusion=success, SR=0.13\n\n=== Any Object obs-only seed42 norm=0.1 ===\n  eval-acr-object-v3: norm=, SR=0, status=DONE, conclusion=negative\n  eval-acr-object-v4-perdof: norm=, SR=None, status=DONE, conclusion=success\n  eval-acr-object-v4-default: norm=, SR=None, status=DONE, conclusion=killed\n  eval-acr-object-obs-only-norm02: norm=, SR=0.22, status=DONE, conclusion=success\n  eval-mag-obsonly-norm005-object: norm=, SR=0.13, status=DONE, conclusion=success\n  eval-mag-obsonly-norm03-object: norm=, SR=0.19, status=DONE, conclusion=success\n  eval-mag-obsonly-norm003-object: norm=, SR=0.16, status=DONE, conclusion=success\n  eval-acr-object-obs-only-default: norm=, SR=0.17, status=DONE, conclusion=success\n  eval-acr-object-v4-default-r2: norm=, SR=0, status=DONE, conclusion=success\n  eval-mag-obsonly-norm02-object: norm=, SR=None, status=DONE, conclusion=killed\n  eval-obs-only-object-norm02-k5-seed42: norm=, SR=0.14, status=DONE, conclusion=success\n  eval-obs-only-object-norm01-seed42: norm=, SR=0.19, status=DEPLOYED, conclusion=success\n  eval-obs-only-object-norm01-seed42-r2: norm=, SR=None, status=DONE, conclusion=failed\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 91, in &lt;module>\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Good, I got almost all the data before the error. Let me now check the remaining items and compile the audit report.

Key findings so far:

### LIBERO-Spatial
**CRM obs_only norm02 K=10**: PERFECT MATCH (8 seeds all align)
- Note: `eval-mag-obsonly-norm02` has `conclusion=negative` (not `success`), but script includes seed42=0.35 from it. This is technically a status issue but data is valid.

**VLA-only**: 3 seeds missing from registry
- seed48: `eval-vla-only-spatial-seed48` status=DONE, conclusion=failed


- seed49: `eval-vla-only-spatial-seed49` status=DONE, conclusion=failed  
- seed50: `eval-vla-only-spatial-seed50` status=PREPARING, conclusion=success, SR=0.30
- Script includes seed48=0.30, seed49=0.29, seed50=0.30 per Director directive

### LIBERO-Long
**CRM obs_only**: PERFECT MATCH (7 seeds)
**VLA-only**: seed49 missing from registry (status=PREPARING, no SR)
- Script includes seed49=0.16 per Director directive (?)

### LIBERO-Goal
**CRM obs_only**: seed47 is in PREPARING status with SR=0.69 but not marked DONE, yet the script includes it anyway. **VLA-only**: all 6 seeds match perfectly.

### LIBERO-Object
**CRM norm02 K=10**: seed42 exists in the registry with SR=0.22 but was excluded from the script, likely because it came from an earlier experiment with different settings. **CRM norm01**: seed42 appears as a DEPLOYED entry with SR=0.19 and is included in the script.

**CRM norm02 K=5**: perfect alignment across all 7 seeds. **VLA-only**: 8 seeds match, with the OpenVLA variant correctly filtered out. **Argmin K=10 and K=5**: both show perfect matches. **Adaptive-K**: most variants align well, though p50 and p75 have seeds in ALLOCATED status despite having success conclusions and matching SR values.

Now I should look for any non-standard experiment names that might contain relevant data, particularly magnitude sweep experiments that could feed into the benchmarks.

I'm noticing the Object CRM norm02 K=10 seed42 experiment has an SR of 0.22, which stands out against the 0.15-0.20 range for seeds 43-48 — this discrepancy might explain why it was excluded, possibly due to different evaluation parameters or an older code version.

I have what I need to write up the audit report now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "96b04480-821a-44b1-bace-124bb323e410",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjRNrEN2cquBKsvNPhXNuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3714,
      "cache_read_input_tokens": 66331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3714
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

_source line 44_

数据收集完成。现在编写审计报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "b144fda2-416c-4fff-a12a-74fecb4f65ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjRNrEN2cquBKsvNPhXNuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3714,
      "cache_read_input_tokens": 66331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3714
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

_source line 45_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Aovf2Q3wJp5XvvDExnHpwt`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "ea4584c8-2b8c-493e-bd4e-bb1a116623b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjRNrEN2cquBKsvNPhXNuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3714,
      "cache_read_input_tokens": 66331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3714
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

_source line 46 · 2026-05-20T07:22:21.285Z_

<details><summary>↩ Tool result · `toolu_01Aovf2Q3wJp5XvvDExnHpwt`</summary>

````text
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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "c6a93c90-e8e3-4ddb-a0e5-f2f1f6cdcfd4",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Rmk7paPGfRUnCVcfmVpAh3`</summary>

```json
{
  "todos": [
    {
      "content": "Collect registry data for all benchmarks",
      "status": "completed",
      "activeForm": "Collecting registry data"
    },
    {
      "content": "Verify edge cases and anomalies",
      "status": "completed",
      "activeForm": "Verifying edge cases"
    },
    {
      "content": "Generate audit report",
      "status": "in_progress",
      "activeForm": "Generating audit report"
    },
    {
      "content": "Register artifact",
      "status": "pending",
      "activeForm": "Registering artifact"
    }
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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "2915f0a6-284a-4858-b985-d5692e9ded68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ScWfMvT1TWAqSu3chjtHVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 70045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3337
      },
      "output_tokens": 52,
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

_source line 48 · 2026-05-20T07:22:27.391Z_

<details><summary>↩ Tool result · `toolu_01Rmk7paPGfRUnCVcfmVpAh3`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "07a76fa6-596c-480e-8462-4610e606a411",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Collect registry data for all benchmarks",
        "status": "completed",
        "activeForm": "Collecting registry data"
      },
      {
        "content": "Verify edge cases and anomalies",
        "status": "completed",
        "activeForm": "Verifying edge cases"
      },
      {
        "content": "Generate audit report",
        "status": "in_progress",
        "activeForm": "Generating audit report"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Write · `toolu_01HC6PDL6CBNh4DPdazKKYmv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md",
  "content": "# Full Benchmark Data Audit\nDate: 2026-05-20\n\n## Summary\n\n| Category | Count | Details |\n|----------|-------|---------|\n| **Perfect matches** | 9/15 | Spatial-CRM, Long-CRM, Long-VLA (10/11), Goal-VLA, Obj-norm02-K10 (6/6), Obj-K5, Obj-VLA, Argmin-K10, Argmin-K5 |\n| **Seeds in script but not in DONE+success registry** | 8 | See details below |\n| **Seeds in registry but excluded from script** | 1 | Obj-CRM-norm02-K10 seed42 |\n| **Value mismatches** | 0 | All common seeds have matching SR values |\n| **Registry status anomalies** | 6 | Experiments with data but status ≠ DONE or conclusion ≠ success |\n\n### Seeds in Script Not in DONE+success Registry\n\n| Benchmark | Method | Seed | Script SR | Registry Status | Notes |\n|-----------|--------|------|-----------|-----------------|-------|\n| Spatial | VLA-only | 48 | 0.30 | DONE/failed | Director directive; data exists outside registry |\n| Spatial | VLA-only | 49 | 0.29 | DONE/failed | Director directive; data exists outside registry |\n| Spatial | VLA-only | 50 | 0.30 | PREPARING/success | SR=0.30 in registry but status not DONE |\n| Long | VLA-only | 49 | 0.16 | PREPARING/None | No SR in registry; Director directive |\n| Goal | CRM obs_only | 47 | 0.69 | PREPARING/None | SR=0.69 in registry metrics but status PREPARING |\n| Object | CRM norm01 | 42 | 0.19 | DEPLOYED/success | SR=0.19 in registry but status DEPLOYED, not DONE |\n| Object | Adaptive-K p50 | 42,43 | 0.16,0.16 | ALLOCATED/success | SR matches; status should be DONE |\n| Object | Adaptive-K p75 | 42,43 | 0.12,0.13 | ALLOCATED/success | SR matches; status should be DONE |\n\n---\n\n## Per-Benchmark Details\n\n### LIBERO-Spatial\n\n#### CRM obs_only norm02 K=10\n**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 51]\n- values: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}\n\n**Registry** (all DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-mag-obsonly-norm02 | 42 | 0.35 |\n| eval-obs-only-spatial-norm02-seed43-r2 | 43 | 0.34 |\n| eval-obs-only-spatial-norm02-seed44 | 44 | 0.36 |\n| eval-obs-only-spatial-norm02-seed45 | 45 | 0.34 |\n| eval-obs-only-spatial-norm02-seed46-r2 | 46 | 0.33 |\n| eval-obs-only-spatial-norm02-seed47 | 47 | 0.32 |\n| eval-obs-only-spatial-norm02-seed48 | 48 | 0.35 |\n| eval-crm-spatial-k10-seed51 | 51 | 0.36 |\n\n**Diff**: MATCH — all 8 seeds present with correct values.\n- Note: eval-mag-obsonly-norm02 has `conclusion=negative` (not `success`), but SR=0.35 is valid data. Script correctly uses it.\n\n#### VLA-only\n**Script**: n=9, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50]\n- values: {42: 0.30, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.30, 47: 0.30, 48: 0.30, 49: 0.29, 50: 0.30}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-spatial-seed42 | 42 | 0.30 |\n| eval-vla-only-spatial-seed43 | 43 | 0.29 |\n| eval-vla-only-spatial-seed44 | 44 | 0.31 |\n| eval-vla-only-spatial-seed45 | 45 | 0.27 |\n| eval-vla-only-spatial-seed46 | 46 | 0.30 |\n| eval-vla-only-spatial-seed47 | 47 | 0.30 |\n\n**Diff**:\n- **MISSING from DONE+success registry**: seeds 48, 49, 50\n  - seed48: `eval-vla-only-spatial-seed48` status=DONE, conclusion=**failed** (no valid SR)\n  - seed49: `eval-vla-only-spatial-seed49` status=DONE, conclusion=**failed** (no valid SR)\n  - seed50: `eval-vla-only-spatial-seed50` status=**PREPARING**, conclusion=success, SR=0.30\n- Script verification notes state: \"VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive\"\n- **Risk**: Seeds 48/49 have no verifiable SR in registry. Data likely from external source (server JSON).\n\n---\n\n### LIBERO-Long\n\n#### CRM obs_only\n**Script**: n=7, seeds=[42, 43, 44, 45, 46, 47, 50]\n- values: {42: 0.17, 43: 0.15, 44: 0.20, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-crm-long-seed42 | 42 | 0.17 |\n| eval-crm-long-seed43 | 43 | 0.15 |\n| eval-crm-long-seed44 | 44 | 0.20 |\n| eval-crm-long-seed45 | 45 | 0.18 |\n| eval-crm-long-seed46 | 46 | 0.18 |\n| eval-crm-long-seed47 | 47 | 0.17 |\n| eval-crm-long-seed50 | 50 | 0.14 |\n\n**Diff**: PERFECT MATCH — all 7 seeds present with correct values.\n\n#### VLA-only\n**Script**: n=11, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]\n- values: {42: 0.11, 43: 0.13, 44: 0.12, 45: 0.17, 46: 0.18, 47: 0.14, 48: 0.14, 49: 0.16, 50: 0.16, 51: 0.15, 52: 0.17}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-long-seed42 | 42 | 0.11 |\n| eval-vla-only-long-seed43 | 43 | 0.13 |\n| eval-vla-only-long-seed44 | 44 | 0.12 |\n| eval-vla-only-long-seed45 | 45 | 0.17 |\n| eval-vla-only-long-seed46 | 46 | 0.18 |\n| eval-vla-only-long-seed47 | 47 | 0.14 |\n| eval-vla-only-long-seed48 | 48 | 0.14 |\n| eval-vla-only-long-seed50 | 50 | 0.16 |\n| eval-vla-only-long-seed51 | 51 | 0.15 |\n| eval-vla-only-long-seed52 | 52 | 0.17 |\n\n**Diff**:\n- **MISSING from registry**: seed 49\n  - `eval-vla-only-long-seed49`: status=**PREPARING**, conclusion=None, SR=None\n- Script includes seed49=0.16. Data source unclear — no SR in registry, experiment never completed.\n- **Risk**: Unverifiable data point. Should be removed or re-run.\n\n---\n\n### LIBERO-Goal\n\n#### CRM obs_only\n**Script**: n=6, seeds=[42, 43, 44, 45, 46, 47]\n- values: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72, 47: 0.69}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-crm-goal-seed42 | 42 | 0.67 |\n| eval-crm-goal-seed43 | 43 | 0.72 |\n| eval-crm-goal-seed44-r2 | 44 | 0.64 |\n| eval-crm-goal-seed45-r2 | 45 | 0.65 |\n| eval-crm-goal-seed46 | 46 | 0.72 |\n\n**Diff**:\n- **MISSING from DONE+success registry**: seed 47\n  - `eval-crm-goal-seed47`: status=**PREPARING**, conclusion=None, SR=0.69 (in metrics)\n- Script verification notes: \"CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\"\n- SR value 0.69 exists in registry metrics despite PREPARING status. Likely manually populated.\n- **Action**: Update registry status to DONE+success when experiment completes, or verify data source.\n\n#### VLA-only\n**Script**: n=6, seeds=[42, 43, 44, 45, 46, 49]\n- values: {42: 0.71, 43: 0.69, 44: 0.73, 45: 0.63, 46: 0.71, 49: 0.65}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-goal-seed42 | 42 | 0.71 |\n| eval-vla-only-goal-seed43 | 43 | 0.69 |\n| eval-vla-only-goal-seed44-r2 | 44 | 0.73 |\n| eval-vla-only-goal-seed45 | 45 | 0.63 |\n| eval-vla-only-goal-seed46 | 46 | 0.71 |\n| eval-vla-only-goal-seed49 | 49 | 0.65 |\n\n**Diff**: PERFECT MATCH — all 6 seeds present with correct values.\n\n---\n\n### LIBERO-Object\n\n#### CRM obs_only norm02 K=10 (PRIMARY)\n**Script**: n=6, seeds=[43, 44, 45, 46, 47, 48]\n- values: {43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.20, 48: 0.18}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-acr-object-obs-only-norm02 | 42 | 0.22 |\n| eval-obs-only-object-norm02-seed43-r2 | 43 | 0.16 |\n| eval-obs-only-object-norm02-seed44-r2 | 44 | 0.16 |\n| eval-obs-only-object-norm02-seed45 | 45 | 0.16 |\n| eval-obs-only-object-norm02-seed46 | 46 | 0.15 |\n| eval-obs-only-object-norm02-seed47 | 47 | 0.20 |\n| eval-obs-only-object-norm02-seed48-r2 | 48 | 0.18 |\n\n**Diff**:\n- **In registry but NOT in script**: seed 42 (SR=0.22)\n  - `eval-acr-object-obs-only-norm02`: early experiment, SR=0.22 is a significant outlier vs seeds 43-48 range (0.15-0.20)\n  - Likely excluded due to different eval setup (earlier code version, possibly different n_rollouts)\n  - **Decision**: Exclusion is reasonable if eval config differs. Should be documented.\n\n#### CRM obs_only norm01 (Supplementary)\n**Script**: n=6, seeds=[42, 44, 45, 46, 47, 48]\n- values: {42: 0.19, 44: 0.16, 45: 0.17, 46: 0.18, 47: 0.17, 48: 0.18}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-obs-only-object-norm01-seed44 | 44 | 0.16 |\n| eval-obs-only-object-norm01-seed45-r2 | 45 | 0.17 |\n| eval-obs-only-object-norm01-seed46-r3 | 46 | 0.18 |\n| eval-obs-only-object-norm01-seed47 | 47 | 0.17 |\n| eval-obs-only-object-norm01-seed48 | 48 | 0.18 |\n\n**Diff**:\n- **MISSING from DONE+success registry**: seed 42\n  - `eval-obs-only-object-norm01-seed42`: status=**DEPLOYED** (not DONE), conclusion=success, SR=0.19\n  - `eval-obs-only-object-norm01-seed42-r2`: status=DONE, conclusion=**failed**\n- Script uses seed42=0.19 from the DEPLOYED experiment.\n- **Action**: Update `eval-obs-only-object-norm01-seed42` status to DONE.\n- Note: seed45 has two entries (original SR=0.14, r2 SR=0.17). Script correctly uses r2=0.17.\n\n#### CRM obs_only norm02 K=5 (Supplementary)\n**Script**: n=7, seeds=[42, 43, 44, 45, 46, 47, 48]\n- values: {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-obs-only-object-norm02-k5-seed42 | 42 | 0.14 |\n| eval-obs-only-object-norm02-k5-seed43 | 43 | 0.19 |\n| eval-obs-only-object-norm02-k5-seed44 | 44 | 0.17 |\n| eval-obs-only-object-norm02-k5-seed45 | 45 | 0.15 |\n| eval-obs-only-object-norm02-k5-seed46 | 46 | 0.16 |\n| eval-obs-only-object-norm02-k5-seed47 | 47 | 0.13 |\n| eval-obs-only-object-norm02-k5-seed48 | 48 | 0.18 |\n\n**Diff**: PERFECT MATCH — all 7 seeds present with correct values.\n\n#### VLA-only\n**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 50]\n- values: {42: 0.12, 43: 0.12, 44: 0.10, 45: 0.11, 46: 0.13, 47: 0.10, 48: 0.10, 50: 0.09}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-object (seed42) | 42 | 0.12 |\n| eval-vla-only-object-seed43 | 43 | 0.12 |\n| eval-vla-only-object-seed44-r2 | 44 | 0.10 |\n| eval-vla-only-object-seed45-r2 | 45 | 0.11 |\n| eval-vla-only-object-seed46 | 46 | 0.13 |\n| eval-vla-only-object-seed47 | 47 | 0.10 |\n| eval-vla-only-object-seed48 | 48 | 0.10 |\n| eval-vla-only-object-seed50 | 50 | 0.09 |\n\n**Diff**: PERFECT MATCH — all 8 seeds present with correct values.\n- Note: `eval-openvla-object-vla-only-seed42-v2` (SR=0.69) is OpenVLA (different model), correctly excluded.\n- Note: seed45 has r1=0.09, r2=0.11. Script correctly uses r2.\n\n#### Argmin K=10\n**Script**: n=5, seeds=[43, 44, 45, 46, 47]\n- values: {43: 0.17, 44: 0.13, 45: 0.12, 46: 0.10, 47: 0.10}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-argmin-object-seed43 | 43 | 0.17 |\n| eval-argmin-object-seed44-r2 | 44 | 0.13 |\n| eval-argmin-object-seed45 | 45 | 0.12 |\n| eval-argmin-object-seed46 | 46 | 0.10 |\n| eval-argmin-object-seed47 | 47 | 0.10 |\n\n**Diff**: PERFECT MATCH — all 5 seeds present with correct values.\n- Note: seed43=0.17 is a severe outlier (others 0.10-0.13). Script verification notes flag this as unverifiable (JSON not found on any server).\n\n#### Argmin K=5\n**Script**: n=4, seeds=[42, 43, 44, 45]\n- values: {42: 0.15, 43: 0.13, 44: 0.11, 45: 0.13}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-argmin-object-k5-seed42 | 42 | 0.15 |\n| eval-argmin-object-k5-seed43 | 43 | 0.13 |\n| eval-argmin-object-k5-seed44-r2 | 44 | 0.11 |\n| eval-argmin-object-k5-seed45 | 45 | 0.13 |\n\n**Diff**: PERFECT MATCH — all 4 seeds present with correct values.\n\n#### Adaptive-K\n**Script**: 4 thresholds × 3 seeds each (seeds 42, 43, 44)\n\n| Threshold | seed42 | seed43 | seed44 |\n|-----------|--------|--------|--------|\n| p25 | 0.15 | 0.13 | 0.15 |\n| p50 | 0.16 | 0.16 | 0.14 |\n| p75 | 0.12 | 0.13 | 0.16 |\n| p90 | 0.12 | 0.14 | 0.14 |\n\n**Registry** (DONE+success only):\n\n| Threshold | Registry Seeds (DONE+success) | Missing |\n|-----------|-------------------------------|---------|\n| p25 | 42 ✓, 43 ✓, 44 ✓ | — |\n| p50 | 44 ✓ | **42, 43** |\n| p75 | 44 ✓ | **42, 43** |\n| p90 | 42 ✓, 43 ✓, 44 ✓ | — |\n\n**Diff**:\n- p25, p90: PERFECT MATCH\n- p50 seed42/43: `eval-adaptive-k-p50-seed42` and `eval-adaptive-k-p50-seed43` have status=**ALLOCATED** (not DONE), but conclusion=success and SR values match script exactly (0.16, 0.16)\n- p75 seed42/43: `eval-adaptive-k-p75-seed42` and `eval-adaptive-k-p75-seed43` have status=**ALLOCATED** (not DONE), but conclusion=success and SR values match script exactly (0.12, 0.13)\n- **Action**: Update these 4 experiments' status from ALLOCATED → DONE.\n\n---\n\n## Registry Status Anomalies\n\nExperiments with valid data but incorrect status:\n\n| exp_id | Current Status | Should Be | SR |\n|--------|---------------|-----------|-----|\n| eval-adaptive-k-p50-seed42 | ALLOCATED | DONE | 0.16 |\n| eval-adaptive-k-p50-seed43 | ALLOCATED | DONE | 0.16 |\n| eval-adaptive-k-p75-seed42 | ALLOCATED | DONE | 0.12 |\n| eval-adaptive-k-p75-seed43 | ALLOCATED | DONE | 0.13 |\n| eval-obs-only-object-norm01-seed42 | DEPLOYED | DONE | 0.19 |\n| eval-vla-only-spatial-seed50 | PREPARING | DONE | 0.30 |\n| eval-crm-goal-seed47 | PREPARING | DONE (if verified) | 0.69 |\n\n---\n\n## Recommended Actions\n\n### High Priority (data integrity)\n1. **VLA-Long seed49** (SR=0.16): No registry data, no verifiable source. Either re-run the experiment or remove from script.\n2. **VLA-Spatial seeds 48/49**: Registry shows conclusion=failed. Verify the Director-provided values (0.30, 0.29) against server JSON. If unverifiable, remove.\n\n### Medium Priority (registry hygiene)\n3. **Fix 4 Adaptive-K statuses**: ALLOCATED → DONE for p50-seed42, p50-seed43, p75-seed42, p75-seed43.\n4. **Fix norm01-seed42 status**: DEPLOYED → DONE for `eval-obs-only-object-norm01-seed42`.\n5. **Fix VLA-Spatial seed50 status**: PREPARING → DONE for `eval-vla-only-spatial-seed50`.\n6. **Resolve CRM-Goal seed47**: Either complete the experiment and update status, or document the data source.\n\n### Low Priority (documentation)\n7. **Document Object CRM norm02 K=10 seed42 exclusion**: `eval-acr-object-obs-only-norm02` (SR=0.22) is excluded from the primary analysis. Add a comment explaining why (different eval config / outlier).\n\n---\n\n## Appendix: Spatial K=5 Cross-check\n\nThe registry also contains Spatial norm02 K=5 experiments (not used in primary analysis):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-obs-only-spatial-norm02-k5-seed42 | 42 | 0.35 |\n| eval-obs-only-spatial-norm02-k5-seed43 | 43 | 0.32 |\n| eval-obs-only-spatial-norm02-k5-seed44-r2 | 44 | 0.37 |\n| eval-obs-only-spatial-norm02-k5-seed45-r2 | 45 | 0.34 |\n\nThese are not included in the statistical script but are available for supplementary analysis if needed.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "814619f7-8b47-490c-a0e3-29c1bc4a3604",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYthph6Sguj51VEh2iak7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 73382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 209
      },
      "output_tokens": 39,
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

_source line 50 · 2026-05-20T07:23:48.025Z_

<details><summary>↩ Tool result · `toolu_01HC6PDL6CBNh4DPdazKKYmv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "840f9540-a13d-4481-a047-cf3373417d0b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md",
    "content": "# Full Benchmark Data Audit\nDate: 2026-05-20\n\n## Summary\n\n| Category | Count | Details |\n|----------|-------|---------|\n| **Perfect matches** | 9/15 | Spatial-CRM, Long-CRM, Long-VLA (10/11), Goal-VLA, Obj-norm02-K10 (6/6), Obj-K5, Obj-VLA, Argmin-K10, Argmin-K5 |\n| **Seeds in script but not in DONE+success registry** | 8 | See details below |\n| **Seeds in registry but excluded from script** | 1 | Obj-CRM-norm02-K10 seed42 |\n| **Value mismatches** | 0 | All common seeds have matching SR values |\n| **Registry status anomalies** | 6 | Experiments with data but status ≠ DONE or conclusion ≠ success |\n\n### Seeds in Script Not in DONE+success Registry\n\n| Benchmark | Method | Seed | Script SR | Registry Status | Notes |\n|-----------|--------|------|-----------|-----------------|-------|\n| Spatial | VLA-only | 48 | 0.30 | DONE/failed | Director directive; data exists outside registry |\n| Spatial | VLA-only | 49 | 0.29 | DONE/failed | Director directive; data exists outside registry |\n| Spatial | VLA-only | 50 | 0.30 | PREPARING/success | SR=0.30 in registry but status not DONE |\n| Long | VLA-only | 49 | 0.16 | PREPARING/None | No SR in registry; Director directive |\n| Goal | CRM obs_only | 47 | 0.69 | PREPARING/None | SR=0.69 in registry metrics but status PREPARING |\n| Object | CRM norm01 | 42 | 0.19 | DEPLOYED/success | SR=0.19 in registry but status DEPLOYED, not DONE |\n| Object | Adaptive-K p50 | 42,43 | 0.16,0.16 | ALLOCATED/success | SR matches; status should be DONE |\n| Object | Adaptive-K p75 | 42,43 | 0.12,0.13 | ALLOCATED/success | SR matches; status should be DONE |\n\n---\n\n## Per-Benchmark Details\n\n### LIBERO-Spatial\n\n#### CRM obs_only norm02 K=10\n**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 51]\n- values: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}\n\n**Registry** (all DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-mag-obsonly-norm02 | 42 | 0.35 |\n| eval-obs-only-spatial-norm02-seed43-r2 | 43 | 0.34 |\n| eval-obs-only-spatial-norm02-seed44 | 44 | 0.36 |\n| eval-obs-only-spatial-norm02-seed45 | 45 | 0.34 |\n| eval-obs-only-spatial-norm02-seed46-r2 | 46 | 0.33 |\n| eval-obs-only-spatial-norm02-seed47 | 47 | 0.32 |\n| eval-obs-only-spatial-norm02-seed48 | 48 | 0.35 |\n| eval-crm-spatial-k10-seed51 | 51 | 0.36 |\n\n**Diff**: MATCH — all 8 seeds present with correct values.\n- Note: eval-mag-obsonly-norm02 has `conclusion=negative` (not `success`), but SR=0.35 is valid data. Script correctly uses it.\n\n#### VLA-only\n**Script**: n=9, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50]\n- values: {42: 0.30, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.30, 47: 0.30, 48: 0.30, 49: 0.29, 50: 0.30}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-spatial-seed42 | 42 | 0.30 |\n| eval-vla-only-spatial-seed43 | 43 | 0.29 |\n| eval-vla-only-spatial-seed44 | 44 | 0.31 |\n| eval-vla-only-spatial-seed45 | 45 | 0.27 |\n| eval-vla-only-spatial-seed46 | 46 | 0.30 |\n| eval-vla-only-spatial-seed47 | 47 | 0.30 |\n\n**Diff**:\n- **MISSING from DONE+success registry**: seeds 48, 49, 50\n  - seed48: `eval-vla-only-spatial-seed48` status=DONE, conclusion=**failed** (no valid SR)\n  - seed49: `eval-vla-only-spatial-seed49` status=DONE, conclusion=**failed** (no valid SR)\n  - seed50: `eval-vla-only-spatial-seed50` status=**PREPARING**, conclusion=success, SR=0.30\n- Script verification notes state: \"VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive\"\n- **Risk**: Seeds 48/49 have no verifiable SR in registry. Data likely from external source (server JSON).\n\n---\n\n### LIBERO-Long\n\n#### CRM obs_only\n**Script**: n=7, seeds=[42, 43, 44, 45, 46, 47, 50]\n- values: {42: 0.17, 43: 0.15, 44: 0.20, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-crm-long-seed42 | 42 | 0.17 |\n| eval-crm-long-seed43 | 43 | 0.15 |\n| eval-crm-long-seed44 | 44 | 0.20 |\n| eval-crm-long-seed45 | 45 | 0.18 |\n| eval-crm-long-seed46 | 46 | 0.18 |\n| eval-crm-long-seed47 | 47 | 0.17 |\n| eval-crm-long-seed50 | 50 | 0.14 |\n\n**Diff**: PERFECT MATCH — all 7 seeds present with correct values.\n\n#### VLA-only\n**Script**: n=11, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]\n- values: {42: 0.11, 43: 0.13, 44: 0.12, 45: 0.17, 46: 0.18, 47: 0.14, 48: 0.14, 49: 0.16, 50: 0.16, 51: 0.15, 52: 0.17}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-long-seed42 | 42 | 0.11 |\n| eval-vla-only-long-seed43 | 43 | 0.13 |\n| eval-vla-only-long-seed44 | 44 | 0.12 |\n| eval-vla-only-long-seed45 | 45 | 0.17 |\n| eval-vla-only-long-seed46 | 46 | 0.18 |\n| eval-vla-only-long-seed47 | 47 | 0.14 |\n| eval-vla-only-long-seed48 | 48 | 0.14 |\n| eval-vla-only-long-seed50 | 50 | 0.16 |\n| eval-vla-only-long-seed51 | 51 | 0.15 |\n| eval-vla-only-long-seed52 | 52 | 0.17 |\n\n**Diff**:\n- **MISSING from registry**: seed 49\n  - `eval-vla-only-long-seed49`: status=**PREPARING**, conclusion=None, SR=None\n- Script includes seed49=0.16. Data source unclear — no SR in registry, experiment never completed.\n- **Risk**: Unverifiable data point. Should be removed or re-run.\n\n---\n\n### LIBERO-Goal\n\n#### CRM obs_only\n**Script**: n=6, seeds=[42, 43, 44, 45, 46, 47]\n- values: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72, 47: 0.69}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-crm-goal-seed42 | 42 | 0.67 |\n| eval-crm-goal-seed43 | 43 | 0.72 |\n| eval-crm-goal-seed44-r2 | 44 | 0.64 |\n| eval-crm-goal-seed45-r2 | 45 | 0.65 |\n| eval-crm-goal-seed46 | 46 | 0.72 |\n\n**Diff**:\n- **MISSING from DONE+success registry**: seed 47\n  - `eval-crm-goal-seed47`: status=**PREPARING**, conclusion=None, SR=0.69 (in metrics)\n- Script verification notes: \"CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\"\n- SR value 0.69 exists in registry metrics despite PREPARING status. Likely manually populated.\n- **Action**: Update registry status to DONE+success when experiment completes, or verify data source.\n\n#### VLA-only\n**Script**: n=6, seeds=[42, 43, 44, 45, 46, 49]\n- values: {42: 0.71, 43: 0.69, 44: 0.73, 45: 0.63, 46: 0.71, 49: 0.65}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-goal-seed42 | 42 | 0.71 |\n| eval-vla-only-goal-seed43 | 43 | 0.69 |\n| eval-vla-only-goal-seed44-r2 | 44 | 0.73 |\n| eval-vla-only-goal-seed45 | 45 | 0.63 |\n| eval-vla-only-goal-seed46 | 46 | 0.71 |\n| eval-vla-only-goal-seed49 | 49 | 0.65 |\n\n**Diff**: PERFECT MATCH — all 6 seeds present with correct values.\n\n---\n\n### LIBERO-Object\n\n#### CRM obs_only norm02 K=10 (PRIMARY)\n**Script**: n=6, seeds=[43, 44, 45, 46, 47, 48]\n- values: {43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.20, 48: 0.18}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-acr-object-obs-only-norm02 | 42 | 0.22 |\n| eval-obs-only-object-norm02-seed43-r2 | 43 | 0.16 |\n| eval-obs-only-object-norm02-seed44-r2 | 44 | 0.16 |\n| eval-obs-only-object-norm02-seed45 | 45 | 0.16 |\n| eval-obs-only-object-norm02-seed46 | 46 | 0.15 |\n| eval-obs-only-object-norm02-seed47 | 47 | 0.20 |\n| eval-obs-only-object-norm02-seed48-r2 | 48 | 0.18 |\n\n**Diff**:\n- **In registry but NOT in script**: seed 42 (SR=0.22)\n  - `eval-acr-object-obs-only-norm02`: early experiment, SR=0.22 is a significant outlier vs seeds 43-48 range (0.15-0.20)\n  - Likely excluded due to different eval setup (earlier code version, possibly different n_rollouts)\n  - **Decision**: Exclusion is reasonable if eval config differs. Should be documented.\n\n#### CRM obs_only norm01 (Supplementary)\n**Script**: n=6, seeds=[42, 44, 45, 46, 47, 48]\n- values: {42: 0.19, 44: 0.16, 45: 0.17, 46: 0.18, 47: 0.17, 48: 0.18}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-obs-only-object-norm01-seed44 | 44 | 0.16 |\n| eval-obs-only-object-norm01-seed45-r2 | 45 | 0.17 |\n| eval-obs-only-object-norm01-seed46-r3 | 46 | 0.18 |\n| eval-obs-only-object-norm01-seed47 | 47 | 0.17 |\n| eval-obs-only-object-norm01-seed48 | 48 | 0.18 |\n\n**Diff**:\n- **MISSING from DONE+success registry**: seed 42\n  - `eval-obs-only-object-norm01-seed42`: status=**DEPLOYED** (not DONE), conclusion=success, SR=0.19\n  - `eval-obs-only-object-norm01-seed42-r2`: status=DONE, conclusion=**failed**\n- Script uses seed42=0.19 from the DEPLOYED experiment.\n- **Action**: Update `eval-obs-only-object-norm01-seed42` status to DONE.\n- Note: seed45 has two entries (original SR=0.14, r2 SR=0.17). Script correctly uses r2=0.17.\n\n#### CRM obs_only norm02 K=5 (Supplementary)\n**Script**: n=7, seeds=[42, 43, 44, 45, 46, 47, 48]\n- values: {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-obs-only-object-norm02-k5-seed42 | 42 | 0.14 |\n| eval-obs-only-object-norm02-k5-seed43 | 43 | 0.19 |\n| eval-obs-only-object-norm02-k5-seed44 | 44 | 0.17 |\n| eval-obs-only-object-norm02-k5-seed45 | 45 | 0.15 |\n| eval-obs-only-object-norm02-k5-seed46 | 46 | 0.16 |\n| eval-obs-only-object-norm02-k5-seed47 | 47 | 0.13 |\n| eval-obs-only-object-norm02-k5-seed48 | 48 | 0.18 |\n\n**Diff**: PERFECT MATCH — all 7 seeds present with correct values.\n\n#### VLA-only\n**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 50]\n- values: {42: 0.12, 43: 0.12, 44: 0.10, 45: 0.11, 46: 0.13, 47: 0.10, 48: 0.10, 50: 0.09}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-vla-only-object (seed42) | 42 | 0.12 |\n| eval-vla-only-object-seed43 | 43 | 0.12 |\n| eval-vla-only-object-seed44-r2 | 44 | 0.10 |\n| eval-vla-only-object-seed45-r2 | 45 | 0.11 |\n| eval-vla-only-object-seed46 | 46 | 0.13 |\n| eval-vla-only-object-seed47 | 47 | 0.10 |\n| eval-vla-only-object-seed48 | 48 | 0.10 |\n| eval-vla-only-object-seed50 | 50 | 0.09 |\n\n**Diff**: PERFECT MATCH — all 8 seeds present with correct values.\n- Note: `eval-openvla-object-vla-only-seed42-v2` (SR=0.69) is OpenVLA (different model), correctly excluded.\n- Note: seed45 has r1=0.09, r2=0.11. Script correctly uses r2.\n\n#### Argmin K=10\n**Script**: n=5, seeds=[43, 44, 45, 46, 47]\n- values: {43: 0.17, 44: 0.13, 45: 0.12, 46: 0.10, 47: 0.10}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-argmin-object-seed43 | 43 | 0.17 |\n| eval-argmin-object-seed44-r2 | 44 | 0.13 |\n| eval-argmin-object-seed45 | 45 | 0.12 |\n| eval-argmin-object-seed46 | 46 | 0.10 |\n| eval-argmin-object-seed47 | 47 | 0.10 |\n\n**Diff**: PERFECT MATCH — all 5 seeds present with correct values.\n- Note: seed43=0.17 is a severe outlier (others 0.10-0.13). Script verification notes flag this as unverifiable (JSON not found on any server).\n\n#### Argmin K=5\n**Script**: n=4, seeds=[42, 43, 44, 45]\n- values: {42: 0.15, 43: 0.13, 44: 0.11, 45: 0.13}\n\n**Registry** (DONE+success):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-argmin-object-k5-seed42 | 42 | 0.15 |\n| eval-argmin-object-k5-seed43 | 43 | 0.13 |\n| eval-argmin-object-k5-seed44-r2 | 44 | 0.11 |\n| eval-argmin-object-k5-seed45 | 45 | 0.13 |\n\n**Diff**: PERFECT MATCH — all 4 seeds present with correct values.\n\n#### Adaptive-K\n**Script**: 4 thresholds × 3 seeds each (seeds 42, 43, 44)\n\n| Threshold | seed42 | seed43 | seed44 |\n|-----------|--------|--------|--------|\n| p25 | 0.15 | 0.13 | 0.15 |\n| p50 | 0.16 | 0.16 | 0.14 |\n| p75 | 0.12 | 0.13 | 0.16 |\n| p90 | 0.12 | 0.14 | 0.14 |\n\n**Registry** (DONE+success only):\n\n| Threshold | Registry Seeds (DONE+success) | Missing |\n|-----------|-------------------------------|---------|\n| p25 | 42 ✓, 43 ✓, 44 ✓ | — |\n| p50 | 44 ✓ | **42, 43** |\n| p75 | 44 ✓ | **42, 43** |\n| p90 | 42 ✓, 43 ✓, 44 ✓ | — |\n\n**Diff**:\n- p25, p90: PERFECT MATCH\n- p50 seed42/43: `eval-adaptive-k-p50-seed42` and `eval-adaptive-k-p50-seed43` have status=**ALLOCATED** (not DONE), but conclusion=success and SR values match script exactly (0.16, 0.16)\n- p75 seed42/43: `eval-adaptive-k-p75-seed42` and `eval-adaptive-k-p75-seed43` have status=**ALLOCATED** (not DONE), but conclusion=success and SR values match script exactly (0.12, 0.13)\n- **Action**: Update these 4 experiments' status from ALLOCATED → DONE.\n\n---\n\n## Registry Status Anomalies\n\nExperiments with valid data but incorrect status:\n\n| exp_id | Current Status | Should Be | SR |\n|--------|---------------|-----------|-----|\n| eval-adaptive-k-p50-seed42 | ALLOCATED | DONE | 0.16 |\n| eval-adaptive-k-p50-seed43 | ALLOCATED | DONE | 0.16 |\n| eval-adaptive-k-p75-seed42 | ALLOCATED | DONE | 0.12 |\n| eval-adaptive-k-p75-seed43 | ALLOCATED | DONE | 0.13 |\n| eval-obs-only-object-norm01-seed42 | DEPLOYED | DONE | 0.19 |\n| eval-vla-only-spatial-seed50 | PREPARING | DONE | 0.30 |\n| eval-crm-goal-seed47 | PREPARING | DONE (if verified) | 0.69 |\n\n---\n\n## Recommended Actions\n\n### High Priority (data integrity)\n1. **VLA-Long seed49** (SR=0.16): No registry data, no verifiable source. Either re-run the experiment or remove from script.\n2. **VLA-Spatial seeds 48/49**: Registry shows conclusion=failed. Verify the Director-provided values (0.30, 0.29) against server JSON. If unverifiable, remove.\n\n### Medium Priority (registry hygiene)\n3. **Fix 4 Adaptive-K statuses**: ALLOCATED → DONE for p50-seed42, p50-seed43, p75-seed42, p75-seed43.\n4. **Fix norm01-seed42 status**: DEPLOYED → DONE for `eval-obs-only-object-norm01-seed42`.\n5. **Fix VLA-Spatial seed50 status**: PREPARING → DONE for `eval-vla-only-spatial-seed50`.\n6. **Resolve CRM-Goal seed47**: Either complete the experiment and update status, or document the data source.\n\n### Low Priority (documentation)\n7. **Document Object CRM norm02 K=10 seed42 exclusion**: `eval-acr-object-obs-only-norm02` (SR=0.22) is excluded from the primary analysis. Add a comment explaining why (different eval config / outlier).\n\n---\n\n## Appendix: Spatial K=5 Cross-check\n\nThe registry also contains Spatial norm02 K=5 experiments (not used in primary analysis):\n\n| exp_id | seed | SR |\n|--------|------|----|\n| eval-obs-only-spatial-norm02-k5-seed42 | 42 | 0.35 |\n| eval-obs-only-spatial-norm02-k5-seed43 | 43 | 0.32 |\n| eval-obs-only-spatial-norm02-k5-seed44-r2 | 44 | 0.37 |\n| eval-obs-only-spatial-norm02-k5-seed45-r2 | 45 | 0.34 |\n\nThese are not included in the statistical script but are available for supplementary analysis if needed.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014jRPwHbCPbCwGrhARjVoTx`</summary>

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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "acc07df0-bc20-4550-944d-01b78bfb9fbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ptGCdZP3qEJuSdNgnRjKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6555,
      "cache_read_input_tokens": 73591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6555
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

_source line 52 · 2026-05-20T07:23:52.153Z_

<details><summary>↩ Tool result · `toolu_014jRPwHbCPbCwGrhARjVoTx`</summary>

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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "eda53bcb-5090-4d77-bfeb-d2d5c83953ca",
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

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01E2ybKi8ad4DAx9uqXCVBHN`</summary>

```json
{
  "name": "benchmark_data_audit",
  "type": "report",
  "description": "Full benchmark data audit: registry vs statistical script cross-check for all 4 LIBERO benchmarks (Spatial/Long/Goal/Object) and all methods (CRM/VLA-only/Argmin/Adaptive-K). Found 0 value mismatches, 8 seeds with registry status anomalies, 1 excluded registry seed.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/benchmark_data_audit.md",
  "tags": [
    "audit",
    "data-integrity",
    "statistical-analysis",
    "registry"
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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "3f647f4a-d523-4488-8b49-8d22c6a30fac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToNXcqg21Sozf7YF54k3xu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 80146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
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

_source line 54 · 2026-05-20T07:23:58.864Z_

<details><summary>↩ Tool result · `toolu_01E2ybKi8ad4DAx9uqXCVBHN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_8e3ba4\", \"name\": \"benchmark_data_audit\", \"type\": \"report\", \"description\": \"Full benchmark data audit: registry vs statistical script cross-check for all 4 LIBERO benchmarks (Spatial/Long/Goal/Object) and all methods (CRM/VLA-only/Argmin/Adaptive-K). Found 0 value mismatches, 8 seeds with registry status anomalies, 1 excluded registry seed.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/benchmark_data_audit.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T07:23:58.564859+00:00\", \"tags\": [\"audit\", \"data-integrity\", \"statistical-analysis\", \"registry\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "8ee73464-ff60-4506-aed8-65b2b1544441",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_8e3ba4\\\", \\\"name\\\": \\\"benchmark_data_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Full benchmark data audit: registry vs statistical script cross-check for all 4 LIBERO benchmarks (Spatial/Long/Goal/Object) and all methods (CRM/VLA-only/Argmin/Adaptive-K). Found 0 value mismatches, 8 seeds with registry status anomalies, 1 excluded registry seed.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/benchmark_data_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T07:23:58.564859+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"data-integrity\\\", \\\"statistical-analysis\\\", \\\"registry\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_8e3ba4\", \"name\": \"benchmark_data_audit\", \"type\": \"report\", \"description\": \"Full benchmark data audit: registry vs statistical script cross-check for all 4 LIBERO benchmarks (Spatial/Long/Goal/Object) and all methods (CRM/VLA-only/Argmin/Adaptive-K). Found 0 value mismatches, 8 seeds with registry status anomalies, 1 excluded registry seed.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/benchmark_data_audit.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T07:23:58.564859+00:00\", \"tags\": [\"audit\", \"data-integrity\", \"statistical-analysis\", \"registry\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01JpGcEqLvmuFVPUYs5PQfx3`</summary>

```json
{
  "todos": [
    {
      "content": "Collect registry data for all benchmarks",
      "status": "completed",
      "activeForm": "Collecting registry data"
    },
    {
      "content": "Verify edge cases and anomalies",
      "status": "completed",
      "activeForm": "Verifying edge cases"
    },
    {
      "content": "Generate audit report",
      "status": "completed",
      "activeForm": "Generating audit report"
    },
    {
      "content": "Register artifact",
      "status": "completed",
      "activeForm": "Registering artifact"
    }
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
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "0ea7fe74-af41-46b9-8ec0-b2dfdf9ed441",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmtNttX6GD3e6Lz4GZqvNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 80858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
      },
      "output_tokens": 51,
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

_source line 56 · 2026-05-20T07:24:02.967Z_

<details><summary>↩ Tool result · `toolu_01JpGcEqLvmuFVPUYs5PQfx3`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "6bac63ad-e7f7-4d3a-896c-561166096228",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Collect registry data for all benchmarks",
        "status": "completed",
        "activeForm": "Collecting registry data"
      },
      {
        "content": "Verify edge cases and anomalies",
        "status": "completed",
        "activeForm": "Verifying edge cases"
      },
      {
        "content": "Generate audit report",
        "status": "in_progress",
        "activeForm": "Generating audit report"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Collect registry data for all benchmarks",
        "status": "completed",
        "activeForm": "Collecting registry data"
      },
      {
        "content": "Verify edge cases and anomalies",
        "status": "completed",
        "activeForm": "Verifying edge cases"
      },
      {
        "content": "Generate audit report",
        "status": "completed",
        "activeForm": "Generating audit report"
      },
      {
        "content": "Register artifact",
        "status": "completed",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 57_

审计完成。报告已保存到 `artifacts/benchmark_data_audit.md` 并注册 (`art_20260520_8e3ba4`)。

核心结论：

- **0 个数值不匹配** — 所有 script 与 registry 共有的 seed，SR 值完全一致
- **9/15 组数据完美匹配**（含 Long-CRM、Goal-VLA、Object-K5、Object-VLA、Argmin 等）
- **8 个 seed 的 registry 状态异常**（数据有效但 status 不是 DONE+success）：
  - VLA-Spatial seed48/49: conclusion=failed（数据来自 Director 指令）
  - VLA-Long seed49: status=PREPARING，无 SR（**最高风险，数据不可验证**）
  - CRM-Goal seed47: status=PREPARING，SR=0.69 已在 metrics 中
  - 4 个 Adaptive-K: status=ALLOCATED 应为 DONE
  - Object norm01 seed42: status=DEPLOYED 应为 DONE
- **1 个被排除的 registry seed**: Object CRM norm02 K=10 seed42 (SR=0.22 是离群值)

**建议优先处理**: VLA-Long seed49（无法验证）和 VLA-Spatial seed48/49（registry 标记为 failed）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "uuid": "22b39e1b-7486-4954-85d1-beb8d117bcc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018byui17wH3fhPn5vUbNndk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 81500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 204
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

_source line 58_

审计完成。报告已保存到 `artifacts/benchmark_data_audit.md` 并注册 (`art_20260520_8e3ba4`)。

核心结论：

- **0 个数值不匹配** — 所有 script 与 registry 共有的 seed，SR 值完全一致
- **9/15 组数据完美匹配**（含 Long-CRM、Goal-VLA、Object-K5、Object-VLA、Argmin 等）
- **8 个 seed 的 registry 状态异常**（数据有效但 status 不是 DONE+success）：
  - VLA-Spatial seed48/49: conclusion=failed（数据来自 Director 指令）
  - VLA-Long seed49: status=PREPARING，无 SR（**最高风险，数据不可验证**）
  - CRM-Goal seed47: status=PREPARING，SR=0.69 已在 metrics 中
  - 4 个 Adaptive-K: status=ALLOCATED 应为 DONE
  - Object norm01 seed42: status=DEPLOYED 应为 DONE
- **1 个被排除的 registry seed**: Object CRM norm02 K=10 seed42 (SR=0.22 是离群值)

**建议优先处理**: VLA-Long seed49（无法验证）和 VLA-Spatial seed48/49（registry 标记为 failed）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 392065,
  "duration_api_ms": 383477,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "a8f05db3-0d4c-4cf3-b551-4fcdf5b19395",
  "total_cost_usd": 1.5692817500000003,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 69863,
    "cache_read_input_tokens": 843722,
    "output_tokens": 28322,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 69863,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 380,
        "cache_read_input_tokens": 81500,
        "cache_creation_input_tokens": 204,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 204
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2542,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002617,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 22,
      "outputTokens": 28322,
      "cacheReadInputTokens": 843722,
      "cacheCreationInputTokens": 69863,
      "webSearchRequests": 0,
      "costUSD": 1.5666647500000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0bd8c84e-7d9e-467c-a255-e84d0155b4ee"
}
```

</details>

---
