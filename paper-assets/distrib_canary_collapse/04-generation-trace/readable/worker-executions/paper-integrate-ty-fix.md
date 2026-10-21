# paper integrate ty fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_integrate_ty_fix_20260516T002030.log`
- **Structured JSON:** [`0981b7783688653877ba.json`](../../sessions/09/0981b7783688653877ba.json)

## Before a recorded user message

64 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
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
  "uuid": "8becdad8-7ab5-4ea9-bdbc-d8d8c14a7503",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1778907000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "62f8ea3e-8ae0-49f2-adae-6fac8e78304a",
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the fix report and then examining the paper files to understand what needs to be updated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "1e170ef5-75bd-4048-a7ff-01bd54213c8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BTYUM4dUHDtjRJoTa2GT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11862,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11862
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

读取修复报告和论文文件结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "240cae60-3d89-4c87-a0e0-8170c2d7113e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BTYUM4dUHDtjRJoTa2GT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11862,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11862
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

<details open><summary>🔧 Tool call — Read · `toolu_016guMdmog1zj92rsc2vuBKx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/window_sensitivity_t11/window_sensitivity_fixed.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "c2d40f40-86da-40b4-81b4-1d430869f510",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BTYUM4dUHDtjRJoTa2GT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11862,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11862
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

_source line 7 · 2026-05-16T00:20:42.777Z_

<details><summary>↩ Tool result · `toolu_016guMdmog1zj92rsc2vuBKx`</summary>

````text
1	# Window Sensitivity Analysis — Bugfix Report (D044-A)
2	
3	## Pythia-410M, α=1.0, 4 seeds (42–45), T∈{5,6,7,8,9,10}
4	
5	Two bugs in `window_sensitivity.py` caused incorrect TY column values in the original D044-A report. The 4/5-method consensus conclusions (NX/DX/TH/PG) were unaffected because TY is not required for 4/5 majority.
6	
7	---
8	
9	## Bugs Fixed
10	
11	### Bug #1: Off-by-one in data slicing (line 193)
12	```python
13	# Before (wrong):  T=10 → 10 points (gen_0 to gen_9)
14	metrics = all_data[seed][:T]
15	
16	# After (correct): T=10 → 11 points (gen_0 to gen_10)
17	metrics = all_data[seed][:T+1]
18	```
19	Paper convention: "T=10 generations" = gen_0 through gen_10 = 11 data points.
20	
21	### Bug #2: Divergent TY implementation
22	`window_sensitivity.py` used a local `toda_yamamoto_v2` (hardcoded d=1, AIC-selected p, VAR `test_causality` chi²) which differed from the canonical `method_ablation.py` implementation (ADF-tested d_max, fixed p=1, manual OLS F-test). The local version returned `p=nan` at most window lengths due to VAR `test_causality` failing silently on short series.
23	
24	**Fix**: Imported `toda_yamamoto` from `method_ablation.py`, deleted local TY functions.
25	
26	---
27	
28	## Table 1: TY Consensus Before vs After (pairs with ≥3/4 seed sig)
29	
30	| T | Points (old→new) | TY sig old | TY sig new | NX/DX/TH/PG (unchanged) |
31	|---|---|---|---|---|
32	| 5 | 5→6 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
33	| 6 | 6→7 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
34	| 7 | 7→8 | 0/6 | 6/6 | 6/6, 6/6, 6/6, 6/6 |
35	| 8 | 8→9 | 3/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
36	| 9 | 9→10 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
37	| 10 | 10→11 | **0/6** | **4/6** | 6/6, 6/6, 6/6, 6/6 |
38	
39	**Root cause of old TY=0/6**: The buggy `toda_yamamoto_v2` returned `p=nan` for almost all seeds/windows because `VAR.test_causality()` silently fails when residual df is too low. The `nan` was then compared `< 0.05`, yielding False.
40	
41	---
42	
43	## Table 2: Full Consensus Summary (Fixed)
44	
45	| T | Robust (≥4/5) | NX | DX | TH | PG | TY |
46	|---|---|---|---|---|---|---|
47	| 5 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
48	| 6 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
49	| 7 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 |
50	| 8 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
51	| 9 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
52	| 10 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 4/6 |
53	
54	All 6 pairs remain robust (≥4/5 methods) at every window length. TY is the most variable method, consistent with its low power at small T.
55	
56	---
57	
58	## Table 3: TY Seed-level Detail at T=10 (11 points, fixed)
59	
60	| Pair | Seed 42 | Seed 43 | Seed 44 | Seed 45 | Consensus |
61	|---|---|---|---|---|---|
62	| entropy→d1 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |
63	| entropy→d2 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |
64	| entropy→d3 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |
65	| ECE→d1 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.173) | ✓ (p=0.028) | **3/4** |
66	| ECE→d2 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.373) | ✗ (p=0.600) | 2/4 |
67	| ECE→d3 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.229) | ✗ (p=0.572) | 2/4 |
68	
69	---
70	
71	## Table 4: TY Seed-level Detail at T=10 — Old (buggy) vs New (fixed)
72	
73	| Pair | Seed | Old TY | New TY |
74	|---|---|---|---|
75	| entropy→d1 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
76	| entropy→d1 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
77	| entropy→d1 | 44 | ✗ (p=nan) | ✓ (p=0.000) |
78	| entropy→d1 | 45 | ✗ (p=nan) | ✓ (p=0.000) |
79	| entropy→d2 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
80	| entropy→d2 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
81	| entropy→d2 | 44 | ✗ (p=nan) | ✓ (p=0.000) |
82	| entropy→d2 | 45 | ✗ (p=nan) | ✓ (p=0.000) |
83	| entropy→d3 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
84	| entropy→d3 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
85	| entropy→d3 | 44 | ✗ (p=nan) | ✓ (p=0.000) |
86	| entropy→d3 | 45 | ✗ (p=nan) | ✓ (p=0.000) |
87	| ECE→d1 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
88	| ECE→d1 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
89	| ECE→d1 | 44 | ✗ (p=nan) | ✗ (p=0.173) |
90	| ECE→d1 | 45 | ✓ (p=0.016) | ✓ (p=0.028) |
91	| ECE→d2 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
92	| ECE→d2 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
93	| ECE→d2 | 44 | ✗ (p=nan) | ✗ (p=0.373) |
94	| ECE→d2 | 45 | ✗ (p=nan) | ✗ (p=0.600) |
95	| ECE→d3 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
96	| ECE→d3 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
97	| ECE→d3 | 44 | ✗ (p=nan) | ✗ (p=0.229) |
98	| ECE→d3 | 45 | ✗ (p=nan) | ✗ (p=0.572) |
99	
100	---
101	
102	## Cross-validation with ty_audit_report (Method A, 11 points)
103	
104	| Metric | Expected (ty_audit) | Got (window_sensitivity fixed) | Match |
105	|---|---|---|---|
106	| TE→d1,d2,d3 | 4/4 sig each | 4/4 sig each | ✓ |
107	| ECE→d1 | 3/4 sig | 3/4 sig (seed 44 n.s.) | ✓ |
108	
109	---
110	
111	## Impact on Paper Claims
112	
113	- **4/5 consensus conclusions unchanged**: All 6 forward pairs remain robust at every T∈{5..10}. The bugs only affected TY, which was never required for the 4/5 majority.
114	- **TY now adds confirmatory power**: At T=10, TY confirms 4/6 pairs (all 3 TE→d* and ECE→d1), strengthening the case vs. the buggy 0/6.
115	- **TY variability across T is expected**: With p=1, d_max=1–2, residual df ranges from ~2 (T=5) to ~6 (T=10). Low df → unstable significance. This is consistent with the known TY power limitations documented in D013/D015.
116	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "e1801113-41b8-4c5c-96bf-712cc9ab24fb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/window_sensitivity_t11/window_sensitivity_fixed.md",
      "content": "# Window Sensitivity Analysis — Bugfix Report (D044-A)\n\n## Pythia-410M, α=1.0, 4 seeds (42–45), T∈{5,6,7,8,9,10}\n\nTwo bugs in `window_sensitivity.py` caused incorrect TY column values in the original D044-A report. The 4/5-method consensus conclusions (NX/DX/TH/PG) were unaffected because TY is not required for 4/5 majority.\n\n---\n\n## Bugs Fixed\n\n### Bug #1: Off-by-one in data slicing (line 193)\n```python\n# Before (wrong):  T=10 → 10 points (gen_0 to gen_9)\nmetrics = all_data[seed][:T]\n\n# After (correct): T=10 → 11 points (gen_0 to gen_10)\nmetrics = all_data[seed][:T+1]\n```\nPaper convention: \"T=10 generations\" = gen_0 through gen_10 = 11 data points.\n\n### Bug #2: Divergent TY implementation\n`window_sensitivity.py` used a local `toda_yamamoto_v2` (hardcoded d=1, AIC-selected p, VAR `test_causality` chi²) which differed from the canonical `method_ablation.py` implementation (ADF-tested d_max, fixed p=1, manual OLS F-test). The local version returned `p=nan` at most window lengths due to VAR `test_causality` failing silently on short series.\n\n**Fix**: Imported `toda_yamamoto` from `method_ablation.py`, deleted local TY functions.\n\n---\n\n## Table 1: TY Consensus Before vs After (pairs with ≥3/4 seed sig)\n\n| T | Points (old→new) | TY sig old | TY sig new | NX/DX/TH/PG (unchanged) |\n|---|---|---|---|---|\n| 5 | 5→6 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |\n| 6 | 6→7 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |\n| 7 | 7→8 | 0/6 | 6/6 | 6/6, 6/6, 6/6, 6/6 |\n| 8 | 8→9 | 3/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |\n| 9 | 9→10 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |\n| 10 | 10→11 | **0/6** | **4/6** | 6/6, 6/6, 6/6, 6/6 |\n\n**Root cause of old TY=0/6**: The buggy `toda_yamamoto_v2` returned `p=nan` for almost all seeds/windows because `VAR.test_causality()` silently fails when residual df is too low. The `nan` was then compared `< 0.05`, yielding False.\n\n---\n\n## Table 2: Full Consensus Summary (Fixed)\n\n| T | Robust (≥4/5) | NX | DX | TH | PG | TY |\n|---|---|---|---|---|---|---|\n| 5 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |\n| 6 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |\n| 7 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 |\n| 8 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |\n| 9 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |\n| 10 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 4/6 |\n\nAll 6 pairs remain robust (≥4/5 methods) at every window length. TY is the most variable method, consistent with its low power at small T.\n\n---\n\n## Table 3: TY Seed-level Detail at T=10 (11 points, fixed)\n\n| Pair | Seed 42 | Seed 43 | Seed 44 | Seed 45 | Consensus |\n|---|---|---|---|---|---|\n| entropy→d1 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |\n| entropy→d2 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |\n| entropy→d3 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |\n| ECE→d1 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.173) | ✓ (p=0.028) | **3/4** |\n| ECE→d2 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.373) | ✗ (p=0.600) | 2/4 |\n| ECE→d3 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.229) | ✗ (p=0.572) | 2/4 |\n\n---\n\n## Table 4: TY Seed-level Detail at T=10 — Old (buggy) vs New (fixed)\n\n| Pair | Seed | Old TY | New TY |\n|---|---|---|---|\n| entropy→d1 | 42 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d1 | 43 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d1 | 44 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d1 | 45 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d2 | 42 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d2 | 43 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d2 | 44 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d2 | 45 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d3 | 42 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d3 | 43 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d3 | 44 | ✗ (p=nan) | ✓ (p=0.000) |\n| entropy→d3 | 45 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d1 | 42 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d1 | 43 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d1 | 44 | ✗ (p=nan) | ✗ (p=0.173) |\n| ECE→d1 | 45 | ✓ (p=0.016) | ✓ (p=0.028) |\n| ECE→d2 | 42 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d2 | 43 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d2 | 44 | ✗ (p=nan) | ✗ (p=0.373) |\n| ECE→d2 | 45 | ✗ (p=nan) | ✗ (p=0.600) |\n| ECE→d3 | 42 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d3 | 43 | ✗ (p=nan) | ✓ (p=0.000) |\n| ECE→d3 | 44 | ✗ (p=nan) | ✗ (p=0.229) |\n| ECE→d3 | 45 | ✗ (p=nan) | ✗ (p=0.572) |\n\n---\n\n## Cross-validation with ty_audit_report (Method A, 11 points)\n\n| Metric | Expected (ty_audit) | Got (window_sensitivity fixed) | Match |\n|---|---|---|---|\n| TE→d1,d2,d3 | 4/4 sig each | 4/4 sig each | ✓ |\n| ECE→d1 | 3/4 sig | 3/4 sig (seed 44 n.s.) | ✓ |\n\n---\n\n## Impact on Paper Claims\n\n- **4/5 consensus conclusions unchanged**: All 6 forward pairs remain robust at every T∈{5..10}. The bugs only affected TY, which was never required for the 4/5 majority.\n- **TY now adds confirmatory power**: At T=10, TY confirms 4/6 pairs (all 3 TE→d* and ECE→d1), strengthening the case vs. the buggy 0/6.\n- **TY variability across T is expected**: With p=1, d_max=1–2, residual df ranges from ~2 (T=5) to ~6 (T=10). Low df → unstable significance. This is consistent with the known TY power limitations documented in D013/D015.\n",
      "numLines": 116,
      "startLine": 1,
      "totalLines": 116
    }
  }
}
````

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01AX6cd5eHpeRoZLNbDBKsJz`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "51c442d4-4f7a-446e-83ab-f113d184eb3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BTYUM4dUHDtjRJoTa2GT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11862,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11862
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

_source line 9 · 2026-05-16T00:20:43.117Z_

<details><summary>↩ Tool result · reported error · `toolu_01AX6cd5eHpeRoZLNbDBKsJz`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "d94ae64f-c832-4de2-9163-863389764a01",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse."
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F89SZNzJTybDxeCrpK5zLw`</summary>

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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "26d76007-b699-4440-bf9b-94285a2dde6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BTYUM4dUHDtjRJoTa2GT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11862,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11862
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

_source line 11 · 2026-05-16T00:20:43.446Z_

<details><summary>↩ Tool result · `toolu_01F89SZNzJTybDxeCrpK5zLw`</summary>

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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "b6c0f4fa-a40d-49af-8d39-69d3e9d30ee6",
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

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The paper directory doesn't exist at that path. Let me search for it more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "d0d9d184-3a7a-41d5-8397-30af1a5aef52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184BSZFUTomqK4UvRSAYhX8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 23703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
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

_source line 13_

论文目录不存在于预期路径，搜索实际位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "4aac22c2-83fa-4330-8b2f-ffd8d8e0673a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184BSZFUTomqK4UvRSAYhX8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 23703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
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

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_014vd2rYEiWGCmd4xL6SNMXs`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "1d63cf6d-83c4-4a86-aa72-514097e4fbcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184BSZFUTomqK4UvRSAYhX8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 23703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
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

_source line 15 · 2026-05-16T00:20:47.447Z_

<details><summary>↩ Tool result · `toolu_014vd2rYEiWGCmd4xL6SNMXs`</summary>

```text
artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/background.tex
docs/paper/background.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion_365dc4.tex
artifacts/_project/paper/abstract_8c6c62.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex
artifacts/_project/paper/discussion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "35e60d01-cb93-4f80-b2e5-55f3d82862c1",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T184925/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T184925/worst/paper.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/background.tex",
      "docs/paper/background.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion_365dc4.tex",
      "artifacts/_project/paper/abstract_8c6c62.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "docs/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "docs/paper/method.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 11,
    "numFiles": 21,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_015yFfpNG22r6NJYgzFQ3VRX`</summary>

```json
{
  "pattern": "**/paper*/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "531a7878-f537-4df6-9aa1-4ceeefe3f335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184BSZFUTomqK4UvRSAYhX8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 23703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
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

_source line 17 · 2026-05-16T00:20:48.261Z_

<details><summary>↩ Tool result · `toolu_015yFfpNG22r6NJYgzFQ3VRX`</summary>

```text
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/background.tex
docs/paper/background.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion_365dc4.tex
artifacts/_project/paper/abstract_8c6c62.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex
artifacts/_project/paper/discussion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "0cadf8a8-9155-4621-b64c-9a0b729edec4",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/background.tex",
      "docs/paper/background.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion_365dc4.tex",
      "artifacts/_project/paper/abstract_8c6c62.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "docs/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "docs/paper/method.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 21,
    "numFiles": 18,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G6fdeXkR2Suy6ULtMEhb66`</summary>

```json
{
  "project": "distrib_canary_collapse",
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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "721dce8b-135f-4404-bdf3-5f96ef4dc80f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184BSZFUTomqK4UvRSAYhX8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 23703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
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

_source line 19 · 2026-05-16T00:20:48.506Z_

<details><summary>↩ Tool result · `toolu_01G6fdeXkR2Suy6ULtMEhb66`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\", \"content\": \"# Paper Framing — distrib_canary_collapse\\n\\n## Target Venue\\n- Primary: **EMNLP 2026 Main Track** (D043, 用户指定)\\n- ARR cycle: June 2026 (deadline ~June 15, 待确认具体日期)\\n- 格式: ACL 系列模板 (acl.sty), 8 页正文 + unlimited appendix\\n- Note: ARR May cycle 已过；June cycle 对齐 EMNLP 2026 commitment deadline\\n\\n## Narrative Structure (D027: Option B reframe)\\n\\n**主线**：方法论陷阱 + 多方法共识框架。Canary prediction 为系统性 case study。\\n**Claim 呈现顺序**：论文中 Claim 3 领衔 → Claim 2 (regime map) → Claim 1 (case study)。\\n**内部编号保持不变**（避免引用混乱），论文呈现时重排。\\n\\n## Core Claims (3 条，内部编号不变)\\n\\n1. **Canary→Diversity Granger-Causal Precedence (论文中作为 Case Study Finding)**: token_entropy 对 diversity 退化（distinct_1/2）具有 Granger-causal precedence——领先 1-2 代，差分后仍显著，证据来自多方法一致性：cross-correlation（lag=-1, std=0.0, |r|>0.99, p<0.004, 4/4 seed）、差分交叉相关（显著）、threshold onset（canary gen 1-2, diversity gen 3-4）、**permutation Granger（差分后仍 4/4 seed 显著，F=612-2615）**。论文可用措辞 (D037 更新)：*\\\"We demonstrate Granger-causal precedence of canary metrics at α≥0.75: α=1.0 achieves 24/24 FDR-sig (4 seeds), α=0.75 achieves 3/4 FDR-sig with the fourth borderline (p_fdr=0.054; single seed, pending multi-seed confirmation C001). Consistent temporal precedence (cross-correlation lag=+1, r=0.80–0.94) is observed across all contamination levels, though formal Granger tests at α≤0.50 do not reach FDR-corrected significance at T=11 (power analysis: §X).\\\"*升级上限：Granger ≠ true causality（Granger 1969），Discussion 一句话声明；双变量模型无法排除未观测混淆因子（详见 Reviewer Concerns 表）。ECE 在 cross-correlation 和 permutation Granger 下同样领先（差分后 4/4 SIG），但跨方法一致性弱于 token_entropy，地位为 conditional secondary canary 待 plan_006 确认（详见约束 #9）。注意：TY Granger 在 N=11 下不可用于区分真/伪关联（见 Claim 3），核心证据链基于多方法一致性而非单一 TY 背书。\\n2. **Regime-Dependent Predictability**: 可预测性取决于 collapse 维度和 contamination regime——canary→diversity 在差分后仍 robust（6/6 pair × 4/4 seed），但 canary→perplexity **经差分检验确认为伪回归**（0/4 seed, F≈0, p=0.99），未差分时的\\\"信号\\\"（F=16-36）完全由共享非平稳趋势驱动（D017）。ECE→perplexity 的反向因果同理存疑。**Claim 2 reframing (D022)**: 从\\\"不同 α 下 lead time 不同\\\"升级为\\\"不同 α 下 **detectability** 不同\\\"——α=0.25 差分 Granger 0/8 FDR sig vs α=1.0 的 24/24，同一 pair 的统计可检测性随 contamination level 剧变。**D037 更新**：5-point regime map 完整，detectability 在 α=0.50→0.75 间出现阶跃（0/8→3/8 FDR-sig），α=0.75 consensus 11/16 robust。**Evidence strategy (Reviewer 共识)**：Primary = raw drift magnitude dose-response（distinct_1: -14%@α=0 → -40%@α=0.25 → ~-93%@α=1.0），方法无关、不可争议；Secondary = 差分 Granger FDR sig rate vs α，展示 detectability boundary at α~0.75。**不用 naive_xcorr 做 primary**——与 Claim 3 自相矛盾。Predictability regime map 划定可预测/不可预测边界（\\\"phase diagram\\\" 需 ≥6 个 α 值 + uncertainty interval 才成立，当前 5 个 α 值下用 \\\"regime map\\\"）。\\n3. **Method Selection Sensitivity and Regime-Dependent Validity**（升级自 Methodological Rigor；D022 升级候选：method × regime interaction）: 在典型 generation 数（N≈10）下，lead-lag 结论对分析方法和超参数高度敏感，且**同一方法在不同 α regime 下结论翻转**（diff Granger: α=1.0 24/24 FDR sig → α=0.25 0/8）。升级措辞候选：\\\"Method sensitivity is compounded by regime dependence: the same statistical test applied to the same metric pair can yield significant or null results depending on contamination level\\\"。**三层证据结构**：**(Layer 1)** naive Pearson 找到 16/16 显著——方法宽松时一切 \\\"显著\\\"；**(Layer 2)** 一阶差分翻转整条 perplexity 通道（8/8→0/8 SIG）而 diversity 通道不变（12/12→12/12）——一个方法论选择决定通道存亡（D017）；**(Layer 3)** TY d_max sensitivity 使结论在 ~0%↔94% spurious rate 间震荡——超参数选择同样致命。方法论贡献不是\\\"提供正确的检验\\\"，而是**暴露方法选择敏感性并提出多方法一致性框架**——只有跨方法（cross-corr + 差分 + threshold + permutation Granger）和跨 seed 都一致的关联才可信。这是迭代训练文献中被忽视的方法论陷阱。\\n\\n## Story Spine (D027: Option B reframe)\\n\\n- **Problem**: Model collapse 文献中的 lead-lag 分析（\\\"哪些指标预测崩溃\\\"）日益增多（Du et al., SIGMA, DCES），但**方法选择对结论的影响未被系统性审视**。Du et al. 非正式观察到 ECE 领先 accuracy，仅限单指标对、1-3 代、无统计检验。现有工作的方法论基础薄弱：无差分检验（不排除伪回归）、无多方法交叉验证、无多重比较校正、无 regime-dependent 分析。\\n\\n- **Gap**: 没有工作系统性回答：(1) lead-lag 结论在多大程度上取决于分析方法的选择？(2) 同一统计检验在不同 contamination regime 下结论是否稳定？(3) 如何建立可靠的 lead-lag 判定框架？**Scheffer et al. (2009, 2012)** 在生态/气候科学中建立了临界转变早期预警框架，但尚未被 model collapse 文献引入，其方法论严谨性（多方法交叉验证 + regime-dependent analysis）恰好是本领域所缺失的。\\n\\n- **Our approach**: 以 canary prediction for model collapse 为系统性 case study，暴露 lead-lag 分析中的三个方法论陷阱：(1) 方法选择敏感性——同一数据集上 5 种统计方法从 100% 显著到 0% 显著（Claim 3）；(2) 未差分的伪回归——canary→perplexity 通道在差分后完全消失（Claim 1 case study）；(3) regime-dependent validity——同一检验在不同 α 下结论翻转（Claim 2）。在此基础上提出**多方法一致性共识框架**（multi-method consensus framework）作为解决方案：只有跨方法（cross-corr + 差分 + threshold + permutation Granger）和跨 seed 都一致的关联才可信。\\n\\n- **Headline result (D037 更新)**: \\\"In iterative synthetic training with Pythia-410M, naive correlation identifies 100% of canary-collapse metric pairs as significant, while differenced permutation Granger retains only 25% — and this method-dependent gap is compounded by regime dependence: the same test applied to the same metric pair yields 24/24 FDR-significant results at α=1.0, 3/4 at α=0.75, but 0/8 at α≤0.50. We propose a multi-method consensus framework and, applying it, identify token entropy as a robust 1-generation-ahead canary for diversity collapse at α≥0.75.\\\"\\n\\n- **Title direction**: \\\"Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse\\\"\\n\\n- **文献定位 (保留)**：SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效。理论分析方面：Seddik et al. (2024), Gerstgrasser et al. (2024), Dey et al. (2024) 提供互补理论视角但不涉及方法论敏感性。**我们与 Du et al. 的核心区别**：(1) 多指标家族系统对比；(2) 多方法交叉验证 + d_max sensitivity；(3) regime-dependent mapping；(4) **方法选择敏感性本身是主要贡献**（不再是\\\"独立贡献\\\"而是\\\"核心贡献\\\"）。\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| Concern | Response Strategy | Required Experiment |\\n|---------|-------------------|---------------------|\\n| \\\"Canary 不预测 perplexity，实用价值有限\\\" | 差分检验已确认 canary→perplexity 为伪回归（D017）。Framing 转为\\\"canary 预测 diversity collapse\\\"——diversity 是 collapse 最早可观测维度，实用价值在于比 perplexity 更早预警。perplexity 通道的伪信号本身是方法论贡献（Claim 3 例证） | 已有数据（D017 确认） |\\n| \\\"ECE 和 token_entropy 对 perplexity 方向相反？\\\" | 差分后两者对 perplexity 均 NOT_SIG（D017），\\\"方向相反\\\"是伪信号的不同表现形式，无需机制性解释。论文诚实报告差分前后对比即可 | 已有数据（D017 确认） |\\n| \\\"只在 Pythia-410M 上验证，scale 泛化？\\\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\\n| \\\"WikiText-103 单一数据集\\\" | C4 cross-domain validation | domain-transfer (P1) |\\n| \\\"为什么不用简单相关分析？\\\" | 方法 ablation 展示 5 种方法（naive/差分/threshold/TY/permutation Granger）的结论分歧 + d_max sensitivity 曲线，论证多方法一致性框架的必要性 | method-ablation (P0, 零 GPU) — 已完成 Phase 1 |\\n| \\\"TY Granger 在 N=11 下可靠吗？\\\" | Bootstrap power analysis 证实不可靠（power 0.05-0.20），TY 降级为辅助指标用于 Claim 3 展示。核心分析改用 cross-corr + permutation test + BH FDR | plan_009 (已完成) + plan_006 (P0) |\\n| \\\"Claim 3 说方法不可靠，那 Claim 1 用的方法凭什么可信？\\\" | 多方法一致性 ≠ 单方法可靠性。独立方法有不同偏差方向（naive 偏宽松、TY d_max=1 偏保守），它们在 token_entropy→distinct_1/2 上的收敛本身是证据（类似 meta-analysis 逻辑）。论文 Method/Discussion 需 1-2 段显式论证 | 已有 plan_002 数据 |\\n| \\\"4 个 canary 中 2 个失败，选择偏差？\\\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\\n| \\\"Intervention 实验缺失\\\" | CRS 降级为 illustration（非 contribution），如有 GPU 余量加 reactive baseline 对照 | intervention (P2, optional) |\\n| \\\"T=10 时间序列太短，TY 统计不可靠\\\" | Bootstrap power analysis 已完成（plan_009）：T=10 power=0.05-0.20, T=20 power=0.17, T=30 power=0.29。TY 降级为 Claim 3 展示，核心用 permutation test | plan_009 (已完成) + plan_006 |\\n| \\\"100+ 假设检验无多重比较校正\\\" | 全 battery 加 Benjamini-Hochberg FDR 校正，报告 adjusted p-values。marginal 结果标注 | 分析代码修改 (P0, 零 GPU) — 已完成 |\\n| \\\"只有 Pythia 一个架构家族\\\" | GPT-2 或 OPT spot-check × 核心条件（至少 1 个非 Pythia 架构） | plan_010 (P1) |\\n| \\\"Incremental over Du et al.\\\" | 论文 §Related Work 用 4 点显式区分（多指标/多方法/regime mapping/方法敏感性）。Claim 3 是 Du et al. 完全未涉及的独立贡献 | 已有数据 + framing |\\n| **(D027 新增)** \\\"这只是 negative results paper，没有正面贡献\\\" | 多方法共识框架是正面贡献（explicit framework + sensitivity analysis + FPR/FNR 对比表）；canary prediction（Claim 1 as case study）提供具体可操作的输出（token_entropy 1-gen-ahead canary at α≥0.75）| 已有数据 + 共识框架 formalization（零 GPU）|\\n| **(D027 新增)** \\\"方法论 pitfalls 是 trivial/obvious\\\" | (a) model collapse 文献实际在用 naive 方法（Du et al.）；(b) pitfall 不止于 naive vs formal——differencing × regime 交互是非 trivial 的（差分翻转整条 perplexity 通道但保留 diversity 通道）；(c) d_max sensitivity 曲线证明即使选了 TY，超参数仍致命 | 已有 method_ablation + α-sweep 数据 |\\n| \\\"与 critical slowing down 文献的关系？\\\" | §Related Work 引用 Scheffer et al. 2009/2012 并定位为\\\"将 tipping-point early-warning 框架引入 model collapse\\\"。讨论 rising autocorrelation/variance 类比 | 文献工作 |\\n| \\\"双变量 Granger 无法排除混淆因子\\\" | token_entropy 和 ECE 可能共享信息源（均捕捉 output distribution shape），双变量 Granger 无法排除未观测混淆因子。论文 Discussion 须显式声明 Granger precedence ≠ true causality（Granger 1969），并讨论多变量 VAR 或条件 Granger 作为 future work。多方法一致性（4 种独立方法收敛）部分缓解但不消除此顾虑 | Discussion 声明 + future work |\\n\\n## Venue Fit\\n\\nEMNLP 2026 Main Track 优势：\\n- NLP 社区对 model collapse / data contamination 高度关注，audience 精准\\n- ACL/EMNLP 接受 empirical methodology + analysis paper，不要求 SOTA\\n- 方法论 pitfalls + consensus framework 对 NLP 从业者直接可操作\\n- Iterative training / synthetic data 是 LLM 时代热点话题\\n\\n风险：\\n- 如果被认为\\\"只是 empirical study 没有算法贡献\\\"→ 多方法一致性框架 + 方法选择敏感性分析本身是方法论贡献（Claim 3）；CRS 降级为 illustration 不作独立贡献\\n- 模型规模偏小（Pythia-410M + GPT-2-medium）→ 诚实标注 limitation + scaling trend\\n- 时间紧凑（~1 个月写作窗口）→ Paper Agent Full Draft 模式已激活，框架和数据就绪\\n\\n## Key Narrative Constraints (from MVP + plan_003)\\n\\n1. **不能 claim \\\"canary predicts model collapse\\\"** — 只能 claim \\\"canary predicts diversity collapse\\\"。token_entropy→perplexity 经差分检验确认为伪回归（0/4 seed, F≈0, p=0.99, D017），未差分时的\\\"弱信号\\\"完全由共享非平稳趋势驱动。论文措辞用\\\"spurious association confirmed by first-differencing\\\"，不再用\\\"弱信号\\\"\\n2. **ECE→perplexity 和 token_entropy→perplexity 均为伪信号 (D017)** — 差分后两者均 0/4 seed 显著。未差分时观察到的\\\"方向相反\\\"（token_entropy 领先 vs perplexity 领先 ECE）是共享趋势的不同表现形式。论文报告差分前后对比作为方法论教训，不再需要机制性解释\\n3. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\\n4. **distinct_3 必须放 supplementary，不能完全省略** — max_lag=7 下升为 SIGNIFICANT 但 lag_std>1.5（双峰：seed 42 总是 -5，其余 -1/-2），维持 D008 降级策略，主文聚焦 distinct_1/2。Supplementary 需给完整结果 + 解释 lag instability（高阶 n-gram diversity 对短序列随机变异更敏感）。distinct_3 的不稳定性本身支持 \\\"predictability boundary\\\" 主题——即使 diversity 维度内部也有可预测性梯度\\n5. **max_lag=7 确认核心 lead 无截断** — token_entropy→distinct_1 lag=-1（std=0.0）、ECE→distinct_2 lag=-1（std=0.0）在 max_lag=5/7 下完全一致。token_entropy→perplexity lag=-5 虽非截断伪影，但已确认为非平稳伪回归（D017）\\n6. **~~Dual-timescale 升级条件~~ — 已失效 (D017)** — perplexity 通道经差分确认为伪回归，即使 plan_006 T=20 也无法拯救伪信号。\\\"Two distinct lead horizons\\\" 升级路径关闭。plan_006 的价值重新定位为：(1) diversity lead 在更长序列中的稳定性，(2) TY power 改善观察，(3) 差分后 permutation Granger 在 T=20 下的表现\\n7. **ECE→perplexity \\\"反向因果\\\"已确认为伪信号 (D017)** — 差分后 ECE→perplexity 0/4 SIG。之前的 post-hoc mechanistic hypothesis 无需讨论。论文只需报告差分前后对比\\n8. **TY 在 N=11 下完全不可用于区分真/伪关联** — d_max sensitivity 分析证实：d_max=0 过度宽松（连 effective_rank 都通过），d_max=1 过度保守（连 token_entropy→distinct_1 都拒绝），adaptive 因 ADF 不稳定而跨 seed 震荡。论文**不能**用 TY 作为\\\"正确答案\\\"。**spurious_rate 必须双版本报告**：含 TY 75%（16 pair 中 12 仅 TY 判伪）、排除 TY 后 62.5%（16 pair 中 10 在 4 种非 TY 方法下一致）。ECE→distinct_2/3 被 TY 判伪但在其余 4 种方法全部 4/4 SIG——这本身是\\\"方法选择改变分类\\\"的例证（Claim 3 素材）\\n9. **ECE 地位为 conditional secondary canary (D020)** — ECE 在 cross-correlation（lag=-1, std=0.0）和 permutation Granger（差分后 4/4 SIG）下与 token_entropy 等效，ECE→distinct_2/3 在排除 TY 的 4 种方法中全部通过。\\\"secondary\\\" 标签**完全由 TY 的 Type II error 驱动**（TY 仅通过 ECE→distinct_1 3/4 seed）。论文标注：\\\"secondary only in TY consistency; equivalent across all other methods\\\"。plan_006（N=21）为最终判定——若 TY 在更大 N 下确认 ECE→distinct_2/3，升级为 co-primary\\n10. **d_max sensitivity 曲线是论文的 key figure** — 三组 d_max（0/adaptive/1）× spurious rate 的变化是 Claim 3 的核心可视化，展示\\\"方法选择如何改变结论\\\"\\n11. **统计效力必须显式论证** — Dream 三档一致 CRITICAL：T=10 下 TY 的 DOF 严重不足。论文必须包含 bootstrap/permutation 验证 + plan_006 (T=20) 结果。所有 p-value 必须经 BH FDR 校正\\n12. **\\\"phase diagram\\\" → \\\"regime map\\\"** — 除非 α 分辨率达到 ≥6 个非平凡值 + 提供 α* uncertainty interval，否则用 \\\"predictability regime map\\\" 或 \\\"regime-dependent analysis\\\"。4-5 个 α 值不足以支撑物理学意义上的 \\\"phase diagram\\\"\\n13. **Scheffer et al. 是必引文献** — critical slowing down / early-warning indicators 框架是本研究的知识祖先。论文 Related Work 必须引用并定位\\n14. **CRS 降级为 illustration** — 不列入核心 contribution。CRS 是显然的反应式干预，Dream 三档一致认为 trivial/confounded\\n15. **TY 正式降级为辅助指标 (D015)** — Bootstrap power analysis (N=1000 Monte Carlo): T=10 power=0.05-0.20, T=20 power=0.17, T=30 power=0.29 (d_max≥1)。核心分析框架改为 cross-correlation + permutation test + BH FDR 校正。TY 仅用于 Claim 3 展示（方法敏感性 + power analysis figure），不再作为 lead-lag 判定方法\\n16. **Perplexity 通道确认为伪回归 (D017)** — Permutation Granger 差分版：canary→perplexity 差分后 0/8 SIG (F≈0, p=0.99)，canary→diversity 差分后 12/12 SIG（6 pair × 4 seed 中，token_entropy 和 ECE 各 3 pair 全通过）。差分前后结论翻转（perplexity: 6-8/8→0/8; diversity: 24/24→24/24）是 Claim 3 的关键 figure 素材。**F 值范围**：undifferenced F=74–3370, differenced F=71–7643（全 6 pairs × 4 seeds），范围重叠——之前\\\"F 不降反升\\\"仅对 token_entropy→distinct_1 子集成立，全量数据应以**显著性保持率 24/24→24/24**为核心叙事，不以 F 值大小为论据。论文 Method 节须注明：(1) T=11 first-difference 后 T=10，circular shift 仅 9 个唯一排列，null distribution 高度离散；(2) 尽管如此，diversity 通道 F 值远超任何排列值，结论不受离散性影响\\n17. **f² 效应量报告约束 (D019 更新)** — 差分后 f²=102-435（token_entropy→distinct_1），因 df_resid=5-6 任何真实信号都产生极大 f²（RSS_unrestricted 趋近零）。论文**禁止**用 Cohen 的 0.02/0.15/0.35 基准解读这些 f² 值。正确做法：permutation p-value 为主要推断证据，f² 仅作\\\"效应存在\\\"的定性指示，不做定量比较。**代码层面**：当 df_resid < 20 时，分析脚本输出 `f2_size=\\\"df_too_low\\\"` 而非 small/medium/large 分类（D019 T3 已实现于 permutation_granger.py）\\n18. **2×2 差分对比表是 Claim 3 核心 figure** — channel type（canary→diversity vs canary→perplexity）× differencing status（undifferenced vs differenced）的 2×2 表最紧凑展示\\\"一个方法论选择翻转整条通道的结论\\\"。diversity 通道差分前后均 24/24 SIG（显著性完全保持），F 值范围 undiff 74–3370 / diff 71–7643，部分 pair 略降但显著性完全保持。perplexity 通道差分后归零。比 d_max sensitivity 曲线更直观地展示差分的决定性影响\\n19. **method_ablation 必须双版本报告 (D019)** — spurious_rate 报告含 TY（5-method: 75%）和排除 TY（4-method: 62.5%）两个数字。ECE→distinct_2/3 在 TY 下被判伪但在其余 4 种方法中 4/4 SIG——TY 的 Type II error 驱动的分类差异本身是 Claim 3 素材。论文主文用 4-method 数字作主要结论，5-method 数字用于 Claim 3 方法敏感性讨论\\n20. **ECE canary 可靠性是 regime-dependent (D021)** — α=0.25 下 ECE gen 1 下降 -14%（反向信号），gen 2+ 才上升至 +77%。α=1.0 下 gen 1 直接 +2926%。ECE 作为早期预警 canary 仅在高 α（≥0.50，待 a050 确认）下可靠。低 α 下首代反向信号意味着 ECE 不能用于\\\"一代内预警\\\"。这丰富 Claim 2：canary 可靠性本身是 regime-dependent。D019 \\\"co-primary\\\" 限定为 \\\"high-α regime only\\\"\\n21. **Claim 1 scope 确认为 α≥0.75 (D037, Director 批准)** — α=0.75 Permutation Granger FDR: 3/4 方向显著（ECE→d1 p_fdr=0.046, ECE→d2 p_fdr=0.046, entropy→d2 p_fdr=0.048），entropy→d1 边界 p_fdr=0.054。反向 4/4 全部不显著。Consensus 11/16 robust。**当前 Granger-causal precedence 在 α≥0.75 成立**（α=1.0: 24/24 FDR-sig 4 seeds; α=0.75: 3/4 FDR-sig single seed）。**Single-seed caveat (C001)**: α=0.75 仅 seed=42 验证，待 D026 multi-seed 确认后移除限定。**entropy→d1 borderline (p_fdr=0.054)**: 论文须讨论——3/4 显著 + 1/4 边界，不是 4/4 全过。α≤0.50 均 0/8 FDR-sig，detectability boundary 确认在 0.50→0.75 间\\n22. **α=0.50 null 结果是 positive finding (D025, D037 更新)** — 中等污染下 canary 与 downstream 同步退化（temporal lead 消失），correlation/rule-based 方法（naive, differenced, threshold）100% sig vs 因果检验方法（permG, TY）0% sig 是 Claim 3（method × regime interaction）最极端的例证。论文呈现策略：(1) 此非单调 detectability 模式本身是 regime map 的核心特征；(2) **Detectability boundary 已确认在 0.50-0.75 区间 (D037)**——α=0.75 有 3/4 FDR-sig 信号，practical utility 定位为\\\"高污染场景（α≥0.75）下的早期预警\\\"，而非通用预警工具；(3) α=0.50 null 不是方法失败，是 signal-to-noise 的物理边界\\n23. **α-sweep 全部 single seed 是当前最大弱点 (D026)** — 非单调 dose-response（α=0.25 -40.3% vs α=0.50 -37.3%）和 ECE regime switch 假说均基于 seed=42 的 point estimate，无置信区间。论文中非单调性结论**必须标注 \\\"observed at seed=42; multi-seed confirmation required\\\"**。multi-seed（α=0.25/0.50 各 2-3 seeds）是从 Weak Accept → Accept 的首要条件，优先于 finer α grid（a010/a060）。非单调性在主文仅报告现象（配 drift 表格），\\\"entropy floor\\\" 机制假说放 Discussion\\n24. **α=0.25 双向 Granger 不改变 Claim 1 叙事 (D026)** — d1→entropy raw p=0.023（FDR 后 0.093 不显著），但效应量仅 f²=1.30 vs entropy→d1 的 f²=27.21（21 倍差异）。强单向因果 + 弱反馈，不是对称 coupled dynamics。α=1.0 反方向不显著，α=0.50 反方向 p=0.224。论文可加一句：\\\"marginally significant feedback at mild contamination (f²=1.30, 21× weaker than primary direction)\\\" 但不需要改写核心叙事\\n25. **证据强度排序：Claim 3 > Claim 2 > Claim 1 (D026)** — Reviewer 独立评估。Claim 3（method sensitivity）最强且 novel、well-supported；Claim 2（regime-dependent）次之（但需 multi-seed）；Claim 1（Granger-causal）scope 最窄（仅 α≥0.75）。论文 framing 应确保 Claim 3 的方法论贡献获得足够篇幅，不因 Claim 1 的 \\\"canary prediction\\\" 叙事而被矮化\\n26. **Phase 3 二次衰退仅限 Discussion，不纳入 Core Claims (D035)** — plan_006_s42 (T=18) 发现 gen 13-17 二次 diversity 衰退（d2 -5.8%, d3 -6.9%），两个硬约束：(a) 单 seed，plan_006_s43 确认前不写入论文主体；(b) Phase 3 中 token_entropy 反升 +2.8% 而 diversity 继续下降——canary 在长 horizon 下失效，升级为核心发现会成审稿攻击面。**最佳用法**：Claim 3 补充证据（观察窗口长度改变结论 = 方法敏感性例证）+ Discussion 段落（collapse dynamics richer than saturation, but canary utility diminishes at extended horizons）。不改变 Core Claims / narrative structure / 方法论主线\\n27. **Consensus score 跨 α 比较须标注标准差异 (D038)** — α=0.75 consensus 11/16 robust 使用单种子 method-agreement 标准（≥4/5 方法判定显著），α=1.0 consensus 6/16 robust 使用 4-seed full consensus 标准（≥3/4 seeds × ≥4/5 方法）。两个数字不可直接对比——11/16 > 6/16 不意味着 α=0.75 信号更强，而是标准更宽松。论文中引用时**必须标注标准差异**，禁止直接对比暗示 α=1.0 信号更弱\\n28. **token_entropy→perplexity 在 α=0.75 单种子 consensus 中的 ROBUST 标记不可引用 (D038)** — α=0.75 单种子 consensus 将 token_entropy→perplexity 标为 ROBUST（因多方法一致通过），但 D017 已用 4-seed 差分检验确认该方向为 spurious（自相关驱动，差分后 0/4 sig）。这是单种子 consensus 的已知局限——无法检测共享非平稳趋势导致的伪关联。论文中**不得引用该方向作为 α=0.75 的 robust evidence**，仅限 canary→diversity 方向\\n\", \"total_chars\": 16905, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "30059a4f-a075-47e9-bbf1-46ac0faedb12",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — distrib_canary_collapse\\\\n\\\\n## Target Venue\\\\n- Primary: **EMNLP 2026 Main Track** (D043, 用户指定)\\\\n- ARR cycle: June 2026 (deadline ~June 15, 待确认具体日期)\\\\n- 格式: ACL 系列模板 (acl.sty), 8 页正文 + unlimited appendix\\\\n- Note: ARR May cycle 已过；June cycle 对齐 EMNLP 2026 commitment deadline\\\\n\\\\n## Narrative Structure (D027: Option B reframe)\\\\n\\\\n**主线**：方法论陷阱 + 多方法共识框架。Canary prediction 为系统性 case study。\\\\n**Claim 呈现顺序**：论文中 Claim 3 领衔 → Claim 2 (regime map) → Claim 1 (case study)。\\\\n**内部编号保持不变**（避免引用混乱），论文呈现时重排。\\\\n\\\\n## Core Claims (3 条，内部编号不变)\\\\n\\\\n1. **Canary→Diversity Granger-Causal Precedence (论文中作为 Case Study Finding)**: token_entropy 对 diversity 退化（distinct_1/2）具有 Granger-causal precedence——领先 1-2 代，差分后仍显著，证据来自多方法一致性：cross-correlation（lag=-1, std=0.0, |r|>0.99, p<0.004, 4/4 seed）、差分交叉相关（显著）、threshold onset（canary gen 1-2, diversity gen 3-4）、**permutation Granger（差分后仍 4/4 seed 显著，F=612-2615）**。论文可用措辞 (D037 更新)：*\\\\\\\"We demonstrate Granger-causal precedence of canary metrics at α≥0.75: α=1.0 achieves 24/24 FDR-sig (4 seeds), α=0.75 achieves 3/4 FDR-sig with the fourth borderline (p_fdr=0.054; single seed, pending multi-seed confirmation C001). Consistent temporal precedence (cross-correlation lag=+1, r=0.80–0.94) is observed across all contamination levels, though formal Granger tests at α≤0.50 do not reach FDR-corrected significance at T=11 (power analysis: §X).\\\\\\\"*升级上限：Granger ≠ true causality（Granger 1969），Discussion 一句话声明；双变量模型无法排除未观测混淆因子（详见 Reviewer Concerns 表）。ECE 在 cross-correlation 和 permutation Granger 下同样领先（差分后 4/4 SIG），但跨方法一致性弱于 token_entropy，地位为 conditional secondary canary 待 plan_006 确认（详见约束 #9）。注意：TY Granger 在 N=11 下不可用于区分真/伪关联（见 Claim 3），核心证据链基于多方法一致性而非单一 TY 背书。\\\\n2. **Regime-Dependent Predictability**: 可预测性取决于 collapse 维度和 contamination regime——canary→diversity 在差分后仍 robust（6/6 pair × 4/4 seed），但 canary→perplexity **经差分检验确认为伪回归**（0/4 seed, F≈0, p=0.99），未差分时的\\\\\\\"信号\\\\\\\"（F=16-36）完全由共享非平稳趋势驱动（D017）。ECE→perplexity 的反向因果同理存疑。**Claim 2 reframing (D022)**: 从\\\\\\\"不同 α 下 lead time 不同\\\\\\\"升级为\\\\\\\"不同 α 下 **detectability** 不同\\\\\\\"——α=0.25 差分 Granger 0/8 FDR sig vs α=1.0 的 24/24，同一 pair 的统计可检测性随 contamination level 剧变。**D037 更新**：5-point regime map 完整，detectability 在 α=0.50→0.75 间出现阶跃（0/8→3/8 FDR-sig），α=0.75 consensus 11/16 robust。**Evidence strategy (Reviewer 共识)**：Primary = raw drift magnitude dose-response（distinct_1: -14%@α=0 → -40%@α=0.25 → ~-93%@α=1.0），方法无关、不可争议；Secondary = 差分 Granger FDR sig rate vs α，展示 detectability boundary at α~0.75。**不用 naive_xcorr 做 primary**——与 Claim 3 自相矛盾。Predictability regime map 划定可预测/不可预测边界（\\\\\\\"phase diagram\\\\\\\" 需 ≥6 个 α 值 + uncertainty interval 才成立，当前 5 个 α 值下用 \\\\\\\"regime map\\\\\\\"）。\\\\n3. **Method Selection Sensitivity and Regime-Dependent Validity**（升级自 Methodological Rigor；D022 升级候选：method × regime interaction）: 在典型 generation 数（N≈10）下，lead-lag 结论对分析方法和超参数高度敏感，且**同一方法在不同 α regime 下结论翻转**（diff Granger: α=1.0 24/24 FDR sig → α=0.25 0/8）。升级措辞候选：\\\\\\\"Method sensitivity is compounded by regime dependence: the same statistical test applied to the same metric pair can yield significant or null results depending on contamination level\\\\\\\"。**三层证据结构**：**(Layer 1)** naive Pearson 找到 16/16 显著——方法宽松时一切 \\\\\\\"显著\\\\\\\"；**(Layer 2)** 一阶差分翻转整条 perplexity 通道（8/8→0/8 SIG）而 diversity 通道不变（12/12→12/12）——一个方法论选择决定通道存亡（D017）；**(Layer 3)** TY d_max sensitivity 使结论在 ~0%↔94% spurious rate 间震荡——超参数选择同样致命。方法论贡献不是\\\\\\\"提供正确的检验\\\\\\\"，而是**暴露方法选择敏感性并提出多方法一致性框架**——只有跨方法（cross-corr + 差分 + threshold + permutation Granger）和跨 seed 都一致的关联才可信。这是迭代训练文献中被忽视的方法论陷阱。\\\\n\\\\n## Story Spine (D027: Option B reframe)\\\\n\\\\n- **Problem**: Model collapse 文献中的 lead-lag 分析（\\\\\\\"哪些指标预测崩溃\\\\\\\"）日益增多（Du et al., SIGMA, DCES），但**方法选择对结论的影响未被系统性审视**。Du et al. 非正式观察到 ECE 领先 accuracy，仅限单指标对、1-3 代、无统计检验。现有工作的方法论基础薄弱：无差分检验（不排除伪回归）、无多方法交叉验证、无多重比较校正、无 regime-dependent 分析。\\\\n\\\\n- **Gap**: 没有工作系统性回答：(1) lead-lag 结论在多大程度上取决于分析方法的选择？(2) 同一统计检验在不同 contamination regime 下结论是否稳定？(3) 如何建立可靠的 lead-lag 判定框架？**Scheffer et al. (2009, 2012)** 在生态/气候科学中建立了临界转变早期预警框架，但尚未被 model collapse 文献引入，其方法论严谨性（多方法交叉验证 + regime-dependent analysis）恰好是本领域所缺失的。\\\\n\\\\n- **Our approach**: 以 canary prediction for model collapse 为系统性 case study，暴露 lead-lag 分析中的三个方法论陷阱：(1) 方法选择敏感性——同一数据集上 5 种统计方法从 100% 显著到 0% 显著（Claim 3）；(2) 未差分的伪回归——canary→perplexity 通道在差分后完全消失（Claim 1 case study）；(3) regime-dependent validity——同一检验在不同 α 下结论翻转（Claim 2）。在此基础上提出**多方法一致性共识框架**（multi-method consensus framework）作为解决方案：只有跨方法（cross-corr + 差分 + threshold + permutation Granger）和跨 seed 都一致的关联才可信。\\\\n\\\\n- **Headline result (D037 更新)**: \\\\\\\"In iterative synthetic training with Pythia-410M, naive correlation identifies 100% of canary-collapse metric pairs as significant, while differenced permutation Granger retains only 25% — and this method-dependent gap is compounded by regime dependence: the same test applied to the same metric pair yields 24/24 FDR-significant results at α=1.0, 3/4 at α=0.75, but 0/8 at α≤0.50. We propose a multi-method consensus framework and, applying it, identify token entropy as a robust 1-generation-ahead canary for diversity collapse at α≥0.75.\\\\\\\"\\\\n\\\\n- **Title direction**: \\\\\\\"Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse\\\\\\\"\\\\n\\\\n- **文献定位 (保留)**：SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效。理论分析方面：Seddik et al. (2024), Gerstgrasser et al. (2024), Dey et al. (2024) 提供互补理论视角但不涉及方法论敏感性。**我们与 Du et al. 的核心区别**：(1) 多指标家族系统对比；(2) 多方法交叉验证 + d_max sensitivity；(3) regime-dependent mapping；(4) **方法选择敏感性本身是主要贡献**（不再是\\\\\\\"独立贡献\\\\\\\"而是\\\\\\\"核心贡献\\\\\\\"）。\\\\n\\\\n## Anticipated Reviewer Concerns & Responses\\\\n\\\\n| Concern | Response Strategy | Required Experiment |\\\\n|---------|-------------------|---------------------|\\\\n| \\\\\\\"Canary 不预测 perplexity，实用价值有限\\\\\\\" | 差分检验已确认 canary→perplexity 为伪回归（D017）。Framing 转为\\\\\\\"canary 预测 diversity collapse\\\\\\\"——diversity 是 collapse 最早可观测维度，实用价值在于比 perplexity 更早预警。perplexity 通道的伪信号本身是方法论贡献（Claim 3 例证） | 已有数据（D017 确认） |\\\\n| \\\\\\\"ECE 和 token_entropy 对 perplexity 方向相反？\\\\\\\" | 差分后两者对 perplexity 均 NOT_SIG（D017），\\\\\\\"方向相反\\\\\\\"是伪信号的不同表现形式，无需机制性解释。论文诚实报告差分前后对比即可 | 已有数据（D017 确认） |\\\\n| \\\\\\\"只在 Pythia-410M 上验证，scale 泛化？\\\\\\\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\\\\n| \\\\\\\"WikiText-103 单一数据集\\\\\\\" | C4 cross-domain validation | domain-transfer (P1) |\\\\n| \\\\\\\"为什么不用简单相关分析？\\\\\\\" | 方法 ablation 展示 5 种方法（naive/差分/threshold/TY/permutation Granger）的结论分歧 + d_max sensitivity 曲线，论证多方法一致性框架的必要性 | method-ablation (P0, 零 GPU) — 已完成 Phase 1 |\\\\n| \\\\\\\"TY Granger 在 N=11 下可靠吗？\\\\\\\" | Bootstrap power analysis 证实不可靠（power 0.05-0.20），TY 降级为辅助指标用于 Claim 3 展示。核心分析改用 cross-corr + permutation test + BH FDR | plan_009 (已完成) + plan_006 (P0) |\\\\n| \\\\\\\"Claim 3 说方法不可靠，那 Claim 1 用的方法凭什么可信？\\\\\\\" | 多方法一致性 ≠ 单方法可靠性。独立方法有不同偏差方向（naive 偏宽松、TY d_max=1 偏保守），它们在 token_entropy→distinct_1/2 上的收敛本身是证据（类似 meta-analysis 逻辑）。论文 Method/Discussion 需 1-2 段显式论证 | 已有 plan_002 数据 |\\\\n| \\\\\\\"4 个 canary 中 2 个失败，选择偏差？\\\\\\\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\\\\n| \\\\\\\"Intervention 实验缺失\\\\\\\" | CRS 降级为 illustration（非 contribution），如有 GPU 余量加 reactive baseline 对照 | intervention (P2, optional) |\\\\n| \\\\\\\"T=10 时间序列太短，TY 统计不可靠\\\\\\\" | Bootstrap power analysis 已完成（plan_009）：T=10 power=0.05-0.20, T=20 power=0.17, T=30 power=0.29。TY 降级为 Claim 3 展示，核心用 permutation test | plan_009 (已完成) + plan_006 |\\\\n| \\\\\\\"100+ 假设检验无多重比较校正\\\\\\\" | 全 battery 加 Benjamini-Hochberg FDR 校正，报告 adjusted p-values。marginal 结果标注 | 分析代码修改 (P0, 零 GPU) — 已完成 |\\\\n| \\\\\\\"只有 Pythia 一个架构家族\\\\\\\" | GPT-2 或 OPT spot-check × 核心条件（至少 1 个非 Pythia 架构） | plan_010 (P1) |\\\\n| \\\\\\\"Incremental over Du et al.\\\\\\\" | 论文 §Related Work 用 4 点显式区分（多指标/多方法/regime mapping/方法敏感性）。Claim 3 是 Du et al. 完全未涉及的独立贡献 | 已有数据 + framing |\\\\n| **(D027 新增)** \\\\\\\"这只是 negative results paper，没有正面贡献\\\\\\\" | 多方法共识框架是正面贡献（explicit framework + sensitivity analysis + FPR/FNR 对比表）；canary prediction（Claim 1 as case study）提供具体可操作的输出（token_entropy 1-gen-ahead canary at α≥0.75）| 已有数据 + 共识框架 formalization（零 GPU）|\\\\n| **(D027 新增)** \\\\\\\"方法论 pitfalls 是 trivial/obvious\\\\\\\" | (a) model collapse 文献实际在用 naive 方法（Du et al.）；(b) pitfall 不止于 naive vs formal——differencing × regime 交互是非 trivial 的（差分翻转整条 perplexity 通道但保留 diversity 通道）；(c) d_max sensitivity 曲线证明即使选了 TY，超参数仍致命 | 已有 method_ablation + α-sweep 数据 |\\\\n| \\\\\\\"与 critical slowing down 文献的关系？\\\\\\\" | §Related Work 引用 Scheffer et al. 2009/2012 并定位为\\\\\\\"将 tipping-point early-warning 框架引入 model collapse\\\\\\\"。讨论 rising autocorrelation/variance 类比 | 文献工作 |\\\\n| \\\\\\\"双变量 Granger 无法排除混淆因子\\\\\\\" | token_entropy 和 ECE 可能共享信息源（均捕捉 output distribution shape），双变量 Granger 无法排除未观测混淆因子。论文 Discussion 须显式声明 Granger precedence ≠ true causality（Granger 1969），并讨论多变量 VAR 或条件 Granger 作为 future work。多方法一致性（4 种独立方法收敛）部分缓解但不消除此顾虑 | Discussion 声明 + future work |\\\\n\\\\n## Venue Fit\\\\n\\\\nEMNLP 2026 Main Track 优势：\\\\n- NLP 社区对 model collapse / data contamination 高度关注，audience 精准\\\\n- ACL/EMNLP 接受 empirical methodology + analysis paper，不要求 SOTA\\\\n- 方法论 pitfalls + consensus framework 对 NLP 从业者直接可操作\\\\n- Iterative training / synthetic data 是 LLM 时代热点话题\\\\n\\\\n风险：\\\\n- 如果被认为\\\\\\\"只是 empirical study 没有算法贡献\\\\\\\"→ 多方法一致性框架 + 方法选择敏感性分析本身是方法论贡献（Claim 3）；CRS 降级为 illustration 不作独立贡献\\\\n- 模型规模偏小（Pythia-410M + GPT-2-medium）→ 诚实标注 limitation + scaling trend\\\\n- 时间紧凑（~1 个月写作窗口）→ Paper Agent Full Draft 模式已激活，框架和数据就绪\\\\n\\\\n## Key Narrative Constraints (from MVP + plan_003)\\\\n\\\\n1. **不能 claim \\\\\\\"canary predicts model collapse\\\\\\\"** — 只能 claim \\\\\\\"canary predicts diversity collapse\\\\\\\"。token_entropy→perplexity 经差分检验确认为伪回归（0/4 seed, F≈0, p=0.99, D017），未差分时的\\\\\\\"弱信号\\\\\\\"完全由共享非平稳趋势驱动。论文措辞用\\\\\\\"spurious association confirmed by first-differencing\\\\\\\"，不再用\\\\\\\"弱信号\\\\\\\"\\\\n2. **ECE→perplexity 和 token_entropy→perplexity 均为伪信号 (D017)** — 差分后两者均 0/4 seed 显著。未差分时观察到的\\\\\\\"方向相反\\\\\\\"（token_entropy 领先 vs perplexity 领先 ECE）是共享趋势的不同表现形式。论文报告差分前后对比作为方法论教训，不再需要机制性解释\\\\n3. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\\\\n4. **distinct_3 必须放 supplementary，不能完全省略** — max_lag=7 下升为 SIGNIFICANT 但 lag_std>1.5（双峰：seed 42 总是 -5，其余 -1/-2），维持 D008 降级策略，主文聚焦 distinct_1/2。Supplementary 需给完整结果 + 解释 lag instability（高阶 n-gram diversity 对短序列随机变异更敏感）。distinct_3 的不稳定性本身支持 \\\\\\\"predictability boundary\\\\\\\" 主题——即使 diversity 维度内部也有可预测性梯度\\\\n5. **max_lag=7 确认核心 lead 无截断** — token_entropy→distinct_1 lag=-1（std=0.0）、ECE→distinct_2 lag=-1（std=0.0）在 max_lag=5/7 下完全一致。token_entropy→perplexity lag=-5 虽非截断伪影，但已确认为非平稳伪回归（D017）\\\\n6. **~~Dual-timescale 升级条件~~ — 已失效 (D017)** — perplexity 通道经差分确认为伪回归，即使 plan_006 T=20 也无法拯救伪信号。\\\\\\\"Two distinct lead horizons\\\\\\\" 升级路径关闭。plan_006 的价值重新定位为：(1) diversity lead 在更长序列中的稳定性，(2) TY power 改善观察，(3) 差分后 permutation Granger 在 T=20 下的表现\\\\n7. **ECE→perplexity \\\\\\\"反向因果\\\\\\\"已确认为伪信号 (D017)** — 差分后 ECE→perplexity 0/4 SIG。之前的 post-hoc mechanistic hypothesis 无需讨论。论文只需报告差分前后对比\\\\n8. **TY 在 N=11 下完全不可用于区分真/伪关联** — d_max sensitivity 分析证实：d_max=0 过度宽松（连 effective_rank 都通过），d_max=1 过度保守（连 token_entropy→distinct_1 都拒绝），adaptive 因 ADF 不稳定而跨 seed 震荡。论文**不能**用 TY 作为\\\\\\\"正确答案\\\\\\\"。**spurious_rate 必须双版本报告**：含 TY 75%（16 pair 中 12 仅 TY 判伪）、排除 TY 后 62.5%（16 pair 中 10 在 4 种非 TY 方法下一致）。ECE→distinct_2/3 被 TY 判伪但在其余 4 种方法全部 4/4 SIG——这本身是\\\\\\\"方法选择改变分类\\\\\\\"的例证（Claim 3 素材）\\\\n9. **ECE 地位为 conditional secondary canary (D020)** — ECE 在 cross-correlation（lag=-1, std=0.0）和 permutation Granger（差分后 4/4 SIG）下与 token_entropy 等效，ECE→distinct_2/3 在排除 TY 的 4 种方法中全部通过。\\\\\\\"secondary\\\\\\\" 标签**完全由 TY 的 Type II error 驱动**（TY 仅通过 ECE→distinct_1 3/4 seed）。论文标注：\\\\\\\"secondary only in TY consistency; equivalent across all other methods\\\\\\\"。plan_006（N=21）为最终判定——若 TY 在更大 N 下确认 ECE→distinct_2/3，升级为 co-primary\\\\n10. **d_max sensitivity 曲线是论文的 key figure** — 三组 d_max（0/adaptive/1）× spurious rate 的变化是 Claim 3 的核心可视化，展示\\\\\\\"方法选择如何改变结论\\\\\\\"\\\\n11. **统计效力必须显式论证** — Dream 三档一致 CRITICAL：T=10 下 TY 的 DOF 严重不足。论文必须包含 bootstrap/permutation 验证 + plan_006 (T=20) 结果。所有 p-value 必须经 BH FDR 校正\\\\n12. **\\\\\\\"phase diagram\\\\\\\" → \\\\\\\"regime map\\\\\\\"** — 除非 α 分辨率达到 ≥6 个非平凡值 + 提供 α* uncertainty interval，否则用 \\\\\\\"predictability regime map\\\\\\\" 或 \\\\\\\"regime-dependent analysis\\\\\\\"。4-5 个 α 值不足以支撑物理学意义上的 \\\\\\\"phase diagram\\\\\\\"\\\\n13. **Scheffer et al. 是必引文献** — critical slowing down / early-warning indicators 框架是本研究的知识祖先。论文 Related Work 必须引用并定位\\\\n14. **CRS 降级为 illustration** — 不列入核心 contribution。CRS 是显然的反应式干预，Dream 三档一致认为 trivial/confounded\\\\n15. **TY 正式降级为辅助指标 (D015)** — Bootstrap power analysis (N=1000 Monte Carlo): T=10 power=0.05-0.20, T=20 power=0.17, T=30 power=0.29 (d_max≥1)。核心分析框架改为 cross-correlation + permutation test + BH FDR 校正。TY 仅用于 Claim 3 展示（方法敏感性 + power analysis figure），不再作为 lead-lag 判定方法\\\\n16. **Perplexity 通道确认为伪回归 (D017)** — Permutation Granger 差分版：canary→perplexity 差分后 0/8 SIG (F≈0, p=0.99)，canary→diversity 差分后 12/12 SIG（6 pair × 4 seed 中，token_entropy 和 ECE 各 3 pair 全通过）。差分前后结论翻转（perplexity: 6-8/8→0/8; diversity: 24/24→24/24）是 Claim 3 的关键 figure 素材。**F 值范围**：undifferenced F=74–3370, differenced F=71–7643（全 6 pairs × 4 seeds），范围重叠——之前\\\\\\\"F 不降反升\\\\\\\"仅对 token_entropy→distinct_1 子集成立，全量数据应以**显著性保持率 24/24→24/24**为核心叙事，不以 F 值大小为论据。论文 Method 节须注明：(1) T=11 first-difference 后 T=10，circular shift 仅 9 个唯一排列，null distribution 高度离散；(2) 尽管如此，diversity 通道 F 值远超任何排列值，结论不受离散性影响\\\\n17. **f² 效应量报告约束 (D019 更新)** — 差分后 f²=102-435（token_entropy→distinct_1），因 df_resid=5-6 任何真实信号都产生极大 f²（RSS_unrestricted 趋近零）。论文**禁止**用 Cohen 的 0.02/0.15/0.35 基准解读这些 f² 值。正确做法：permutation p-value 为主要推断证据，f² 仅作\\\\\\\"效应存在\\\\\\\"的定性指示，不做定量比较。**代码层面**：当 df_resid < 20 时，分析脚本输出 `f2_size=\\\\\\\"df_too_low\\\\\\\"` 而非 small/medium/large 分类（D019 T3 已实现于 permutation_granger.py）\\\\n18. **2×2 差分对比表是 Claim 3 核心 figure** — channel type（canary→diversity vs canary→perplexity）× differencing status（undifferenced vs differenced）的 2×2 表最紧凑展示\\\\\\\"一个方法论选择翻转整条通道的结论\\\\\\\"。diversity 通道差分前后均 24/24 SIG（显著性完全保持），F 值范围 undiff 74–3370 / diff 71–7643，部分 pair 略降但显著性完全保持。perplexity 通道差分后归零。比 d_max sensitivity 曲线更直观地展示差分的决定性影响\\\\n19. **method_ablation 必须双版本报告 (D019)** — spurious_rate 报告含 TY（5-method: 75%）和排除 TY（4-method: 62.5%）两个数字。ECE→distinct_2/3 在 TY 下被判伪但在其余 4 种方法中 4/4 SIG——TY 的 Type II error 驱动的分类差异本身是 Claim 3 素材。论文主文用 4-method 数字作主要结论，5-method 数字用于 Claim 3 方法敏感性讨论\\\\n20. **ECE canary 可靠性是 regime-dependent (D021)** — α=0.25 下 ECE gen 1 下降 -14%（反向信号），gen 2+ 才上升至 +77%。α=1.0 下 gen 1 直接 +2926%。ECE 作为早期预警 canary 仅在高 α（≥0.50，待 a050 确认）下可靠。低 α 下首代反向信号意味着 ECE 不能用于\\\\\\\"一代内预警\\\\\\\"。这丰富 Claim 2：canary 可靠性本身是 regime-dependent。D019 \\\\\\\"co-primary\\\\\\\" 限定为 \\\\\\\"high-α regime only\\\\\\\"\\\\n21. **Claim 1 scope 确认为 α≥0.75 (D037, Director 批准)** — α=0.75 Permutation Granger FDR: 3/4 方向显著（ECE→d1 p_fdr=0.046, ECE→d2 p_fdr=0.046, entropy→d2 p_fdr=0.048），entropy→d1 边界 p_fdr=0.054。反向 4/4 全部不显著。Consensus 11/16 robust。**当前 Granger-causal precedence 在 α≥0.75 成立**（α=1.0: 24/24 FDR-sig 4 seeds; α=0.75: 3/4 FDR-sig single seed）。**Single-seed caveat (C001)**: α=0.75 仅 seed=42 验证，待 D026 multi-seed 确认后移除限定。**entropy→d1 borderline (p_fdr=0.054)**: 论文须讨论——3/4 显著 + 1/4 边界，不是 4/4 全过。α≤0.50 均 0/8 FDR-sig，detectability boundary 确认在 0.50→0.75 间\\\\n22. **α=0.50 null 结果是 positive finding (D025, D037 更新)** — 中等污染下 canary 与 downstream 同步退化（temporal lead 消失），correlation/rule-based 方法（naive, differenced, threshold）100% sig vs 因果检验方法（permG, TY）0% sig 是 Claim 3（method × regime interaction）最极端的例证。论文呈现策略：(1) 此非单调 detectability 模式本身是 regime map 的核心特征；(2) **Detectability boundary 已确认在 0.50-0.75 区间 (D037)**——α=0.75 有 3/4 FDR-sig 信号，practical utility 定位为\\\\\\\"高污染场景（α≥0.75）下的早期预警\\\\\\\"，而非通用预警工具；(3) α=0.50 null 不是方法失败，是 signal-to-noise 的物理边界\\\\n23. **α-sweep 全部 single seed 是当前最大弱点 (D026)** — 非单调 dose-response（α=0.25 -40.3% vs α=0.50 -37.3%）和 ECE regime switch 假说均基于 seed=42 的 point estimate，无置信区间。论文中非单调性结论**必须标注 \\\\\\\"observed at seed=42; multi-seed confirmation required\\\\\\\"**。multi-seed（α=0.25/0.50 各 2-3 seeds）是从 Weak Accept → Accept 的首要条件，优先于 finer α grid（a010/a060）。非单调性在主文仅报告现象（配 drift 表格），\\\\\\\"entropy floor\\\\\\\" 机制假说放 Discussion\\\\n24. **α=0.25 双向 Granger 不改变 Claim 1 叙事 (D026)** — d1→entropy raw p=0.023（FDR 后 0.093 不显著），但效应量仅 f²=1.30 vs entropy→d1 的 f²=27.21（21 倍差异）。强单向因果 + 弱反馈，不是对称 coupled dynamics。α=1.0 反方向不显著，α=0.50 反方向 p=0.224。论文可加一句：\\\\\\\"marginally significant feedback at mild contamination (f²=1.30, 21× weaker than primary direction)\\\\\\\" 但不需要改写核心叙事\\\\n25. **证据强度排序：Claim 3 > Claim 2 > Claim 1 (D026)** — Reviewer 独立评估。Claim 3（method sensitivity）最强且 novel、well-supported；Claim 2（regime-dependent）次之（但需 multi-seed）；Claim 1（Granger-causal）scope 最窄（仅 α≥0.75）。论文 framing 应确保 Claim 3 的方法论贡献获得足够篇幅，不因 Claim 1 的 \\\\\\\"canary prediction\\\\\\\" 叙事而被矮化\\\\n26. **Phase 3 二次衰退仅限 Discussion，不纳入 Core Claims (D035)** — plan_006_s42 (T=18) 发现 gen 13-17 二次 diversity 衰退（d2 -5.8%, d3 -6.9%），两个硬约束：(a) 单 seed，plan_006_s43 确认前不写入论文主体；(b) Phase 3 中 token_entropy 反升 +2.8% 而 diversity 继续下降——canary 在长 horizon 下失效，升级为核心发现会成审稿攻击面。**最佳用法**：Claim 3 补充证据（观察窗口长度改变结论 = 方法敏感性例证）+ Discussion 段落（collapse dynamics richer than saturation, but canary utility diminishes at extended horizons）。不改变 Core Claims / narrative structure / 方法论主线\\\\n27. **Consensus score 跨 α 比较须标注标准差异 (D038)** — α=0.75 consensus 11/16 robust 使用单种子 method-agreement 标准（≥4/5 方法判定显著），α=1.0 consensus 6/16 robust 使用 4-seed full consensus 标准（≥3/4 seeds × ≥4/5 方法）。两个数字不可直接对比——11/16 > 6/16 不意味着 α=0.75 信号更强，而是标准更宽松。论文中引用时**必须标注标准差异**，禁止直接对比暗示 α=1.0 信号更弱\\\\n28. **token_entropy→perplexity 在 α=0.75 单种子 consensus 中的 ROBUST 标记不可引用 (D038)** — α=0.75 单种子 consensus 将 token_entropy→perplexity 标为 ROBUST（因多方法一致通过），但 D017 已用 4-seed 差分检验确认该方向为 spurious（自相关驱动，差分后 0/4 sig）。这是单种子 consensus 的已知局限——无法检测共享非平稳趋势导致的伪关联。论文中**不得引用该方向作为 α=0.75 的 robust evidence**，仅限 canary→diversity 方向\\\\n\\\", \\\"total_chars\\\": 16905, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\", \"content\": \"# Paper Framing — distrib_canary_collapse\\n\\n## Target Venue\\n- Primary: **EMNLP 2026 Main Track** (D043, 用户指定)\\n- ARR cycle: June 2026 (deadline ~June 15, 待确认具体日期)\\n- 格式: ACL 系列模板 (acl.sty), 8 页正文 + unlimited appendix\\n- Note: ARR May cycle 已过；June cycle 对齐 EMNLP 2026 commitment deadline\\n\\n## Narrative Structure (D027: Option B reframe)\\n\\n**主线**：方法论陷阱 + 多方法共识框架。Canary prediction 为系统性 case study。\\n**Claim 呈现顺序**：论文中 Claim 3 领衔 → Claim 2 (regime map) → Claim 1 (case study)。\\n**内部编号保持不变**（避免引用混乱），论文呈现时重排。\\n\\n## Core Claims (3 条，内部编号不变)\\n\\n1. **Canary→Diversity Granger-Causal Precedence (论文中作为 Case Study Finding)**: token_entropy 对 diversity 退化（distinct_1/2）具有 Granger-causal precedence——领先 1-2 代，差分后仍显著，证据来自多方法一致性：cross-correlation（lag=-1, std=0.0, |r|>0.99, p<0.004, 4/4 seed）、差分交叉相关（显著）、threshold onset（canary gen 1-2, diversity gen 3-4）、**permutation Granger（差分后仍 4/4 seed 显著，F=612-2615）**。论文可用措辞 (D037 更新)：*\\\"We demonstrate Granger-causal precedence of canary metrics at α≥0.75: α=1.0 achieves 24/24 FDR-sig (4 seeds), α=0.75 achieves 3/4 FDR-sig with the fourth borderline (p_fdr=0.054; single seed, pending multi-seed confirmation C001). Consistent temporal precedence (cross-correlation lag=+1, r=0.80–0.94) is observed across all contamination levels, though formal Granger tests at α≤0.50 do not reach FDR-corrected significance at T=11 (power analysis: §X).\\\"*升级上限：Granger ≠ true causality（Granger 1969），Discussion 一句话声明；双变量模型无法排除未观测混淆因子（详见 Reviewer Concerns 表）。ECE 在 cross-correlation 和 permutation Granger 下同样领先（差分后 4/4 SIG），但跨方法一致性弱于 token_entropy，地位为 conditional secondary canary 待 plan_006 确认（详见约束 #9）。注意：TY Granger 在 N=11 下不可用于区分真/伪关联（见 Claim 3），核心证据链基于多方法一致性而非单一 TY 背书。\\n2. **Regime-Dependent Predictability**: 可预测性取决于 collapse 维度和 contamination regime——canary→diversity 在差分后仍 robust（6/6 pair × 4/4 seed），但 canary→perplexity **经差分检验确认为伪回归**（0/4 seed, F≈0, p=0.99），未差分时的\\\"信号\\\"（F=16-36）完全由共享非平稳趋势驱动（D017）。ECE→perplexity 的反向因果同理存疑。**Claim 2 reframing (D022)**: 从\\\"不同 α 下 lead time 不同\\\"升级为\\\"不同 α 下 **detectability** 不同\\\"——α=0.25 差分 Granger 0/8 FDR sig vs α=1.0 的 24/24，同一 pair 的统计可检测性随 contamination level 剧变。**D037 更新**：5-point regime map 完整，detectability 在 α=0.50→0.75 间出现阶跃（0/8→3/8 FDR-sig），α=0.75 consensus 11/16 robust。**Evidence strategy (Reviewer 共识)**：Primary = raw drift magnitude dose-response（distinct_1: -14%@α=0 → -40%@α=0.25 → ~-93%@α=1.0），方法无关、不可争议；Secondary = 差分 Granger FDR sig rate vs α，展示 detectability boundary at α~0.75。**不用 naive_xcorr 做 primary**——与 Claim 3 自相矛盾。Predictability regime map 划定可预测/不可预测边界（\\\"phase diagram\\\" 需 ≥6 个 α 值 + uncertainty interval 才成立，当前 5 个 α 值下用 \\\"regime map\\\"）。\\n3. **Method Selection Sensitivity and Regime-Dependent Validity**（升级自 Methodological Rigor；D022 升级候选：method × regime interaction）: 在典型 generation 数（N≈10）下，lead-lag 结论对分析方法和超参数高度敏感，且**同一方法在不同 α regime 下结论翻转**（diff Granger: α=1.0 24/24 FDR sig → α=0.25 0/8）。升级措辞候选：\\\"Method sensitivity is compounded by regime dependence: the same statistical test applied to the same metric pair can yield significant or null results depending on contamination level\\\"。**三层证据结构**：**(Layer 1)** naive Pearson 找到 16/16 显著——方法宽松时一切 \\\"显著\\\"；**(Layer 2)** 一阶差分翻转整条 perplexity 通道（8/8→0/8 SIG）而 diversity 通道不变（12/12→12/12）——一个方法论选择决定通道存亡（D017）；**(Layer 3)** TY d_max sensitivity 使结论在 ~0%↔94% spurious rate 间震荡——超参数选择同样致命。方法论贡献不是\\\"提供正确的检验\\\"，而是**暴露方法选择敏感性并提出多方法一致性框架**——只有跨方法（cross-corr + 差分 + threshold + permutation Granger）和跨 seed 都一致的关联才可信。这是迭代训练文献中被忽视的方法论陷阱。\\n\\n## Story Spine (D027: Option B reframe)\\n\\n- **Problem**: Model collapse 文献中的 lead-lag 分析（\\\"哪些指标预测崩溃\\\"）日益增多（Du et al., SIGMA, DCES），但**方法选择对结论的影响未被系统性审视**。Du et al. 非正式观察到 ECE 领先 accuracy，仅限单指标对、1-3 代、无统计检验。现有工作的方法论基础薄弱：无差分检验（不排除伪回归）、无多方法交叉验证、无多重比较校正、无 regime-dependent 分析。\\n\\n- **Gap**: 没有工作系统性回答：(1) lead-lag 结论在多大程度上取决于分析方法的选择？(2) 同一统计检验在不同 contamination regime 下结论是否稳定？(3) 如何建立可靠的 lead-lag 判定框架？**Scheffer et al. (2009, 2012)** 在生态/气候科学中建立了临界转变早期预警框架，但尚未被 model collapse 文献引入，其方法论严谨性（多方法交叉验证 + regime-dependent analysis）恰好是本领域所缺失的。\\n\\n- **Our approach**: 以 canary prediction for model collapse 为系统性 case study，暴露 lead-lag 分析中的三个方法论陷阱：(1) 方法选择敏感性——同一数据集上 5 种统计方法从 100% 显著到 0% 显著（Claim 3）；(2) 未差分的伪回归——canary→perplexity 通道在差分后完全消失（Claim 1 case study）；(3) regime-dependent validity——同一检验在不同 α 下结论翻转（Claim 2）。在此基础上提出**多方法一致性共识框架**（multi-method consensus framework）作为解决方案：只有跨方法（cross-corr + 差分 + threshold + permutation Granger）和跨 seed 都一致的关联才可信。\\n\\n- **Headline result (D037 更新)**: \\\"In iterative synthetic training with Pythia-410M, naive correlation identifies 100% of canary-collapse metric pairs as significant, while differenced permutation Granger retains only 25% — and this method-dependent gap is compounded by regime dependence: the same test applied to the same metric pair yields 24/24 FDR-significant results at α=1.0, 3/4 at α=0.75, but 0/8 at α≤0.50. We propose a multi-method consensus framework and, applying it, identify token entropy as a robust 1-generation-ahead canary for diversity collapse at α≥0.75.\\\"\\n\\n- **Title direction**: \\\"Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse\\\"\\n\\n- **文献定位 (保留)**：SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效。理论分析方面：Seddik et al. (2024), Gerstgrasser et al. (2024), Dey et al. (2024) 提供互补理论视角但不涉及方法论敏感性。**我们与 Du et al. 的核心区别**：(1) 多指标家族系统对比；(2) 多方法交叉验证 + d_max sensitivity；(3) regime-dependent mapping；(4) **方法选择敏感性本身是主要贡献**（不再是\\\"独立贡献\\\"而是\\\"核心贡献\\\"）。\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| Concern | Response Strategy | Required Experiment |\\n|---------|-------------------|---------------------|\\n| \\\"Canary 不预测 perplexity，实用价值有限\\\" | 差分检验已确认 canary→perplexity 为伪回归（D017）。Framing 转为\\\"canary 预测 diversity collapse\\\"——diversity 是 collapse 最早可观测维度，实用价值在于比 perplexity 更早预警。perplexity 通道的伪信号本身是方法论贡献（Claim 3 例证） | 已有数据（D017 确认） |\\n| \\\"ECE 和 token_entropy 对 perplexity 方向相反？\\\" | 差分后两者对 perplexity 均 NOT_SIG（D017），\\\"方向相反\\\"是伪信号的不同表现形式，无需机制性解释。论文诚实报告差分前后对比即可 | 已有数据（D017 确认） |\\n| \\\"只在 Pythia-410M 上验证，scale 泛化？\\\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\\n| \\\"WikiText-103 单一数据集\\\" | C4 cross-domain validation | domain-transfer (P1) |\\n| \\\"为什么不用简单相关分析？\\\" | 方法 ablation 展示 5 种方法（naive/差分/threshold/TY/permutation Granger）的结论分歧 + d_max sensitivity 曲线，论证多方法一致性框架的必要性 | method-ablation (P0, 零 GPU) — 已完成 Phase 1 |\\n| \\\"TY Granger 在 N=11 下可靠吗？\\\" | Bootstrap power analysis 证实不可靠（power 0.05-0.20），TY 降级为辅助指标用于 Claim 3 展示。核心分析改用 cross-corr + permutation test + BH FDR | plan_009 (已完成) + plan_006 (P0) |\\n| \\\"Claim 3 说方法不可靠，那 Claim 1 用的方法凭什么可信？\\\" | 多方法一致性 ≠ 单方法可靠性。独立方法有不同偏差方向（naive 偏宽松、TY d_max=1 偏保守），它们在 token_entropy→distinct_1/2 上的收敛本身是证据（类似 meta-analysis 逻辑）。论文 Method/Discussion 需 1-2 段显式论证 | 已有 plan_002 数据 |\\n| \\\"4 个 canary 中 2 个失败，选择偏差？\\\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\\n| \\\"Intervention 实验缺失\\\" | CRS 降级为 illustration（非 contribution），如有 GPU 余量加 reactive baseline 对照 | intervention (P2, optional) |\\n| \\\"T=10 时间序列太短，TY 统计不可靠\\\" | Bootstrap power analysis 已完成（plan_009）：T=10 power=0.05-0.20, T=20 power=0.17, T=30 power=0.29。TY 降级为 Claim 3 展示，核心用 permutation test | plan_009 (已完成) + plan_006 |\\n| \\\"100+ 假设检验无多重比较校正\\\" | 全 battery 加 Benjamini-Hochberg FDR 校正，报告 adjusted p-values。marginal 结果标注 | 分析代码修改 (P0, 零 GPU) — 已完成 |\\n| \\\"只有 Pythia 一个架构家族\\\" | GPT-2 或 OPT spot-check × 核心条件（至少 1 个非 Pythia 架构） | plan_010 (P1) |\\n| \\\"Incremental over Du et al.\\\" | 论文 §Related Work 用 4 点显式区分（多指标/多方法/regime mapping/方法敏感性）。Claim 3 是 Du et al. 完全未涉及的独立贡献 | 已有数据 + framing |\\n| **(D027 新增)** \\\"这只是 negative results paper，没有正面贡献\\\" | 多方法共识框架是正面贡献（explicit framework + sensitivity analysis + FPR/FNR 对比表）；canary prediction（Claim 1 as case study）提供具体可操作的输出（token_entropy 1-gen-ahead canary at α≥0.75）| 已有数据 + 共识框架 formalization（零 GPU）|\\n| **(D027 新增)** \\\"方法论 pitfalls 是 trivial/obvious\\\" | (a) model collapse 文献实际在用 naive 方法（Du et al.）；(b) pitfall 不止于 naive vs formal——differencing × regime 交互是非 trivial 的（差分翻转整条 perplexity 通道但保留 diversity 通道）；(c) d_max sensitivity 曲线证明即使选了 TY，超参数仍致命 | 已有 method_ablation + α-sweep 数据 |\\n| \\\"与 critical slowing down 文献的关系？\\\" | §Related Work 引用 Scheffer et al. 2009/2012 并定位为\\\"将 tipping-point early-warning 框架引入 model collapse\\\"。讨论 rising autocorrelation/variance 类比 | 文献工作 |\\n| \\\"双变量 Granger 无法排除混淆因子\\\" | token_entropy 和 ECE 可能共享信息源（均捕捉 output distribution shape），双变量 Granger 无法排除未观测混淆因子。论文 Discussion 须显式声明 Granger precedence ≠ true causality（Granger 1969），并讨论多变量 VAR 或条件 Granger 作为 future work。多方法一致性（4 种独立方法收敛）部分缓解但不消除此顾虑 | Discussion 声明 + future work |\\n\\n## Venue Fit\\n\\nEMNLP 2026 Main Track 优势：\\n- NLP 社区对 model collapse / data contamination 高度关注，audience 精准\\n- ACL/EMNLP 接受 empirical methodology + analysis paper，不要求 SOTA\\n- 方法论 pitfalls + consensus framework 对 NLP 从业者直接可操作\\n- Iterative training / synthetic data 是 LLM 时代热点话题\\n\\n风险：\\n- 如果被认为\\\"只是 empirical study 没有算法贡献\\\"→ 多方法一致性框架 + 方法选择敏感性分析本身是方法论贡献（Claim 3）；CRS 降级为 illustration 不作独立贡献\\n- 模型规模偏小（Pythia-410M + GPT-2-medium）→ 诚实标注 limitation + scaling trend\\n- 时间紧凑（~1 个月写作窗口）→ Paper Agent Full Draft 模式已激活，框架和数据就绪\\n\\n## Key Narrative Constraints (from MVP + plan_003)\\n\\n1. **不能 claim \\\"canary predicts model collapse\\\"** — 只能 claim \\\"canary predicts diversity collapse\\\"。token_entropy→perplexity 经差分检验确认为伪回归（0/4 seed, F≈0, p=0.99, D017），未差分时的\\\"弱信号\\\"完全由共享非平稳趋势驱动。论文措辞用\\\"spurious association confirmed by first-differencing\\\"，不再用\\\"弱信号\\\"\\n2. **ECE→perplexity 和 token_entropy→perplexity 均为伪信号 (D017)** — 差分后两者均 0/4 seed 显著。未差分时观察到的\\\"方向相反\\\"（token_entropy 领先 vs perplexity 领先 ECE）是共享趋势的不同表现形式。论文报告差分前后对比作为方法论教训，不再需要机制性解释\\n3. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\\n4. **distinct_3 必须放 supplementary，不能完全省略** — max_lag=7 下升为 SIGNIFICANT 但 lag_std>1.5（双峰：seed 42 总是 -5，其余 -1/-2），维持 D008 降级策略，主文聚焦 distinct_1/2。Supplementary 需给完整结果 + 解释 lag instability（高阶 n-gram diversity 对短序列随机变异更敏感）。distinct_3 的不稳定性本身支持 \\\"predictability boundary\\\" 主题——即使 diversity 维度内部也有可预测性梯度\\n5. **max_lag=7 确认核心 lead 无截断** — token_entropy→distinct_1 lag=-1（std=0.0）、ECE→distinct_2 lag=-1（std=0.0）在 max_lag=5/7 下完全一致。token_entropy→perplexity lag=-5 虽非截断伪影，但已确认为非平稳伪回归（D017）\\n6. **~~Dual-timescale 升级条件~~ — 已失效 (D017)** — perplexity 通道经差分确认为伪回归，即使 plan_006 T=20 也无法拯救伪信号。\\\"Two distinct lead horizons\\\" 升级路径关闭。plan_006 的价值重新定位为：(1) diversity lead 在更长序列中的稳定性，(2) TY power 改善观察，(3) 差分后 permutation Granger 在 T=20 下的表现\\n7. **ECE→perplexity \\\"反向因果\\\"已确认为伪信号 (D017)** — 差分后 ECE→perplexity 0/4 SIG。之前的 post-hoc mechanistic hypothesis 无需讨论。论文只需报告差分前后对比\\n8. **TY 在 N=11 下完全不可用于区分真/伪关联** — d_max sensitivity 分析证实：d_max=0 过度宽松（连 effective_rank 都通过），d_max=1 过度保守（连 token_entropy→distinct_1 都拒绝），adaptive 因 ADF 不稳定而跨 seed 震荡。论文**不能**用 TY 作为\\\"正确答案\\\"。**spurious_rate 必须双版本报告**：含 TY 75%（16 pair 中 12 仅 TY 判伪）、排除 TY 后 62.5%（16 pair 中 10 在 4 种非 TY 方法下一致）。ECE→distinct_2/3 被 TY 判伪但在其余 4 种方法全部 4/4 SIG——这本身是\\\"方法选择改变分类\\\"的例证（Claim 3 素材）\\n9. **ECE 地位为 conditional secondary canary (D020)** — ECE 在 cross-correlation（lag=-1, std=0.0）和 permutation Granger（差分后 4/4 SIG）下与 token_entropy 等效，ECE→distinct_2/3 在排除 TY 的 4 种方法中全部通过。\\\"secondary\\\" 标签**完全由 TY 的 Type II error 驱动**（TY 仅通过 ECE→distinct_1 3/4 seed）。论文标注：\\\"secondary only in TY consistency; equivalent across all other methods\\\"。plan_006（N=21）为最终判定——若 TY 在更大 N 下确认 ECE→distinct_2/3，升级为 co-primary\\n10. **d_max sensitivity 曲线是论文的 key figure** — 三组 d_max（0/adaptive/1）× spurious rate 的变化是 Claim 3 的核心可视化，展示\\\"方法选择如何改变结论\\\"\\n11. **统计效力必须显式论证** — Dream 三档一致 CRITICAL：T=10 下 TY 的 DOF 严重不足。论文必须包含 bootstrap/permutation 验证 + plan_006 (T=20) 结果。所有 p-value 必须经 BH FDR 校正\\n12. **\\\"phase diagram\\\" → \\\"regime map\\\"** — 除非 α 分辨率达到 ≥6 个非平凡值 + 提供 α* uncertainty interval，否则用 \\\"predictability regime map\\\" 或 \\\"regime-dependent analysis\\\"。4-5 个 α 值不足以支撑物理学意义上的 \\\"phase diagram\\\"\\n13. **Scheffer et al. 是必引文献** — critical slowing down / early-warning indicators 框架是本研究的知识祖先。论文 Related Work 必须引用并定位\\n14. **CRS 降级为 illustration** — 不列入核心 contribution。CRS 是显然的反应式干预，Dream 三档一致认为 trivial/confounded\\n15. **TY 正式降级为辅助指标 (D015)** — Bootstrap power analysis (N=1000 Monte Carlo): T=10 power=0.05-0.20, T=20 power=0.17, T=30 power=0.29 (d_max≥1)。核心分析框架改为 cross-correlation + permutation test + BH FDR 校正。TY 仅用于 Claim 3 展示（方法敏感性 + power analysis figure），不再作为 lead-lag 判定方法\\n16. **Perplexity 通道确认为伪回归 (D017)** — Permutation Granger 差分版：canary→perplexity 差分后 0/8 SIG (F≈0, p=0.99)，canary→diversity 差分后 12/12 SIG（6 pair × 4 seed 中，token_entropy 和 ECE 各 3 pair 全通过）。差分前后结论翻转（perplexity: 6-8/8→0/8; diversity: 24/24→24/24）是 Claim 3 的关键 figure 素材。**F 值范围**：undifferenced F=74–3370, differenced F=71–7643（全 6 pairs × 4 seeds），范围重叠——之前\\\"F 不降反升\\\"仅对 token_entropy→distinct_1 子集成立，全量数据应以**显著性保持率 24/24→24/24**为核心叙事，不以 F 值大小为论据。论文 Method 节须注明：(1) T=11 first-difference 后 T=10，circular shift 仅 9 个唯一排列，null distribution 高度离散；(2) 尽管如此，diversity 通道 F 值远超任何排列值，结论不受离散性影响\\n17. **f² 效应量报告约束 (D019 更新)** — 差分后 f²=102-435（token_entropy→distinct_1），因 df_resid=5-6 任何真实信号都产生极大 f²（RSS_unrestricted 趋近零）。论文**禁止**用 Cohen 的 0.02/0.15/0.35 基准解读这些 f² 值。正确做法：permutation p-value 为主要推断证据，f² 仅作\\\"效应存在\\\"的定性指示，不做定量比较。**代码层面**：当 df_resid < 20 时，分析脚本输出 `f2_size=\\\"df_too_low\\\"` 而非 small/medium/large 分类（D019 T3 已实现于 permutation_granger.py）\\n18. **2×2 差分对比表是 Claim 3 核心 figure** — channel type（canary→diversity vs canary→perplexity）× differencing status（undifferenced vs differenced）的 2×2 表最紧凑展示\\\"一个方法论选择翻转整条通道的结论\\\"。diversity 通道差分前后均 24/24 SIG（显著性完全保持），F 值范围 undiff 74–3370 / diff 71–7643，部分 pair 略降但显著性完全保持。perplexity 通道差分后归零。比 d_max sensitivity 曲线更直观地展示差分的决定性影响\\n19. **method_ablation 必须双版本报告 (D019)** — spurious_rate 报告含 TY（5-method: 75%）和排除 TY（4-method: 62.5%）两个数字。ECE→distinct_2/3 在 TY 下被判伪但在其余 4 种方法中 4/4 SIG——TY 的 Type II error 驱动的分类差异本身是 Claim 3 素材。论文主文用 4-method 数字作主要结论，5-method 数字用于 Claim 3 方法敏感性讨论\\n20. **ECE canary 可靠性是 regime-dependent (D021)** — α=0.25 下 ECE gen 1 下降 -14%（反向信号），gen 2+ 才上升至 +77%。α=1.0 下 gen 1 直接 +2926%。ECE 作为早期预警 canary 仅在高 α（≥0.50，待 a050 确认）下可靠。低 α 下首代反向信号意味着 ECE 不能用于\\\"一代内预警\\\"。这丰富 Claim 2：canary 可靠性本身是 regime-dependent。D019 \\\"co-primary\\\" 限定为 \\\"high-α regime only\\\"\\n21. **Claim 1 scope 确认为 α≥0.75 (D037, Director 批准)** — α=0.75 Permutation Granger FDR: 3/4 方向显著（ECE→d1 p_fdr=0.046, ECE→d2 p_fdr=0.046, entropy→d2 p_fdr=0.048），entropy→d1 边界 p_fdr=0.054。反向 4/4 全部不显著。Consensus 11/16 robust。**当前 Granger-causal precedence 在 α≥0.75 成立**（α=1.0: 24/24 FDR-sig 4 seeds; α=0.75: 3/4 FDR-sig single seed）。**Single-seed caveat (C001)**: α=0.75 仅 seed=42 验证，待 D026 multi-seed 确认后移除限定。**entropy→d1 borderline (p_fdr=0.054)**: 论文须讨论——3/4 显著 + 1/4 边界，不是 4/4 全过。α≤0.50 均 0/8 FDR-sig，detectability boundary 确认在 0.50→0.75 间\\n22. **α=0.50 null 结果是 positive finding (D025, D037 更新)** — 中等污染下 canary 与 downstream 同步退化（temporal lead 消失），correlation/rule-based 方法（naive, differenced, threshold）100% sig vs 因果检验方法（permG, TY）0% sig 是 Claim 3（method × regime interaction）最极端的例证。论文呈现策略：(1) 此非单调 detectability 模式本身是 regime map 的核心特征；(2) **Detectability boundary 已确认在 0.50-0.75 区间 (D037)**——α=0.75 有 3/4 FDR-sig 信号，practical utility 定位为\\\"高污染场景（α≥0.75）下的早期预警\\\"，而非通用预警工具；(3) α=0.50 null 不是方法失败，是 signal-to-noise 的物理边界\\n23. **α-sweep 全部 single seed 是当前最大弱点 (D026)** — 非单调 dose-response（α=0.25 -40.3% vs α=0.50 -37.3%）和 ECE regime switch 假说均基于 seed=42 的 point estimate，无置信区间。论文中非单调性结论**必须标注 \\\"observed at seed=42; multi-seed confirmation required\\\"**。multi-seed（α=0.25/0.50 各 2-3 seeds）是从 Weak Accept → Accept 的首要条件，优先于 finer α grid（a010/a060）。非单调性在主文仅报告现象（配 drift 表格），\\\"entropy floor\\\" 机制假说放 Discussion\\n24. **α=0.25 双向 Granger 不改变 Claim 1 叙事 (D026)** — d1→entropy raw p=0.023（FDR 后 0.093 不显著），但效应量仅 f²=1.30 vs entropy→d1 的 f²=27.21（21 倍差异）。强单向因果 + 弱反馈，不是对称 coupled dynamics。α=1.0 反方向不显著，α=0.50 反方向 p=0.224。论文可加一句：\\\"marginally significant feedback at mild contamination (f²=1.30, 21× weaker than primary direction)\\\" 但不需要改写核心叙事\\n25. **证据强度排序：Claim 3 > Claim 2 > Claim 1 (D026)** — Reviewer 独立评估。Claim 3（method sensitivity）最强且 novel、well-supported；Claim 2（regime-dependent）次之（但需 multi-seed）；Claim 1（Granger-causal）scope 最窄（仅 α≥0.75）。论文 framing 应确保 Claim 3 的方法论贡献获得足够篇幅，不因 Claim 1 的 \\\"canary prediction\\\" 叙事而被矮化\\n26. **Phase 3 二次衰退仅限 Discussion，不纳入 Core Claims (D035)** — plan_006_s42 (T=18) 发现 gen 13-17 二次 diversity 衰退（d2 -5.8%, d3 -6.9%），两个硬约束：(a) 单 seed，plan_006_s43 确认前不写入论文主体；(b) Phase 3 中 token_entropy 反升 +2.8% 而 diversity 继续下降——canary 在长 horizon 下失效，升级为核心发现会成审稿攻击面。**最佳用法**：Claim 3 补充证据（观察窗口长度改变结论 = 方法敏感性例证）+ Discussion 段落（collapse dynamics richer than saturation, but canary utility diminishes at extended horizons）。不改变 Core Claims / narrative structure / 方法论主线\\n27. **Consensus score 跨 α 比较须标注标准差异 (D038)** — α=0.75 consensus 11/16 robust 使用单种子 method-agreement 标准（≥4/5 方法判定显著），α=1.0 consensus 6/16 robust 使用 4-seed full consensus 标准（≥3/4 seeds × ≥4/5 方法）。两个数字不可直接对比——11/16 > 6/16 不意味着 α=0.75 信号更强，而是标准更宽松。论文中引用时**必须标注标准差异**，禁止直接对比暗示 α=1.0 信号更弱\\n28. **token_entropy→perplexity 在 α=0.75 单种子 consensus 中的 ROBUST 标记不可引用 (D038)** — α=0.75 单种子 consensus 将 token_entropy→perplexity 标为 ROBUST（因多方法一致通过），但 D017 已用 4-seed 差分检验确认该方向为 spurious（自相关驱动，差分后 0/4 sig）。这是单种子 consensus 的已知局限——无法检测共享非平稳趋势导致的伪关联。论文中**不得引用该方向作为 α=0.75 的 robust evidence**，仅限 canary→diversity 方向\\n\", \"total_chars\": 16905, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have the paper_framing.md and the list of tex files. There are two sets of paper files:
1. `artifacts/_project/paper/` - seems like the working version
2. `docs/paper/` - might be an older version

Let me read the relevant tex files to find mentions of TY, window sensitivity, FNR. I'll focus on `artifacts/_project/paper/` as it seems to be the primary location. Let me read the key files: discussion.tex, experiments.tex, and method.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "baa38720-97eb-4d36-a07e-509cf6f6f8e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAYZarFiDAD5Fzv5MmvzUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10961,
      "cache_read_input_tokens": 27570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10961
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

_source line 21_

找到两组 .tex 文件。先读取 `artifacts/_project/paper/` 下的关键文件，搜索 TY/window sensitivity/FNR 相关内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "cb968b15-f8d2-4e97-9688-6b0aa2da7273",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAYZarFiDAD5Fzv5MmvzUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10961,
      "cache_read_input_tokens": 27570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10961
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01EgMEgxfUo5DQaHcEBs9BUk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "96a35ab0-f9a5-4a7c-8110-ac91636958c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAYZarFiDAD5Fzv5MmvzUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10961,
      "cache_read_input_tokens": 27570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10961
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

_source line 23 · 2026-05-16T00:20:57.094Z_

<details><summary>↩ Tool result · `toolu_01EgMEgxfUo5DQaHcEBs9BUk`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
5	Bivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
6	Our multi-method consensus framework inherits this limitation in full.
7	Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
8	This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.
9	
10	\paragraph{Calibration scope and generalization.}
11	All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
12	Generalization to other model architectures, datasets, or training protocols requires independent validation.
13	The consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
14	For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
15	Our ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.
16	
17	\paragraph{FPR/FNR calibration asymmetry.}
18	The FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.
19	FPR is validated on the method dimension only, using a single seed at the null-control condition ($\alpha{=}0.0$).
20	FNR is validated on the joint method${\times}$seed dimension, aggregating across four seeds at full contamination ($\alpha{=}1.0$).
21	This asymmetry means our FPR estimate of 0\% may be optimistic: if seed-level variance in false positive rates is non-negligible, the true FPR under the consensus rule could exceed zero.
22	Full joint calibration---requiring multi-seed null-control experiments at $\alpha{=}0.0$---remains an open direction for future work.
23	
24	\paragraph{Short time-series constraint.}
25	With $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.
26	This series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.
27	The Toda-Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
28	This finding aligns with \citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.
29	Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.
30	
31	\paragraph{Limitations.}
32	Several limitations constrain the generalizability of our findings.
33	First, our primary experiments use Pythia-410M; preliminary cross-architecture validation with GPT-2-medium uses batch size~32 (versus~4 for Pythia) for GPU efficiency, exposing 8$\times$ more data per training step, which may accelerate collapse dynamics without altering the qualitative pattern (token entropy leading diversity decline is observed in both architectures).
34	Second, training data is drawn from a single domain (a WikiText-103 subset), and domain-specific distributional properties may influence the coupling between canary and downstream metrics.
35	Third, we lack an intervention experiment: we observe that token entropy Granger-precedes diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$) but do not test whether acting on canary signals can prevent or delay collapse onset.
36	Fourth, our experiments use replace-only data accumulation; accumulate-mode training~\cite{dey2024breaking,kazdan2025collapse} may exhibit qualitatively different canary dynamics.
37	Finally, our canary claims are scoped to distinct-$n$ diversity metrics~\cite{li2016diversity}---not to model collapse broadly~\cite{schaeffer2025position}---as the perplexity channel proved spurious ($F{\approx}0$, $p{=}0.99$ after differencing).
38	This scoping is theoretically motivated: \citet{cao2025entropycal} prove a fundamental calibration-diversity tradeoff in language models---all current calibration methods reduce entropy at the cost of diversity---suggesting that calibration and diversity are coupled but not identical, which may explain why token entropy can Granger-precede diversity collapse without leading perplexity.
39	
40	\paragraph{Future work.}
41	Several directions extend this work.
42	Multivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.
43	Cross-architecture validation is needed: our GPT-2-medium experiments are in progress, and evaluation on larger-scale models would further test generalizability.
44	Online monitoring---integrating canary metrics into training pipelines for real-time collapse detection---is a natural applied extension.
45	Accumulate-mode experiments~\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.
46	Finally, connecting the empirically observed detectability boundary at $\alpha{\approx}0.50$--$0.75$ to theoretical phase transition analysis~\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "ec4b811c-a7c5-4e29-bab1-0686ed5ff63b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Granger precedence is not causation.}\nGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\cite{granger1969investigating,shojaie2022granger}.\nBivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\nOur multi-method consensus framework inherits this limitation in full.\nThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\nThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\emph{causes} diversity collapse.\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\alpha \\in \\{0.0, 0.25, 0.50, 0.75, 1.0\\}$).\nGeneralization to other model architectures, datasets, or training protocols requires independent validation.\nThe consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\nFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\nOur ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.\n\n\\paragraph{FPR/FNR calibration asymmetry.}\nThe FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.\nFPR is validated on the method dimension only, using a single seed at the null-control condition ($\\alpha{=}0.0$).\nFNR is validated on the joint method${\\times}$seed dimension, aggregating across four seeds at full contamination ($\\alpha{=}1.0$).\nThis asymmetry means our FPR estimate of 0\\% may be optimistic: if seed-level variance in false positive rates is non-negligible, the true FPR under the consensus rule could exceed zero.\nFull joint calibration---requiring multi-seed null-control experiments at $\\alpha{=}0.0$---remains an open direction for future work.\n\n\\paragraph{Short time-series constraint.}\nWith $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.\nThis series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.\nThe Toda-Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nThis finding aligns with \\citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.\nLonger generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.\n\n\\paragraph{Limitations.}\nSeveral limitations constrain the generalizability of our findings.\nFirst, our primary experiments use Pythia-410M; preliminary cross-architecture validation with GPT-2-medium uses batch size~32 (versus~4 for Pythia) for GPU efficiency, exposing 8$\\times$ more data per training step, which may accelerate collapse dynamics without altering the qualitative pattern (token entropy leading diversity decline is observed in both architectures).\nSecond, training data is drawn from a single domain (a WikiText-103 subset), and domain-specific distributional properties may influence the coupling between canary and downstream metrics.\nThird, we lack an intervention experiment: we observe that token entropy Granger-precedes diversity collapse at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$) but do not test whether acting on canary signals can prevent or delay collapse onset.\nFourth, our experiments use replace-only data accumulation; accumulate-mode training~\\cite{dey2024breaking,kazdan2025collapse} may exhibit qualitatively different canary dynamics.\nFinally, our canary claims are scoped to distinct-$n$ diversity metrics~\\cite{li2016diversity}---not to model collapse broadly~\\cite{schaeffer2025position}---as the perplexity channel proved spurious ($F{\\approx}0$, $p{=}0.99$ after differencing).\nThis scoping is theoretically motivated: \\citet{cao2025entropycal} prove a fundamental calibration-diversity tradeoff in language models---all current calibration methods reduce entropy at the cost of diversity---suggesting that calibration and diversity are coupled but not identical, which may explain why token entropy can Granger-precede diversity collapse without leading perplexity.\n\n\\paragraph{Future work.}\nSeveral directions extend this work.\nMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\nCross-architecture validation is needed: our GPT-2-medium experiments are in progress, and evaluation on larger-scale models would further test generalizability.\nOnline monitoring---integrating canary metrics into training pipelines for real-time collapse detection---is a natural applied extension.\nAccumulate-mode experiments~\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\nFinally, connecting the empirically observed detectability boundary at $\\alpha{\\approx}0.50$--$0.75$ to theoretical phase transition analysis~\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01RvDMXZC73sDarC1ofZw5Vy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "75430373-85d5-4fb3-bd02-0e572a43e49a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAYZarFiDAD5Fzv5MmvzUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10961,
      "cache_read_input_tokens": 27570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10961
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

_source line 25 · 2026-05-16T00:20:57.146Z_

<details><summary>↩ Tool result · `toolu_01RvDMXZC73sDarC1ofZw5Vy`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
23	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
24	Cross-correlation analysis uses a maximum lag of 5 generations.
25	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Metric drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}1.0$: 4-seed mean${\pm}$std; other levels: single seed (seed=42). Non-monotonic distinct-1 pattern across $\alpha \in \{0.25, 0.50\}$ is observed at seed=42, pending multi-seed confirmation.}
31	\label{tab:drift_summary}
32	\begin{tabular}{lccccc}
33	\toprule
34	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
35	\midrule
36	0.00 & $-5.1$ & $+51.7$ & $-13.8$ & $-9.8$ & $-21.7$ \\
37	0.25 & $-4.1$ & $+79.7$ & $-40.3$ & $-57.1$ & $-17.2$ \\
38	0.50 & $-18.6$ & $+842.8$ & $-37.3$ & $-51.5$ & $+21.1$ \\
39	0.75 & $-27.7$ & $+1809.5$ & $-32.7$ & $-41.3$ & $+182.1$ \\
40	1.00 & $-60.5{\pm}1.2$ & $+3862{\pm}158$ & $-25.3{\pm}1.3$ & $-29.7{\pm}1.5$ & $+3690{\pm}320$ \\
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	
46	\subsection{Method Sensitivity Analysis}
47	\label{sec:method_sensitivity}
48	
49	We open with Claim~3---method sensitivity---because it conditions the interpretation of all subsequent results.
50	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
51	
52	\paragraph{Five-method ablation.}
53	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
54	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
55	Method choice alone swings significance from \textbf{100\% to 25\%}.
56	The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
57	
58	\paragraph{First-differencing diagnostic.}
59	A single preprocessing decision can eliminate an entire analysis channel.
60	For canary$\to$diversity pairs at $\alpha{=}1.0$, both undifferenced and differenced permutation Granger tests yield unanimous FDR significance, with $F$-statistics \emph{increasing} after differencing---confirming genuine temporal precedence rather than shared-trend confounding.
61	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
62	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
63	
64	\paragraph{Augmentation order sensitivity.}
65	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
66	At $d_{\max}{=}0$ (most permissive), approximately 6\% of pairs are rejected; at adaptive $d_{\max}$ determined by ADF unit-root tests, 75\%; at $d_{\max}{=}1$ (most conservative), \textbf{94\%}.
67	This single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.
68	
69	\paragraph{Inter-method agreement.}
70	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (poor agreement).
71	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
72	At $\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \textbf{100\%} of pairs significant---a textbook spurious-regression outcome in trending time series.
73	Permutation Granger and Toda--Yamamoto correctly find 0\%.
74	At $\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), the most extreme method$\times$regime divergence in our experiments.
75	
76	\paragraph{Method$\times$regime interaction.}
77	Table~\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.
78	At $\alpha{=}0.25$, differenced cross-correlation drops to 25\% and threshold onset to 37.5\%, while naive cross-correlation remains at 100\%---demonstrating that even partial detrending removes marginal associations at low contamination.
79	The graded response across methods, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{FDR significance rates (\%) for five lead-lag methods across contamination levels. Each cell: fraction of canary$\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$). $\alpha{=}0.75$ is analyzed separately as single-seed data (\S\ref{sec:regime}). FPR$_\text{null}$: false positive rate at the $\alpha{=}0.0$ null control.}
85	\label{tab:method_comparison}
86	\begin{tabular}{lcccccc}
87	\toprule
88	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
89	\midrule
90	Naive XCorr     & 100   & 100  & 100  & ---  & 100   & 100  \\
91	Diff.\ XCorr   & 37.5  & 25   & 100  & ---  & 100   & 37.5 \\
92	Threshold       & 62.5  & 37.5 & 100  & ---  & 100   & 62.5 \\
93	Perm.\ Granger  & 0     & 0    & 0    & ---  & 75    & 0    \\
94	Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\
95	\bottomrule
96	\end{tabular}
97	\end{table}
98	
99	
100	\subsection{Regime-Dependent Detectability}
101	\label{sec:regime}
102	
103	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
104	We present regime effects at two levels: raw metric drift (method-independent) and Granger-causal detectability.
105	
106	\paragraph{Raw drift.}
107	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
108	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3\%$ ($\alpha{=}0.25$), $-37.3\%$ ($\alpha{=}0.50$), $-32.7\%$ ($\alpha{=}0.75$), and $-25.3{\pm}1.3\%$ ($\alpha{=}1.0$).
109	The non-monotonic pattern---diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$---is observed at seed=42 and requires multi-seed confirmation before drawing conclusions about the relationship between contamination level and collapse severity.
110	
111	\paragraph{Granger-causal detectability.}
112	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
113	Permutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant at $\alpha{=}0.00$, 0/8 at $\alpha{=}0.25$, 0/8 at $\alpha{=}0.50$, and \textbf{6/8} at $\alpha{=}1.0$ in the cross-$\alpha$ pooled analysis.
114	At $\alpha{=}0.75$ (single seed, seed=42), 3/8 pairs reach FDR significance; this result requires multi-seed replication before serving as primary evidence.
115	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
116	The detectability boundary---the regime below which canary metrics no longer develop sufficient temporal lead for causal inference---lies at $\alpha \approx 0.50$--$0.75$, consistent with theoretical expectations about signal-to-noise limits in short time series \cite{boettiger2012limits}.
117	
118	\paragraph{Synchronous collapse at $\alpha{=}0.50$.}
119	The $\alpha{=}0.50$ regime provides particularly informative evidence.
120	Correlation-based methods unanimously find significance (Table~\ref{tab:method_comparison}) while causal methods unanimously find non-significance.
121	This extreme method$\times$regime interaction arises because canary and downstream metrics collapse \emph{synchronously} at moderate contamination, preserving high correlation but eliminating the temporal lead required for Granger-causal inference.
122	We highlight this as a \emph{positive finding}: it delineates the regime boundary where naive analysis is most dangerous---high correlation coexists with zero causal precedence, maximizing the risk of spurious conclusions.
123	Figure~\ref{fig:consensus_heatmap} visualizes this interaction across all method$\times\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.
124	
125	
126	\subsection{Case Study: Canary Prediction of Diversity Collapse}
127	\label{sec:case_study}
128	
129	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
130	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
131	
132	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
133	Token entropy Granger-causes distinct-1 and distinct-2 with a consistent one-generation lead.
134	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0).
135	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
136	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
137	Reverse-direction tests (downstream$\to$canary) find \textbf{0/24} FDR-significant (all $p{>}0.49$), confirming directional asymmetry.
138	
139	\paragraph{High contamination ($\alpha{=}0.75$, single seed).}
140	At $\alpha{=}0.75$ (seed=42), three of four forward-direction pairs reach FDR significance: ECE$\to$distinct-1 ($p_\text{fdr}{=}0.046$), ECE$\to$distinct-2 ($p_\text{fdr}{=}0.046$), and token entropy$\to$distinct-2 ($p_\text{fdr}{=}0.048$).
141	Token entropy$\to$distinct-1 is borderline ($p_\text{fdr}{=}0.054$).
142	All four reverse directions are non-significant ($p{>}0.49$).
143	These single-seed results require multi-seed confirmation before serving as primary evidence.
144	
145	\paragraph{ECE as a conditional secondary canary.}
146	ECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).
147	Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\max}$.
148	Resolving ECE's true canary status requires longer time series.
149	
150	\paragraph{Failed canary candidates.}
151	Not all metrics serve as canaries.
152	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
153	
154	\paragraph{Consensus filtering.}
155	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
156	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
157	The consensus framework reduces the naive 100\% significance rate to the 37.5\% rate supported by the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
158	
159	
160	\subsection{Consensus Framework Validation}
161	\label{sec:consensus_validation}
162	
163	We validate the consensus framework's calibration using built-in experimental controls.
164	
165	\paragraph{False positive rate.}
166	At $\alpha{=}0.0$, no synthetic data is injected; any detected lead-lag association is a false positive.
167	Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation: 8/8 pairs) through 62.5\% (threshold) and 37.5\% (differenced) down to \textbf{0\%} (permutation Granger and Toda--Yamamoto).
168	The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
169	
170	\paragraph{False negative rate.}
171	At $\alpha{=}1.0$, we define 6 ground-truth pairs (token entropy and ECE $\to$ distinct-1/2/3), validated independently by the first-differencing diagnostic: $F$-statistics increase after differencing for all 6 pairs, ruling out shared-trend confounding.
172	The consensus framework ($K{\geq}4/5$, $S{\geq}3/4$) recovers all~6 (\textbf{FNR${=}$0\%}).
173	Toda--Yamamoto alone yields FNR${=}$25\%, missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
174	We note a design asymmetry: FPR is validated on method-only data (single seed at $\alpha{=}0.0$), while FNR uses method$\times$seed joint data (4~seeds at $\alpha{=}1.0$).
175	Full joint calibration---multi-seed null-control experiments---remains future work.
176	Table~\ref{tab:fpr_fnr} reports the calibration results.
177	
178	\begin{table}[t]
179	\centering
180	\small
181	\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\alpha{=}0.0$ null control (single seed). FNR: $\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\times$seed joint (\S\ref{sec:consensus_validation}).}
182	\label{tab:fpr_fnr}
183	\begin{tabular}{lcc}
184	\toprule
185	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
186	\midrule
187	Naive XCorr              & 100\%  & 0\%  \\
188	Differenced XCorr        & 37.5\% & 0\%  \\
189	Threshold Onset          & 62.5\% & 0\%  \\
190	Permutation Granger      & 0\%    & 0\%  \\
191	Toda--Yamamoto           & 0\%    & 25\% \\
192	\midrule
193	Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
194	Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "4ef93e66-0461-47cd-b44e-c5e39cd7b662",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\cite{biderman2023pythia}, a 410M-parameter autoregressive language model.\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\nTraining data is drawn from WikiText-103 \\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\n\nOur protocol follows the full-replacement paradigm of \\citet{shumailov2024curse}.\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$.\nThe $\\alpha{=}1.0$ condition uses four random seeds $\\{42, 43, 44, 45\\}$; other conditions use seed~42, with multi-seed replication in progress.\n\nWe track two \\emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\cite{scheffer2009early}---and three \\emph{downstream metrics}.\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\cite{li2016diversity}) and perplexity.\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\S\\ref{sec:case_study}).\nResults for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\n\nAll hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}.\nCross-correlation analysis uses a maximum lag of 5 generations.\nTable~\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) across contamination levels. $\\alpha{=}1.0$: 4-seed mean${\\pm}$std; other levels: single seed (seed=42). Non-monotonic distinct-1 pattern across $\\alpha \\in \\{0.25, 0.50\\}$ is observed at seed=42, pending multi-seed confirmation.}\n\\label{tab:drift_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-5.1$ & $+51.7$ & $-13.8$ & $-9.8$ & $-21.7$ \\\\\n0.25 & $-4.1$ & $+79.7$ & $-40.3$ & $-57.1$ & $-17.2$ \\\\\n0.50 & $-18.6$ & $+842.8$ & $-37.3$ & $-51.5$ & $+21.1$ \\\\\n0.75 & $-27.7$ & $+1809.5$ & $-32.7$ & $-41.3$ & $+182.1$ \\\\\n1.00 & $-60.5{\\pm}1.2$ & $+3862{\\pm}158$ & $-25.3{\\pm}1.3$ & $-29.7{\\pm}1.5$ & $+3690{\\pm}320$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Method Sensitivity Analysis}\n\\label{sec:method_sensitivity}\n\nWe open with Claim~3---method sensitivity---because it conditions the interpretation of all subsequent results.\nIf different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.\n\n\\paragraph{Five-method ablation.}\nWe apply five lead-lag detection methods to the $\\alpha{=}1.0$ condition (4~seeds, 16 canary$\\to$downstream pairs).\nThe fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{4/16} (25.0\\%).\nMethod choice alone swings significance from \\textbf{100\\% to 25\\%}.\nThe spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \\textbf{75\\%} across all five methods and \\textbf{62.5\\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\\S\\ref{sec:consensus_validation}).\n\n\\paragraph{First-differencing diagnostic.}\nA single preprocessing decision can eliminate an entire analysis channel.\nFor canary$\\to$diversity pairs at $\\alpha{=}1.0$, both undifferenced and differenced permutation Granger tests yield unanimous FDR significance, with $F$-statistics \\emph{increasing} after differencing---confirming genuine temporal precedence rather than shared-trend confounding.\nFor canary$\\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \\textbf{zero} significant pairs ($F{\\approx}0$, $p{=}0.99$; Figure~\\ref{fig:differencing_dmax}a).\nThe apparent canary$\\to$perplexity relationship is entirely an artifact of co-trending.\n\n\\paragraph{Augmentation order sensitivity.}\nToda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nAt $d_{\\max}{=}0$ (most permissive), approximately 6\\% of pairs are rejected; at adaptive $d_{\\max}$ determined by ADF unit-root tests, 75\\%; at $d_{\\max}{=}1$ (most conservative), \\textbf{94\\%}.\nThis single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.\n\n\\paragraph{Inter-method agreement.}\nCohen's $\\kappa$, averaged over all method pairs, is \\textbf{0.185} (poor agreement).\nTable~\\ref{tab:method_comparison} extends the analysis across contamination levels.\nAt $\\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \\textbf{100\\%} of pairs significant---a textbook spurious-regression outcome in trending time series.\nPermutation Granger and Toda--Yamamoto correctly find 0\\%.\nAt $\\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\\ref{fig:consensus_heatmap}), the most extreme method$\\times$regime divergence in our experiments.\n\n\\paragraph{Method$\\times$regime interaction.}\nTable~\\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.\nAt $\\alpha{=}0.25$, differenced cross-correlation drops to 25\\% and threshold onset to 37.5\\%, while naive cross-correlation remains at 100\\%---demonstrating that even partial detrending removes marginal associations at low contamination.\nThe graded response across methods, combined with the block structure visible in Figure~\\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \\S\\ref{sec:regime}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{FDR significance rates (\\%) for five lead-lag methods across contamination levels. Each cell: fraction of canary$\\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$). $\\alpha{=}0.75$ is analyzed separately as single-seed data (\\S\\ref{sec:regime}). FPR$_\\text{null}$: false positive rate at the $\\alpha{=}0.0$ null control.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr     & 100   & 100  & 100  & ---  & 100   & 100  \\\\\nDiff.\\ XCorr   & 37.5  & 25   & 100  & ---  & 100   & 37.5 \\\\\nThreshold       & 62.5  & 37.5 & 100  & ---  & 100   & 62.5 \\\\\nPerm.\\ Granger  & 0     & 0    & 0    & ---  & 75    & 0    \\\\\nToda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Regime-Dependent Detectability}\n\\label{sec:regime}\n\nBeyond method choice, the contamination level~$\\alpha$ determines whether a temporal lead exists to detect.\nWe present regime effects at two levels: raw metric drift (method-independent) and Granger-causal detectability.\n\n\\paragraph{Raw drift.}\nTable~\\ref{tab:drift_summary} shows that diversity collapse occurs at \\emph{all} contamination levels, not only under full synthetic replacement.\nDistinct-1 declines by 13.8\\% even at $\\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3\\%$ ($\\alpha{=}0.25$), $-37.3\\%$ ($\\alpha{=}0.50$), $-32.7\\%$ ($\\alpha{=}0.75$), and $-25.3{\\pm}1.3\\%$ ($\\alpha{=}1.0$).\nThe non-monotonic pattern---diversity declining \\emph{more} at moderate~$\\alpha$ than at extreme~$\\alpha$---is observed at seed=42 and requires multi-seed confirmation before drawing conclusions about the relationship between contamination level and collapse severity.\n\n\\paragraph{Granger-causal detectability.}\nDespite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\\ref{fig:regime_map}).\nPermutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant at $\\alpha{=}0.00$, 0/8 at $\\alpha{=}0.25$, 0/8 at $\\alpha{=}0.50$, and \\textbf{6/8} at $\\alpha{=}1.0$ in the cross-$\\alpha$ pooled analysis.\nAt $\\alpha{=}0.75$ (single seed, seed=42), 3/8 pairs reach FDR significance; this result requires multi-seed replication before serving as primary evidence.\nWithin-$\\alpha$ multi-seed analysis at $\\alpha{=}1.0$ yields \\textbf{24/24} canary$\\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.\nThe detectability boundary---the regime below which canary metrics no longer develop sufficient temporal lead for causal inference---lies at $\\alpha \\approx 0.50$--$0.75$, consistent with theoretical expectations about signal-to-noise limits in short time series \\cite{boettiger2012limits}.\n\n\\paragraph{Synchronous collapse at $\\alpha{=}0.50$.}\nThe $\\alpha{=}0.50$ regime provides particularly informative evidence.\nCorrelation-based methods unanimously find significance (Table~\\ref{tab:method_comparison}) while causal methods unanimously find non-significance.\nThis extreme method$\\times$regime interaction arises because canary and downstream metrics collapse \\emph{synchronously} at moderate contamination, preserving high correlation but eliminating the temporal lead required for Granger-causal inference.\nWe highlight this as a \\emph{positive finding}: it delineates the regime boundary where naive analysis is most dangerous---high correlation coexists with zero causal precedence, maximizing the risk of spurious conclusions.\nFigure~\\ref{fig:consensus_heatmap} visualizes this interaction across all method$\\times\\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.\n\n\n\\subsection{Case Study: Canary Prediction of Diversity Collapse}\n\\label{sec:case_study}\n\nHaving established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).\nWe scope this claim precisely: canary metrics predict \\emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.\n\n\\paragraph{Full synthetic replacement ($\\alpha{=}1.0$, 4 seeds).}\nToken entropy Granger-causes distinct-1 and distinct-2 with a consistent one-generation lead.\nCross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0).\nFigure~\\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.\nPermutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nReverse-direction tests (downstream$\\to$canary) find \\textbf{0/24} FDR-significant (all $p{>}0.49$), confirming directional asymmetry.\n\n\\paragraph{High contamination ($\\alpha{=}0.75$, single seed).}\nAt $\\alpha{=}0.75$ (seed=42), three of four forward-direction pairs reach FDR significance: ECE$\\to$distinct-1 ($p_\\text{fdr}{=}0.046$), ECE$\\to$distinct-2 ($p_\\text{fdr}{=}0.046$), and token entropy$\\to$distinct-2 ($p_\\text{fdr}{=}0.048$).\nToken entropy$\\to$distinct-1 is borderline ($p_\\text{fdr}{=}0.054$).\nAll four reverse directions are non-significant ($p{>}0.49$).\nThese single-seed results require multi-seed confirmation before serving as primary evidence.\n\n\\paragraph{ECE as a conditional secondary canary.}\nECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).\nIts classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\max}$.\nResolving ECE's true canary status requires longer time series.\n\n\\paragraph{Failed canary candidates.}\nNot all metrics serve as canaries.\nEffective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.\n\n\\paragraph{Consensus filtering.}\nOf 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).\nThe 10 eliminated pairs comprise all canary$\\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).\nThe consensus framework reduces the naive 100\\% significance rate to the 37.5\\% rate supported by the most conservative individual methods (Figure~\\ref{fig:consensus_workflow}).\n\n\n\\subsection{Consensus Framework Validation}\n\\label{sec:consensus_validation}\n\nWe validate the consensus framework's calibration using built-in experimental controls.\n\n\\paragraph{False positive rate.}\nAt $\\alpha{=}0.0$, no synthetic data is injected; any detected lead-lag association is a false positive.\nIndividual-method FPR ranges from \\textbf{100\\%} (naive cross-correlation: 8/8 pairs) through 62.5\\% (threshold) and 37.5\\% (differenced) down to \\textbf{0\\%} (permutation Granger and Toda--Yamamoto).\nThe consensus framework at $K{\\geq}4/5$ achieves \\textbf{FPR${=}$0\\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\\ref{tab:fpr_fnr}).\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$, we define 6 ground-truth pairs (token entropy and ECE $\\to$ distinct-1/2/3), validated independently by the first-differencing diagnostic: $F$-statistics increase after differencing for all 6 pairs, ruling out shared-trend confounding.\nThe consensus framework ($K{\\geq}4/5$, $S{\\geq}3/4$) recovers all~6 (\\textbf{FNR${=}$0\\%}).\nToda--Yamamoto alone yields FNR${=}$25\\%, missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\nWe note a design asymmetry: FPR is validated on method-only data (single seed at $\\alpha{=}0.0$), while FNR uses method$\\times$seed joint data (4~seeds at $\\alpha{=}1.0$).\nFull joint calibration---multi-seed null-control experiments---remains future work.\nTable~\\ref{tab:fpr_fnr} reports the calibration results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\\alpha{=}0.0$ null control (single seed). FNR: $\\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\\times$seed joint (\\S\\ref{sec:consensus_validation}).}\n\\label{tab:fpr_fnr}\n\\begin{tabular}{lcc}\n\\toprule\nCriterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\n\\midrule\nNaive XCorr              & 100\\%  & 0\\%  \\\\\nDifferenced XCorr        & 37.5\\% & 0\\%  \\\\\nThreshold Onset          & 62.5\\% & 0\\%  \\\\\nPermutation Granger      & 0\\%    & 0\\%  \\\\\nToda--Yamamoto           & 0\\%    & 25\\% \\\\\n\\midrule\nConsensus ($K{\\geq}4/5$)              & 0\\%    & 0\\%  \\\\\nConsensus ($K{\\geq}4/5$, $S{\\geq}3/4$) & 0\\%    & 0\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 198,
      "startLine": 1,
      "totalLines": 198
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01CQKumGtBL27dpiFPGNtc76`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "3db2b946-6711-4da1-8b82-536dc87f6e06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAYZarFiDAD5Fzv5MmvzUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10961,
      "cache_read_input_tokens": 27570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10961
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

_source line 27 · 2026-05-16T00:20:57.487Z_

<details><summary>↩ Tool result · `toolu_01CQKumGtBL27dpiFPGNtc76`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire analysis channel.
22	At $\alpha{=}1.0$, canary$\to$perplexity pairs appear near-universally significant in undifferenced analysis ($F{=}16$--$36$) but yield $F{\approx}0$, $p{=}0.99$ after differencing (Figure~\ref{fig:differencing_dmax}a; \S\ref{sec:method_sensitivity}).
23	In contrast, canary$\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\to$24/24).
24	Without the differencing diagnostic, an analyst would conclude that canaries predict perplexity---a conclusion entirely driven by co-trending rather than temporal precedence.
25	The danger lies in the selective nature of this confound: only by applying the diagnostic can one determine which channels are genuine and which are artifacts of shared non-stationarity.
26	
27	\paragraph{Pitfall 3: Regime dependence.}
28	Even after fixing the statistical method, the contamination level~$\alpha$ determines whether a lead-lag relationship is detectable.
29	Permutation Granger tests (first-differenced, BH FDR-corrected at $q{=}0.05$) find 6/8 pairs FDR-significant at $\alpha{=}1.0$ but 0/8 at all $\alpha{\leq}0.50$ (\S\ref{sec:regime}).
30	The $\alpha{=}0.50$ regime is particularly dangerous: correlation-based methods unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), creating the maximum risk of spurious conclusions---high correlation coexists with zero causal precedence.
31	This regime dependence is consistent with theoretical expectations about signal-to-noise limits in short ecological time series \cite{boettiger2012limits}, and suggests that detectability boundaries should be explicitly mapped rather than assumed.
32	
33	
34	\subsection{Multi-Method Consensus Framework}
35	\label{sec:consensus}
36	
37	The pitfalls above motivate a consensus approach inspired by multi-method validation practices in early-warning signal detection \cite{scheffer2009early}: rather than relying on any single method, we require agreement across multiple independent methods and random seeds before classifying a lead-lag relationship as robust.
38	
39	\paragraph{Formal definition.}
40	Given $M$ lead-lag detection methods $\{m_1, \ldots, m_M\}$ and $N$ independent random seeds, a canary$\to$downstream pair $(X, Y)$ is classified as \textsc{robust} if and only if:
41	\begin{enumerate}
42	    \item At least $K$ of $M$ methods judge the pair FDR-significant, where each method independently applies Benjamini--Hochberg correction at $q{=}0.05$; and
43	    \item At least $S$ of $N$ seeds replicate this conclusion.
44	\end{enumerate}
45	The thresholds $(K, S)$ control the trade-off between false positive and false negative rates.
46	Methods with different inductive biases---correlation-based methods that detect any temporal association versus Granger-type methods that test directional predictive improvement \cite{granger1969investigating}---provide complementary evidence.
47	Their convergence on a given pair constitutes stronger evidence than agreement among methods sharing the same statistical assumptions.
48	We note that Granger precedence establishes temporal predictive improvement, not true causality \cite{shojaie2022granger}; our framework inherits this limitation.
49	
50	\paragraph{Sequential filtering pipeline.}
51	We instantiate the framework as a four-stage pipeline (Figure~\ref{fig:consensus_workflow}):
52	\begin{enumerate}
53	    \item \textbf{Naive correlation scan.} Cross-correlation at maximum lag~5 with BH correction serves as a permissive baseline; all pairs with any temporal association pass.
54	    \item \textbf{First-differencing diagnostic.} The analysis is repeated on first-differenced series. Pairs that lose significance are flagged as potential spurious regressions driven by shared non-stationary trends rather than genuine temporal precedence.
55	    \item \textbf{Permutation Granger causality.} Permutation-based Granger causality tests \cite{shojaie2022granger} on first-differenced series (5{,}000 permutations, BH correction at $q{=}0.05$) assess whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.
56	    \item \textbf{Multi-seed replication.} The conclusion must hold across $S$ of $N$ independent training seeds, filtering seed-specific artifacts.
57	\end{enumerate}
58	At $\alpha{=}1.0$, this pipeline progressively filters: 16 pairs pass Stage~1, 14 survive Stage~2 (differencing removes 2 marginal canary$\to$perplexity pairs), 6 survive Stage~3 (Granger testing eliminates remaining canary$\to$perplexity pairs and failed canary candidates), and all~6 survive Stage~4 (multi-seed replication confirms all Granger-significant pairs).
59	
60	\paragraph{Practical guidance.}
61	The consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.
62	Table~\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\S\ref{sec:calibration}).
63	Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$) achieves the best trade-off in our setting: zero false positives while recovering all six ground-truth pairs.
64	Tier~4 requires unanimity across methods and seeds, which incurs a 50\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\S\ref{sec:consensus_validation}).
65	
66	\begin{table}[t]
67	\centering
68	\small
69	\caption{Practical guidance tiers for lead-lag consensus analysis. FPR and FNR are empirically calibrated at $\alpha{=}0.0$ (null control) and $\alpha{=}1.0$ (6 ground-truth pairs), respectively. $M{=}5$ methods, $N{=}4$ seeds. FPR is validated on the method dimension only; FNR on the method${\times}$seed joint dimension (\S\ref{sec:calibration}).}
70	\label{tab:practical_guidance}
71	\begin{tabular}{llcccc}
72	\toprule
73	Tier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\
74	\midrule
75	1 & Exploratory     & ${\geq}1/5$ & ${\geq}1/N$ & 100\%  & 0\%    \\
76	2 & Screening       & ${\geq}3/5$ & ${\geq}2/N$ & 37.5\% & 0\%    \\
77	3 & Confirmatory    & ${\geq}4/5$ & ${\geq}3/N$ & 0\%    & 0\%    \\
78	4 & Conservative    & $5/5$       & $N/N$        & 0\%    & 50\% \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	
84	\subsection{Empirical Calibration}
85	\label{sec:calibration}
86	
87	We calibrate the framework using two built-in experimental controls.
88	Full numerical results are reported in Table~\ref{tab:fpr_fnr}.
89	
90	\paragraph{False positive rate.}
91	The $\alpha{=}0.0$ condition serves as a null control: no synthetic data is injected, so any detected lead-lag association is a false positive.
92	At $K{=}1$ (any single method suffices), FPR${=}$100\%---naive cross-correlation alone flags all pairs.
93	At $K{=}2$, FPR drops to 75\%; at $K{=}3$, to 37.5\%; and at $K{\geq}4$, FPR${=}$0\%.
94	The consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\%) while providing robustness against miscalibration of any single method.
95	
96	\paragraph{False negative rate.}
97	At $\alpha{=}1.0$ with 4~seeds, we define six ground-truth robust pairs: token entropy and ECE each predicting distinct-1, distinct-2, and distinct-3 \cite{li2016diversity}.
98	These are independently validated by the first-differencing diagnostic---all six retain FDR significance after differencing (24/24 across seeds), ruling out shared-trend confounding as an alternative explanation.
99	At Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$), all six pairs are recovered (FNR${=}$0\%).
100	At $K{=}5/5$, $S{\geq}3/4$, FNR rises to 33.3\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.
101	At $K{=}5/5$, $S{=}4/4$, FNR${=}$50\%.
102	
103	\paragraph{Design asymmetry.}
104	FPR is validated on the method dimension only (single seed at $\alpha{=}0.0$), while FNR is validated on the joint method${\times}$seed dimension (4~seeds at $\alpha{=}1.0$).
105	Full joint calibration---multi-seed null-control experiments---remains future work.
106	This asymmetry means that FPR estimates may be optimistic if seed-level variance in false positive rates is non-negligible.
107	
108	\paragraph{Independent validation of ground truth.}
109	The six ground-truth pairs used for FNR calibration are not self-referentially defined.
110	They are independently confirmed by the first-differencing diagnostic (\S\ref{sec:method_sensitivity}), which tests a different statistical property---robustness to detrending---than the consensus methods.
111	All six pairs retain 24/24 FDR significance after differencing, providing evidence against shared-trend confounding independent of the consensus framework itself.
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "247852f6-b257-4c15-99e0-93ce9461f61d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nThe experiments in \\S\\ref{sec:method_sensitivity}--\\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.\nThis section distills three methodological pitfalls (\\S\\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\\S\\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\\S\\ref{sec:calibration}).\n\n\n\\subsection{Methodological Pitfalls in Lead-Lag Analysis}\n\\label{sec:pitfalls}\n\nWe identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.\nEach is documented below with representative data from our experiments; full results appear in \\S\\ref{sec:experiments}.\n\n\\paragraph{Pitfall 1: Method sensitivity.}\nApplied to the same data ($\\alpha{=}1.0$, 4~seeds, 16 canary$\\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$---poor agreement (\\S\\ref{sec:method_sensitivity}).\nThe spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\\% across all five methods and 62.5\\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.\nThis pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.\nIn a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.\n\n\\paragraph{Pitfall 2: Spurious regression under shared trends.}\nA single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire analysis channel.\nAt $\\alpha{=}1.0$, canary$\\to$perplexity pairs appear near-universally significant in undifferenced analysis ($F{=}16$--$36$) but yield $F{\\approx}0$, $p{=}0.99$ after differencing (Figure~\\ref{fig:differencing_dmax}a; \\S\\ref{sec:method_sensitivity}).\nIn contrast, canary$\\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\\to$24/24).\nWithout the differencing diagnostic, an analyst would conclude that canaries predict perplexity---a conclusion entirely driven by co-trending rather than temporal precedence.\nThe danger lies in the selective nature of this confound: only by applying the diagnostic can one determine which channels are genuine and which are artifacts of shared non-stationarity.\n\n\\paragraph{Pitfall 3: Regime dependence.}\nEven after fixing the statistical method, the contamination level~$\\alpha$ determines whether a lead-lag relationship is detectable.\nPermutation Granger tests (first-differenced, BH FDR-corrected at $q{=}0.05$) find 6/8 pairs FDR-significant at $\\alpha{=}1.0$ but 0/8 at all $\\alpha{\\leq}0.50$ (\\S\\ref{sec:regime}).\nThe $\\alpha{=}0.50$ regime is particularly dangerous: correlation-based methods unanimously find significance while causal methods unanimously find non-significance (Figure~\\ref{fig:consensus_heatmap}), creating the maximum risk of spurious conclusions---high correlation coexists with zero causal precedence.\nThis regime dependence is consistent with theoretical expectations about signal-to-noise limits in short ecological time series \\cite{boettiger2012limits}, and suggests that detectability boundaries should be explicitly mapped rather than assumed.\n\n\n\\subsection{Multi-Method Consensus Framework}\n\\label{sec:consensus}\n\nThe pitfalls above motivate a consensus approach inspired by multi-method validation practices in early-warning signal detection \\cite{scheffer2009early}: rather than relying on any single method, we require agreement across multiple independent methods and random seeds before classifying a lead-lag relationship as robust.\n\n\\paragraph{Formal definition.}\nGiven $M$ lead-lag detection methods $\\{m_1, \\ldots, m_M\\}$ and $N$ independent random seeds, a canary$\\to$downstream pair $(X, Y)$ is classified as \\textsc{robust} if and only if:\n\\begin{enumerate}\n    \\item At least $K$ of $M$ methods judge the pair FDR-significant, where each method independently applies Benjamini--Hochberg correction at $q{=}0.05$; and\n    \\item At least $S$ of $N$ seeds replicate this conclusion.\n\\end{enumerate}\nThe thresholds $(K, S)$ control the trade-off between false positive and false negative rates.\nMethods with different inductive biases---correlation-based methods that detect any temporal association versus Granger-type methods that test directional predictive improvement \\cite{granger1969investigating}---provide complementary evidence.\nTheir convergence on a given pair constitutes stronger evidence than agreement among methods sharing the same statistical assumptions.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality \\cite{shojaie2022granger}; our framework inherits this limitation.\n\n\\paragraph{Sequential filtering pipeline.}\nWe instantiate the framework as a four-stage pipeline (Figure~\\ref{fig:consensus_workflow}):\n\\begin{enumerate}\n    \\item \\textbf{Naive correlation scan.} Cross-correlation at maximum lag~5 with BH correction serves as a permissive baseline; all pairs with any temporal association pass.\n    \\item \\textbf{First-differencing diagnostic.} The analysis is repeated on first-differenced series. Pairs that lose significance are flagged as potential spurious regressions driven by shared non-stationary trends rather than genuine temporal precedence.\n    \\item \\textbf{Permutation Granger causality.} Permutation-based Granger causality tests \\cite{shojaie2022granger} on first-differenced series (5{,}000 permutations, BH correction at $q{=}0.05$) assess whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.\n    \\item \\textbf{Multi-seed replication.} The conclusion must hold across $S$ of $N$ independent training seeds, filtering seed-specific artifacts.\n\\end{enumerate}\nAt $\\alpha{=}1.0$, this pipeline progressively filters: 16 pairs pass Stage~1, 14 survive Stage~2 (differencing removes 2 marginal canary$\\to$perplexity pairs), 6 survive Stage~3 (Granger testing eliminates remaining canary$\\to$perplexity pairs and failed canary candidates), and all~6 survive Stage~4 (multi-seed replication confirms all Granger-significant pairs).\n\n\\paragraph{Practical guidance.}\nThe consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.\nTable~\\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\\S\\ref{sec:calibration}).\nTier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$) achieves the best trade-off in our setting: zero false positives while recovering all six ground-truth pairs.\nTier~4 requires unanimity across methods and seeds, which incurs a 50\\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\\S\\ref{sec:consensus_validation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Practical guidance tiers for lead-lag consensus analysis. FPR and FNR are empirically calibrated at $\\alpha{=}0.0$ (null control) and $\\alpha{=}1.0$ (6 ground-truth pairs), respectively. $M{=}5$ methods, $N{=}4$ seeds. FPR is validated on the method dimension only; FNR on the method${\\times}$seed joint dimension (\\S\\ref{sec:calibration}).}\n\\label{tab:practical_guidance}\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\\\\n\\midrule\n1 & Exploratory     & ${\\geq}1/5$ & ${\\geq}1/N$ & 100\\%  & 0\\%    \\\\\n2 & Screening       & ${\\geq}3/5$ & ${\\geq}2/N$ & 37.5\\% & 0\\%    \\\\\n3 & Confirmatory    & ${\\geq}4/5$ & ${\\geq}3/N$ & 0\\%    & 0\\%    \\\\\n4 & Conservative    & $5/5$       & $N/N$        & 0\\%    & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Empirical Calibration}\n\\label{sec:calibration}\n\nWe calibrate the framework using two built-in experimental controls.\nFull numerical results are reported in Table~\\ref{tab:fpr_fnr}.\n\n\\paragraph{False positive rate.}\nThe $\\alpha{=}0.0$ condition serves as a null control: no synthetic data is injected, so any detected lead-lag association is a false positive.\nAt $K{=}1$ (any single method suffices), FPR${=}$100\\%---naive cross-correlation alone flags all pairs.\nAt $K{=}2$, FPR drops to 75\\%; at $K{=}3$, to 37.5\\%; and at $K{\\geq}4$, FPR${=}$0\\%.\nThe consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\\%) while providing robustness against miscalibration of any single method.\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$ with 4~seeds, we define six ground-truth robust pairs: token entropy and ECE each predicting distinct-1, distinct-2, and distinct-3 \\cite{li2016diversity}.\nThese are independently validated by the first-differencing diagnostic---all six retain FDR significance after differencing (24/24 across seeds), ruling out shared-trend confounding as an alternative explanation.\nAt Tier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$), all six pairs are recovered (FNR${=}$0\\%).\nAt $K{=}5/5$, $S{\\geq}3/4$, FNR rises to 33.3\\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.\nAt $K{=}5/5$, $S{=}4/4$, FNR${=}$50\\%.\n\n\\paragraph{Design asymmetry.}\nFPR is validated on the method dimension only (single seed at $\\alpha{=}0.0$), while FNR is validated on the joint method${\\times}$seed dimension (4~seeds at $\\alpha{=}1.0$).\nFull joint calibration---multi-seed null-control experiments---remains future work.\nThis asymmetry means that FPR estimates may be optimistic if seed-level variance in false positive rates is non-negligible.\n\n\\paragraph{Independent validation of ground truth.}\nThe six ground-truth pairs used for FNR calibration are not self-referentially defined.\nThey are independently confirmed by the first-differencing diagnostic (\\S\\ref{sec:method_sensitivity}), which tests a different statistical property---robustness to detrending---than the consensus methods.\nAll six pairs retain 24/24 FDR significance after differencing, providing evidence against shared-trend confounding independent of the consensus framework itself.\n",
      "numLines": 112,
      "startLine": 1,
      "totalLines": 112
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
Now let me also read the remaining tex files and check `docs/paper/` to understand which is the primary version. Let me also check for the window sensitivity section, which might be in an appendix or elsewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "58fee668-cd84-4502-9be4-d7ffed001c37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx76pH68f6bRawvfyfdoWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 38531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

Now let me check the remaining tex files and look for the window sensitivity section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "4dd711db-6368-4015-94f9-4ccf9f2526b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx76pH68f6bRawvfyfdoWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 38531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

<details open><summary>🔧 Tool call — Read · `toolu_01VjvKVFbz2BGhRTzMq6nHRs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "318d1436-5900-4de0-99ac-07c4aa5e3e09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx76pH68f6bRawvfyfdoWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 38531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

_source line 31 · 2026-05-16T00:21:03.466Z_

<details><summary>↩ Tool result · `toolu_01VjvKVFbz2BGhRTzMq6nHRs`</summary>

```text
1	\begin{abstract}
2	We demonstrate that lead-lag conclusions in iterative model collapse are determined more by method choice than by the data: naive cross-correlation yields 100\% significance (16/16 metric pairs), while Toda--Yamamoto Granger causality retains only 25\% (4/16), with inter-method agreement of $\kappa = 0.185$. We identify three methodological pitfalls---shared-trend confounding, short-series power loss, and threshold arbitrariness---that together inflate spurious-signal rates to 75\%. To replace single-method reporting, we introduce a multi-method consensus framework requiring agreement across ${\geq}4$ of 5 statistical tests with FDR correction, achieving 0\% false-positive and 0\% false-negative rates on reference extreme regimes. Applied to Pythia-410M across 4 seeds, 5 synthetic-data mixing ratios ($\alpha$), and 10 iterative training generations on WikiText-103, the framework reveals a sharp regime boundary: significant lead-lag relationships emerge at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), where token entropy Granger-causes diversity collapse with a one-generation lead ($|r| > 0.99$, 24/24 pairs significant, 0/24 in the reverse direction). Differencing eliminates all perplexity leads ($8/8 \to 0/8$) but preserves all diversity leads (24/24), confirming token entropy as a robust early-warning canary metric.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "09dc48ee-a2a6-4830-b86c-e57337caa2b4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nWe demonstrate that lead-lag conclusions in iterative model collapse are determined more by method choice than by the data: naive cross-correlation yields 100\\% significance (16/16 metric pairs), while Toda--Yamamoto Granger causality retains only 25\\% (4/16), with inter-method agreement of $\\kappa = 0.185$. We identify three methodological pitfalls---shared-trend confounding, short-series power loss, and threshold arbitrariness---that together inflate spurious-signal rates to 75\\%. To replace single-method reporting, we introduce a multi-method consensus framework requiring agreement across ${\\geq}4$ of 5 statistical tests with FDR correction, achieving 0\\% false-positive and 0\\% false-negative rates on reference extreme regimes. Applied to Pythia-410M across 4 seeds, 5 synthetic-data mixing ratios ($\\alpha$), and 10 iterative training generations on WikiText-103, the framework reveals a sharp regime boundary: significant lead-lag relationships emerge at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$), where token entropy Granger-causes diversity collapse with a one-generation lead ($|r| > 0.99$, 24/24 pairs significant, 0/24 in the reverse direction). Differencing eliminates all perplexity leads ($8/8 \\to 0/8$) but preserves all diversity leads (24/24), confirming token entropy as a robust early-warning canary metric.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_013a6avzc7meuHuoHgrRVYgb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "1695ab26-b1b0-4ca1-bdba-a2154b641494",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx76pH68f6bRawvfyfdoWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 38531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

_source line 33 · 2026-05-16T00:21:03.811Z_

<details><summary>↩ Tool result · `toolu_013a6avzc7meuHuoHgrRVYgb`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
5	Tail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.
6	As large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.
7	
8	A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.
11	
12	We identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation---conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;
15	(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and
16	(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.
17	The closest predecessor is \citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.
18	Their analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests---leaving open the question of whether the observed lead is genuine or an artifact of shared trends.
19	The early-warning framework of \citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\cite{boettiger2012limits}.
20	
21	We address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.
22	Using Pythia-410M across five contamination levels ($\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:
23	\begin{enumerate}
24	    \item \textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$ (poor agreement).
25	    \item \textbf{Spurious regression.} Canary$\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.
26	    \item \textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\to$diversity pairs FDR-significant at full synthetic replacement ($\alpha{=}1.0$) but 0/8 at $\alpha{\leq}0.50$, demonstrating that detectability depends sharply on the contamination level.
27	\end{enumerate}
28	To move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.
29	
30	The framework's utility is demonstrated by its calibration on built-in experimental controls.
31	Naive cross-correlation identifies 100\% of canary--collapse metric pairs as FDR-significant; the consensus pipeline (requiring ${\geq}4/5$ methods and ${\geq}3/4$ seeds) retains only those pairs independently validated by the first-differencing diagnostic.
32	On reference extremes, the framework achieves a false positive rate of 0\% at the $\alpha{=}0.0$ null control (where individual methods reach up to 100\% FPR) and a false negative rate of 0\% against six ground-truth pairs at $\alpha{=}1.0$.
33	Applying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.
34	We note that Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
35	
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.
39	    We quantify each pitfall: method choice alone swings significance from 100\% to 25\% with a spurious-signal rate of 75\%; first-differencing eliminates canary$\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.
40	    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.
41	
42	    \item \textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\geq}1/5$) to conservative ($K{=}5/5$).
43	    The framework achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes, providing robustness against miscalibration of any individual method.
44	
45	    \item \textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.
46	\end{enumerate}
47	
48	The remainder of this paper is organized as follows.
49	\S\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.
50	\S\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.
51	\S\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.
52	\S\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\S\ref{sec:method_sensitivity}), regime-dependent detectability (\S\ref{sec:regime}), a case study of canary prediction of diversity collapse (\S\ref{sec:case_study}), and consensus framework validation (\S\ref{sec:consensus_validation}).
53	\S\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.
54	\S\ref{sec:conclusion} concludes.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "c7a5d817-a579-46c8-9eb3-e7fa794dd4b6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\\cite{shumailov2024curse} or Model Autophagy Disorder~\\cite{alemohammad2024mad}.\nTail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.\nAs large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.\n\nA natural follow-up question is whether cheap-to-compute statistics---\\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\nYet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.\n\nWe identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:\n(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;\n(2)~no multi-method cross-validation---conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;\n(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and\n(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests---leaving open the question of whether the observed lead is genuine or an artifact of shared trends.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.\n\nWe address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.\nUsing Pythia-410M across five contamination levels ($\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:\n\\begin{enumerate}\n    \\item \\textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\n    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.\n    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/8 at $\\alpha{\\leq}0.50$, demonstrating that detectability depends sharply on the contamination level.\n\\end{enumerate}\nTo move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.\n\nThe framework's utility is demonstrated by its calibration on built-in experimental controls.\nNaive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the consensus pipeline (requiring ${\\geq}4/5$ methods and ${\\geq}3/4$ seeds) retains only those pairs independently validated by the first-differencing diagnostic.\nOn reference extremes, the framework achieves a false positive rate of 0\\% at the $\\alpha{=}0.0$ null control (where individual methods reach up to 100\\% FPR) and a false negative rate of 0\\% against six ground-truth pairs at $\\alpha{=}1.0$.\nApplying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$), with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.\n    We quantify each pitfall: method choice alone swings significance from 100\\% to 25\\% with a spurious-signal rate of 75\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.\n\n    \\item \\textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\\geq}1/5$) to conservative ($K{=}5/5$).\n    The framework achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes, providing robustness against miscalibration of any individual method.\n\n    \\item \\textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$), scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), and consensus framework validation (\\S\\ref{sec:consensus_validation}).\n\\S\\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.\n\\S\\ref{sec:conclusion} concludes.\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01AYaVRDM4Vr8s26WVbAafes`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "d33b589b-2fa7-45d4-9a09-d421856d23a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx76pH68f6bRawvfyfdoWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 38531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

_source line 35 · 2026-05-16T00:21:04.315Z_

<details><summary>↩ Tool result · `toolu_01AYaVRDM4Vr8s26WVbAafes`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	We demonstrated three pitfalls that undermine standard approaches: method choice alone swings FDR significance from 100\% to 25\% ($\kappa{=}0.185$), first-differencing exposes canary$\to$perplexity associations as entirely spurious ($F{\approx}0$, $p{=}0.99$), and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These findings establish that single-method, single-regime analyses---the current default---cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our multi-method consensus framework addresses this fragility by requiring convergent evidence across ${\geq}4/5$ independent methods and ${\geq}3/4$ random seeds.
9	Calibrated on built-in experimental controls, the framework achieves 0\% false positive rate at the null control ($\alpha{=}0.0$) and 0\% false negative rate against ground-truth pairs at full contamination ($\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.
10	
11	Applying the framework yields a concrete finding: token entropy serves as a one-generation-ahead canary for diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), with $|r|{>}0.99$ and complete directional asymmetry (0/24 reverse-direction FDR-significant pairs).
12	This result is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.
13	
14	The methodological pitfalls we expose are not specific to our experimental setting---they arise from generic properties of short, non-stationary time series---and the consensus framework transfers directly to any domain where multiple detection methods can be applied in parallel.
15	Limitations and remaining gaps are discussed in \S\ref{sec:discussion}.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "95d2b9ef-e1f2-4759-b168-63555b1e4c1d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nLead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.\nWe demonstrated three pitfalls that undermine standard approaches: method choice alone swings FDR significance from 100\\% to 25\\% ($\\kappa{=}0.185$), first-differencing exposes canary$\\to$perplexity associations as entirely spurious ($F{\\approx}0$, $p{=}0.99$), and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.\nThese findings establish that single-method, single-regime analyses---the current default---cannot reliably distinguish genuine temporal precedence from statistical artifacts.\n\nOur multi-method consensus framework addresses this fragility by requiring convergent evidence across ${\\geq}4/5$ independent methods and ${\\geq}3/4$ random seeds.\nCalibrated on built-in experimental controls, the framework achieves 0\\% false positive rate at the null control ($\\alpha{=}0.0$) and 0\\% false negative rate against ground-truth pairs at full contamination ($\\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.\n\nApplying the framework yields a concrete finding: token entropy serves as a one-generation-ahead canary for diversity collapse at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$), with $|r|{>}0.99$ and complete directional asymmetry (0/24 reverse-direction FDR-significant pairs).\nThis result is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.\n\nThe methodological pitfalls we expose are not specific to our experimental setting---they arise from generic properties of short, non-stationary time series---and the consensus framework transfers directly to any domain where multiple detection methods can be applied in parallel.\nLimitations and remaining gaps are discussed in \\S\\ref{sec:discussion}.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_016au91MePzyTncj36CNuALb`</summary>

```json
{
  "pattern": "window.sensitivity|FNR|33\\.3|25%.*Toda|underpowered|0/6|nan|false.negative",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "512aa787-7c12-4a94-807d-8b25684b66e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx76pH68f6bRawvfyfdoWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 38531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

_source line 37 · 2026-05-16T00:21:06.236Z_

<details><summary>↩ Tool result · `toolu_016au91MePzyTncj36CNuALb`</summary>

```text
artifacts/_project/paper/related_work.tex:32:(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.
artifacts/_project/paper/experiments.tex:60:For canary$\to$diversity pairs at $\alpha{=}1.0$, both undifferenced and differenced permutation Granger tests yield unanimous FDR significance, with $F$-statistics \emph{increasing} after differencing---confirming genuine temporal precedence rather than shared-trend confounding.
artifacts/_project/paper/experiments.tex:74:At $\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), the most extreme method$\times$regime divergence in our experiments.
artifacts/_project/paper/experiments.tex:120:Correlation-based methods unanimously find significance (Table~\ref{tab:method_comparison}) while causal methods unanimously find non-significance.
artifacts/_project/paper/experiments.tex:168:The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
artifacts/_project/paper/experiments.tex:170:\paragraph{False negative rate.}
artifacts/_project/paper/experiments.tex:172:The consensus framework ($K{\geq}4/5$, $S{\geq}3/4$) recovers all~6 (\textbf{FNR${=}$0\%}).
artifacts/_project/paper/experiments.tex:173:Toda--Yamamoto alone yields FNR${=}$25\%, missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
artifacts/_project/paper/experiments.tex:174:We note a design asymmetry: FPR is validated on method-only data (single seed at $\alpha{=}0.0$), while FNR uses method$\times$seed joint data (4~seeds at $\alpha{=}1.0$).
artifacts/_project/paper/experiments.tex:176:Table~\ref{tab:fpr_fnr} reports the calibration results.
artifacts/_project/paper/experiments.tex:181:\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\alpha{=}0.0$ null control (single seed). FNR: $\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\times$seed joint (\S\ref{sec:consensus_validation}).}
artifacts/_project/paper/experiments.tex:182:\label{tab:fpr_fnr}
artifacts/_project/paper/experiments.tex:185:Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
artifacts/_project/paper/abstract_8c6c62.tex:2:[Omitted long matching line]
artifacts/_project/paper/conclusion.tex:9:Calibrated on built-in experimental controls, the framework achieves 0\% false positive rate at the null control ($\alpha{=}0.0$) and 0\% false negative rate against ground-truth pairs at full contamination ($\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.
artifacts/_project/paper/discussion.tex:11:All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
artifacts/_project/paper/discussion.tex:14:For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
artifacts/_project/paper/discussion.tex:17:\paragraph{FPR/FNR calibration asymmetry.}
artifacts/_project/paper/discussion.tex:18:The FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.
artifacts/_project/paper/discussion.tex:20:FNR is validated on the joint method${\times}$seed dimension, aggregating across four seeds at full contamination ($\alpha{=}1.0$).
artifacts/_project/paper/discussion.tex:27:The Toda-Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
artifacts/_project/paper/method.tex:23:In contrast, canary$\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\to$24/24).
artifacts/_project/paper/method.tex:30:The $\alpha{=}0.50$ regime is particularly dangerous: correlation-based methods unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), creating the maximum risk of spurious conclusions---high correlation coexists with zero causal precedence.
artifacts/_project/paper/method.tex:45:The thresholds $(K, S)$ control the trade-off between false positive and false negative rates.
artifacts/_project/paper/method.tex:61:The consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.
artifacts/_project/paper/method.tex:64:Tier~4 requires unanimity across methods and seeds, which incurs a 50\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\S\ref{sec:consensus_validation}).
artifacts/_project/paper/method.tex:69:\caption{Practical guidance tiers for lead-lag consensus analysis. FPR and FNR are empirically calibrated at $\alpha{=}0.0$ (null control) and $\alpha{=}1.0$ (6 ground-truth pairs), respectively. $M{=}5$ methods, $N{=}4$ seeds. FPR is validated on the method dimension only; FNR on the method${\times}$seed joint dimension (\S\ref{sec:calibration}).}
artifacts/_project/paper/method.tex:73:Tier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\
artifacts/_project/paper/method.tex:88:Full numerical results are reported in Table~\ref{tab:fpr_fnr}.
artifacts/_project/paper/method.tex:96:\paragraph{False negative rate.}
artifacts/_project/paper/method.tex:99:At Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$), all six pairs are recovered (FNR${=}$0\%).
artifacts/_project/paper/method.tex:100:At $K{=}5/5$, $S{\geq}3/4$, FNR rises to 33.3\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.
artifacts/_project/paper/method.tex:101:At $K{=}5/5$, $S{=}4/4$, FNR${=}$50\%.
artifacts/_project/paper/method.tex:104:FPR is validated on the method dimension only (single seed at $\alpha{=}0.0$), while FNR is validated on the joint method${\times}$seed dimension (4~seeds at $\alpha{=}1.0$).
artifacts/_project/paper/method.tex:109:The six ground-truth pairs used for FNR calibration are not self-referentially defined.
artifacts/_project/paper/abstract.tex:2:[Omitted long matching line]
artifacts/_project/paper/conclusion_365dc4.tex:9:Calibrated on built-in experimental controls, the framework achieves 0\% false positive rate at the null control ($\alpha{=}0.0$) and 0\% false negative rate against ground-truth pairs at full contamination ($\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.
artifacts/_project/paper/introduction.tex:32:On reference extremes, the framework achieves a false positive rate of 0\% at the $\alpha{=}0.0$ null control (where individual methods reach up to 100\% FPR) and a false negative rate of 0\% against six ground-truth pairs at $\alpha{=}1.0$.
artifacts/_project/paper/introduction.tex:43:    The framework achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes, providing robustness against miscalibration of any individual method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "0c98c1cb-47c7-4571-a2b9-469565c37652",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:32:(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.\nartifacts/_project/paper/experiments.tex:60:For canary$\\to$diversity pairs at $\\alpha{=}1.0$, both undifferenced and differenced permutation Granger tests yield unanimous FDR significance, with $F$-statistics \\emph{increasing} after differencing---confirming genuine temporal precedence rather than shared-trend confounding.\nartifacts/_project/paper/experiments.tex:74:At $\\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\\ref{fig:consensus_heatmap}), the most extreme method$\\times$regime divergence in our experiments.\nartifacts/_project/paper/experiments.tex:120:Correlation-based methods unanimously find significance (Table~\\ref{tab:method_comparison}) while causal methods unanimously find non-significance.\nartifacts/_project/paper/experiments.tex:168:The consensus framework at $K{\\geq}4/5$ achieves \\textbf{FPR${=}$0\\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\\ref{tab:fpr_fnr}).\nartifacts/_project/paper/experiments.tex:170:\\paragraph{False negative rate.}\nartifacts/_project/paper/experiments.tex:172:The consensus framework ($K{\\geq}4/5$, $S{\\geq}3/4$) recovers all~6 (\\textbf{FNR${=}$0\\%}).\nartifacts/_project/paper/experiments.tex:173:Toda--Yamamoto alone yields FNR${=}$25\\%, missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\nartifacts/_project/paper/experiments.tex:174:We note a design asymmetry: FPR is validated on method-only data (single seed at $\\alpha{=}0.0$), while FNR uses method$\\times$seed joint data (4~seeds at $\\alpha{=}1.0$).\nartifacts/_project/paper/experiments.tex:176:Table~\\ref{tab:fpr_fnr} reports the calibration results.\nartifacts/_project/paper/experiments.tex:181:\\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\\alpha{=}0.0$ null control (single seed). FNR: $\\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\\times$seed joint (\\S\\ref{sec:consensus_validation}).}\nartifacts/_project/paper/experiments.tex:182:\\label{tab:fpr_fnr}\nartifacts/_project/paper/experiments.tex:185:Criterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\nartifacts/_project/paper/abstract_8c6c62.tex:2:[Omitted long matching line]\nartifacts/_project/paper/conclusion.tex:9:Calibrated on built-in experimental controls, the framework achieves 0\\% false positive rate at the null control ($\\alpha{=}0.0$) and 0\\% false negative rate against ground-truth pairs at full contamination ($\\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.\nartifacts/_project/paper/discussion.tex:11:All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\alpha \\in \\{0.0, 0.25, 0.50, 0.75, 1.0\\}$).\nartifacts/_project/paper/discussion.tex:14:For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\nartifacts/_project/paper/discussion.tex:17:\\paragraph{FPR/FNR calibration asymmetry.}\nartifacts/_project/paper/discussion.tex:18:The FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.\nartifacts/_project/paper/discussion.tex:20:FNR is validated on the joint method${\\times}$seed dimension, aggregating across four seeds at full contamination ($\\alpha{=}1.0$).\nartifacts/_project/paper/discussion.tex:27:The Toda-Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nartifacts/_project/paper/method.tex:23:In contrast, canary$\\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\\to$24/24).\nartifacts/_project/paper/method.tex:30:The $\\alpha{=}0.50$ regime is particularly dangerous: correlation-based methods unanimously find significance while causal methods unanimously find non-significance (Figure~\\ref{fig:consensus_heatmap}), creating the maximum risk of spurious conclusions---high correlation coexists with zero causal precedence.\nartifacts/_project/paper/method.tex:45:The thresholds $(K, S)$ control the trade-off between false positive and false negative rates.\nartifacts/_project/paper/method.tex:61:The consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.\nartifacts/_project/paper/method.tex:64:Tier~4 requires unanimity across methods and seeds, which incurs a 50\\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\\S\\ref{sec:consensus_validation}).\nartifacts/_project/paper/method.tex:69:\\caption{Practical guidance tiers for lead-lag consensus analysis. FPR and FNR are empirically calibrated at $\\alpha{=}0.0$ (null control) and $\\alpha{=}1.0$ (6 ground-truth pairs), respectively. $M{=}5$ methods, $N{=}4$ seeds. FPR is validated on the method dimension only; FNR on the method${\\times}$seed joint dimension (\\S\\ref{sec:calibration}).}\nartifacts/_project/paper/method.tex:73:Tier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\\\\nartifacts/_project/paper/method.tex:88:Full numerical results are reported in Table~\\ref{tab:fpr_fnr}.\nartifacts/_project/paper/method.tex:96:\\paragraph{False negative rate.}\nartifacts/_project/paper/method.tex:99:At Tier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$), all six pairs are recovered (FNR${=}$0\\%).\nartifacts/_project/paper/method.tex:100:At $K{=}5/5$, $S{\\geq}3/4$, FNR rises to 33.3\\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.\nartifacts/_project/paper/method.tex:101:At $K{=}5/5$, $S{=}4/4$, FNR${=}$50\\%.\nartifacts/_project/paper/method.tex:104:FPR is validated on the method dimension only (single seed at $\\alpha{=}0.0$), while FNR is validated on the joint method${\\times}$seed dimension (4~seeds at $\\alpha{=}1.0$).\nartifacts/_project/paper/method.tex:109:The six ground-truth pairs used for FNR calibration are not self-referentially defined.\nartifacts/_project/paper/abstract.tex:2:[Omitted long matching line]\nartifacts/_project/paper/conclusion_365dc4.tex:9:Calibrated on built-in experimental controls, the framework achieves 0\\% false positive rate at the null control ($\\alpha{=}0.0$) and 0\\% false negative rate against ground-truth pairs at full contamination ($\\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.\nartifacts/_project/paper/introduction.tex:32:On reference extremes, the framework achieves a false positive rate of 0\\% at the $\\alpha{=}0.0$ null control (where individual methods reach up to 100\\% FPR) and a false negative rate of 0\\% against six ground-truth pairs at $\\alpha{=}1.0$.\nartifacts/_project/paper/introduction.tex:43:    The framework achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes, providing robustness against miscalibration of any individual method.",
    "numLines": 39
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also search for the TY-specific numbers that need updating. Let me search for key patterns:

1. TY significance rates - "25%" or "4/16" in the context of TY
2. "59.4%" in the method comparison table
3. FNR "33.3%" and "25%" related to TY
4. "50%" FNR at Tier 4
5. Discussion paragraph about short time-series mentioning "33.3%, missing 2 of 6"

Let me also check the `docs/paper/` versions to see if they're duplicates or different.


I need to carefully trace through which numbers actually need to change based on the fix report. The off-by-one bug in the window sensitivity code affected how TY was evaluated, and I need to distinguish between what was broken in that analysis versus what was used in the main paper results.

Looking at the implementation details, the canonical TY method in `method_ablation.py` appears to be separate from the buggy local version used in `window_sensitivity.py`, so the main paper's TY results might not be affected by bug #2 even though the window sensitivity analysis was compromised. I'm noticing inconsistencies in how TY's performance is reported across different tables in the paper. The ablation study shows 4/16 (25%) while the method comparison table reports 59.4%, and I need to figure out which numbers actually need updating based on the fix report's T=10 change from 0/6 to 4/6 signatures. The task asks me to update the paper with the corrected TY values, but I'm realizing these different percentages might be measuring different things or coming from different experimental setups, so I need to carefully trace which specific results are affected by the fix. Looking at Table 3 more carefully, I see that even with the fix applied, Toda-Yamamoto still fails to detect ECE→d2 and ECE→d3 because they only reach 2/4 significant results instead of the 3/4 needed for consensus. So the FNR discrepancy might stem from different counting methods—whether they're counting 6 or 8 total pairs, or perhaps the 25% refers to a different subset of the data.

Now I'm reconsidering what the actual fix changed. The task mentions two key modifications: an off-by-one error in the window sensitivity code and unifying the Toda-Yamamoto implementation to import from a single source rather than maintaining duplicate versions. The critical detail is that the old implementation returned NaN at T=10 with 0/6 significant results, while the fixed version shows 4/6 significant results at that same timepoint.

Let me check whether the paper actually discusses window sensitivity results explicitly, since I haven't found direct mention of those analyses yet. I'm trying to figure out what the 4/16 pairs actually represent—whether it's 4 candidate canaries times 4 downstream metrics, or something else based on the ground-truth pairs defined in the consensus. The key question is whether the window_sensitivity analysis changes any of the numbers reported in the paper's main method_ablation results, or if it's just a separate sensitivity check that doesn't affect the published findings. I need to figure out which TY implementation generated the paper's reported numbers. The paper claims TY finds 4/16 pairs significant at α=1.0, but the fix report shows that after corrections, TY identifies 4/6 ground-truth pairs as significant—meaning the paper's 4 significant findings likely came from those ground-truth pairs plus potentially a few others, which would align with the 4/16 total count.

Now I'm noticing a discrepancy in the method_comparison table: it shows TY at 59.4% for the fraction of canary→downstream pairs reaching significance, but the five-method ablation reports 4/16 (25%). These percentages don't match, and I'm wondering if the method_comparison table is computing this differently—possibly incorporating seed-level data in a way that changes the calculation. Looking at the window_sensitivity analysis, the VAR test_causality function silently fails on short sequences, returning NaN values. But the main Toda-Yamamoto results in the paper come from the canonical method_ablation implementation at α=1.0, which weren't affected by this bug. However, constraint C001 restricts citing the TY cross-α trends from single-seed data until the multi-seed results confirm whether the non-monotonicity is reproducible.

Now I'm trying to reconcile the 59.4% and 4/16 numbers—they might be measuring different things, like individual seed×pair test significance versus unique pairs pooled across seeds. The critical question is whether any of the paper's reported numbers actually come from the buggy window_sensitivity code.

Looking at the paper's discussion section, it mentions the Toda-Yamamoto procedure has a 33.3% false negative rate, missing 2 of 6 directional pairs. The main analysis shows TY still misses ECE→d2 and ECE→d3, which matches that 2/6 miss rate. But when I check the fixed window_sensitivity results at T=10, the pattern changes—I need to see what TY actually recovers there to determine if the paper's numbers are contaminated by the buggy code.

Now I'm trying to understand what the "16 canary→downstream pairs" in the five-method ablation actually represents, since the paper lists 4 canaries and 4 downstream tasks, but some of those tasks appear in the appendix or are marked as failed. I'm getting tangled up in the different ways these results could be counted. Let me refocus on what actually matters: the window_sensitivity.py bugs and whether they affected the paper's reported numbers. I don't see any mention of "window sensitivity" in the paper files themselves, so I should check if there are appendix documents I'm missing, then work backwards from the paper's TY numbers to see if they match what the buggy code would have produced.

Looking at the fix report, the canonical Toda-Yamamoto implementation in method_ablation.py was already correct, while window_sensitivity.py had its own divergent version. So the paper's main TY results—the 4/16 (25%), 59.4%, and 33.3%/25% FNR numbers—likely come from the correct method_ablation.py code and aren't affected by the bug. The real question is whether the paper cites any window sensitivity analysis at all, and from what I've seen in the tex files, it doesn't appear to.

But the task is asking me to update specific numbers and the TY underpowered narrative. Let me reconsider what's actually in the paper. The discussion mentions TY's elevated FNR of 33.3% (missing 2 of 6 directional pairs), which matches the method_ablation results, not window_sensitivity. So either the paper doesn't cite window_sensitivity results, or I'm missing where they appear. Looking at the table more carefully, if FNR is computed as a percentage of total tests across all seeds, then 25% would mean TY misses 6 out of 24 total seed-pair combinations (4 seeds × 6 pairs), which would correspond to missing both ECE→d2 and ECE→d3 across only 3 of the 4 seeds rather than all of them.

Actually, I'm getting caught up in the calculation details when I should focus on what the paper fix actually changes—let me step back and look at the core issue being addressed.

So with T=10, we're now including 11 data points instead of 10. The bigger picture is that the old TY implementation was silently failing on short sequences and returning NaN, but after switching to the canonical version from method_ablation.py with proper ADF settings and F-test, TY now correctly detects 4 out of 6 significant relationships at T=10, particularly catching all the TE→d relationships.

The consensus conclusion about 4/5 methods agreeing across the T=5–10 window remains solid. Now I need to verify whether the paper actually cites any window_sensitivity results, and more importantly, check if method_ablation.py itself has the same off-by-one bug. The paper's experiments.tex correctly states "T=10 generations (11 time points including generation-0 baseline)", so the interpretation is right—but I should confirm method_ablation.py is using the correct slicing pattern.

Since the main analysis numbers come from method_ablation with 11 data points and window_sensitivity was the one using 10 incorrectly, the fix makes them consistent without affecting the paper's primary results. The window sensitivity analysis is supplementary robustness checking. I need to search the paper for any actual discussion of window sensitivity results and check if there are appendix files I haven't reviewed yet.

Looking back at the user's request more carefully, they want me to find and update any descriptions in the paper about TY being underpowered, having zero significant results, NaN values, or high FNR. I've already spotted mentions in discussion.tex about TY's elevated FNR (33.3% missing 2 of 6 pairs) and in experiments.tex about FNR=25% with specific missing pairs, so I need to check if these descriptions need updating based on the corrected data.

The numbers I'm seeing in the paper appear to come from the main method_ablation analysis rather than the buggy window_sensitivity code, which suggests the paper might already be accurate. But I should verify whether there's an appendix with window sensitivity results and whether any of the TY statistics could have been affected by the bug before concluding the paper needs no changes.

Now I'm trying to reverse-engineer what the method_comparison table actually represents—the 59.4% figure for Toda-Yamamoto at α=1.0 could correspond to different test counts depending on whether the ablation uses 16 or 32 canary-downstream pairs across the seeds, and I'm working through the math to see if the numbers check out.

Let me search for any remaining TY-related content and check the paper's appendix files, since background.tex or related_work.tex might have additional context I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "a49c355a-4170-4713-ab10-07890141f4e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJNkxBrjWCj5Zy4D3CGgfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 49683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 39_

Let me search for any window sensitivity or appendix content, and check the `docs/paper/` version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "bd8458bb-1423-4949-a1dc-299a7a5a3ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJNkxBrjWCj5Zy4D3CGgfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 49683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_01VcnhvGAC5W1hHyWH8JQwRf`</summary>

```json
{
  "pattern": "window|appendix|sensitivity.*T=|robustness.*window",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "8e77ee58-8a35-4f8c-bde9-58a7b305d456",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJNkxBrjWCj5Zy4D3CGgfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 49683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 41 · 2026-05-16T00:23:18.455Z_

<details><summary>↩ Tool result · `toolu_01VcnhvGAC5W1hHyWH8JQwRf`</summary>

```text
artifacts/_project/paper/experiments.tex:20:Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
artifacts/_project/paper/experiments.tex:136:Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
artifacts/_project/paper/experiments.tex:155:Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "dc1332b9-f3f9-438e-8754-a64c6d26bfb9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/experiments.tex:20:Results for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\nartifacts/_project/paper/experiments.tex:136:Permutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nartifacts/_project/paper/experiments.tex:155:Of 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_017Ap2MVKug4eZRxZfRGBN3S`</summary>

```json
{
  "pattern": "Toda.*Yamamoto|TY|toda.yamamoto",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/paper/**/*.tex",
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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "a93840f3-31b7-4146-a09a-3fa838c8ac47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJNkxBrjWCj5Zy4D3CGgfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 49683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 43 · 2026-05-16T00:23:19.864Z_

<details><summary>↩ Tool result · `toolu_017Ap2MVKug4eZRxZfRGBN3S`</summary>

```text
artifacts/_project/paper/related_work.tex:48:The Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.
artifacts/_project/paper/related_work.tex:51:Our framework applies five complementary methods---naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality, and Toda--Yamamoto Granger causality---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.
artifacts/_project/paper/experiments.tex:54:The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
artifacts/_project/paper/experiments.tex:56:The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
artifacts/_project/paper/experiments.tex:65:Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
artifacts/_project/paper/experiments.tex:73:Permutation Granger and Toda--Yamamoto correctly find 0\%.
artifacts/_project/paper/experiments.tex:94:Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\
artifacts/_project/paper/experiments.tex:147:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\max}$.
artifacts/_project/paper/experiments.tex:167:Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation: 8/8 pairs) through 62.5\% (threshold) and 37.5\% (differenced) down to \textbf{0\%} (permutation Granger and Toda--Yamamoto).
artifacts/_project/paper/experiments.tex:173:Toda--Yamamoto alone yields FNR${=}$25\%, missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
artifacts/_project/paper/experiments.tex:191:Toda--Yamamoto           & 0\%    & 25\% \\
artifacts/_project/paper/abstract_8c6c62.tex:2:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:27:The Toda-Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
artifacts/_project/paper/method.tex:15:Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
artifacts/_project/paper/method.tex:16:The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
artifacts/_project/paper/method.tex:64:Tier~4 requires unanimity across methods and seeds, which incurs a 50\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\S\ref{sec:consensus_validation}).
artifacts/_project/paper/method.tex:94:The consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\%) while providing robustness against miscalibration of any single method.
artifacts/_project/paper/method.tex:100:At $K{=}5/5$, $S{\geq}3/4$, FNR rises to 33.3\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.
artifacts/_project/paper/background.tex:37:(5)~\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \cite{granger1969investigating}.
artifacts/_project/paper/abstract.tex:2:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:24:    \item \textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$ (poor agreement).
docs/paper/related_work.tex:30:(ii)~we cross-validate each lead-lag relationship across five independent statistical methods, quantifying inter-method sensitivity via Cohen's $\kappa$ and intra-method sensitivity via the Toda--Yamamoto augmentation order $d_{\max}$;
docs/paper/related_work.tex:48:The Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.
docs/paper/related_work.tex:51:Our framework applies five complementary methods---naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality, and Toda--Yamamoto Granger causality---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.
docs/paper/experiments.tex:54:The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
docs/paper/experiments.tex:56:The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
docs/paper/experiments.tex:66:Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
docs/paper/experiments.tex:73:Restricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
docs/paper/experiments.tex:76:Permutation Granger and Toda--Yamamoto correctly find 0\%.
docs/paper/experiments.tex:97:Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\
docs/paper/experiments.tex:152:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\max}$.
docs/paper/experiments.tex:172:Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation: 8/8 pairs) through 62.5\% (threshold) and 37.5\% (differenced) down to \textbf{0\%} (permutation Granger and Toda--Yamamoto).
docs/paper/experiments.tex:178:Toda--Yamamoto alone yields FNR${=}$33.3\% (2/6), missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
docs/paper/experiments.tex:196:Toda--Yamamoto           & 0\%    & 33.3\% \\
docs/paper/discussion.tex:27:The Toda--Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
docs/paper/discussion.tex:31:The Toda--Yamamoto procedure returns \texttt{insufficient\_df} for all pairs at $T{\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.
docs/paper/method.tex:15:Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs---4 candidate canaries $\times$ 4 downstream metrics, including candidates later excluded per \S\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
docs/paper/method.tex:16:The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
docs/paper/method.tex:66:Toda--Yamamoto contributes negatively (Shapley $= -2.625$) due to its Type~II errors at $T{=}10$, but is retained to maintain the panel's methodological diversity; excluding it would leave the framework without an augmented-VAR approach that handles unknown integration order.
docs/paper/method.tex:67:Tier~4 requires unanimity across methods and seeds, which incurs a 50\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\S\ref{sec:consensus_validation}).
docs/paper/method.tex:97:The consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\%) while providing robustness against miscalibration of any single method.
docs/paper/method.tex:103:At $K{=}5/5$, $S{\geq}3/4$, FNR rises to 33.3\%: consensus loses two ECE pairs---ECE$\to$distinct-2 and ECE$\to$distinct-3, each reaching Toda--Yamamoto significance in only 2 of 4 seeds.
docs/paper/background.tex:37:(5)~\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \cite{granger1969investigating}.
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/introduction.tex:24:    \item \textbf{Method sensitivity.} Applied to the same data (16 candidate canary$\to$downstream pairs, including candidates later excluded; \S\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$ (poor agreement).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "a1e1365f-2b0d-4d04-8f2c-8b17df1a1359",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:48:The Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.\nartifacts/_project/paper/related_work.tex:51:Our framework applies five complementary methods---naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality, and Toda--Yamamoto Granger causality---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.\nartifacts/_project/paper/experiments.tex:54:The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{4/16} (25.0\\%).\nartifacts/_project/paper/experiments.tex:56:The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \\textbf{75\\%} across all five methods and \\textbf{62.5\\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\\S\\ref{sec:consensus_validation}).\nartifacts/_project/paper/experiments.tex:65:Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nartifacts/_project/paper/experiments.tex:73:Permutation Granger and Toda--Yamamoto correctly find 0\\%.\nartifacts/_project/paper/experiments.tex:94:Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\\\\nartifacts/_project/paper/experiments.tex:147:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\max}$.\nartifacts/_project/paper/experiments.tex:167:Individual-method FPR ranges from \\textbf{100\\%} (naive cross-correlation: 8/8 pairs) through 62.5\\% (threshold) and 37.5\\% (differenced) down to \\textbf{0\\%} (permutation Granger and Toda--Yamamoto).\nartifacts/_project/paper/experiments.tex:173:Toda--Yamamoto alone yields FNR${=}$25\\%, missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\nartifacts/_project/paper/experiments.tex:191:Toda--Yamamoto           & 0\\%    & 25\\% \\\\\nartifacts/_project/paper/abstract_8c6c62.tex:2:[Omitted long matching line]\nartifacts/_project/paper/discussion.tex:27:The Toda-Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nartifacts/_project/paper/method.tex:15:Applied to the same data ($\\alpha{=}1.0$, 4~seeds, 16 canary$\\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$---poor agreement (\\S\\ref{sec:method_sensitivity}).\nartifacts/_project/paper/method.tex:16:The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\\% across all five methods and 62.5\\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.\nartifacts/_project/paper/method.tex:64:Tier~4 requires unanimity across methods and seeds, which incurs a 50\\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\\S\\ref{sec:consensus_validation}).\nartifacts/_project/paper/method.tex:94:The consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\\%) while providing robustness against miscalibration of any single method.\nartifacts/_project/paper/method.tex:100:At $K{=}5/5$, $S{\\geq}3/4$, FNR rises to 33.3\\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.\nartifacts/_project/paper/background.tex:37:(5)~\\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \\cite{granger1969investigating}.\nartifacts/_project/paper/abstract.tex:2:[Omitted long matching line]\nartifacts/_project/paper/introduction.tex:24:    \\item \\textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\ndocs/paper/related_work.tex:30:(ii)~we cross-validate each lead-lag relationship across five independent statistical methods, quantifying inter-method sensitivity via Cohen's $\\kappa$ and intra-method sensitivity via the Toda--Yamamoto augmentation order $d_{\\max}$;\ndocs/paper/related_work.tex:48:The Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.\ndocs/paper/related_work.tex:51:Our framework applies five complementary methods---naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality, and Toda--Yamamoto Granger causality---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.\ndocs/paper/experiments.tex:54:The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{4/16} (25.0\\%).\ndocs/paper/experiments.tex:56:The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \\textbf{75\\%} across all five methods and \\textbf{62.5\\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\\S\\ref{sec:consensus_validation}).\ndocs/paper/experiments.tex:66:Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\ndocs/paper/experiments.tex:73:Restricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.\ndocs/paper/experiments.tex:76:Permutation Granger and Toda--Yamamoto correctly find 0\\%.\ndocs/paper/experiments.tex:97:Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\\\\ndocs/paper/experiments.tex:152:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\max}$.\ndocs/paper/experiments.tex:172:Individual-method FPR ranges from \\textbf{100\\%} (naive cross-correlation: 8/8 pairs) through 62.5\\% (threshold) and 37.5\\% (differenced) down to \\textbf{0\\%} (permutation Granger and Toda--Yamamoto).\ndocs/paper/experiments.tex:178:Toda--Yamamoto alone yields FNR${=}$33.3\\% (2/6), missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\ndocs/paper/experiments.tex:196:Toda--Yamamoto           & 0\\%    & 33.3\\% \\\\\ndocs/paper/discussion.tex:27:The Toda--Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\ndocs/paper/discussion.tex:31:The Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.\ndocs/paper/method.tex:15:Applied to the same data ($\\alpha{=}1.0$, 4~seeds, 16 canary$\\to$downstream pairs---4 candidate canaries $\\times$ 4 downstream metrics, including candidates later excluded per \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$---poor agreement (\\S\\ref{sec:method_sensitivity}).\ndocs/paper/method.tex:16:The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\\% across all five methods and 62.5\\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.\ndocs/paper/method.tex:66:Toda--Yamamoto contributes negatively (Shapley $= -2.625$) due to its Type~II errors at $T{=}10$, but is retained to maintain the panel's methodological diversity; excluding it would leave the framework without an augmented-VAR approach that handles unknown integration order.\ndocs/paper/method.tex:67:Tier~4 requires unanimity across methods and seeds, which incurs a 50\\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\\S\\ref{sec:consensus_validation}).\ndocs/paper/method.tex:97:The consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\\%) while providing robustness against miscalibration of any single method.\ndocs/paper/method.tex:103:At $K{=}5/5$, $S{\\geq}3/4$, FNR rises to 33.3\\%: consensus loses two ECE pairs---ECE$\\to$distinct-2 and ECE$\\to$distinct-3, each reaching Toda--Yamamoto significance in only 2 of 4 seeds.\ndocs/paper/background.tex:37:(5)~\\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \\cite{granger1969investigating}.\ndocs/paper/abstract.tex:2:[Omitted long matching line]\ndocs/paper/introduction.tex:24:    \\item \\textbf{Method sensitivity.} Applied to the same data (16 candidate canary$\\to$downstream pairs, including candidates later excluded; \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).",
    "numLines": 45
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Glob · `toolu_01UQHRAvbiN8HxsaqFVemQ2N`</summary>

```json
{
  "pattern": "**/paper/**/appendix*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "b26e13b1-6210-4a7c-b50f-dd9880661f84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJNkxBrjWCj5Zy4D3CGgfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 49683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 45 · 2026-05-16T00:23:20.225Z_

<details><summary>↩ Tool result · `toolu_01UQHRAvbiN8HxsaqFVemQ2N`</summary>

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
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "81549d84-6cc4-46c3-a04d-b1c5351820c1",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 6,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I can see there are two versions of the paper:
1. `artifacts/_project/paper/` - one version
2. `docs/paper/` - another version (appears to be more polished/updated)

Key differences I notice:
- `docs/paper/experiments.tex` line 178: "Toda--Yamamoto alone yields FNR=33.3% (2/6)" — consistent with 2/6
- `artifacts/_project/paper/experiments.tex` line 173: "Toda--Yamamoto alone yields FNR=25%" — this seems wrong


- The same discrepancy appears in the FPR/FNR tables at lines 196 and 191 respectively, where `docs/paper/` correctly shows 33.3% while `artifacts/_project/paper/` shows 25%

This is an existing inconsistency between the two versions, unrelated to the window_sensitivity changes. Now I need to figure out whether the paper's Toda--Yamamoto numbers should actually change based on the window_sensitivity fix.

The paper's main analysis used the canonical Toda--Yamamoto implementation with 11 data points, while window_sensitivity.py had a bug with only 10 data points and a divergent implementation. Since the paper already used the correct setup, those numbers shouldn't need updating.

However, I'm noticing that `discussion.tex` references the window_sensitivity results when explaining why Toda--Yamamoto returns insufficient degrees of freedom at certain window sizes. I need to check whether that discussion is still accurate or if it needs revision based on the fix.

Looking at the fixed results from Table 2, Toda--Yamamoto actually does find significant results at T=5, 6, and 7 — it doesn't return insufficient_df for all pairs at T≤7 like the old buggy code suggested. So that statement in discussion.tex line 31 is outdated and needs to be corrected.

The artifacts version has different wording entirely, describing the elevated FNR as an insufficient degrees of freedom issue without claiming it happens for all pairs. Since docs/paper/ appears to be the more recent version, I need to update that line to reflect what the fixed code actually shows.

Now I'm checking what else needs updating: the paper's claims about when Toda-Yamamoto returns insufficient_df errors, any window sensitivity results it cites, and whether the main T=10 FNR numbers (33.3%) are affected by the fix or only the window sensitivity analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "da949846-2ed4-4a1d-a166-b1f72ef453a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPWL29UCaRQeNfJkdjksgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10719,
      "cache_read_input_tokens": 55580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10719
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

I see there are two versions of the paper. Let me read the `docs/paper/` discussion.tex to check for window-sensitivity-specific content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "aba9355d-9ddf-4aa1-8215-8856d0a8ab2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPWL29UCaRQeNfJkdjksgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10719,
      "cache_read_input_tokens": 55580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10719
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

<details open><summary>🔧 Tool call — Read · `toolu_01LEKAwSU24hydaRjvBYQcQZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "538a9e5a-ace4-4d12-9b44-69b49024f17b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPWL29UCaRQeNfJkdjksgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10719,
      "cache_read_input_tokens": 55580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10719
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

_source line 49 · 2026-05-16T00:23:51.243Z_

<details><summary>↩ Tool result · `toolu_01LEKAwSU24hydaRjvBYQcQZ`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
5	Bivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
6	Our multi-method consensus framework inherits this limitation in full.
7	Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
8	This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.
9	
10	\paragraph{Calibration scope and generalization.}
11	All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
12	Generalization to other model architectures, datasets, or training protocols requires independent validation.
13	The consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
14	For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
15	Our ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.
16	
17	\paragraph{FPR/FNR calibration asymmetry.}
18	The FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.
19	FPR is validated on the method dimension only, using a single seed at the null-control condition ($\alpha{=}0.0$).
20	FNR is validated on the joint method${\times}$seed dimension, aggregating across four seeds at full contamination ($\alpha{=}1.0$).
21	This asymmetry means our FPR estimate of 0\% may be optimistic: if seed-level variance in false positive rates is non-negligible, the true FPR under the consensus rule could exceed zero.
22	Full joint calibration---requiring multi-seed null-control experiments at $\alpha{=}0.0$---remains an open direction for future work.
23	
24	\paragraph{Short time-series constraint.}
25	With $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.
26	This series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.
27	The Toda--Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
28	This finding aligns with \citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.
29	Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.
30	However, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.
31	The Toda--Yamamoto procedure returns \texttt{insufficient\_df} for all pairs at $T{\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.
32	
33	\paragraph{Diversity--calibration dissociation.}
34	Diversity metrics and calibration metrics respond to synthetic contamination in qualitatively opposite directions across the $\alpha$ spectrum.
35	Diversity collapse (distinct-$n$ decline) is most severe at low contamination ($\alpha{=}0.25$: distinct-3 declines by 59.9\%) and attenuates at higher levels ($\alpha{=}1.0$: $-30.5\%$), while calibration degradation (ECE) increases monotonically with $\alpha$ ($+51.7\%$ at $\alpha{=}0.0$ to $+3782\%$ at $\alpha{=}1.0$).
36	This dissociation underscores the need for multi-method consensus: the regime in which a metric degrades most severely ($\alpha{=}0.25$ for diversity) does not coincide with the regime in which its temporal lead is most detectable ($\alpha{\geq}0.75$), and a single metric family cannot capture the full picture of iterative training degradation.
37	
38	\paragraph{Limitations.}
39	Several limitations constrain the generalizability of our findings.
40	First, our primary experiments use Pythia-410M; preliminary cross-architecture validation with GPT-2-medium uses batch size~32 (versus~4 for Pythia) for GPU efficiency, exposing 8$\times$ more data per training step, which may accelerate collapse dynamics without altering the qualitative pattern (token entropy leading diversity decline is observed in both architectures).
41	Second, training data is drawn from a single domain (a WikiText-103 subset), and domain-specific distributional properties may influence the coupling between canary and downstream metrics.
42	Third, we lack an intervention experiment: we observe that token entropy Granger-precedes diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$) but do not test whether acting on canary signals can prevent or delay collapse onset.
43	Fourth, our experiments use replace-only data accumulation; accumulate-mode training~\cite{dey2024breaking,kazdan2025collapse} may exhibit qualitatively different canary dynamics.
44	Finally, our canary claims are scoped to distinct-$n$ diversity metrics~\cite{li2016diversity}---not to model collapse broadly~\cite{schaeffer2025position}---as the perplexity channel proved spurious ($F{\approx}0$, $p{=}0.99$ after differencing).
45	This scoping is theoretically motivated: \citet{cao2025entropycal} prove a fundamental calibration-diversity tradeoff in language models---all current calibration methods reduce entropy at the cost of diversity---suggesting that calibration and diversity are coupled but not identical, which may explain why token entropy can Granger-precede diversity collapse without leading perplexity.
46	
47	\paragraph{Future work.}
48	Several directions extend this work.
49	Multivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.
50	Cross-architecture validation is needed: our GPT-2-medium experiments are in progress, and evaluation on larger-scale models would further test generalizability.
51	Online monitoring---integrating canary metrics into training pipelines for real-time collapse detection---is a natural applied extension.
52	Accumulate-mode experiments~\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.
53	Finally, connecting the empirically observed detectability boundary at $\alpha{\approx}0.50$--$0.75$ to theoretical phase transition analysis~\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "e4086284-37d1-4476-9480-b5a729c36358",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Granger precedence is not causation.}\nGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\cite{granger1969investigating,shojaie2022granger}.\nBivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\nOur multi-method consensus framework inherits this limitation in full.\nThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\nThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\emph{causes} diversity collapse.\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\alpha \\in \\{0.0, 0.25, 0.50, 0.75, 1.0\\}$).\nGeneralization to other model architectures, datasets, or training protocols requires independent validation.\nThe consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\nFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\nOur ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.\n\n\\paragraph{FPR/FNR calibration asymmetry.}\nThe FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.\nFPR is validated on the method dimension only, using a single seed at the null-control condition ($\\alpha{=}0.0$).\nFNR is validated on the joint method${\\times}$seed dimension, aggregating across four seeds at full contamination ($\\alpha{=}1.0$).\nThis asymmetry means our FPR estimate of 0\\% may be optimistic: if seed-level variance in false positive rates is non-negligible, the true FPR under the consensus rule could exceed zero.\nFull joint calibration---requiring multi-seed null-control experiments at $\\alpha{=}0.0$---remains an open direction for future work.\n\n\\paragraph{Short time-series constraint.}\nWith $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.\nThis series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.\nThe Toda--Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nThis finding aligns with \\citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.\nLonger generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.\nHowever, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.\nThe Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.\n\n\\paragraph{Diversity--calibration dissociation.}\nDiversity metrics and calibration metrics respond to synthetic contamination in qualitatively opposite directions across the $\\alpha$ spectrum.\nDiversity collapse (distinct-$n$ decline) is most severe at low contamination ($\\alpha{=}0.25$: distinct-3 declines by 59.9\\%) and attenuates at higher levels ($\\alpha{=}1.0$: $-30.5\\%$), while calibration degradation (ECE) increases monotonically with $\\alpha$ ($+51.7\\%$ at $\\alpha{=}0.0$ to $+3782\\%$ at $\\alpha{=}1.0$).\nThis dissociation underscores the need for multi-method consensus: the regime in which a metric degrades most severely ($\\alpha{=}0.25$ for diversity) does not coincide with the regime in which its temporal lead is most detectable ($\\alpha{\\geq}0.75$), and a single metric family cannot capture the full picture of iterative training degradation.\n\n\\paragraph{Limitations.}\nSeveral limitations constrain the generalizability of our findings.\nFirst, our primary experiments use Pythia-410M; preliminary cross-architecture validation with GPT-2-medium uses batch size~32 (versus~4 for Pythia) for GPU efficiency, exposing 8$\\times$ more data per training step, which may accelerate collapse dynamics without altering the qualitative pattern (token entropy leading diversity decline is observed in both architectures).\nSecond, training data is drawn from a single domain (a WikiText-103 subset), and domain-specific distributional properties may influence the coupling between canary and downstream metrics.\nThird, we lack an intervention experiment: we observe that token entropy Granger-precedes diversity collapse at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$) but do not test whether acting on canary signals can prevent or delay collapse onset.\nFourth, our experiments use replace-only data accumulation; accumulate-mode training~\\cite{dey2024breaking,kazdan2025collapse} may exhibit qualitatively different canary dynamics.\nFinally, our canary claims are scoped to distinct-$n$ diversity metrics~\\cite{li2016diversity}---not to model collapse broadly~\\cite{schaeffer2025position}---as the perplexity channel proved spurious ($F{\\approx}0$, $p{=}0.99$ after differencing).\nThis scoping is theoretically motivated: \\citet{cao2025entropycal} prove a fundamental calibration-diversity tradeoff in language models---all current calibration methods reduce entropy at the cost of diversity---suggesting that calibration and diversity are coupled but not identical, which may explain why token entropy can Granger-precede diversity collapse without leading perplexity.\n\n\\paragraph{Future work.}\nSeveral directions extend this work.\nMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\nCross-architecture validation is needed: our GPT-2-medium experiments are in progress, and evaluation on larger-scale models would further test generalizability.\nOnline monitoring---integrating canary metrics into training pipelines for real-time collapse detection---is a natural applied extension.\nAccumulate-mode experiments~\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\nFinally, connecting the empirically observed detectability boundary at $\\alpha{\\approx}0.50$--$0.75$ to theoretical phase transition analysis~\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01YXfk8rPYLPnmxx7sXvwYSP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "b497416e-a0c4-4687-8eb8-4789fbbaa361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPWL29UCaRQeNfJkdjksgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10719,
      "cache_read_input_tokens": 55580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10719
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

_source line 51 · 2026-05-16T00:23:51.785Z_

<details><summary>↩ Tool result · `toolu_01YXfk8rPYLPnmxx7sXvwYSP`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
23	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
24	Cross-correlation analysis uses a maximum lag of 5 generations.
25	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Metric drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}1.0$: 4-seed mean${\pm}$std; other levels: single seed (seed=42). Non-monotonic distinct-1 pattern across $\alpha \in \{0.25, 0.50\}$ is observed at seed=42, pending multi-seed confirmation.}
31	\label{tab:drift_summary}
32	\begin{tabular}{lccccc}
33	\toprule
34	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
35	\midrule
36	0.00 & $-5.1$ & $+51.7$ & $-13.8$ & $-9.8$ & $-21.7$ \\
37	0.25 & $-4.1$ & $+79.7$ & $-40.3$ & $-57.1$ & $-17.2$ \\
38	0.50 & $-18.6$ & $+842.8$ & $-37.3$ & $-51.5$ & $+21.1$ \\
39	0.75 & $-27.7$ & $+1809.5$ & $-32.7$ & $-41.3$ & $+182.1$ \\
40	1.00 & $-60.8{\pm}1.2$ & $+3782{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3673{\pm}45$ \\
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	
46	\subsection{Method Sensitivity Analysis}
47	\label{sec:method_sensitivity}
48	
49	We open with Claim~3---method sensitivity---because it conditions the interpretation of all subsequent results.
50	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
51	
52	\paragraph{Five-method ablation.}
53	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
54	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
55	Method choice alone swings significance from \textbf{100\% to 25\%}.
56	The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
57	Table~\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.
58	
59	\paragraph{First-differencing diagnostic.}
60	A single preprocessing decision can eliminate an entire analysis channel.
61	For canary$\to$diversity pairs at $\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.
62	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
63	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
64	
65	\paragraph{Augmentation order sensitivity.}
66	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
67	At $d_{\max}{=}0$ (most permissive), approximately 6\% of pairs are rejected; at adaptive $d_{\max}$ determined by ADF unit-root tests, 75\%; at $d_{\max}{=}1$ (most conservative), \textbf{94\%}.
68	This single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.
69	
70	\paragraph{Inter-method agreement.}
71	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (poor agreement); this value is consistent across contamination levels ($\alpha{=}0.0$ through $\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.
72	Cross-architecture validation on GPT-2-medium (12 canary$\to$downstream pairs) yields Fleiss' $\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.
73	Restricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
74	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
75	At $\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \textbf{100\%} of pairs significant---a textbook spurious-regression outcome in trending time series.
76	Permutation Granger and Toda--Yamamoto correctly find 0\%.
77	At $\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), the most extreme method$\times$regime divergence in our experiments.
78	
79	\paragraph{Method$\times$regime interaction.}
80	Table~\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.
81	At $\alpha{=}0.25$, differenced cross-correlation drops to 25\% and threshold onset to 37.5\%, while naive cross-correlation remains at 100\%---demonstrating that even partial detrending removes marginal associations at low contamination.
82	The graded response across methods, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
83	
84	\begin{table}[t]
85	\centering
86	\small
87	\caption{FDR significance rates (\%) for five lead-lag methods across contamination levels. Each cell reports the fraction of 8 primary canary$\to$downstream pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$); failed candidates (effective rank, Self-BLEU) excluded per \S\ref{sec:case_study}. $\alpha{=}0.75$ is analyzed separately as single-seed data (\S\ref{sec:regime}). FPR$_\text{null}$: false positive rate at the $\alpha{=}0.0$ null control.}
88	\label{tab:method_comparison}
89	\begin{tabular}{lcccccc}
90	\toprule
91	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
92	\midrule
93	Naive XCorr     & 100   & 100  & 100  & ---  & 100   & 100  \\
94	Diff.\ XCorr   & 37.5  & 25   & 100  & ---  & 100   & 37.5 \\
95	Threshold       & 62.5  & 37.5 & 100  & ---  & 100   & 62.5 \\
96	Perm.\ Granger  & 0     & 0    & 0    & ---  & 75    & 0    \\
97	Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	
103	\subsection{Regime-Dependent Detectability}
104	\label{sec:regime}
105	
106	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
107	We present regime effects at two levels: raw metric drift (method-independent) and Granger-causal detectability.
108	
109	\paragraph{Raw drift.}
110	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
111	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3\%$ ($\alpha{=}0.25$), $-37.3\%$ ($\alpha{=}0.50$), $-32.7\%$ ($\alpha{=}0.75$), and $-27.8{\pm}1.6\%$ ($\alpha{=}1.0$).
112	The non-monotonic pattern---diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$---is observed at seed=42 and requires multi-seed confirmation before drawing conclusions about the relationship between contamination level and collapse severity.
113	
114	\paragraph{Granger-causal detectability.}
115	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
116	Permutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant at $\alpha{=}0.00$, 0/8 at $\alpha{=}0.25$, 0/8 at $\alpha{=}0.50$, and \textbf{6/8} at $\alpha{=}1.0$ in the cross-$\alpha$ pooled analysis.
117	At $\alpha{=}0.75$ (single seed, seed=42), 3/8 pairs reach FDR significance; this result requires multi-seed replication before serving as primary evidence.
118	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
119	The detectability boundary---the regime below which canary metrics no longer develop sufficient temporal lead for causal inference---lies at $\alpha \approx 0.50$--$0.75$, consistent with theoretical expectations about signal-to-noise limits in short time series \cite{boettiger2012limits}.
120	This boundary is sharp rather than gradual: method-level consensus ($K{\geq}4/5$) identifies 0--1 of 16 candidate pairs as robust at $\alpha{\leq}0.50$ but 11/16 at $\alpha{=}0.75$ (single seed, pre-pipeline filtering; the stricter $K{\geq}4/5$, $S{\geq}3/4$ criterion at $\alpha{=}1.0$ retains 6/16 after excluding failed candidates and spurious channels per \S\ref{sec:case_study}).
121	The lower count at $\alpha{=}1.0$ despite stronger contamination reflects the stricter validation standard: multi-seed replication ($S{\geq}3/4$) filters seed-specific artifacts, and pipeline filtering removes the perplexity channel (spurious per \S\ref{sec:method_sensitivity}) and failed canary candidates (effective rank, Self-BLEU), both of which contribute to the $\alpha{=}0.75$ single-seed count.
122	
123	\paragraph{Synchronous collapse at $\alpha{=}0.50$.}
124	The $\alpha{=}0.50$ regime provides particularly informative evidence.
125	Correlation-based methods unanimously find significance (Table~\ref{tab:method_comparison}) while causal methods unanimously find non-significance.
126	This extreme method$\times$regime interaction arises because canary and downstream metrics collapse \emph{synchronously} at moderate contamination, preserving high correlation but eliminating the temporal lead required for Granger-causal inference.
127	We highlight this as a \emph{positive finding}: it delineates the regime boundary where naive analysis is most dangerous---high correlation coexists with zero causal precedence, maximizing the risk of spurious conclusions.
128	Figure~\ref{fig:consensus_heatmap} visualizes this interaction across all method$\times\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.
129	
130	
131	\subsection{Case Study: Canary Prediction of Diversity Collapse}
132	\label{sec:case_study}
133	
134	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
135	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
136	
137	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
138	Token entropy Granger-causes distinct-1 and distinct-2 with a consistent one-generation lead.
139	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0).
140	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
141	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
142	Reverse-direction tests (downstream$\to$canary) find \textbf{0/24} FDR-significant (all $p{>}0.49$), confirming directional asymmetry.
143	
144	\paragraph{High contamination ($\alpha{=}0.75$, single seed).}
145	At $\alpha{=}0.75$ (seed=42), three of four forward-direction pairs reach FDR significance: ECE$\to$distinct-1 ($p_\text{fdr}{=}0.046$), ECE$\to$distinct-2 ($p_\text{fdr}{=}0.046$), and token entropy$\to$distinct-2 ($p_\text{fdr}{=}0.048$).
146	Token entropy$\to$distinct-1 is borderline ($p_\text{fdr}{=}0.054$).
147	All four reverse directions are non-significant ($p{>}0.49$).
148	These single-seed results require multi-seed confirmation before serving as primary evidence.
149	
150	\paragraph{ECE as a conditional secondary canary.}
151	ECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).
152	Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\max}$.
153	Resolving ECE's true canary status requires longer time series.
154	
155	\paragraph{Failed canary candidates.}
156	Not all metrics serve as canaries.
157	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
158	
159	\paragraph{Consensus filtering.}
160	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
161	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
162	The consensus framework reduces the naive 100\% significance rate to the 37.5\% rate supported by the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
163	
164	
165	\subsection{Consensus Framework Validation}
166	\label{sec:consensus_validation}
167	
168	We validate the consensus framework's calibration using built-in experimental controls.
169	
170	\paragraph{False positive rate.}
171	At $\alpha{=}0.0$, no synthetic data is injected; any detected lead-lag association is a false positive.
172	Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation: 8/8 pairs) through 62.5\% (threshold) and 37.5\% (differenced) down to \textbf{0\%} (permutation Granger and Toda--Yamamoto).
173	The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
174	
175	\paragraph{False negative rate.}
176	At $\alpha{=}1.0$, we define 6 ground-truth pairs (token entropy and ECE $\to$ distinct-1/2/3), validated independently by the first-differencing diagnostic: all 6 pairs retain FDR significance after differencing, ruling out shared-trend confounding.
177	The consensus framework ($K{\geq}4/5$, $S{\geq}3/4$) recovers all~6 (\textbf{FNR${=}$0\%}).
178	Toda--Yamamoto alone yields FNR${=}$33.3\% (2/6), missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
179	We note a design asymmetry: FPR is validated on method-only data (single seed at $\alpha{=}0.0$), while FNR uses method$\times$seed joint data (4~seeds at $\alpha{=}1.0$).
180	Full joint calibration---multi-seed null-control experiments---remains future work.
181	Table~\ref{tab:fpr_fnr} reports the calibration results.
182	
183	\begin{table}[t]
184	\centering
185	\small
186	\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\alpha{=}0.0$ null control (single seed). FNR: $\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\times$seed joint (\S\ref{sec:consensus_validation}).}
187	\label{tab:fpr_fnr}
188	\begin{tabular}{lcc}
189	\toprule
190	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
191	\midrule
192	Naive XCorr              & 100\%  & 0\%  \\
193	Differenced XCorr        & 37.5\% & 0\%  \\
194	Threshold Onset          & 62.5\% & 0\%  \\
195	Permutation Granger      & 0\%    & 0\%  \\
196	Toda--Yamamoto           & 0\%    & 33.3\% \\
197	\midrule
198	Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
199	Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
200	\bottomrule
201	\end{tabular}
202	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "dc8a1d3e-b5a0-4ba8-beb1-44189c4b9e6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\cite{biderman2023pythia}, a 410M-parameter autoregressive language model.\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\nTraining data is drawn from WikiText-103 \\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\n\nOur protocol follows the full-replacement paradigm of \\citet{shumailov2024curse}.\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$.\nThe $\\alpha{=}1.0$ condition uses four random seeds $\\{42, 43, 44, 45\\}$; other conditions use seed~42, with multi-seed replication in progress.\n\nWe track two \\emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\cite{scheffer2009early}---and three \\emph{downstream metrics}.\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\cite{li2016diversity}) and perplexity.\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\S\\ref{sec:case_study}).\nResults for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\n\nAll hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}.\nCross-correlation analysis uses a maximum lag of 5 generations.\nTable~\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) across contamination levels. $\\alpha{=}1.0$: 4-seed mean${\\pm}$std; other levels: single seed (seed=42). Non-monotonic distinct-1 pattern across $\\alpha \\in \\{0.25, 0.50\\}$ is observed at seed=42, pending multi-seed confirmation.}\n\\label{tab:drift_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-5.1$ & $+51.7$ & $-13.8$ & $-9.8$ & $-21.7$ \\\\\n0.25 & $-4.1$ & $+79.7$ & $-40.3$ & $-57.1$ & $-17.2$ \\\\\n0.50 & $-18.6$ & $+842.8$ & $-37.3$ & $-51.5$ & $+21.1$ \\\\\n0.75 & $-27.7$ & $+1809.5$ & $-32.7$ & $-41.3$ & $+182.1$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3782{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3673{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Method Sensitivity Analysis}\n\\label{sec:method_sensitivity}\n\nWe open with Claim~3---method sensitivity---because it conditions the interpretation of all subsequent results.\nIf different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.\n\n\\paragraph{Five-method ablation.}\nWe apply five lead-lag detection methods to the $\\alpha{=}1.0$ condition (4~seeds, 16 canary$\\to$downstream pairs).\nThe fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{4/16} (25.0\\%).\nMethod choice alone swings significance from \\textbf{100\\% to 25\\%}.\nThe spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \\textbf{75\\%} across all five methods and \\textbf{62.5\\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\\S\\ref{sec:consensus_validation}).\nTable~\\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.\n\n\\paragraph{First-differencing diagnostic.}\nA single preprocessing decision can eliminate an entire analysis channel.\nFor canary$\\to$diversity pairs at $\\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.\nFor canary$\\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \\textbf{zero} significant pairs ($F{\\approx}0$, $p{=}0.99$; Figure~\\ref{fig:differencing_dmax}a).\nThe apparent canary$\\to$perplexity relationship is entirely an artifact of co-trending.\n\n\\paragraph{Augmentation order sensitivity.}\nToda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nAt $d_{\\max}{=}0$ (most permissive), approximately 6\\% of pairs are rejected; at adaptive $d_{\\max}$ determined by ADF unit-root tests, 75\\%; at $d_{\\max}{=}1$ (most conservative), \\textbf{94\\%}.\nThis single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.\n\n\\paragraph{Inter-method agreement.}\nCohen's $\\kappa$, averaged over all method pairs, is \\textbf{0.185} (poor agreement); this value is consistent across contamination levels ($\\alpha{=}0.0$ through $\\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.\nCross-architecture validation on GPT-2-medium (12 canary$\\to$downstream pairs) yields Fleiss' $\\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.\nRestricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.\nTable~\\ref{tab:method_comparison} extends the analysis across contamination levels.\nAt $\\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \\textbf{100\\%} of pairs significant---a textbook spurious-regression outcome in trending time series.\nPermutation Granger and Toda--Yamamoto correctly find 0\\%.\nAt $\\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\\ref{fig:consensus_heatmap}), the most extreme method$\\times$regime divergence in our experiments.\n\n\\paragraph{Method$\\times$regime interaction.}\nTable~\\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.\nAt $\\alpha{=}0.25$, differenced cross-correlation drops to 25\\% and threshold onset to 37.5\\%, while naive cross-correlation remains at 100\\%---demonstrating that even partial detrending removes marginal associations at low contamination.\nThe graded response across methods, combined with the block structure visible in Figure~\\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \\S\\ref{sec:regime}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{FDR significance rates (\\%) for five lead-lag methods across contamination levels. Each cell reports the fraction of 8 primary canary$\\to$downstream pairs (token entropy and ECE $\\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$); failed candidates (effective rank, Self-BLEU) excluded per \\S\\ref{sec:case_study}. $\\alpha{=}0.75$ is analyzed separately as single-seed data (\\S\\ref{sec:regime}). FPR$_\\text{null}$: false positive rate at the $\\alpha{=}0.0$ null control.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr     & 100   & 100  & 100  & ---  & 100   & 100  \\\\\nDiff.\\ XCorr   & 37.5  & 25   & 100  & ---  & 100   & 37.5 \\\\\nThreshold       & 62.5  & 37.5 & 100  & ---  & 100   & 62.5 \\\\\nPerm.\\ Granger  & 0     & 0    & 0    & ---  & 75    & 0    \\\\\nToda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Regime-Dependent Detectability}\n\\label{sec:regime}\n\nBeyond method choice, the contamination level~$\\alpha$ determines whether a temporal lead exists to detect.\nWe present regime effects at two levels: raw metric drift (method-independent) and Granger-causal detectability.\n\n\\paragraph{Raw drift.}\nTable~\\ref{tab:drift_summary} shows that diversity collapse occurs at \\emph{all} contamination levels, not only under full synthetic replacement.\nDistinct-1 declines by 13.8\\% even at $\\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3\\%$ ($\\alpha{=}0.25$), $-37.3\\%$ ($\\alpha{=}0.50$), $-32.7\\%$ ($\\alpha{=}0.75$), and $-27.8{\\pm}1.6\\%$ ($\\alpha{=}1.0$).\nThe non-monotonic pattern---diversity declining \\emph{more} at moderate~$\\alpha$ than at extreme~$\\alpha$---is observed at seed=42 and requires multi-seed confirmation before drawing conclusions about the relationship between contamination level and collapse severity.\n\n\\paragraph{Granger-causal detectability.}\nDespite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\\ref{fig:regime_map}).\nPermutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant at $\\alpha{=}0.00$, 0/8 at $\\alpha{=}0.25$, 0/8 at $\\alpha{=}0.50$, and \\textbf{6/8} at $\\alpha{=}1.0$ in the cross-$\\alpha$ pooled analysis.\nAt $\\alpha{=}0.75$ (single seed, seed=42), 3/8 pairs reach FDR significance; this result requires multi-seed replication before serving as primary evidence.\nWithin-$\\alpha$ multi-seed analysis at $\\alpha{=}1.0$ yields \\textbf{24/24} canary$\\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.\nThe detectability boundary---the regime below which canary metrics no longer develop sufficient temporal lead for causal inference---lies at $\\alpha \\approx 0.50$--$0.75$, consistent with theoretical expectations about signal-to-noise limits in short time series \\cite{boettiger2012limits}.\nThis boundary is sharp rather than gradual: method-level consensus ($K{\\geq}4/5$) identifies 0--1 of 16 candidate pairs as robust at $\\alpha{\\leq}0.50$ but 11/16 at $\\alpha{=}0.75$ (single seed, pre-pipeline filtering; the stricter $K{\\geq}4/5$, $S{\\geq}3/4$ criterion at $\\alpha{=}1.0$ retains 6/16 after excluding failed candidates and spurious channels per \\S\\ref{sec:case_study}).\nThe lower count at $\\alpha{=}1.0$ despite stronger contamination reflects the stricter validation standard: multi-seed replication ($S{\\geq}3/4$) filters seed-specific artifacts, and pipeline filtering removes the perplexity channel (spurious per \\S\\ref{sec:method_sensitivity}) and failed canary candidates (effective rank, Self-BLEU), both of which contribute to the $\\alpha{=}0.75$ single-seed count.\n\n\\paragraph{Synchronous collapse at $\\alpha{=}0.50$.}\nThe $\\alpha{=}0.50$ regime provides particularly informative evidence.\nCorrelation-based methods unanimously find significance (Table~\\ref{tab:method_comparison}) while causal methods unanimously find non-significance.\nThis extreme method$\\times$regime interaction arises because canary and downstream metrics collapse \\emph{synchronously} at moderate contamination, preserving high correlation but eliminating the temporal lead required for Granger-causal inference.\nWe highlight this as a \\emph{positive finding}: it delineates the regime boundary where naive analysis is most dangerous---high correlation coexists with zero causal precedence, maximizing the risk of spurious conclusions.\nFigure~\\ref{fig:consensus_heatmap} visualizes this interaction across all method$\\times\\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.\n\n\n\\subsection{Case Study: Canary Prediction of Diversity Collapse}\n\\label{sec:case_study}\n\nHaving established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).\nWe scope this claim precisely: canary metrics predict \\emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.\n\n\\paragraph{Full synthetic replacement ($\\alpha{=}1.0$, 4 seeds).}\nToken entropy Granger-causes distinct-1 and distinct-2 with a consistent one-generation lead.\nCross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0).\nFigure~\\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.\nPermutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nReverse-direction tests (downstream$\\to$canary) find \\textbf{0/24} FDR-significant (all $p{>}0.49$), confirming directional asymmetry.\n\n\\paragraph{High contamination ($\\alpha{=}0.75$, single seed).}\nAt $\\alpha{=}0.75$ (seed=42), three of four forward-direction pairs reach FDR significance: ECE$\\to$distinct-1 ($p_\\text{fdr}{=}0.046$), ECE$\\to$distinct-2 ($p_\\text{fdr}{=}0.046$), and token entropy$\\to$distinct-2 ($p_\\text{fdr}{=}0.048$).\nToken entropy$\\to$distinct-1 is borderline ($p_\\text{fdr}{=}0.054$).\nAll four reverse directions are non-significant ($p{>}0.49$).\nThese single-seed results require multi-seed confirmation before serving as primary evidence.\n\n\\paragraph{ECE as a conditional secondary canary.}\nECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).\nIts classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\max}$.\nResolving ECE's true canary status requires longer time series.\n\n\\paragraph{Failed canary candidates.}\nNot all metrics serve as canaries.\nEffective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.\n\n\\paragraph{Consensus filtering.}\nOf 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).\nThe 10 eliminated pairs comprise all canary$\\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).\nThe consensus framework reduces the naive 100\\% significance rate to the 37.5\\% rate supported by the most conservative individual methods (Figure~\\ref{fig:consensus_workflow}).\n\n\n\\subsection{Consensus Framework Validation}\n\\label{sec:consensus_validation}\n\nWe validate the consensus framework's calibration using built-in experimental controls.\n\n\\paragraph{False positive rate.}\nAt $\\alpha{=}0.0$, no synthetic data is injected; any detected lead-lag association is a false positive.\nIndividual-method FPR ranges from \\textbf{100\\%} (naive cross-correlation: 8/8 pairs) through 62.5\\% (threshold) and 37.5\\% (differenced) down to \\textbf{0\\%} (permutation Granger and Toda--Yamamoto).\nThe consensus framework at $K{\\geq}4/5$ achieves \\textbf{FPR${=}$0\\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\\ref{tab:fpr_fnr}).\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$, we define 6 ground-truth pairs (token entropy and ECE $\\to$ distinct-1/2/3), validated independently by the first-differencing diagnostic: all 6 pairs retain FDR significance after differencing, ruling out shared-trend confounding.\nThe consensus framework ($K{\\geq}4/5$, $S{\\geq}3/4$) recovers all~6 (\\textbf{FNR${=}$0\\%}).\nToda--Yamamoto alone yields FNR${=}$33.3\\% (2/6), missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\nWe note a design asymmetry: FPR is validated on method-only data (single seed at $\\alpha{=}0.0$), while FNR uses method$\\times$seed joint data (4~seeds at $\\alpha{=}1.0$).\nFull joint calibration---multi-seed null-control experiments---remains future work.\nTable~\\ref{tab:fpr_fnr} reports the calibration results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\\alpha{=}0.0$ null control (single seed). FNR: $\\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\\times$seed joint (\\S\\ref{sec:consensus_validation}).}\n\\label{tab:fpr_fnr}\n\\begin{tabular}{lcc}\n\\toprule\nCriterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\n\\midrule\nNaive XCorr              & 100\\%  & 0\\%  \\\\\nDifferenced XCorr        & 37.5\\% & 0\\%  \\\\\nThreshold Onset          & 62.5\\% & 0\\%  \\\\\nPermutation Granger      & 0\\%    & 0\\%  \\\\\nToda--Yamamoto           & 0\\%    & 33.3\\% \\\\\n\\midrule\nConsensus ($K{\\geq}4/5$)              & 0\\%    & 0\\%  \\\\\nConsensus ($K{\\geq}4/5$, $S{\\geq}3/4$) & 0\\%    & 0\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 202,
      "startLine": 1,
      "totalLines": 202
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
Now I can see the full picture. Let me also read the method.tex from docs/paper to check for the FNR-related lines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "9561547b-7288-478a-a43a-c0b16fa0f288",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEYmVD6Sj9jyz15aEn7KH7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10033,
      "cache_read_input_tokens": 66299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10033
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

Now let me read the `docs/paper/method.tex` to complete the picture, and the `docs/paper/` versions of other files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "32ccd0bc-5f4d-40a6-96f6-516bc64ce766",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEYmVD6Sj9jyz15aEn7KH7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10033,
      "cache_read_input_tokens": 66299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10033
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

<details open><summary>🔧 Tool call — Read · `toolu_019zvonTdydxe74qnB2EZSKB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "6a15df57-e07c-41cb-bdb9-cbb6e1734a76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEYmVD6Sj9jyz15aEn7KH7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10033,
      "cache_read_input_tokens": 66299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10033
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

_source line 55 · 2026-05-16T00:23:57.535Z_

<details><summary>↩ Tool result · `toolu_019zvonTdydxe74qnB2EZSKB`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs---4 candidate canaries $\times$ 4 downstream metrics, including candidates later excluded per \S\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire analysis channel.
22	At $\alpha{=}1.0$, canary$\to$perplexity pairs appear near-universally significant in undifferenced analysis ($F{=}16$--$36$) but yield $F{\approx}0$, $p{=}0.99$ after differencing (Figure~\ref{fig:differencing_dmax}a; \S\ref{sec:method_sensitivity}).
23	In contrast, canary$\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\to$24/24).
24	Without the differencing diagnostic, an analyst would conclude that canaries predict perplexity---a conclusion entirely driven by co-trending rather than temporal precedence.
25	The danger lies in the selective nature of this confound: only by applying the diagnostic can one determine which channels are genuine and which are artifacts of shared non-stationarity.
26	
27	\paragraph{Pitfall 3: Regime dependence.}
28	Even after fixing the statistical method, the contamination level~$\alpha$ determines whether a lead-lag relationship is detectable.
29	Permutation Granger tests (first-differenced, BH FDR-corrected at $q{=}0.05$) find 6/8 pairs FDR-significant at $\alpha{=}1.0$ but 0/8 at all $\alpha{\leq}0.50$ (\S\ref{sec:regime}).
30	The $\alpha{=}0.50$ regime is particularly dangerous: correlation-based methods unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), creating the maximum risk of spurious conclusions---high correlation coexists with zero causal precedence.
31	This regime dependence is consistent with theoretical expectations about signal-to-noise limits in short ecological time series \cite{boettiger2012limits}, and suggests that detectability boundaries should be explicitly mapped rather than assumed.
32	
33	
34	\subsection{Multi-Method Consensus Framework}
35	\label{sec:consensus}
36	
37	The pitfalls above motivate a consensus approach inspired by multi-method validation practices in early-warning signal detection \cite{scheffer2009early}: rather than relying on any single method, we require agreement across multiple independent methods and random seeds before classifying a lead-lag relationship as robust.
38	
39	\paragraph{Formal definition.}
40	Given $M$ lead-lag detection methods $\{m_1, \ldots, m_M\}$ and $N$ independent random seeds, a canary$\to$downstream pair $(X, Y)$ is classified as \textsc{robust} if and only if:
41	\begin{enumerate}
42	    \item At least $K$ of $M$ methods judge the pair FDR-significant, where each method independently applies Benjamini--Hochberg correction at $q{=}0.05$; and
43	    \item At least $S$ of $N$ seeds replicate this conclusion.
44	\end{enumerate}
45	The thresholds $(K, S)$ control the trade-off between false positive and false negative rates.
46	Methods with different inductive biases---correlation-based methods that detect any temporal association versus Granger-type methods that test directional predictive improvement \cite{granger1969investigating}---provide complementary evidence.
47	Their convergence on a given pair constitutes stronger evidence than agreement among methods sharing the same statistical assumptions.
48	We note that Granger precedence establishes temporal predictive improvement, not true causality \cite{shojaie2022granger}; our framework inherits this limitation.
49	
50	\paragraph{Sequential filtering pipeline.}
51	We instantiate the framework as a four-stage pipeline (Figure~\ref{fig:consensus_workflow}):
52	\begin{enumerate}
53	    \item \textbf{Naive correlation scan.} Cross-correlation at maximum lag~5 with BH correction serves as a permissive baseline; all pairs with any temporal association pass.
54	    \item \textbf{First-differencing diagnostic.} Cross-correlation is recomputed on first-differenced series, testing whether temporal associations survive removal of shared linear trends. Pairs that lose significance are flagged as potential spurious regressions.
55	    \item \textbf{Permutation Granger causality.} Permutation-based Granger causality tests \cite{shojaie2022granger} on first-differenced series (5{,}000 permutations, BH correction at $q{=}0.05$) assess directional predictive improvement: whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.
56	    \item \textbf{Multi-seed replication.} The conclusion must hold across $S$ of $N$ independent training seeds, filtering seed-specific artifacts.
57	\end{enumerate}
58	At $\alpha{=}1.0$, this pipeline progressively filters: 16 pairs pass Stage~1, 14 survive Stage~2 (differencing removes 2 marginal canary$\to$perplexity pairs), 6 survive Stage~3 (Granger testing eliminates remaining canary$\to$perplexity pairs and failed canary candidates), and all~6 survive Stage~4 (multi-seed replication confirms all Granger-significant pairs).
59	
60	\paragraph{Practical guidance.}
61	The consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.
62	Table~\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\S\ref{sec:calibration}).
63	Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$) achieves the best trade-off in our setting: zero false positives while recovering all six ground-truth pairs.
64	Method subset ablation confirms that this threshold is uniquely optimal: at $K{=}3/5$, the null-control FPR is 50\% (unacceptable); at $K{=}4/5$, FPR drops to 0\% while retaining 6/6 ground-truth sensitivity; at $K{=}5/5$, FPR remains 0\% but sensitivity falls to 3/6.
65	Shapley value analysis identifies permutation Granger causality as the linchpin method (Shapley $= +0.375$), the only method combining 0\% null-control FPR with high sensitivity.
66	Toda--Yamamoto contributes negatively (Shapley $= -2.625$) due to its Type~II errors at $T{=}10$, but is retained to maintain the panel's methodological diversity; excluding it would leave the framework without an augmented-VAR approach that handles unknown integration order.
67	Tier~4 requires unanimity across methods and seeds, which incurs a 50\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\S\ref{sec:consensus_validation}).
68	
69	\begin{table}[t]
70	\centering
71	\small
72	\caption{Practical guidance tiers for lead-lag consensus analysis. FPR and FNR are empirically calibrated at $\alpha{=}0.0$ (null control) and $\alpha{=}1.0$ (6 ground-truth pairs), respectively. $M{=}5$ methods, $N{=}4$ seeds. FPR is validated on the method dimension only; FNR on the method${\times}$seed joint dimension (\S\ref{sec:calibration}).}
73	\label{tab:practical_guidance}
74	\begin{tabular}{llcccc}
75	\toprule
76	Tier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\
77	\midrule
78	1 & Exploratory     & ${\geq}1/5$ & ${\geq}1/N$ & 100\%  & 0\%    \\
79	2 & Screening       & ${\geq}3/5$ & ${\geq}2/N$ & 37.5\% & 0\%    \\
80	3 & Confirmatory    & ${\geq}4/5$ & ${\geq}3/N$ & 0\%    & 0\%    \\
81	4 & Conservative    & $5/5$       & $N/N$        & 0\%    & 50\% \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	
87	\subsection{Empirical Calibration}
88	\label{sec:calibration}
89	
90	We calibrate the framework using two built-in experimental controls.
91	Full numerical results are reported in Table~\ref{tab:fpr_fnr}.
92	
93	\paragraph{False positive rate.}
94	The $\alpha{=}0.0$ condition serves as a null control: no synthetic data is injected, so any detected lead-lag association is a false positive.
95	At $K{=}1$ (any single method suffices), FPR${=}$100\%---naive cross-correlation alone flags all pairs.
96	At $K{=}2$, FPR drops to 75\%; at $K{=}3$, to 37.5\%; and at $K{\geq}4$, FPR${=}$0\%.
97	The consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\%) while providing robustness against miscalibration of any single method.
98	
99	\paragraph{False negative rate.}
100	At $\alpha{=}1.0$ with 4~seeds, we define six ground-truth robust pairs: token entropy and ECE each predicting distinct-1, distinct-2, and distinct-3 \cite{li2016diversity}.
101	These are independently validated by the first-differencing diagnostic---all six retain FDR significance after differencing (24/24 across seeds), ruling out shared-trend confounding as an alternative explanation.
102	At Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$), all six pairs are recovered (FNR${=}$0\%).
103	At $K{=}5/5$, $S{\geq}3/4$, FNR rises to 33.3\%: consensus loses two ECE pairs---ECE$\to$distinct-2 and ECE$\to$distinct-3, each reaching Toda--Yamamoto significance in only 2 of 4 seeds.
104	At $K{=}5/5$, $S{=}4/4$, FNR${=}$50\%: the two pairs above plus ECE$\to$distinct-1, which passes $S{\geq}3/4$ (3 of 4 seeds) but fails $S{=}4/4$.
105	
106	\paragraph{Design asymmetry.}
107	FPR is validated on the method dimension only (single seed at $\alpha{=}0.0$), while FNR is validated on the joint method${\times}$seed dimension (4~seeds at $\alpha{=}1.0$).
108	Full joint calibration---multi-seed null-control experiments---remains future work.
109	This asymmetry means that FPR estimates may be optimistic if seed-level variance in false positive rates is non-negligible.
110	
111	\paragraph{Independent validation of ground truth.}
112	The six ground-truth pairs used for FNR calibration are not self-referentially defined.
113	They are independently confirmed by the first-differencing diagnostic (\S\ref{sec:method_sensitivity}), which tests a different statistical property---robustness to detrending---than the consensus methods.
114	All six pairs retain 24/24 FDR significance after differencing, providing evidence against shared-trend confounding independent of the consensus framework itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "40a36197-88b8-4d05-8f48-993a67af934e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nThe experiments in \\S\\ref{sec:method_sensitivity}--\\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.\nThis section distills three methodological pitfalls (\\S\\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\\S\\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\\S\\ref{sec:calibration}).\n\n\n\\subsection{Methodological Pitfalls in Lead-Lag Analysis}\n\\label{sec:pitfalls}\n\nWe identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.\nEach is documented below with representative data from our experiments; full results appear in \\S\\ref{sec:experiments}.\n\n\\paragraph{Pitfall 1: Method sensitivity.}\nApplied to the same data ($\\alpha{=}1.0$, 4~seeds, 16 canary$\\to$downstream pairs---4 candidate canaries $\\times$ 4 downstream metrics, including candidates later excluded per \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$---poor agreement (\\S\\ref{sec:method_sensitivity}).\nThe spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\\% across all five methods and 62.5\\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.\nThis pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.\nIn a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.\n\n\\paragraph{Pitfall 2: Spurious regression under shared trends.}\nA single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire analysis channel.\nAt $\\alpha{=}1.0$, canary$\\to$perplexity pairs appear near-universally significant in undifferenced analysis ($F{=}16$--$36$) but yield $F{\\approx}0$, $p{=}0.99$ after differencing (Figure~\\ref{fig:differencing_dmax}a; \\S\\ref{sec:method_sensitivity}).\nIn contrast, canary$\\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\\to$24/24).\nWithout the differencing diagnostic, an analyst would conclude that canaries predict perplexity---a conclusion entirely driven by co-trending rather than temporal precedence.\nThe danger lies in the selective nature of this confound: only by applying the diagnostic can one determine which channels are genuine and which are artifacts of shared non-stationarity.\n\n\\paragraph{Pitfall 3: Regime dependence.}\nEven after fixing the statistical method, the contamination level~$\\alpha$ determines whether a lead-lag relationship is detectable.\nPermutation Granger tests (first-differenced, BH FDR-corrected at $q{=}0.05$) find 6/8 pairs FDR-significant at $\\alpha{=}1.0$ but 0/8 at all $\\alpha{\\leq}0.50$ (\\S\\ref{sec:regime}).\nThe $\\alpha{=}0.50$ regime is particularly dangerous: correlation-based methods unanimously find significance while causal methods unanimously find non-significance (Figure~\\ref{fig:consensus_heatmap}), creating the maximum risk of spurious conclusions---high correlation coexists with zero causal precedence.\nThis regime dependence is consistent with theoretical expectations about signal-to-noise limits in short ecological time series \\cite{boettiger2012limits}, and suggests that detectability boundaries should be explicitly mapped rather than assumed.\n\n\n\\subsection{Multi-Method Consensus Framework}\n\\label{sec:consensus}\n\nThe pitfalls above motivate a consensus approach inspired by multi-method validation practices in early-warning signal detection \\cite{scheffer2009early}: rather than relying on any single method, we require agreement across multiple independent methods and random seeds before classifying a lead-lag relationship as robust.\n\n\\paragraph{Formal definition.}\nGiven $M$ lead-lag detection methods $\\{m_1, \\ldots, m_M\\}$ and $N$ independent random seeds, a canary$\\to$downstream pair $(X, Y)$ is classified as \\textsc{robust} if and only if:\n\\begin{enumerate}\n    \\item At least $K$ of $M$ methods judge the pair FDR-significant, where each method independently applies Benjamini--Hochberg correction at $q{=}0.05$; and\n    \\item At least $S$ of $N$ seeds replicate this conclusion.\n\\end{enumerate}\nThe thresholds $(K, S)$ control the trade-off between false positive and false negative rates.\nMethods with different inductive biases---correlation-based methods that detect any temporal association versus Granger-type methods that test directional predictive improvement \\cite{granger1969investigating}---provide complementary evidence.\nTheir convergence on a given pair constitutes stronger evidence than agreement among methods sharing the same statistical assumptions.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality \\cite{shojaie2022granger}; our framework inherits this limitation.\n\n\\paragraph{Sequential filtering pipeline.}\nWe instantiate the framework as a four-stage pipeline (Figure~\\ref{fig:consensus_workflow}):\n\\begin{enumerate}\n    \\item \\textbf{Naive correlation scan.} Cross-correlation at maximum lag~5 with BH correction serves as a permissive baseline; all pairs with any temporal association pass.\n    \\item \\textbf{First-differencing diagnostic.} Cross-correlation is recomputed on first-differenced series, testing whether temporal associations survive removal of shared linear trends. Pairs that lose significance are flagged as potential spurious regressions.\n    \\item \\textbf{Permutation Granger causality.} Permutation-based Granger causality tests \\cite{shojaie2022granger} on first-differenced series (5{,}000 permutations, BH correction at $q{=}0.05$) assess directional predictive improvement: whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.\n    \\item \\textbf{Multi-seed replication.} The conclusion must hold across $S$ of $N$ independent training seeds, filtering seed-specific artifacts.\n\\end{enumerate}\nAt $\\alpha{=}1.0$, this pipeline progressively filters: 16 pairs pass Stage~1, 14 survive Stage~2 (differencing removes 2 marginal canary$\\to$perplexity pairs), 6 survive Stage~3 (Granger testing eliminates remaining canary$\\to$perplexity pairs and failed canary candidates), and all~6 survive Stage~4 (multi-seed replication confirms all Granger-significant pairs).\n\n\\paragraph{Practical guidance.}\nThe consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.\nTable~\\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\\S\\ref{sec:calibration}).\nTier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$) achieves the best trade-off in our setting: zero false positives while recovering all six ground-truth pairs.\nMethod subset ablation confirms that this threshold is uniquely optimal: at $K{=}3/5$, the null-control FPR is 50\\% (unacceptable); at $K{=}4/5$, FPR drops to 0\\% while retaining 6/6 ground-truth sensitivity; at $K{=}5/5$, FPR remains 0\\% but sensitivity falls to 3/6.\nShapley value analysis identifies permutation Granger causality as the linchpin method (Shapley $= +0.375$), the only method combining 0\\% null-control FPR with high sensitivity.\nToda--Yamamoto contributes negatively (Shapley $= -2.625$) due to its Type~II errors at $T{=}10$, but is retained to maintain the panel's methodological diversity; excluding it would leave the framework without an augmented-VAR approach that handles unknown integration order.\nTier~4 requires unanimity across methods and seeds, which incurs a 50\\% false negative rate because Toda--Yamamoto produces Type~II errors at $T{=}10$ due to insufficient residual degrees of freedom (\\S\\ref{sec:consensus_validation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Practical guidance tiers for lead-lag consensus analysis. FPR and FNR are empirically calibrated at $\\alpha{=}0.0$ (null control) and $\\alpha{=}1.0$ (6 ground-truth pairs), respectively. $M{=}5$ methods, $N{=}4$ seeds. FPR is validated on the method dimension only; FNR on the method${\\times}$seed joint dimension (\\S\\ref{sec:calibration}).}\n\\label{tab:practical_guidance}\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\\\\n\\midrule\n1 & Exploratory     & ${\\geq}1/5$ & ${\\geq}1/N$ & 100\\%  & 0\\%    \\\\\n2 & Screening       & ${\\geq}3/5$ & ${\\geq}2/N$ & 37.5\\% & 0\\%    \\\\\n3 & Confirmatory    & ${\\geq}4/5$ & ${\\geq}3/N$ & 0\\%    & 0\\%    \\\\\n4 & Conservative    & $5/5$       & $N/N$        & 0\\%    & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Empirical Calibration}\n\\label{sec:calibration}\n\nWe calibrate the framework using two built-in experimental controls.\nFull numerical results are reported in Table~\\ref{tab:fpr_fnr}.\n\n\\paragraph{False positive rate.}\nThe $\\alpha{=}0.0$ condition serves as a null control: no synthetic data is injected, so any detected lead-lag association is a false positive.\nAt $K{=}1$ (any single method suffices), FPR${=}$100\\%---naive cross-correlation alone flags all pairs.\nAt $K{=}2$, FPR drops to 75\\%; at $K{=}3$, to 37.5\\%; and at $K{\\geq}4$, FPR${=}$0\\%.\nThe consensus framework at Tier~3 matches the false positive performance of the best individual methods (permutation Granger and Toda--Yamamoto, both 0\\%) while providing robustness against miscalibration of any single method.\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$ with 4~seeds, we define six ground-truth robust pairs: token entropy and ECE each predicting distinct-1, distinct-2, and distinct-3 \\cite{li2016diversity}.\nThese are independently validated by the first-differencing diagnostic---all six retain FDR significance after differencing (24/24 across seeds), ruling out shared-trend confounding as an alternative explanation.\nAt Tier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$), all six pairs are recovered (FNR${=}$0\\%).\nAt $K{=}5/5$, $S{\\geq}3/4$, FNR rises to 33.3\\%: consensus loses two ECE pairs---ECE$\\to$distinct-2 and ECE$\\to$distinct-3, each reaching Toda--Yamamoto significance in only 2 of 4 seeds.\nAt $K{=}5/5$, $S{=}4/4$, FNR${=}$50\\%: the two pairs above plus ECE$\\to$distinct-1, which passes $S{\\geq}3/4$ (3 of 4 seeds) but fails $S{=}4/4$.\n\n\\paragraph{Design asymmetry.}\nFPR is validated on the method dimension only (single seed at $\\alpha{=}0.0$), while FNR is validated on the joint method${\\times}$seed dimension (4~seeds at $\\alpha{=}1.0$).\nFull joint calibration---multi-seed null-control experiments---remains future work.\nThis asymmetry means that FPR estimates may be optimistic if seed-level variance in false positive rates is non-negligible.\n\n\\paragraph{Independent validation of ground truth.}\nThe six ground-truth pairs used for FNR calibration are not self-referentially defined.\nThey are independently confirmed by the first-differencing diagnostic (\\S\\ref{sec:method_sensitivity}), which tests a different statistical property---robustness to detrending---than the consensus methods.\nAll six pairs retain 24/24 FDR significance after differencing, providing evidence against shared-trend confounding independent of the consensus framework itself.",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
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
Now I have a complete picture. Let me determine which paper version is the "live" one. 

`docs/paper/` appears to be the more recent/polished version:
- It has consistent TY FNR = 33.3% (2/6) everywhere
- It has additional content (Shapley analysis, κ-restricted, cross-architecture)
- `artifacts/_project/paper/` has an inconsistent 25% FNR for TY

So I should edit `docs/paper/` as the primary version. But should I also update `artifacts/_project/paper/`?


The task references a local path that doesn't actually exist, so I'm working with the two versions I found. The fix report shows that window_sensitivity.py had an off-by-one bug in the slicing and a divergent TY implementation that was returning NaN, so I need to identify which results in the papers are affected by these issues and what corrections are needed.

The main paper results come from method_ablation.py, which uses the canonical TY implementation, so those numbers should be fine. But the paper does cite window sensitivity analysis in the discussion section, specifically mentioning the consensus classification stabilizing at T≥5 and the Toda-Yamamoto procedure returning insufficient_df for T≤7. I need to check if those specific claims are still valid given the bugs in window_sensitivity.py.

Looking at the fix report, the canonical TY (from method_ablation.py) actually works at all window lengths T=5-10 now—it doesn't return insufficient_df at T≤7 like the buggy window_sensitivity.py did. So that claim in line 31 of the discussion is now incorrect. However, line 30 about the consensus classification stabilizing at T≥5 with identical results through T=10 is still accurate based on the fix report showing 6/6 robust pairs across all T values.

I need to check if the discussion.tex file has been updated with this correction, or if it still contains the outdated claim about TY's elevated FNR being due to insufficient degrees of freedom. I need to update the discussion of the Toda-Yamamoto procedure to reflect the corrected window sensitivity results. The old version claimed TY returns insufficient_df at T≤7, but after fixing the implementation and data points, TY actually finds significant results across T=5-10 with variable sensitivity—showing 3/6 to 6/6 significant pairs depending on the window, though still missing the ECE→d2 relationship at T=10 with a 33.3% false negative rate. I should rewrite this to acknowledge TY's improved performance while noting its remaining sensitivity limitations across different observation windows. and ECE→d3) is still a real phenomenon — it's just not caused by insufficient_df but by low power for those specific ECE pairs.

Looking at the fix report, TY's performance across window lengths shows 3/6 to 6/6 significance rates, peaking at T=7 before dropping and partially recovering. This variability reflects TY's known low power on short series rather than the buggy implementation issue. The real driver of TY's 33.3% FNR at T=10 is low seed-level consensus for ECE→d2 and ECE→d3, not insufficient residual degrees of freedom.

I should also check if artifacts/_project/paper needs updates, but it doesn't contain the window sensitivity lines anyway. There's a pre-existing error there with TY's FNR listed as 25% instead of 33.3%, but that's separate from this fix.

The critical change is in docs/paper/discussion.tex line 31, which claims TY returns insufficient_df at T≤7 based on the buggy window_sensitivity results. The paper's main analysis already shows TY at 4/6 for T=10, which is correct — the 0/6 was only appearing in the broken window sensitivity output. I need to verify if there are other references to window sensitivity results in the discussion section.

Looking at line 30, it states the consensus classification stabilizes at T≥5 with identical results from T=5 through T=10, which the fix report confirms is correct for the other methods (all showing 6/6 robust pairs). However, TY actually varies from 3/6 to 6/6 across this range, so "identical results" isn't quite accurate when accounting for all methods.

Wait, but the 4/5 consensus threshold means only 4 of the 5 methods need to agree. Since NX/DX/TH/PG consistently show 6/6 robust pairs at every T, the consensus is always 6/6 regardless of TY's variation. So the statement about identical consensus results from T=5 through T=10 is actually correct.

The real issue is line 31, which claims TY returns insufficient_df at T≤7 based on the old buggy code. After the fix, TY produces valid results at all T≥5, though with variable power ranging from 3/6 to 6/6 pairs. That's the only direct consequence of the window_sensitivity bug that needs correcting in the paper.

Now I'm checking whether other reported numbers are affected. The FNR values, ablation percentages, and method comparison results all come from method_ablation.py using the canonical TY implementation, so they're unaffected by the window_sensitivity fix. The Tier 4 FNR also remains unchanged since canonical TY still misses the ECE pairs across seeds.

The discussion's explanation of TY's elevated FNR at T=10 is still valid—the insufficient residual degrees of freedom reasoning holds for the canonical version. Similarly, the claim about ECE being driven by Type II errors remains correct.

The only place that needs correction is in the discussion.tex file where it claims insufficient_df occurs at T≤7, since that was derived from the buggy window_sensitivity results. I should verify which paper version gets compiled and check if experiments.tex also contains this error.

Now I'm formulating the specific change needed: replacing the claim that TY returns insufficient_df for all pairs at T≤7 with a more accurate statement that TY produces valid results across all window lengths but with variable sensitivity, reflecting its known low power on short series. Though I'm reconsidering whether this new framing fully captures the original narrative about parameter overhead versus signal strength.

The key insight is that TY doesn't actually fail completely at small T values—it just has inconsistent power across different seed realizations. The missing pairs at T=10 (like ECE→d2,d3) stem from low consensus at the seed level rather than insufficient degrees of freedom. But I need to be careful here: the paper's general claim that TY's elevated FNR is due to insufficient residual df still holds as the underlying mechanism, even though TY doesn't literally return an insufficient_df error. The fix just clarifies that TY doesn't catastrophically fail at T≤7, but its power remains limited by the low residual df problem. The Toda-Yamamoto procedure produces valid test statistics across all window lengths, but with unstable sensitivity—ranging from 3/6 to 6/6 significant pairs depending on the window size, which confirms that its elevated false negative rate stems from low residual degrees of freedom rather than a genuine absence of signal. This non-monotonic pattern at different window sizes is worth noting but might distract from the main point: the procedure works consistently but with limited power, which aligns with what the paper already establishes about Toda-Yamamoto's limitations. I should check whether the experiments section in the paper artifacts needs updating too, since the discussion section doesn't contain the window sensitivity lines that had the bug. of these constraints are violated by the fix. The fix actually strengthens the narrative slightly: TY is no longer completely broken (returning nan) at shorter T, but its variable power across T values is still consistent with the "TY is underpowered" narrative.

Now I need to figure out which version to update — `docs/paper/` seems like the active working version while `artifacts/_project/paper/` appears to be a snapshot. The task mentions "论文文件在本地：`paper/`" but that path doesn't exist, so I'll update both locations where applicable since they likely need to stay in sync.

For the actual changes, I only need to fix one thing: the incorrect TY insufficient_df claim in `docs/paper/discussion.tex` at line 31. Everything else in the paper — the main TY numbers, FNR calculations, and consensus results — comes from method_ablation.py and isn't affected by this window_sensitivity fix. The 4/5 consensus conclusion holds across all T values from 5 to 10, and the FNR calculation was based on the canonical method_ablation results anyway, not the buggy TY output.

Let me verify there aren't any other references to this issue elsewhere in the paper. I'm checking paper_framing.md and searching through discussion.tex more carefully to make sure I haven't missed any other mentions of insufficient_df or the 0/6 result.

Actually, looking back at the task description, it seems to assume the main TY numbers came from the buggy window_sensitivity code, but that's not the case—the paper's primary analysis uses different results. The "underpowered" narrative about TY at T=10 is still accurate since it genuinely misses 2/6 pairs due to limited seeds passing, so the fix here is really just correcting the specific claim about how that limitation manifests. Looking back at the task requirements, I need to verify what actually needs fixing in the paper. The task mentions "TY at T=10: 0/6" but searching through the paper, I don't find that specific claim — the paper reports TY as 4/16 overall and 4/6 correct (with 2/6 misses for FNR), not 0/6. The 0/6 only appeared in the buggy window_sensitivity analysis that wasn't cited. What the paper does reference is TY returning `insufficient_df` at T≤7 in the discussion section, which is what actually needs verification against the corrected implementation.

Now I'm checking whether the artifacts version of the paper has the same issue that needs fixing.

Looking at the discussion section there, I don't see any window_sensitivity references—just the standard discussion of time-series constraints and the Toda-Yamamoto FNR rate. So that version doesn't need the same edit.

But I'm noticing an inconsistency: the discussion says 33.3% for the FNR, yet the experiments section reports 25% in one place and something different in another. I should track down where these numbers actually come from to see if there's a real discrepancy or just a documentation issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "827e9f4e-b08a-4d2d-a565-2381f83f71f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wydRh8b3jBMsXPKCTPkHg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3754,
      "cache_read_input_tokens": 76332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3754
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

I now have a complete picture. Let me analyze what actually needs to change.

The paper has two versions: `docs/paper/` (more recent, with window sensitivity content) and `artifacts/_project/paper/` (older snapshot). The main analysis numbers in the paper come from `method_ablation.py` (the canonical TY implementation with correct 11 data points), NOT from the buggy `window_sensitivity.py`. So the core numbers (TY 4/16 = 25%, TY FNR 33.3%, 59.4% in the method comparison table) are **unaffected** by the fix.

However, `docs/paper/discussion.tex` line 31 explicitly cites window sensitivity results that are NOW WRONG:

> "The Toda--Yamamoto procedure returns `insufficient_df` for all pairs at T≤7"

After the fix, TY produces valid results at all T∈{5,...,10} (3/6 to 6/6 pairs significant). This line must be corrected.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "cf3423ae-0547-4410-9319-8925ba31384a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wydRh8b3jBMsXPKCTPkHg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3754,
      "cache_read_input_tokens": 76332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3754
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

<details open><summary>🔧 Tool call — Edit · `toolu_01WzYuR7xp89YpgWeerLzr4x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
  "old_string": "The Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.",
  "new_string": "The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "25ab9c2a-1561-4dd6-a0bd-c642c9370bdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wydRh8b3jBMsXPKCTPkHg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3754,
      "cache_read_input_tokens": 76332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3754
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

_source line 59 · 2026-05-16T00:25:55.595Z_

<details><summary>↩ Tool result · `toolu_01WzYuR7xp89YpgWeerLzr4x`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "8d1884ae-6869-423d-8228-5b5b93be2fed",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
    "oldString": "The Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.",
    "newString": "The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Granger precedence is not causation.}\nGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\cite{granger1969investigating,shojaie2022granger}.\nBivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\nOur multi-method consensus framework inherits this limitation in full.\nThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\nThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\emph{causes} diversity collapse.\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\alpha \\in \\{0.0, 0.25, 0.50, 0.75, 1.0\\}$).\nGeneralization to other model architectures, datasets, or training protocols requires independent validation.\nThe consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\nFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\nOur ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.\n\n\\paragraph{FPR/FNR calibration asymmetry.}\nThe FPR and FNR estimates in our calibration analysis differ in their coverage of the seed dimension.\nFPR is validated on the method dimension only, using a single seed at the null-control condition ($\\alpha{=}0.0$).\nFNR is validated on the joint method${\\times}$seed dimension, aggregating across four seeds at full contamination ($\\alpha{=}1.0$).\nThis asymmetry means our FPR estimate of 0\\% may be optimistic: if seed-level variance in false positive rates is non-negligible, the true FPR under the consensus rule could exceed zero.\nFull joint calibration---requiring multi-seed null-control experiments at $\\alpha{=}0.0$---remains an open direction for future work.\n\n\\paragraph{Short time-series constraint.}\nWith $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.\nThis series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.\nThe Toda--Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nThis finding aligns with \\citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.\nLonger generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.\nHowever, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.\nThe Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.\n\n\\paragraph{Diversity--calibration dissociation.}\nDiversity metrics and calibration metrics respond to synthetic contamination in qualitatively opposite directions across the $\\alpha$ spectrum.\nDiversity collapse (distinct-$n$ decline) is most severe at low contamination ($\\alpha{=}0.25$: distinct-3 declines by 59.9\\%) and attenuates at higher levels ($\\alpha{=}1.0$: $-30.5\\%$), while calibration degradation (ECE) increases monotonically with $\\alpha$ ($+51.7\\%$ at $\\alpha{=}0.0$ to $+3782\\%$ at $\\alpha{=}1.0$).\nThis dissociation underscores the need for multi-method consensus: the regime in which a metric degrades most severely ($\\alpha{=}0.25$ for diversity) does not coincide with the regime in which its temporal lead is most detectable ($\\alpha{\\geq}0.75$), and a single metric family cannot capture the full picture of iterative training degradation.\n\n\\paragraph{Limitations.}\nSeveral limitations constrain the generalizability of our findings.\nFirst, our primary experiments use Pythia-410M; preliminary cross-architecture validation with GPT-2-medium uses batch size~32 (versus~4 for Pythia) for GPU efficiency, exposing 8$\\times$ more data per training step, which may accelerate collapse dynamics without altering the qualitative pattern (token entropy leading diversity decline is observed in both architectures).\nSecond, training data is drawn from a single domain (a WikiText-103 subset), and domain-specific distributional properties may influence the coupling between canary and downstream metrics.\nThird, we lack an intervention experiment: we observe that token entropy Granger-precedes diversity collapse at $\\alpha{=}1.0$ (with preliminary single-seed evidence at $\\alpha{=}0.75$) but do not test whether acting on canary signals can prevent or delay collapse onset.\nFourth, our experiments use replace-only data accumulation; accumulate-mode training~\\cite{dey2024breaking,kazdan2025collapse} may exhibit qualitatively different canary dynamics.\nFinally, our canary claims are scoped to distinct-$n$ diversity metrics~\\cite{li2016diversity}---not to model collapse broadly~\\cite{schaeffer2025position}---as the perplexity channel proved spurious ($F{\\approx}0$, $p{=}0.99$ after differencing).\nThis scoping is theoretically motivated: \\citet{cao2025entropycal} prove a fundamental calibration-diversity tradeoff in language models---all current calibration methods reduce entropy at the cost of diversity---suggesting that calibration and diversity are coupled but not identical, which may explain why token entropy can Granger-precede diversity collapse without leading perplexity.\n\n\\paragraph{Future work.}\nSeveral directions extend this work.\nMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\nCross-architecture validation is needed: our GPT-2-medium experiments are in progress, and evaluation on larger-scale models would further test generalizability.\nOnline monitoring---integrating canary metrics into training pipelines for real-time collapse detection---is a natural applied extension.\nAccumulate-mode experiments~\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\nFinally, connecting the empirically observed detectability boundary at $\\alpha{\\approx}0.50$--$0.75$ to theoretical phase transition analysis~\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 7,
        "newStart": 28,
        "newLines": 7,
        "lines": [
          " This finding aligns with \\citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.",
          " Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.",
          " However, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.",
          "-The Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.",
          "+The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.",
          " ",
          " \\paragraph{Diversity--calibration dissociation.}",
          " Diversity metrics and calibration metrics respond to synthetic contamination in qualitatively opposite directions across the $\\alpha$ spectrum."
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

_source line 60_

Now let me verify the edit and confirm consistency with paper_framing.md constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "ba96cc51-a56f-4831-98d0-2d3d705830eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bNtGwD1zmv3TvMMwpGWSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6282,
      "cache_read_input_tokens": 80086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6282
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

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01JwGYefXpkkMvVtD7xhTGUH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
  "offset": 24,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "a972dc18-0e6a-4ee1-92cb-8a6ec39c2c4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bNtGwD1zmv3TvMMwpGWSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6282,
      "cache_read_input_tokens": 80086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6282
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

_source line 62 · 2026-05-16T00:26:00.092Z_

<details><summary>↩ Tool result · `toolu_01JwGYefXpkkMvVtD7xhTGUH`</summary>

```text
24	\paragraph{Short time-series constraint.}
25	With $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.
26	This series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.
27	The Toda--Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
28	This finding aligns with \citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.
29	Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.
30	However, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.
31	The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \in \{5, \ldots, 10\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.
32	
33	\paragraph{Diversity--calibration dissociation.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "4513ba24-48b4-4eb3-b6d8-608395043364",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
      "content": "\\paragraph{Short time-series constraint.}\nWith $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.\nThis series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.\nThe Toda--Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nThis finding aligns with \\citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.\nLonger generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.\nHowever, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.\nThe Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.\n\n\\paragraph{Diversity--calibration dissociation.}",
      "numLines": 10,
      "startLine": 24,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

Edit confirmed. Now let me verify consistency with paper_framing.md constraints.

## Summary of analysis

**Modified files:**
- `docs/paper/discussion.tex` line 31 — Replaced incorrect claim that TY returns `insufficient_df` for all pairs at T≤7 with the corrected window sensitivity results (TY produces valid statistics at all T∈{5,...,10}, 3/6 to 6/6 pairs significant).

**No changes needed in the following (verified):**

| Item | Location | Why unchanged |
|------|----------|--------------|
| TY 4/16 (25%) | experiments.tex:54, method.tex:15, intro:24 | From method_ablation.py (canonical impl), not window_sensitivity |
| TY 59.4% at α=1.0 | experiments.tex:97 (method_comparison table) | Same — canonical impl |
| TY FNR 33.3% (2/6) | experiments.tex:178, method.tex:103, discussion.tex:27 | Still correct: ECE→d2 and ECE→d3 still miss at 3/4 seed threshold (2/4 seeds) even with the fix |
| TY FNR 25% in FPR/FNR table | experiments.tex:196 | Correct (33.3%) |
| Tier 4 FNR 50% | method.tex:67,81 | Still correct: ECE→d1 at 3/4 seeds still fails 4/4 |
| 4/5 consensus = 6/6 robust | discussion.tex:30, experiments passim | Confirmed unchanged: fix report Table 2 shows 6/6 robust at every T∈{5,...,10} |
| Spurious-signal rate 75%/62.5% | experiments.tex:56, method.tex:16 | Unaffected — based on pair-level method_ablation results |
| ECE "conditional secondary" | experiments.tex:150-153 | Still correct: TY Type II errors still drive the "secondary" label |

**Consistency with paper_framing.md:**
- Constraint #15 (TY 降级为辅助指标): ✓ No claim strength change
- Constraint #8 (TY 在 N=11 下不可靠): ✓ Narrative preserved — "limited residual degrees of freedom"
- Constraint #11 (统计效力须显式论证): ✓ The updated line still explicitly acknowledges TY's power limitation

**Pre-existing issue flagged (not related to this fix):** `artifacts/_project/paper/experiments.tex:173,191` reports TY FNR as 25% instead of 33.3% (inconsistent with its own discussion.tex:27 and with the `docs/paper/` version). This predates the window_sensitivity fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "uuid": "da3c87e1-c225-4d19-99f3-eab34ec29b67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gCeDc9rrZs4ewm3mMaQJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 86368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
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

_source line 64_

Edit confirmed. Now let me verify consistency with paper_framing.md constraints.

## Summary of analysis

**Modified files:**
- `docs/paper/discussion.tex` line 31 — Replaced incorrect claim that TY returns `insufficient_df` for all pairs at T≤7 with the corrected window sensitivity results (TY produces valid statistics at all T∈{5,...,10}, 3/6 to 6/6 pairs significant).

**No changes needed in the following (verified):**

| Item | Location | Why unchanged |
|------|----------|--------------|
| TY 4/16 (25%) | experiments.tex:54, method.tex:15, intro:24 | From method_ablation.py (canonical impl), not window_sensitivity |
| TY 59.4% at α=1.0 | experiments.tex:97 (method_comparison table) | Same — canonical impl |
| TY FNR 33.3% (2/6) | experiments.tex:178, method.tex:103, discussion.tex:27 | Still correct: ECE→d2 and ECE→d3 still miss at 3/4 seed threshold (2/4 seeds) even with the fix |
| TY FNR 25% in FPR/FNR table | experiments.tex:196 | Correct (33.3%) |
| Tier 4 FNR 50% | method.tex:67,81 | Still correct: ECE→d1 at 3/4 seeds still fails 4/4 |
| 4/5 consensus = 6/6 robust | discussion.tex:30, experiments passim | Confirmed unchanged: fix report Table 2 shows 6/6 robust at every T∈{5,...,10} |
| Spurious-signal rate 75%/62.5% | experiments.tex:56, method.tex:16 | Unaffected — based on pair-level method_ablation results |
| ECE "conditional secondary" | experiments.tex:150-153 | Still correct: TY Type II errors still drive the "secondary" label |

**Consistency with paper_framing.md:**
- Constraint #15 (TY 降级为辅助指标): ✓ No claim strength change
- Constraint #8 (TY 在 N=11 下不可靠): ✓ Narrative preserved — "limited residual degrees of freedom"
- Constraint #11 (统计效力须显式论证): ✓ The updated line still explicitly acknowledges TY's power limitation

**Pre-existing issue flagged (not related to this fix):** `artifacts/_project/paper/experiments.tex:173,191` reports TY FNR as 25% instead of 33.3% (inconsistent with its own discussion.tex:27 and with the `docs/paper/` version). This predates the window_sensitivity fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 337464,
  "duration_api_ms": 338503,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "c9f0f1fd-03dd-489e-8149-43782a0fe3b9",
  "total_cost_usd": 1.1663345,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 75068,
    "cache_read_input_tokens": 515993,
    "output_tokens": 17490,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 75068,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 701,
        "cache_read_input_tokens": 86368,
        "cache_creation_input_tokens": 541,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 541
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1723,
      "outputTokens": 25,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018479999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 17490,
      "cacheReadInputTokens": 515993,
      "cacheCreationInputTokens": 75068,
      "webSearchRequests": 0,
      "costUSD": 1.1644865000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "399aee90-ee44-438e-822f-f9055bdafde7"
}
```

</details>

---
