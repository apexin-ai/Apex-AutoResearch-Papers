# data memory lesson audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_data_memory-lesson-audit_20260515T101154.log`
- **Structured JSON:** [`67b1a73f18f9fca42a8e.json`](../../sessions/67/67b1a73f18f9fca42a8e.json)

## Before a recorded user message

38 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
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
  "uuid": "b42d0a7f-7475-4c6f-8da3-e924dc2e7c1f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1779206400,
    "rateLimitType": "seven_day",
    "utilization": 0.78,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "2e9f46b6-def8-4fb1-97c6-902072249f70",
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the three files mentioned to check their current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "a281fb9e-6d1a-49e0-92cf-2a887f542a7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXp9e7SjkDn3Ahhpc68rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11112
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01FerRsoApC2nSm3AjtSM4zA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "9008dcf9-7cf9-4d3d-b5aa-c2b92c1aeac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXp9e7SjkDn3Ahhpc68rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11112
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 6 · 2026-05-15T10:12:05.129Z_

<details><summary>↩ Tool result · `toolu_01FerRsoApC2nSm3AjtSM4zA`</summary>

````text
1	# Eval Sweep Compilation — exec-sim-repair-verifier
2	
3	Generated: 2026-05-15 (updated)
4	
5	---
6	
7	## 1. 8B s42 Val@8192 Sweep (n=9335)
8	
9	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
10	|-----------|-------------|-------------|------------|------------|---------------|
11	| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 |
12	| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |
13	| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |
14	| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |
15	| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |
16	| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |
17	| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |
18	| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |
19	
20	**Val best = ckpt-1000 (88.23%)** — confirmed.
21	
22	Majority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).
23	
24	Notes:
25	- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)
26	- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)
27	- 72.96% is the test set majority baseline, not val — corrected 2026-05-15
28	
29	---
30	
31	## 2. 8B s42 Test@8192 Sweep (n=9784)
32	
33	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
34	|-----------|-------------|-------------|------------|------------|---------------|
35	| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |
36	| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |
37	| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |
38	| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |
39	| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |
40	| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |
41	| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |
42	
43	Majority baseline accuracy = 72.96% (test set, n=9784).
44	
45	Notes:
46	- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)
47	- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)
48	- Val-test disagreement: val-best ckpt-1000 is not test-best
49	- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)
50	
51	---
52	
53	## 3. 4B v5 Val@5120 Sweep (n=9335)
54	
55	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
56	|-----------|-------------|-------------|------------|------------|---------------|
57	| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |
58	| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |
59	| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |
60	| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |
61	| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |
62	
63	**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.
64	
65	4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).
66	
67	---
68	
69	## 3b. 4B v5 Test@5120 (n=9784)
70	
71	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
72	|-----------|-------------|-------------|------------|------------|---------------|
73	| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |
74	| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |
75	
76	Majority baseline accuracy = 72.96% (test set, n=9784).
77	
78	Notes:
79	- Val-selected ckpt-4600 test = 83.63%
80	- Val-test gap consistent with 8B pattern
81	
82	---
83	
84	## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)
85	
86	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
87	|-----------|-------------|-------------|------------|------------|---------------|
88	| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |
89	| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |
90	| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |
91	| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |
92	| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |
93	
94	**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.
95	
96	### 8B seed123 Test@8192
97	
98	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
99	|-----------|-------------|-------------|------------|------------|---------------|
100	| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |
101	
102	---
103	
104	## 5. Summary
105	
106	| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |
107	|--------|----------|----------|----------|----------------|
108	| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |
109	| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |
110	| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |
111	| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |
112	| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |
113	| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |
114	
115	---
116	
117	## 6. JSON (for plotting)
118	
119	```json
120	{
121	  "8b_s42_val8192": {
122	    "majority_baseline": 75.88,
123	    "checkpoints": {
124	      "ckpt-200":  {"accuracy": 63.52, "f1_macro": 61.17, "f1_pass": 70.7,  "f1_fail": 51.6,  "exp_id": "cls8b-s42-ckpt200-val8192-eval-v2"},
125	      "ckpt-400":  {"accuracy": 80.96, "f1_macro": null,  "f1_pass": null,  "f1_fail": null,  "exp_id": "repo-level-cls-8b-conda"},
126	      "ckpt-600":  {"accuracy": 85.00, "f1_macro": null,  "f1_pass": null,  "f1_fail": null,  "exp_id": "repo-level-cls-8b-conda"},
127	      "ckpt-800":  {"accuracy": 84.50, "f1_macro": 79.20, "f1_pass": null,  "f1_fail": null,  "exp_id": "cls8b-s42-ckpt800-val8192-eval"},
128	      "ckpt-1000": {"accuracy": 88.23, "f1_macro": 82.72, "f1_pass": 92.5,  "f1_fail": 73.0,  "exp_id": "cls8b-s42-ckpt1000-val8192-eval"},
129	      "ckpt-1200": {"accuracy": 87.76, "f1_macro": 81.25, "f1_pass": 92.3,  "f1_fail": 70.2,  "exp_id": "cls8b-s42-ckpt1200-val8192-v3"},
130	      "ckpt-1400": {"accuracy": 85.97, "f1_macro": 77.15, "f1_pass": 91.34, "f1_fail": 62.95, "exp_id": "cls8b-s42-ckpt1400-val8192-eval"},
131	      "ckpt-1600": {"accuracy": 86.75, "f1_macro": 78.94, "f1_pass": 91.76, "f1_fail": 66.12, "exp_id": "cls8b-s42-ckpt1600-val8192-v2"}
132	    }
133	  },
134	  "8b_s42_test8192": {
135	    "majority_baseline": 72.96,
136	    "checkpoints": {
137	      "ckpt-400":  {"accuracy": 84.79, "f1_macro": 81.18, "f1_pass": 89.43, "f1_fail": 72.93, "exp_id": "cls8b-s42-ckpt400-test8192-eval"},
138	      "ckpt-600":  {"accuracy": 79.05, "f1_macro": 75.12, "f1_pass": 85.00, "f1_fail": 65.24, "exp_id": "cls8b-s42-ckpt600-test8192-eval"},
139	      "ckpt-800":  {"accuracy": 83.53, "f1_macro": 78.97, "f1_pass": 88.77, "f1_fail": 69.17, "exp_id": "cls8b-s42-ckpt800-test8192-eval"},
140	      "ckpt-1000": {"accuracy": 83.52, "f1_macro": 77.50, "f1_pass": 89.14, "f1_fail": 65.85, "exp_id": "cls8b-s42-ckpt1000-test8192-eval"},
141	      "ckpt-1200": {"accuracy": 83.84, "f1_macro": 77.47, "f1_pass": 89.45, "f1_fail": 65.49, "exp_id": "cls8b-s42-ckpt1200-test8192-eval"},
142	      "ckpt-1400": {"accuracy": 85.47, "f1_macro": 78.90, "f1_pass": 90.67, "f1_fail": 67.13, "exp_id": "cls8b-s42-ckpt1400-test8192-eval"},
143	      "ckpt-1600": {"accuracy": 84.99, "f1_macro": 78.94, "f1_pass": 90.22, "f1_fail": 67.65, "exp_id": "cls8b-s42-ckpt1600-test8192-eval"}
144	    }
145	  },
146	  "4b_v5_val5120": {
147	    "majority_baseline": 75.88,
148	    "checkpoints": {
149	      "ckpt-600":  {"accuracy": 82.82, "f1_macro": 79.81, "f1_pass": 87.60, "f1_fail": 72.03, "exp_id": "cls4b-v5-ckpt600-val5120-eval"},
150	      "ckpt-4000": {"accuracy": 89.84, "f1_macro": 84.25, "f1_pass": 93.64, "f1_fail": 74.85, "exp_id": "cls4b-v5-ckpt4000-val5120-eval"},
151	      "ckpt-4200": {"accuracy": 89.06, "f1_macro": 83.07, "f1_pass": 93.1,  "f1_fail": 73.0,  "exp_id": "cls4b-v5-val-sweep-ckpt4200"},
152	      "ckpt-4400": {"accuracy": 89.96, "f1_macro": 84.94, "f1_pass": 93.64, "f1_fail": 76.25, "exp_id": "cls4b-v5-val-sweep-ckpt4400-v3"},
153	      "ckpt-4600": {"accuracy": 90.07, "f1_macro": 85.04, "f1_pass": 93.71, "f1_fail": 76.37, "exp_id": "cls4b-v5-val-sweep-ckpt4600"}
154	    }
155	  },
156	  "4b_v5_test5120": {
157	    "majority_baseline": 72.96,
158	    "checkpoints": {
159	      "ckpt-4400": {"accuracy": 83.24, "f1_macro": 74.44, "f1_pass": 89.44, "f1_fail": 59.45, "exp_id": "cls4b-v5-ckpt4400-test5120-eval"},
160	      "ckpt-4600": {"accuracy": 83.63, "f1_macro": 75.63, "f1_pass": 89.59, "f1_fail": 61.67, "exp_id": "cls4b-v5-ckpt4600-test5120-eval"}
161	    }
162	  },
163	  "8b_seed123_val8192": {
164	    "majority_baseline": 75.88,
165	    "checkpoints": {
166	      "ckpt-3000": {"accuracy": 88.69, "f1_macro": 81.73, "f1_pass": 93.0,  "f1_fail": 70.5,  "exp_id": "cls8b-seed123-ckpt3000-val8192-eval"},
167	      "ckpt-6200": {"accuracy": 87.52, "f1_macro": 79.26, "f1_pass": 92.35, "f1_fail": 66.16, "exp_id": "cls8b-seed123-ckpt6200-val8192-eval"},
168	      "ckpt-6400": {"accuracy": 87.48, "f1_macro": 79.66, "f1_pass": 92.27, "f1_fail": 67.04, "exp_id": "cls8b-seed123-ckpt6400-val8192-eval"},
169	      "ckpt-6600": {"accuracy": 87.23, "f1_macro": 79.02, "f1_pass": 92.14, "f1_fail": 65.9,  "exp_id": "cls8b-seed123-ckpt6600-val8192-eval"},
170	      "ckpt-6633": {"accuracy": 87.10, "f1_macro": 78.79, "f1_pass": 92.07, "f1_fail": 65.52, "exp_id": "cls8b-seed123-ckpt6633-val8192-eval"}
171	    }
172	  },
173	  "8b_seed123_test8192": {
174	    "majority_baseline": 72.96,
175	    "checkpoints": {
176	      "ckpt-3000": {"accuracy": 85.60, "f1_macro": 78.38, "f1_pass": 90.87, "f1_fail": 65.89, "exp_id": "cls8b-seed123-ckpt3000-test8192-eval-v2"}
177	    }
178	  },
179	  "4b_v5_test5120": {
180	    "majority_baseline": 72.96,
181	    "checkpoints": {
182	      "ckpt-4400": {"accuracy": 83.24, "f1_macro": 74.44, "f1_pass": 89.44, "f1_fail": 59.45, "exp_id": "cls4b-v5-ckpt4400-test5120-eval"},
183	      "ckpt-4600": {"accuracy": 83.63, "f1_macro": 75.63, "f1_pass": 89.59, "f1_fail": 61.67, "exp_id": "cls4b-v5-ckpt4600-test5120-eval"}
184	    }
185	  }
186	}
187	```
188	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "fd12d9d9-61c5-4738-a241-1a46ea2d6412",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
      "content": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
      "numLines": 188,
      "startLine": 1,
      "totalLines": 188
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01SshX7ojdFY8r49TQ5USFwi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "3d189921-eb90-4b82-81fd-1f0f7bf47746",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXp9e7SjkDn3Ahhpc68rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11112
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 8 · 2026-05-15T10:12:05.609Z_

<details><summary>↩ Tool result · `toolu_01SshX7ojdFY8r49TQ5USFwi`</summary>

```text
1	# Comprehensive Results Summary
2	
3	> Generated: 2026-05-15 (updated). All numbers sourced from registry (DONE + success only).
4	> Excluded: `cls8b-seed123-ckpt3000-val8192-eval` (old training artifact, invalid).
5	
6	---
7	
8	## 1. Dataset
9	
10	| Split | Samples | Class Balance | Majority Baseline |
11	|-------|---------|---------------|-------------------|
12	| Train | 15,290 | pass 52% / fail 48% | 52.0% |
13	| Val | 1,896 | — | — |
14	| Test (function) | 1,890 | — | 51.75% |
15	| Test (repo) | 9,784 | — | 72.96% |
16	| Val (repo) | 9,335 | — | ~75.9% |
17	
18	5 mutation types: operator_swap, return_value, boundary_removal, variable_swap, off_by_one.
19	Source: `mvp-b-data-prep`
20	
21	---
22	
23	## 2. Function-level Results (per-test, 1890 test samples)
24	
25	### 2.1 CLS 4B — 5 seeds
26	
27	| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |
28	|------|----------|---------|---------|-----------|----------|-----------|----------|--------|
29	| 42 | 87.83 | 88.06 | 87.59 | 89.45 | 86.71 | 86.20 | 89.04 | `multi-seed-core` |
30	| 123 | 89.52 | 89.64 | 89.40 | 91.76 | 87.63 | 87.34 | 91.56 | `multi-seed-core` |
31	| 456 | 87.88 | 87.53 | 88.21 | 93.60 | 82.21 | 83.12 | 93.97 | `multi-seed-core` |
32	| 789 | 89.00 | 88.90 | 89.10 | 93.30 | 84.90 | 85.20 | 93.40 | `cls-seed789` |
33	| 0 | 87.94 | 87.79 | 88.08 | 92.13 | 83.84 | 84.20 | 92.32 | `cls-seed0` |
34	| **Mean** | **88.43** | **88.38** | **88.48** | | | | | |
35	| **Std** | **0.78** | **0.88** | **0.68** | | | | | |
36	
37	### 2.2 CWM 4B — 5 seeds
38	
39	| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |
40	|------|----------|---------|---------|-------------|-----------|----------|-----------|----------|--------|
41	| 42 | 87.51 | 87.15 | 87.86 | — | 93.24 | 81.80 | 82.75 | 93.64 | `per-test-precision-recall` |
42	| 123 | 87.20 | 86.95 | 87.44 | 84.44 | — | — | — | — | `cwm-seed123` |
43	| 456 | 86.98 | 86.66 | 87.29 | 84.02 | 92.26 | 81.70 | 82.52 | 92.65 | `cwm-seed456` |
44	| 789 | 86.67 | 86.74 | 86.60 | 83.97 | 89.37 | 84.25 | 84.09 | 89.25 | `cwm-seed789` |
45	| 0 | 87.57 | 87.18 | 87.93 | 84.29 | 93.45 | 81.70 | 82.71 | 93.86 | `cwm-seed0` |
46	| **Mean** | **87.19** | **86.94** | **87.42** | **84.18** | | | | | |
47	| **Std** | **0.37** | **0.22** | **0.52** | **0.21** | | | | | |
48	
49	### 2.3 CLS 8B — 3 seeds
50	
51	| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |
52	|------|----------|---------|---------|-----------|----------|-----------|----------|--------|
53	| 42 | 90.48 | 90.86 | 90.06 | 90.22 | 91.51 | 90.76 | 89.36 | `cls8b-eval-seed42` |
54	| 123 | 89.37 | 89.54 | 89.19 | 91.20 | 87.93 | 87.54 | 90.90 | `cls8b-eval-seed123` |
55	| 456 | 88.31 | 88.20 | 88.41 | 92.29 | 84.46 | 84.72 | 92.43 | `cls8b-seed456` |
56	| **Mean** | **89.39** | **89.53** | **89.22** | | | | | |
57	| **Std** | **1.09** | **1.33** | **0.83** | | | | | |
58	
59	### 2.4 CWM 8B — 3 seeds
60	
61	| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Source |
62	|------|----------|---------|---------|-------------|--------|
63	| 42 | 87.67 | 87.57 | 87.77 | 84.39 | `model-size-scaling-cwm8b` |
64	| 123 | 86.98 | 86.83 | 87.13 | 84.13 | `cwm8b-seed123` |
65	| 456 | 86.24 | 85.96 | 86.51 | 82.80 | `cwm8b-seed456` |
66	| **Mean** | **86.96** | **86.79** | **87.14** | **83.77** | |
67	| **Std** | **0.72** | **0.82** | **0.63** | **0.86** | |
68	
69	### 2.5 CLS vs CWM Comparison
70	
71	| Config | CLS Acc (mean) | CWM Acc (mean) | Gap (pp) | Seeds |
72	|--------|---------------|----------------|----------|-------|
73	| 4B | 88.43 ± 0.78 | 87.19 ± 0.37 | **+1.24** | 5 vs 5 |
74	| 8B | 89.39 ± 1.09 | 86.96 ± 0.72 | **+2.43** | 3 vs 3 |
75	
76	Gap widens from +1.24pp (4B) to +2.43pp (8B) — supports complexity hypothesis.
77	
78	### 2.6 Model Size Scaling (4B → 8B)
79	
80	| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |
81	|--------|---------|---------|-------------------|
82	| CLS | 88.43 | 89.39 | **+0.96** |
83	| CWM | 87.19 | 86.96 | **−0.23** |
84	
85	CLS benefits from scaling; CWM does not (bottleneck is generative complexity, not model capacity).
86	
87	---
88	
89	## 3. Trajectory-level Results (1032 variants, 5 seeds)
90	
91	| Seed | Accuracy | Unresolved F1 | Resolved F1 | Consistency | Source |
92	|------|----------|---------------|-------------|-------------|--------|
93	| 42 | 85.66 | 87.50 | 83.18 | 79.94 | `traj-level-finetuned` |
94	| 123 | 85.47 | 87.00 | 83.52 | 78.59 | `traj-level-seed123` |
95	| 456 | 87.40 | 88.70 | 85.80 | 78.80 | `traj-level-seed456` |
96	| 789 | 87.31 | 88.27 | 86.17 | 76.74 | `traj-level-seed789` |
97	| 0 | 85.66 | 87.37 | 83.41 | 79.55 | `traj-level-seed0` |
98	| **Mean** | **86.30** | **87.77** | **84.42** | **78.72** | |
99	| **Std** | **0.97** | **0.68** | **1.45** | **1.26** | |
100	
101	### CLS vs TRAJ (variant-level, clustered bootstrap)
102	
103	| Metric | Value | Source |
104	|--------|-------|--------|
105	| Pooled gap (CLS − TRAJ) | −0.45 pp | `5-paired-clustered-bootstrap` |
106	| 95% CI | [−1.71, +0.84] | `5-paired-clustered-bootstrap` |
107	| p-value | 0.499 (not significant) | `5-paired-clustered-bootstrap` |
108	| TOST p-value (±2pp margin) | 0.0071 (equivalent) | `5-paired-clustered-bootstrap` |
109	
110	Per-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29.
111	
112	**Conclusion**: CLS and TRAJ are statistically equivalent at variant level. Per-test's advantage is diagnostic granularity (which test fails), not raw accuracy.
113	
114	---
115	
116	## 4. Repo-level Results (majority baseline: 72.96%)
117	
118	### 4.1 CLS 4B seed42 — Test Set (v5, home-1x5090, transformers 4.57.6)
119	
120	max_seq_length=2048, eval_samples=9,784, unparseable=132 (1.3%)
121	
122	| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | vs Baseline (pp) | Source |
123	|-----------|----------|----------|---------|---------|-------------------|--------|
124	| 600 | 76.74 | 73.74 | 64.88 | 82.61 | +3.78 | `repo-level-cls-v5` |
125	| 4000 | 81.51 | 72.56 | 56.90 | 88.23 | +8.55 | `repo-level-cls-v5` |
126	| 4200 | 80.64 | 72.10 | 56.66 | 87.54 | +7.68 | `repo-level-cls-v5` |
127	| 4400 | 82.11 | 73.94 | 59.34 | — | +9.15 | `repo-level-cls-v5` |
128	| **4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39** | `repo-level-cls-v5` |
129	
130	Best: ckpt-4600 (both accuracy and F1 macro).
131	
132	### 4.2 CLS 4B seed42 — Val Set (v5, home, max_seq_length=2048)
133	
134	eval_samples=9,335, unparseable=1,883 (20.2%)
135	
136	| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |
137	|-----------|----------|----------|---------|---------|--------|
138	| 600 | 77.25 | 70.81 | 57.11 | 84.52 | `repo-level-cls-v5` |
139	| 4000 | 83.32 | 70.26 | 50.56 | 89.97 | `repo-level-cls-v5` |
140	| 4200 | 82.82 | 69.54 | 49.43 | 89.65 | `repo-level-cls-v5` |
141	| 4400 | 83.49 | 71.63 | 53.29 | 89.97 | `repo-level-cls-v5` |
142	| **4600** | **83.63** | **71.72** | **53.36** | **90.07** | `repo-level-cls-v5` |
143	
144	Val-test consistent: both best at ckpt-4600.
145	
146	### 4.3 CLS 4B seed42 — Test Set (v5-conda, westd, transformers 4.57.6)
147	
148	Apple-to-apple environment match with CWM v12. eval_samples=9,784, unparseable=132 (1.35%)
149	
150	| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |
151	|-----------|----------|----------|---------|---------|--------|
152	| 200 | 52.96 | 52.89 | 51.02 | 54.76 | `repo-level-cls-v5-conda` |
153	| 400 | 78.43 | 68.41 | 50.61 | 86.21 | `repo-level-cls-v5-conda` |
154	| **600** | **76.37** | **71.17** | **58.93** | **83.41** | `repo-level-cls-v5-conda` |
155	
156	Best accuracy: ckpt-400 (78.43%). Best F1 macro: ckpt-600 (71.17%).
157	Home v5 ckpt-600 (76.74%) vs conda v5-conda ckpt-600 (76.37%): only 0.37pp diff → environment difference negligible.
158	
159	### 4.4 CLS 4B seed123 — Val Only (home)
160	
161	| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | Truncated | Source |
162	|-------|-----------|----------|----------|---------|---------|-------------|-----------|--------|
163	| val@2048 | 200 | 62.51 | 55.54 | 37.94 | 73.14 | 1,883 | — | `repo-level-cls-seed123-home` |
164	| val@2048 | 400 | 80.72 | 67.03 | 45.78 | 88.27 | 1,883 | — | `repo-level-cls-seed123-home` |
165	| val@2048 | 600 | 76.78 | 66.81 | 48.63 | 85.00 | 1,883 | — | `repo-level-cls-seed123-home` |
166	| val@2048 | 800 | 81.81 | 69.14 | 49.37 | 88.91 | 1,883 | — | `repo-level-cls-seed123-home` |
167	| val@2048 | 1000 | 82.30 | 67.63 | 45.84 | 89.42 | 1,883 | — | `repo-level-cls-seed123-home` |
168	| val@4096 | 400 | 82.57 | 71.24 | 53.18 | 89.29 | 1,406 | — | `repo-level-cls-seed123-home` |
169	| val@4096 | 600 | 79.18 | 70.73 | 55.00 | 86.45 | 1,406 | — | `repo-level-cls-seed123-home` |
170	| val@4096 | 800 | 83.70 | 73.31 | 56.70 | 90.00 | 1,406 | — | `repo-level-cls-seed123-home` |
171	| val@5120 | 400 | 86.01 | 79.66 | 68.30 | 91.02 | 0 | 234 | `repo-level-cls-seed123-home` |
172	| val@5120 | 600 | 81.89 | 77.01 | 66.43 | 87.60 | 0 | 234 | `repo-level-cls-seed123-home` |
173	| **val@5120** | **800** | **87.92** | **81.95** | **71.57** | **92.33** | **0** | **234** | `repo-level-cls-seed123-home` |
174	
175	Key finding: max_seq_length dramatically affects unparseable rate and accuracy.
176	- @2048: 1,883 unparseable (20.2%), best acc=82.30%
177	- @4096: 1,406 unparseable (15.1%), best acc=83.70%
178	- @5120: 0 unparseable, best acc=87.92%
179	
180	### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)
181	
182	| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |
183	|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|
184	| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |
185	| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |
186	| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |
187	| val@5120 | 400 | 80.47 | 75.84 | — | — | — | 5120 | `repo-level-cls-8b-conda` |
188	| test@2048 | 400 | 84.52 | 80.89 | — | — | — | 2048 | `repo-level-cls-8b-conda` |
189	| test@2048 | 600 | 78.51 | — | — | — | — | 2048 | `repo-level-cls-8b-conda` |
190	| test@8192 | 400 | 84.79 | 81.18 | 72.93 | 89.43 | 0 | 8192 | `cls8b-s42-ckpt400-test8192-eval` |
191	| test@8192 | 600 | 79.05 | 75.12 | 65.24 | 85.00 | 0 | 8192 | `cls8b-s42-ckpt600-test8192-eval` |
192	| test@8192 | 800 | 83.53 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
193	| test@8192 | 1000 | 83.52 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
194	| test@8192 | 1200 | 83.84 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
195	| **test@8192** | **1400** | **85.47** | — | — | — | **0** | **8192** | `cls8b-s42-test-sweep` |
196	| test@8192 | 1600 | 84.99 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
197	
198	Test-best: ckpt-1400 @ 8192 → **85.47% (+12.51pp vs majority baseline)**.
199	Val-best: ckpt-1000 @ 8192 → **88.23%** (test=83.52%).
200	8B s42 test-best (85.47%) vs 4B best (82.35% v5 ckpt-4600) = **+3.12pp scaling gain**.
201	
202	### 4.6 CLS 8B seed123 — Repo-level (westd, @8192)
203	
204	**Val sweep:**
205	
206	| Checkpoint | Accuracy | Status |
207	|-----------|----------|--------|
208	| **3000** | **88.69%** | **val-best** |
209	| 6200 | 87.52% | |
210	| 6400 | 87.48% | |
211	| 6600 | 87.23% | |
212	| 6633 | — | ⏳ running |
213	
214	**Test @8192 (ckpt-3000, val-best):**
215	
216	| Metric | Value |
217	|--------|-------|
218	| Accuracy | 85.60% |
219	| F1 Macro | 78.38% |
220	| Fail F1 | 65.89% |
221	| Pass F1 | 90.87% |
222	| Fail Precision | 91.65% |
223	| Fail Recall | 51.44% |
224	| Pass Precision | 84.52% |
225	| Pass Recall | 98.26% |
226	| vs Majority Baseline | +12.64pp |
227	
228	### 4.7 CLS 4B seed42 — v5 Extended Eval
229	
230	| Split | Checkpoint | Accuracy |
231	|-------|-----------|----------|
232	| val | 4400 | 89.96% |
233	| **val** | **4600** | **90.07%** ← val-best |
234	| test | 4400 | 83.24% |
235	| test | 4600 | 83.63% |
236	
237	### 4.8 Multi-seed 8B Repo-level Comparison
238	
239	| Seed | Val-best Ckpt | Val Acc | Test Acc | CWM Test | CLS−CWM Gap |
240	|------|--------------|---------|----------|----------|-------------|
241	| s42 | ckpt-1000 | 88.23% | 83.52% | 58.04% | 25.48pp |
242	| seed123 | ckpt-3000 | 88.69% | 85.60% | 59.09% | 26.51pp |
243	| **Mean** | — | **88.46%** | **84.56%** | **58.57%** | **25.99pp** |
244	
245	### 4.9 Repo-level Early Versions (for reference)
246	
247	| Experiment | Accuracy | F1 Macro | Status | Source |
248	|-----------|----------|----------|--------|--------|
249	| CLS v4 (4B, early stop) | 66.11 | 56.61 | Below baseline (72.96%) | `repo-level-cls-v4` |
250	| CWM v10 (invalid) | 69.91 | 46.71 | 93% unparseable (max_new_tokens=64) | `repo-level-cwm-v10` |
251	
252	---
253	
254	## 5. Zero-shot LLM Judge Baselines
255	
256	| Model | Accuracy | Fail F1 | Pass F1 | vs Baseline (pp) | vs Fine-tuned 4B (pp) | Source |
257	|-------|----------|---------|---------|-------------------|------------------------|--------|
258	| Qwen3-8B | 64.40 | 72.20 | 50.50 | +12.65 | −24.03 | `llm-judge-8b-zeroshot` |
259	| Qwen3-32B | 71.69 | 75.91 | 65.68 | +19.94 | −16.74 | `llm-judge-32b-zeroshot` |
260	
261	Both models heavily biased toward predicting FAIL. 8B→32B scaling = +7.29pp, but still far below fine-tuned 4B (88.43%).
262	
263	---
264	
265	## 6. Statistical Analyses
266	
267	### 6.1 Block Correlation (ICC)
268	
269	| Metric | Value | Source |
270	|--------|-------|--------|
271	| ICC | 0.1909 | `block-corr-empirical` |
272	| ICC p-value | < 0.0001 | `block-corr-empirical` |
273	| Design Effect (DEFF) | 3.97 | `block-corr-empirical` |
274	| Overall error rate | 12.49% | `block-corr-empirical` |
275	| All-correct problems (observed) | 46 | `block-corr-empirical` |
276	| All-correct problems (expected i.i.d.) | 16.35 | `block-corr-empirical` |
277	| Inference precision | bfloat16 | `block-corr-empirical` |
278	
279	Significant block correlation: tests within the same problem are NOT independent. DEFF=3.97 means effective sample size is ~4x smaller than nominal.
280	
281	### 6.2 Oracle F2P Stratified Analysis
282	
283	| # Tests per Problem | % of Problems | Block Advantage (pp) | Source |
284	|---------------------|---------------|----------------------|--------|
285	| T=1 | 68.7% | −0.09 (none) | `oracle-f2p-stratified` |
286	| T=2 | 19.1% | +31.69 | `oracle-f2p-stratified` |
287	| T=3–5 | 7.1% | +40.74 | `oracle-f2p-stratified` |
288	| T≥6 | 5.1% | +40.06 | `oracle-f2p-stratified` |
289	| **Overall** | | **+10.93** | `oracle-f2p-stratified` |
290	
291	T2 problems contribute 55.3% of overall block advantage despite being only 19.1% of problems.
292	
293	### 6.3 Per-test Diagnostic (CWM seed42)
294	
295	| Metric | Value | Source |
296	|--------|-------|--------|
297	| Best mutation type | return_value (97.26%) | `per-test-precision-recall` |
298	| Worst mutation type | off_by_one (82.56%) | `per-test-precision-recall` |
299	| Perfect problems (114 total) | 48 (42.1%) | `per-test-precision-recall` |
300	| Median problem fail-F1 | 94.12% | `per-test-precision-recall` |
301	| FP count | 58 | `per-test-precision-recall` |
302	| FN count | 178 | `per-test-precision-recall` |
303	
304	---
305	
306	## 7. Simulation Results (MVP-A)
307	
308	| Scenario | i.i.d. Advantage | Block Advantage | Pass? | Source |
309	|----------|-----------------|-----------------|-------|--------|
310	| P2P reg=5% | −1.0% | −0.5% | FAIL | `mvp-a-oracle-sim` |
311	| P2P reg=10% | +13.2% | +8.3% | PASS | `mvp-a-oracle-sim` |
312	| P2P reg=20% | +35.7% | +27.8% | PASS | `mvp-a-oracle-sim` |
313	
314	Real SWE-bench F2P distribution: median T=1, mean T=3, P75=2, P90=3.
315	
316	---
317	
318	## 8. Summary of Key Findings
319	
320	| Finding | Evidence |
321	|---------|----------|
322	| CLS > CWM at function-level | 4B: +1.24pp (88.43 vs 87.19), 8B: +2.43pp (89.39 vs 86.96) |
323	| CLS scaling benefit (4B→8B) | +0.96pp (88.43→89.39) |
324	| CWM no scaling benefit | −0.23pp (87.19→86.96) |
325	| CLS-CWM gap widens with scale | 4B: 1.24pp → 8B: 2.43pp |
326	| CLS ≈ TRAJ at variant level | gap=−0.45pp, TOST p=0.007 |
327	| Per-test advantage is diagnostic | granularity, not raw accuracy |
328	| Fine-tuned 4B >> zero-shot 32B | 88.43% vs 71.69% (+16.74pp) |
329	| Repo-level 8B > 4B | 85.47% vs 82.35% (+3.12pp), updated with full s42 test sweep |
330	| 8B multi-seed repo-level | mean test 84.56%, CLS−CWM gap ~26pp |
331	| 4B v5 extended eval | val-best 90.07% (ckpt-4600), test 83.63% |
332	| max_seq_length critical for repo | @2048: 20% unparseable → @5120: 0% |
333	| Block correlation significant | ICC=0.19, DEFF=3.97 |
334	| Per-test advantage needs reg≥10% | 5% regression → no advantage |
335	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "4b7ea5ca-4bf2-4688-a5c5-6453ba9b5ea2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md",
      "content": "# Comprehensive Results Summary\n\n> Generated: 2026-05-15 (updated). All numbers sourced from registry (DONE + success only).\n> Excluded: `cls8b-seed123-ckpt3000-val8192-eval` (old training artifact, invalid).\n\n---\n\n## 1. Dataset\n\n| Split | Samples | Class Balance | Majority Baseline |\n|-------|---------|---------------|-------------------|\n| Train | 15,290 | pass 52% / fail 48% | 52.0% |\n| Val | 1,896 | — | — |\n| Test (function) | 1,890 | — | 51.75% |\n| Test (repo) | 9,784 | — | 72.96% |\n| Val (repo) | 9,335 | — | ~75.9% |\n\n5 mutation types: operator_swap, return_value, boundary_removal, variable_swap, off_by_one.\nSource: `mvp-b-data-prep`\n\n---\n\n## 2. Function-level Results (per-test, 1890 test samples)\n\n### 2.1 CLS 4B — 5 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-----------|----------|-----------|----------|--------|\n| 42 | 87.83 | 88.06 | 87.59 | 89.45 | 86.71 | 86.20 | 89.04 | `multi-seed-core` |\n| 123 | 89.52 | 89.64 | 89.40 | 91.76 | 87.63 | 87.34 | 91.56 | `multi-seed-core` |\n| 456 | 87.88 | 87.53 | 88.21 | 93.60 | 82.21 | 83.12 | 93.97 | `multi-seed-core` |\n| 789 | 89.00 | 88.90 | 89.10 | 93.30 | 84.90 | 85.20 | 93.40 | `cls-seed789` |\n| 0 | 87.94 | 87.79 | 88.08 | 92.13 | 83.84 | 84.20 | 92.32 | `cls-seed0` |\n| **Mean** | **88.43** | **88.38** | **88.48** | | | | | |\n| **Std** | **0.78** | **0.88** | **0.68** | | | | | |\n\n### 2.2 CWM 4B — 5 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-------------|-----------|----------|-----------|----------|--------|\n| 42 | 87.51 | 87.15 | 87.86 | — | 93.24 | 81.80 | 82.75 | 93.64 | `per-test-precision-recall` |\n| 123 | 87.20 | 86.95 | 87.44 | 84.44 | — | — | — | — | `cwm-seed123` |\n| 456 | 86.98 | 86.66 | 87.29 | 84.02 | 92.26 | 81.70 | 82.52 | 92.65 | `cwm-seed456` |\n| 789 | 86.67 | 86.74 | 86.60 | 83.97 | 89.37 | 84.25 | 84.09 | 89.25 | `cwm-seed789` |\n| 0 | 87.57 | 87.18 | 87.93 | 84.29 | 93.45 | 81.70 | 82.71 | 93.86 | `cwm-seed0` |\n| **Mean** | **87.19** | **86.94** | **87.42** | **84.18** | | | | | |\n| **Std** | **0.37** | **0.22** | **0.52** | **0.21** | | | | | |\n\n### 2.3 CLS 8B — 3 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-----------|----------|-----------|----------|--------|\n| 42 | 90.48 | 90.86 | 90.06 | 90.22 | 91.51 | 90.76 | 89.36 | `cls8b-eval-seed42` |\n| 123 | 89.37 | 89.54 | 89.19 | 91.20 | 87.93 | 87.54 | 90.90 | `cls8b-eval-seed123` |\n| 456 | 88.31 | 88.20 | 88.41 | 92.29 | 84.46 | 84.72 | 92.43 | `cls8b-seed456` |\n| **Mean** | **89.39** | **89.53** | **89.22** | | | | | |\n| **Std** | **1.09** | **1.33** | **0.83** | | | | | |\n\n### 2.4 CWM 8B — 3 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Source |\n|------|----------|---------|---------|-------------|--------|\n| 42 | 87.67 | 87.57 | 87.77 | 84.39 | `model-size-scaling-cwm8b` |\n| 123 | 86.98 | 86.83 | 87.13 | 84.13 | `cwm8b-seed123` |\n| 456 | 86.24 | 85.96 | 86.51 | 82.80 | `cwm8b-seed456` |\n| **Mean** | **86.96** | **86.79** | **87.14** | **83.77** | |\n| **Std** | **0.72** | **0.82** | **0.63** | **0.86** | |\n\n### 2.5 CLS vs CWM Comparison\n\n| Config | CLS Acc (mean) | CWM Acc (mean) | Gap (pp) | Seeds |\n|--------|---------------|----------------|----------|-------|\n| 4B | 88.43 ± 0.78 | 87.19 ± 0.37 | **+1.24** | 5 vs 5 |\n| 8B | 89.39 ± 1.09 | 86.96 ± 0.72 | **+2.43** | 3 vs 3 |\n\nGap widens from +1.24pp (4B) to +2.43pp (8B) — supports complexity hypothesis.\n\n### 2.6 Model Size Scaling (4B → 8B)\n\n| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |\n|--------|---------|---------|-------------------|\n| CLS | 88.43 | 89.39 | **+0.96** |\n| CWM | 87.19 | 86.96 | **−0.23** |\n\nCLS benefits from scaling; CWM does not (bottleneck is generative complexity, not model capacity).\n\n---\n\n## 3. Trajectory-level Results (1032 variants, 5 seeds)\n\n| Seed | Accuracy | Unresolved F1 | Resolved F1 | Consistency | Source |\n|------|----------|---------------|-------------|-------------|--------|\n| 42 | 85.66 | 87.50 | 83.18 | 79.94 | `traj-level-finetuned` |\n| 123 | 85.47 | 87.00 | 83.52 | 78.59 | `traj-level-seed123` |\n| 456 | 87.40 | 88.70 | 85.80 | 78.80 | `traj-level-seed456` |\n| 789 | 87.31 | 88.27 | 86.17 | 76.74 | `traj-level-seed789` |\n| 0 | 85.66 | 87.37 | 83.41 | 79.55 | `traj-level-seed0` |\n| **Mean** | **86.30** | **87.77** | **84.42** | **78.72** | |\n| **Std** | **0.97** | **0.68** | **1.45** | **1.26** | |\n\n### CLS vs TRAJ (variant-level, clustered bootstrap)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp | `5-paired-clustered-bootstrap` |\n| 95% CI | [−1.71, +0.84] | `5-paired-clustered-bootstrap` |\n| p-value | 0.499 (not significant) | `5-paired-clustered-bootstrap` |\n| TOST p-value (±2pp margin) | 0.0071 (equivalent) | `5-paired-clustered-bootstrap` |\n\nPer-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29.\n\n**Conclusion**: CLS and TRAJ are statistically equivalent at variant level. Per-test's advantage is diagnostic granularity (which test fails), not raw accuracy.\n\n---\n\n## 4. Repo-level Results (majority baseline: 72.96%)\n\n### 4.1 CLS 4B seed42 — Test Set (v5, home-1x5090, transformers 4.57.6)\n\nmax_seq_length=2048, eval_samples=9,784, unparseable=132 (1.3%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | vs Baseline (pp) | Source |\n|-----------|----------|----------|---------|---------|-------------------|--------|\n| 600 | 76.74 | 73.74 | 64.88 | 82.61 | +3.78 | `repo-level-cls-v5` |\n| 4000 | 81.51 | 72.56 | 56.90 | 88.23 | +8.55 | `repo-level-cls-v5` |\n| 4200 | 80.64 | 72.10 | 56.66 | 87.54 | +7.68 | `repo-level-cls-v5` |\n| 4400 | 82.11 | 73.94 | 59.34 | — | +9.15 | `repo-level-cls-v5` |\n| **4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39** | `repo-level-cls-v5` |\n\nBest: ckpt-4600 (both accuracy and F1 macro).\n\n### 4.2 CLS 4B seed42 — Val Set (v5, home, max_seq_length=2048)\n\neval_samples=9,335, unparseable=1,883 (20.2%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |\n|-----------|----------|----------|---------|---------|--------|\n| 600 | 77.25 | 70.81 | 57.11 | 84.52 | `repo-level-cls-v5` |\n| 4000 | 83.32 | 70.26 | 50.56 | 89.97 | `repo-level-cls-v5` |\n| 4200 | 82.82 | 69.54 | 49.43 | 89.65 | `repo-level-cls-v5` |\n| 4400 | 83.49 | 71.63 | 53.29 | 89.97 | `repo-level-cls-v5` |\n| **4600** | **83.63** | **71.72** | **53.36** | **90.07** | `repo-level-cls-v5` |\n\nVal-test consistent: both best at ckpt-4600.\n\n### 4.3 CLS 4B seed42 — Test Set (v5-conda, westd, transformers 4.57.6)\n\nApple-to-apple environment match with CWM v12. eval_samples=9,784, unparseable=132 (1.35%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |\n|-----------|----------|----------|---------|---------|--------|\n| 200 | 52.96 | 52.89 | 51.02 | 54.76 | `repo-level-cls-v5-conda` |\n| 400 | 78.43 | 68.41 | 50.61 | 86.21 | `repo-level-cls-v5-conda` |\n| **600** | **76.37** | **71.17** | **58.93** | **83.41** | `repo-level-cls-v5-conda` |\n\nBest accuracy: ckpt-400 (78.43%). Best F1 macro: ckpt-600 (71.17%).\nHome v5 ckpt-600 (76.74%) vs conda v5-conda ckpt-600 (76.37%): only 0.37pp diff → environment difference negligible.\n\n### 4.4 CLS 4B seed123 — Val Only (home)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | Truncated | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-----------|--------|\n| val@2048 | 200 | 62.51 | 55.54 | 37.94 | 73.14 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 400 | 80.72 | 67.03 | 45.78 | 88.27 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 600 | 76.78 | 66.81 | 48.63 | 85.00 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 800 | 81.81 | 69.14 | 49.37 | 88.91 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 1000 | 82.30 | 67.63 | 45.84 | 89.42 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 400 | 82.57 | 71.24 | 53.18 | 89.29 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 600 | 79.18 | 70.73 | 55.00 | 86.45 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 800 | 83.70 | 73.31 | 56.70 | 90.00 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@5120 | 400 | 86.01 | 79.66 | 68.30 | 91.02 | 0 | 234 | `repo-level-cls-seed123-home` |\n| val@5120 | 600 | 81.89 | 77.01 | 66.43 | 87.60 | 0 | 234 | `repo-level-cls-seed123-home` |\n| **val@5120** | **800** | **87.92** | **81.95** | **71.57** | **92.33** | **0** | **234** | `repo-level-cls-seed123-home` |\n\nKey finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|\n| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@5120 | 400 | 80.47 | 75.84 | — | — | — | 5120 | `repo-level-cls-8b-conda` |\n| test@2048 | 400 | 84.52 | 80.89 | — | — | — | 2048 | `repo-level-cls-8b-conda` |\n| test@2048 | 600 | 78.51 | — | — | — | — | 2048 | `repo-level-cls-8b-conda` |\n| test@8192 | 400 | 84.79 | 81.18 | 72.93 | 89.43 | 0 | 8192 | `cls8b-s42-ckpt400-test8192-eval` |\n| test@8192 | 600 | 79.05 | 75.12 | 65.24 | 85.00 | 0 | 8192 | `cls8b-s42-ckpt600-test8192-eval` |\n| test@8192 | 800 | 83.53 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| test@8192 | 1000 | 83.52 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| test@8192 | 1200 | 83.84 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| **test@8192** | **1400** | **85.47** | — | — | — | **0** | **8192** | `cls8b-s42-test-sweep` |\n| test@8192 | 1600 | 84.99 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n\nTest-best: ckpt-1400 @ 8192 → **85.47% (+12.51pp vs majority baseline)**.\nVal-best: ckpt-1000 @ 8192 → **88.23%** (test=83.52%).\n8B s42 test-best (85.47%) vs 4B best (82.35% v5 ckpt-4600) = **+3.12pp scaling gain**.\n\n### 4.6 CLS 8B seed123 — Repo-level (westd, @8192)\n\n**Val sweep:**\n\n| Checkpoint | Accuracy | Status |\n|-----------|----------|--------|\n| **3000** | **88.69%** | **val-best** |\n| 6200 | 87.52% | |\n| 6400 | 87.48% | |\n| 6600 | 87.23% | |\n| 6633 | — | ⏳ running |\n\n**Test @8192 (ckpt-3000, val-best):**\n\n| Metric | Value |\n|--------|-------|\n| Accuracy | 85.60% |\n| F1 Macro | 78.38% |\n| Fail F1 | 65.89% |\n| Pass F1 | 90.87% |\n| Fail Precision | 91.65% |\n| Fail Recall | 51.44% |\n| Pass Precision | 84.52% |\n| Pass Recall | 98.26% |\n| vs Majority Baseline | +12.64pp |\n\n### 4.7 CLS 4B seed42 — v5 Extended Eval\n\n| Split | Checkpoint | Accuracy |\n|-------|-----------|----------|\n| val | 4400 | 89.96% |\n| **val** | **4600** | **90.07%** ← val-best |\n| test | 4400 | 83.24% |\n| test | 4600 | 83.63% |\n\n### 4.8 Multi-seed 8B Repo-level Comparison\n\n| Seed | Val-best Ckpt | Val Acc | Test Acc | CWM Test | CLS−CWM Gap |\n|------|--------------|---------|----------|----------|-------------|\n| s42 | ckpt-1000 | 88.23% | 83.52% | 58.04% | 25.48pp |\n| seed123 | ckpt-3000 | 88.69% | 85.60% | 59.09% | 26.51pp |\n| **Mean** | — | **88.46%** | **84.56%** | **58.57%** | **25.99pp** |\n\n### 4.9 Repo-level Early Versions (for reference)\n\n| Experiment | Accuracy | F1 Macro | Status | Source |\n|-----------|----------|----------|--------|--------|\n| CLS v4 (4B, early stop) | 66.11 | 56.61 | Below baseline (72.96%) | `repo-level-cls-v4` |\n| CWM v10 (invalid) | 69.91 | 46.71 | 93% unparseable (max_new_tokens=64) | `repo-level-cwm-v10` |\n\n---\n\n## 5. Zero-shot LLM Judge Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | vs Baseline (pp) | vs Fine-tuned 4B (pp) | Source |\n|-------|----------|---------|---------|-------------------|------------------------|--------|\n| Qwen3-8B | 64.40 | 72.20 | 50.50 | +12.65 | −24.03 | `llm-judge-8b-zeroshot` |\n| Qwen3-32B | 71.69 | 75.91 | 65.68 | +19.94 | −16.74 | `llm-judge-32b-zeroshot` |\n\nBoth models heavily biased toward predicting FAIL. 8B→32B scaling = +7.29pp, but still far below fine-tuned 4B (88.43%).\n\n---\n\n## 6. Statistical Analyses\n\n### 6.1 Block Correlation (ICC)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| ICC | 0.1909 | `block-corr-empirical` |\n| ICC p-value | < 0.0001 | `block-corr-empirical` |\n| Design Effect (DEFF) | 3.97 | `block-corr-empirical` |\n| Overall error rate | 12.49% | `block-corr-empirical` |\n| All-correct problems (observed) | 46 | `block-corr-empirical` |\n| All-correct problems (expected i.i.d.) | 16.35 | `block-corr-empirical` |\n| Inference precision | bfloat16 | `block-corr-empirical` |\n\nSignificant block correlation: tests within the same problem are NOT independent. DEFF=3.97 means effective sample size is ~4x smaller than nominal.\n\n### 6.2 Oracle F2P Stratified Analysis\n\n| # Tests per Problem | % of Problems | Block Advantage (pp) | Source |\n|---------------------|---------------|----------------------|--------|\n| T=1 | 68.7% | −0.09 (none) | `oracle-f2p-stratified` |\n| T=2 | 19.1% | +31.69 | `oracle-f2p-stratified` |\n| T=3–5 | 7.1% | +40.74 | `oracle-f2p-stratified` |\n| T≥6 | 5.1% | +40.06 | `oracle-f2p-stratified` |\n| **Overall** | | **+10.93** | `oracle-f2p-stratified` |\n\nT2 problems contribute 55.3% of overall block advantage despite being only 19.1% of problems.\n\n### 6.3 Per-test Diagnostic (CWM seed42)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Best mutation type | return_value (97.26%) | `per-test-precision-recall` |\n| Worst mutation type | off_by_one (82.56%) | `per-test-precision-recall` |\n| Perfect problems (114 total) | 48 (42.1%) | `per-test-precision-recall` |\n| Median problem fail-F1 | 94.12% | `per-test-precision-recall` |\n| FP count | 58 | `per-test-precision-recall` |\n| FN count | 178 | `per-test-precision-recall` |\n\n---\n\n## 7. Simulation Results (MVP-A)\n\n| Scenario | i.i.d. Advantage | Block Advantage | Pass? | Source |\n|----------|-----------------|-----------------|-------|--------|\n| P2P reg=5% | −1.0% | −0.5% | FAIL | `mvp-a-oracle-sim` |\n| P2P reg=10% | +13.2% | +8.3% | PASS | `mvp-a-oracle-sim` |\n| P2P reg=20% | +35.7% | +27.8% | PASS | `mvp-a-oracle-sim` |\n\nReal SWE-bench F2P distribution: median T=1, mean T=3, P75=2, P90=3.\n\n---\n\n## 8. Summary of Key Findings\n\n| Finding | Evidence |\n|---------|----------|\n| CLS > CWM at function-level | 4B: +1.24pp (88.43 vs 87.19), 8B: +2.43pp (89.39 vs 86.96) |\n| CLS scaling benefit (4B→8B) | +0.96pp (88.43→89.39) |\n| CWM no scaling benefit | −0.23pp (87.19→86.96) |\n| CLS-CWM gap widens with scale | 4B: 1.24pp → 8B: 2.43pp |\n| CLS ≈ TRAJ at variant level | gap=−0.45pp, TOST p=0.007 |\n| Per-test advantage is diagnostic | granularity, not raw accuracy |\n| Fine-tuned 4B >> zero-shot 32B | 88.43% vs 71.69% (+16.74pp) |\n| Repo-level 8B > 4B | 85.47% vs 82.35% (+3.12pp), updated with full s42 test sweep |\n| 8B multi-seed repo-level | mean test 84.56%, CLS−CWM gap ~26pp |\n| 4B v5 extended eval | val-best 90.07% (ckpt-4600), test 83.63% |\n| max_seq_length critical for repo | @2048: 20% unparseable → @5120: 0% |\n| Block correlation significant | ICC=0.19, DEFF=3.97 |\n| Per-test advantage needs reg≥10% | 5% regression → no advantage |\n",
      "numLines": 335,
      "startLine": 1,
      "totalLines": 335
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01SsbazwQzfEoe8Z61Ye1HAy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/error_analysis_data.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "a51f7088-907f-492a-8f9b-c4175a1cd94b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXp9e7SjkDn3Ahhpc68rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11112
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 10 · 2026-05-15T10:12:06.177Z_

<details><summary>↩ Tool result · `toolu_01SsbazwQzfEoe8Z61Ye1HAy`</summary>

```text
1	# CWM Error Analysis — Paper-Ready Data
2	
3	> Compiled: 2026-05-15. All numbers from registry experiments with matched environments (conda, transformers 4.57.6).
4	
5	---
6	
7	## 1. Headline Numbers: Repo-level CWM vs CLS
8	
9	| Metric | CWM v12 (s42) | CWM seed123 | CLS 4B best | CLS 8B (val-sel) | Majority BL |
10	|--------|---------------|-------------|-------------|------------------|-------------|
11	| **Accuracy** | 58.04% | 59.09% | 82.35% | **83.52%** | 72.96% |
12	| **F1 macro** | 51.67% | 43.43% | 74.74% | **77.50%** | — |
13	| **F1 fail** | 34.12% | 13.67% | 60.87% | **65.85%** | — |
14	| **F1 pass** | 69.22% | 73.19% | 88.60% | **89.14%** | — |
15	| **Unparseable rate** | 53.7% | 67.2% | 1.3% | 0% | — |
16	| **Parseable-only acc** | 42.88% | 42.68% | — | — | — |
17	| **vs Majority (pp)** | −14.92 | −13.87 | +9.39 | +10.56 | 0 |
18	
19	> **D088 修正**: CLS 8B 改用 val-selected ckpt-1000 (test=83.52%)，不再用 test-best ckpt-400 (84.79%)。F1 已从 `cls8b-s42-ckpt1000-test8192-eval` 补填：macro=77.50%, fail=65.85% (P=74.93%/R=58.73%), pass=89.14% (P=85.84%/R=92.72%)。Confusion: TP=6618, FP=1092, FN=520, TN=1554。
20	
21	- CLS-CWM gap (4B apple-to-apple): CLS v5-conda 76.37% vs CWM v12 58.04% = **18.33pp**
22	- CLS-CWM gap (best 4B CLS vs best 4B CWM): 82.35% vs 58.04% = **24.31pp**
23	- CLS-CWM gap (8B CLS vs 4B CWM): 83.52% vs 58.04% = **25.48pp**
24	- Both CWM seeds **below majority baseline** (72.96%) by ~14pp
25	
26	### Experiment References
27	
28	| exp_id | Model | Seed | Checkpoint | Eval Set |
29	|--------|-------|------|------------|----------|
30	| `repo-level-cwm-v12` | Qwen3-4B | 42 | ckpt-500 | test (n=9784) |
31	| `repo-level-cwm-seed123-conda` | Qwen3-4B | 123 | ckpt-500 | test (n=9784) |
32	| `repo-level-cls-v5` | Qwen3-4B | 42 | ckpt-4600 | test (n=9784) |
33	| `repo-level-cls-v5-conda` | Qwen3-4B | 42 | ckpt-600 | test (n=9784) |
34	| ~~`cls8b-s42-ckpt400-test8192-eval`~~ | ~~Qwen3-8B~~ | ~~42~~ | ~~ckpt-400~~ | ~~test@8192 (n=9784)~~ | ⚠️ superseded by D088 |
35	| `cls8b-s42-ckpt1000-test8192-eval` | Qwen3-8B | 42 | ckpt-1000 | test@8192 (n=9784) | **primary (val-sel)** |
36	
37	---
38	
39	## 2. Error Mode Breakdown (v11 subset-500, config identical to v12)
40	
41	Source: `cwm_error_mode_analysis.md` (500-sample analysis from v11 ckpt-600, max_new_tokens=1024, max_seq_length=2048)
42	
43	### 2.1 Unparseable Rate: 75.2% (376/500)
44	
45	| Category | Count | % of Unparseable |
46	|----------|-------|------------------|
47	| Neither pass nor fail keywords (no_keywords) | 289 | 76.9% |
48	| Both pass AND fail keywords (ambiguous_both) | 86 | 22.9% |
49	| Only fail keywords | 1 | 0.3% |
50	| Only pass keywords | 0 | 0.0% |
51	
52	"Neither" subcategories (289 samples):
53	- pytest dot-progress bars: 48.1%
54	- Command output / logs: 51.2%
55	- All cut off at token budget before reaching verdict
56	
57	### 2.2 Error Source Attribution (167 total errors in subset-500)
58	
59	| Error Source | Count | % of Errors |
60	|-------------|-------|-------------|
61	| Unparseable → defaulted to PASS, but true=FAIL | 96 | **57.5%** |
62	| Wrong parseable: true=PASS, pred=FAIL | 64 | 38.3% |
63	| Wrong parseable: true=FAIL, pred=PASS | 7 | 4.2% |
64	
65	**57.5% of all errors come from the unparseable-defaults-to-majority mechanism**, not from model predictions.
66	
67	### 2.3 Token Budget Exhaustion
68	
69	| Statistic | All Samples | "Neither" Unparseable |
70	|-----------|------------|----------------------|
71	| Mean gen length (chars) | 3,398 | 3,773 |
72	| Median | 3,308 | 3,933 |
73	| Max | 7,582 | 6,582 |
74	| Min | 722 | 1,002 |
75	
76	47.8% of all outputs exceed 3,500 chars. Typical pattern: model outputs `pytest -rA ...` → `test session starts` → hundreds of `.` dots → warnings → **cut off** (never reaches `passed/failed` summary).
77	
78	### 2.4 Parseable Prediction Quality (124/500 = 24.8%)
79	
80	| True Label | n | Accuracy |
81	|-----------|---|----------|
82	| FAIL | 39 | 82.1% |
83	| PASS | 85 | 24.7% |
84	| Overall | 124 | 42.7% |
85	
86	Model hallucinates failures: 64/71 wrong parseable predictions are PASS→FAIL.
87	
88	### 2.5 Input Truncation
89	
90	- 4.2% (21/500) truncated at max_seq_length=2048
91	- Truncated accuracy: 38.1% vs non-truncated: 67.9%
92	- 15/21 truncated samples also unparseable
93	
94	### 2.6 Confusion Matrix (v11 subset-500)
95	
96	| | Pred PASS | Pred FAIL |
97	|---|----------|-----------|
98	| True PASS | 301 (TP) | 64 (FP) |
99	| True FAIL | 103 (FN) | 32 (TN) |
100	
101	---
102	
103	## 3. Per-repo Variation
104	
105	From `repo-level-cwm-v12` notes:
106	- **Worst**: pytest — 25-42% accuracy
107	- **Best**: requests — 64-84% accuracy
108	
109	Per-repo unparseable rate (from task background):
110	- scikit-learn: ~0% unparseable
111	- sphinx: 100% unparseable
112	
113	The enormous per-repo variance reflects that CWM's ability to parse depends on the repo's test framework output format. Repos with concise pytest output (scikit-learn) are parseable; repos with verbose build/sphinx output are universally unparseable.
114	
115	---
116	
117	## 4. Cross-complexity Comparison (Function-level vs Repo-level)
118	
119	### Function-level CLS vs CWM (per-test, 1890 samples)
120	
121	| Config | CLS Acc | CWM Acc | Gap (pp) | p-value | Cohen's d |
122	|--------|---------|---------|----------|---------|-----------|
123	| 4B (5 seeds) | 88.43 ± 0.78 | 87.19 ± 0.37 | +1.24 | 0.025 | 1.24 |
124	| 8B (3 seeds) | 89.39 ± 1.09 | 86.96 ± 0.72 | +2.43 | 0.007 | 4.97 |
125	
126	### Repo-level CLS vs CWM (9784 samples)
127	
128	| Config | CLS Acc | CWM Acc | Gap (pp) |
129	|--------|---------|---------|----------|
130	| 4B apple-to-apple | 76.37% | 58.04% | **+18.33** |
131	| 4B best CLS vs CWM | 82.35% | 58.04% | **+24.31** |
132	| 8B CLS (val-sel) vs 4B CWM | 83.52% | 58.04% | **+25.48** |
133	
134	### Gap Amplification Summary
135	
136	| Complexity Level | CLS-CWM Gap (pp) | CWM Unparseable |
137	|-----------------|-------------------|-----------------|
138	| Function-level (4B) | 1.24 | 0% |
139	| Function-level (8B) | 2.43 | 0% |
140	| Repo-level (4B) | 18-24 | 54-67% |
141	
142	The gap explodes from ~1-2pp to ~24pp as code complexity increases from function-level to repo-level. This is the central C1 claim evidence.
143	
144	---
145	
146	## 5. "Correct by Accident" Analysis
147	
148	CWM's ~58-59% accuracy partly comes from unparseable outputs defaulting to majority class (PASS).
149	
150	- 38% of CWM "correct" predictions (in v12) are unparseable samples that happened to be PASS class
151	- Parseable-only accuracy: 42.88% (v12 s42) / 42.68% (seed123)
152	- Both parseable-only accuracies are below random (50%) — the model is **anti-informative** when parseable
153	
154	---
155	
156	## 6. Scaling Behavior (Function-level)
157	
158	| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |
159	|--------|---------|---------|-------------------|
160	| CLS | 88.43 | 89.39 | **+0.96** |
161	| CWM | 87.19 | 86.96 | **−0.23** |
162	
163	CLS benefits from scaling; CWM does not. CWM's bottleneck is generation overhead, not model capacity. Gap widens: 1.24pp (4B) → 2.43pp (8B), probability of widening p=0.988.
164	
165	---
166	
167	## 7. Three Inherent CWM Failure Modes
168	
169	### Mode 1: Token Budget Exhaustion (primary, ~77% of unparseable)
170	CWM must generate ~3400 chars of execution trace to reach a verdict vs CLS's 1-2 tokens. The model produces realistic pytest sessions with dots, warnings, and file paths that consume the entire budget before reaching any pass/fail summary.
171	
172	### Mode 2: Keyword Ambiguity (~23% of unparseable)
173	Realistic execution traces contain mixed pass/fail signals: test names with "fail", deprecation warnings, partial error messages. Keyword extraction cannot resolve these.
174	
175	### Mode 3: Hallucinated Failures (38% of parseable errors)
176	When parseable, CWM hallucinates failures for passing patches (PASS→FAIL = 64/71 wrong parseable). The model's attempt to simulate execution makes it prone to generating plausible-looking error messages.
177	
178	---
179	
180	## 8. Suggested Figures
181	
182	### Figure A: Per-repo Unparseable Rate (Bar Chart)
183	- X-axis: repos (scikit-learn, requests, django, ..., sphinx)
184	- Y-axis: unparseable rate (0-100%)
185	- Shows dramatic variation from ~0% to 100%
186	- **Position**: Error Analysis subsection or Appendix
187	
188	### Figure B: Error Mode Breakdown (Stacked Bar or Pie)
189	- Segments: no_keywords (77%), ambiguous_both (23%), other (<1%)
190	- Or: token exhaustion vs keyword ambiguity vs degenerate repetition
191	- **Position**: Error Analysis subsection
192	
193	### Figure C: CLS-CWM Gap Amplification (Grouped Bar)
194	- X-axis: function-level 4B, function-level 8B, repo-level 4B
195	- Y-axis: accuracy gap (pp)
196	- Values: 1.24, 2.43, 24.31
197	- **Position**: Main results section, key visualization for C1 claim
198	
199	### Figure D: Error Source Attribution (Stacked Bar)
200	- Three segments: unparseable-default (57.5%), wrong parseable PASS→FAIL (38.3%), wrong parseable FAIL→PASS (4.2%)
201	- **Position**: Error Analysis subsection
202	
203	### Figure E: CWM Scaling Non-benefit (Line Plot)
204	- Two lines: CLS (88.43 → 89.39) vs CWM (87.19 → 86.96)
205	- X-axis: 4B, 8B
206	- **Position**: Discussion or Results
207	
208	---
209	
210	## 9. Paper Placement Recommendations
211	
212	| Data | Section | Rationale |
213	|------|---------|-----------|
214	| CLS-CWM gap amplification (§4 table) | **Results §5.3** (Repo-level) | Central finding, C1 claim |
215	| Error mode breakdown (§2) | **Analysis §5.4** or **§6** | Explains WHY CWM fails |
216	| Unparseable rate comparison (54-67% vs 0-1.3%) | **Results §5.3** | Headline comparison metric |
217	| Parseable-only accuracy (42.88%) | **Analysis §5.4** | Shows CWM is anti-informative |
218	| Correct-by-accident (38%) | **Analysis §5.4** | Deflates apparent CWM performance |
219	| Scaling non-benefit (§6) | **Discussion §7** | Architectural implication |
220	| Token exhaustion examples | **Appendix** | Qualitative illustration |
221	| Per-repo breakdown | **Appendix** | Supporting detail |
222	| Confusion matrix | **Appendix** | Full transparency |
223	
224	---
225	
226	## 10. Key Sentences for the Paper
227	
228	1. "CWM accuracy drops from 87.19% at function-level to 58.04% at repo-level (−29pp), falling 14.92pp below the majority baseline, while CLS maintains above-baseline performance at both complexity levels."
229	
230	2. "53.7-67.2% of CWM outputs are unparseable, with 77% of unparseable cases caused by token budget exhaustion — the model generates realistic pytest execution traces that consume the entire generation budget before reaching any verdict."
231	
232	3. "Even among parseable CWM outputs, accuracy is only 42.88% — below random chance — indicating the model is anti-informative when it does produce interpretable predictions."
233	
234	4. "57.5% of CWM errors stem from the unparseable-defaults-to-majority mechanism rather than incorrect predictions, suggesting the generative approach fundamentally cannot produce reliable execution simulations at repo scale."
235	
236	5. "The CLS-CWM gap widens from 1.24pp (4B) to 2.43pp (8B) at function-level (p=0.025, d=1.24), and explodes to 24pp at repo-level, supporting the hypothesis that classification approaches scale better than generation for execution simulation."
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "4f4aa702-8d0a-42be-8c68-0a0890880f1b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/error_analysis_data.md",
      "content": "# CWM Error Analysis — Paper-Ready Data\n\n> Compiled: 2026-05-15. All numbers from registry experiments with matched environments (conda, transformers 4.57.6).\n\n---\n\n## 1. Headline Numbers: Repo-level CWM vs CLS\n\n| Metric | CWM v12 (s42) | CWM seed123 | CLS 4B best | CLS 8B (val-sel) | Majority BL |\n|--------|---------------|-------------|-------------|------------------|-------------|\n| **Accuracy** | 58.04% | 59.09% | 82.35% | **83.52%** | 72.96% |\n| **F1 macro** | 51.67% | 43.43% | 74.74% | **77.50%** | — |\n| **F1 fail** | 34.12% | 13.67% | 60.87% | **65.85%** | — |\n| **F1 pass** | 69.22% | 73.19% | 88.60% | **89.14%** | — |\n| **Unparseable rate** | 53.7% | 67.2% | 1.3% | 0% | — |\n| **Parseable-only acc** | 42.88% | 42.68% | — | — | — |\n| **vs Majority (pp)** | −14.92 | −13.87 | +9.39 | +10.56 | 0 |\n\n> **D088 修正**: CLS 8B 改用 val-selected ckpt-1000 (test=83.52%)，不再用 test-best ckpt-400 (84.79%)。F1 已从 `cls8b-s42-ckpt1000-test8192-eval` 补填：macro=77.50%, fail=65.85% (P=74.93%/R=58.73%), pass=89.14% (P=85.84%/R=92.72%)。Confusion: TP=6618, FP=1092, FN=520, TN=1554。\n\n- CLS-CWM gap (4B apple-to-apple): CLS v5-conda 76.37% vs CWM v12 58.04% = **18.33pp**\n- CLS-CWM gap (best 4B CLS vs best 4B CWM): 82.35% vs 58.04% = **24.31pp**\n- CLS-CWM gap (8B CLS vs 4B CWM): 83.52% vs 58.04% = **25.48pp**\n- Both CWM seeds **below majority baseline** (72.96%) by ~14pp\n\n### Experiment References\n\n| exp_id | Model | Seed | Checkpoint | Eval Set |\n|--------|-------|------|------------|----------|\n| `repo-level-cwm-v12` | Qwen3-4B | 42 | ckpt-500 | test (n=9784) |\n| `repo-level-cwm-seed123-conda` | Qwen3-4B | 123 | ckpt-500 | test (n=9784) |\n| `repo-level-cls-v5` | Qwen3-4B | 42 | ckpt-4600 | test (n=9784) |\n| `repo-level-cls-v5-conda` | Qwen3-4B | 42 | ckpt-600 | test (n=9784) |\n| ~~`cls8b-s42-ckpt400-test8192-eval`~~ | ~~Qwen3-8B~~ | ~~42~~ | ~~ckpt-400~~ | ~~test@8192 (n=9784)~~ | ⚠️ superseded by D088 |\n| `cls8b-s42-ckpt1000-test8192-eval` | Qwen3-8B | 42 | ckpt-1000 | test@8192 (n=9784) | **primary (val-sel)** |\n\n---\n\n## 2. Error Mode Breakdown (v11 subset-500, config identical to v12)\n\nSource: `cwm_error_mode_analysis.md` (500-sample analysis from v11 ckpt-600, max_new_tokens=1024, max_seq_length=2048)\n\n### 2.1 Unparseable Rate: 75.2% (376/500)\n\n| Category | Count | % of Unparseable |\n|----------|-------|------------------|\n| Neither pass nor fail keywords (no_keywords) | 289 | 76.9% |\n| Both pass AND fail keywords (ambiguous_both) | 86 | 22.9% |\n| Only fail keywords | 1 | 0.3% |\n| Only pass keywords | 0 | 0.0% |\n\n\"Neither\" subcategories (289 samples):\n- pytest dot-progress bars: 48.1%\n- Command output / logs: 51.2%\n- All cut off at token budget before reaching verdict\n\n### 2.2 Error Source Attribution (167 total errors in subset-500)\n\n| Error Source | Count | % of Errors |\n|-------------|-------|-------------|\n| Unparseable → defaulted to PASS, but true=FAIL | 96 | **57.5%** |\n| Wrong parseable: true=PASS, pred=FAIL | 64 | 38.3% |\n| Wrong parseable: true=FAIL, pred=PASS | 7 | 4.2% |\n\n**57.5% of all errors come from the unparseable-defaults-to-majority mechanism**, not from model predictions.\n\n### 2.3 Token Budget Exhaustion\n\n| Statistic | All Samples | \"Neither\" Unparseable |\n|-----------|------------|----------------------|\n| Mean gen length (chars) | 3,398 | 3,773 |\n| Median | 3,308 | 3,933 |\n| Max | 7,582 | 6,582 |\n| Min | 722 | 1,002 |\n\n47.8% of all outputs exceed 3,500 chars. Typical pattern: model outputs `pytest -rA ...` → `test session starts` → hundreds of `.` dots → warnings → **cut off** (never reaches `passed/failed` summary).\n\n### 2.4 Parseable Prediction Quality (124/500 = 24.8%)\n\n| True Label | n | Accuracy |\n|-----------|---|----------|\n| FAIL | 39 | 82.1% |\n| PASS | 85 | 24.7% |\n| Overall | 124 | 42.7% |\n\nModel hallucinates failures: 64/71 wrong parseable predictions are PASS→FAIL.\n\n### 2.5 Input Truncation\n\n- 4.2% (21/500) truncated at max_seq_length=2048\n- Truncated accuracy: 38.1% vs non-truncated: 67.9%\n- 15/21 truncated samples also unparseable\n\n### 2.6 Confusion Matrix (v11 subset-500)\n\n| | Pred PASS | Pred FAIL |\n|---|----------|-----------|\n| True PASS | 301 (TP) | 64 (FP) |\n| True FAIL | 103 (FN) | 32 (TN) |\n\n---\n\n## 3. Per-repo Variation\n\nFrom `repo-level-cwm-v12` notes:\n- **Worst**: pytest — 25-42% accuracy\n- **Best**: requests — 64-84% accuracy\n\nPer-repo unparseable rate (from task background):\n- scikit-learn: ~0% unparseable\n- sphinx: 100% unparseable\n\nThe enormous per-repo variance reflects that CWM's ability to parse depends on the repo's test framework output format. Repos with concise pytest output (scikit-learn) are parseable; repos with verbose build/sphinx output are universally unparseable.\n\n---\n\n## 4. Cross-complexity Comparison (Function-level vs Repo-level)\n\n### Function-level CLS vs CWM (per-test, 1890 samples)\n\n| Config | CLS Acc | CWM Acc | Gap (pp) | p-value | Cohen's d |\n|--------|---------|---------|----------|---------|-----------|\n| 4B (5 seeds) | 88.43 ± 0.78 | 87.19 ± 0.37 | +1.24 | 0.025 | 1.24 |\n| 8B (3 seeds) | 89.39 ± 1.09 | 86.96 ± 0.72 | +2.43 | 0.007 | 4.97 |\n\n### Repo-level CLS vs CWM (9784 samples)\n\n| Config | CLS Acc | CWM Acc | Gap (pp) |\n|--------|---------|---------|----------|\n| 4B apple-to-apple | 76.37% | 58.04% | **+18.33** |\n| 4B best CLS vs CWM | 82.35% | 58.04% | **+24.31** |\n| 8B CLS (val-sel) vs 4B CWM | 83.52% | 58.04% | **+25.48** |\n\n### Gap Amplification Summary\n\n| Complexity Level | CLS-CWM Gap (pp) | CWM Unparseable |\n|-----------------|-------------------|-----------------|\n| Function-level (4B) | 1.24 | 0% |\n| Function-level (8B) | 2.43 | 0% |\n| Repo-level (4B) | 18-24 | 54-67% |\n\nThe gap explodes from ~1-2pp to ~24pp as code complexity increases from function-level to repo-level. This is the central C1 claim evidence.\n\n---\n\n## 5. \"Correct by Accident\" Analysis\n\nCWM's ~58-59% accuracy partly comes from unparseable outputs defaulting to majority class (PASS).\n\n- 38% of CWM \"correct\" predictions (in v12) are unparseable samples that happened to be PASS class\n- Parseable-only accuracy: 42.88% (v12 s42) / 42.68% (seed123)\n- Both parseable-only accuracies are below random (50%) — the model is **anti-informative** when parseable\n\n---\n\n## 6. Scaling Behavior (Function-level)\n\n| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |\n|--------|---------|---------|-------------------|\n| CLS | 88.43 | 89.39 | **+0.96** |\n| CWM | 87.19 | 86.96 | **−0.23** |\n\nCLS benefits from scaling; CWM does not. CWM's bottleneck is generation overhead, not model capacity. Gap widens: 1.24pp (4B) → 2.43pp (8B), probability of widening p=0.988.\n\n---\n\n## 7. Three Inherent CWM Failure Modes\n\n### Mode 1: Token Budget Exhaustion (primary, ~77% of unparseable)\nCWM must generate ~3400 chars of execution trace to reach a verdict vs CLS's 1-2 tokens. The model produces realistic pytest sessions with dots, warnings, and file paths that consume the entire budget before reaching any pass/fail summary.\n\n### Mode 2: Keyword Ambiguity (~23% of unparseable)\nRealistic execution traces contain mixed pass/fail signals: test names with \"fail\", deprecation warnings, partial error messages. Keyword extraction cannot resolve these.\n\n### Mode 3: Hallucinated Failures (38% of parseable errors)\nWhen parseable, CWM hallucinates failures for passing patches (PASS→FAIL = 64/71 wrong parseable). The model's attempt to simulate execution makes it prone to generating plausible-looking error messages.\n\n---\n\n## 8. Suggested Figures\n\n### Figure A: Per-repo Unparseable Rate (Bar Chart)\n- X-axis: repos (scikit-learn, requests, django, ..., sphinx)\n- Y-axis: unparseable rate (0-100%)\n- Shows dramatic variation from ~0% to 100%\n- **Position**: Error Analysis subsection or Appendix\n\n### Figure B: Error Mode Breakdown (Stacked Bar or Pie)\n- Segments: no_keywords (77%), ambiguous_both (23%), other (<1%)\n- Or: token exhaustion vs keyword ambiguity vs degenerate repetition\n- **Position**: Error Analysis subsection\n\n### Figure C: CLS-CWM Gap Amplification (Grouped Bar)\n- X-axis: function-level 4B, function-level 8B, repo-level 4B\n- Y-axis: accuracy gap (pp)\n- Values: 1.24, 2.43, 24.31\n- **Position**: Main results section, key visualization for C1 claim\n\n### Figure D: Error Source Attribution (Stacked Bar)\n- Three segments: unparseable-default (57.5%), wrong parseable PASS→FAIL (38.3%), wrong parseable FAIL→PASS (4.2%)\n- **Position**: Error Analysis subsection\n\n### Figure E: CWM Scaling Non-benefit (Line Plot)\n- Two lines: CLS (88.43 → 89.39) vs CWM (87.19 → 86.96)\n- X-axis: 4B, 8B\n- **Position**: Discussion or Results\n\n---\n\n## 9. Paper Placement Recommendations\n\n| Data | Section | Rationale |\n|------|---------|-----------|\n| CLS-CWM gap amplification (§4 table) | **Results §5.3** (Repo-level) | Central finding, C1 claim |\n| Error mode breakdown (§2) | **Analysis §5.4** or **§6** | Explains WHY CWM fails |\n| Unparseable rate comparison (54-67% vs 0-1.3%) | **Results §5.3** | Headline comparison metric |\n| Parseable-only accuracy (42.88%) | **Analysis §5.4** | Shows CWM is anti-informative |\n| Correct-by-accident (38%) | **Analysis §5.4** | Deflates apparent CWM performance |\n| Scaling non-benefit (§6) | **Discussion §7** | Architectural implication |\n| Token exhaustion examples | **Appendix** | Qualitative illustration |\n| Per-repo breakdown | **Appendix** | Supporting detail |\n| Confusion matrix | **Appendix** | Full transparency |\n\n---\n\n## 10. Key Sentences for the Paper\n\n1. \"CWM accuracy drops from 87.19% at function-level to 58.04% at repo-level (−29pp), falling 14.92pp below the majority baseline, while CLS maintains above-baseline performance at both complexity levels.\"\n\n2. \"53.7-67.2% of CWM outputs are unparseable, with 77% of unparseable cases caused by token budget exhaustion — the model generates realistic pytest execution traces that consume the entire generation budget before reaching any verdict.\"\n\n3. \"Even among parseable CWM outputs, accuracy is only 42.88% — below random chance — indicating the model is anti-informative when it does produce interpretable predictions.\"\n\n4. \"57.5% of CWM errors stem from the unparseable-defaults-to-majority mechanism rather than incorrect predictions, suggesting the generative approach fundamentally cannot produce reliable execution simulations at repo scale.\"\n\n5. \"The CLS-CWM gap widens from 1.24pp (4B) to 2.43pp (8B) at function-level (p=0.025, d=1.24), and explodes to 24pp at repo-level, supporting the hypothesis that classification approaches scale better than generation for execution simulation.\"\n",
      "numLines": 237,
      "startLine": 1,
      "totalLines": 237
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze each file against the requirements:

### 1. val_sweep_compilation.md

**Check: seed123 ckpt-6200 test and ckpt-6400 test should be marked as "v1 failed (--max_samples 8192), v2 重跑中"**

Looking at section 4 "Cross-seed Reference: 8B seed123", the test section (line 96-101) only has ckpt-3000. There are no ckpt-6200 or ckpt-6400 test entries at all. 

The user wants these annotated even though they don't exist in the table—they only appear in the val sweep. I need to add notes indicating that ckpt-6200 and ckpt-6400 test evaluations failed in v1 and v2 is currently being re-run.

**Check: s42 ckpt-200 val should be marked as "FAILED: resume 目录无 ckpt-200"**

Looking at section 1 (line 11), ckpt-200 actually has data: accuracy 63.52, f1_macro 61.17, etc. from exp_id "cls8b-s42-ckpt200-val8192-eval-v2". But the user's requirement says this should be marked as failed because the resume directory doesn't have ckpt-200, so there's a conflict between what the table shows and what the user expects. Looking at what's actually in the data versus what should be there, I need to identify three gaps: seed123 needs test entries for ckpt-6200 and ckpt-6400 marked with v1 failed annotations, s42 ckpt-200 val should be flagged as failed despite showing data, and the 4B seed123 test results with that specific accuracy metric are completely missing. Looking at the comprehensive results summary, I see that section 4.4 only contains validation results for seed123, with no test entries—and the user mentions a 4B seed123 test result with 75.33% accuracy that should be added. For the edits, I need to add the missing seed123 test entries with notes about v1 failures and v2 reruns, update the val_sweep_compilation.md file accordingly, and include the negative test result the user referenced. I need to verify what the user is actually asking for—whether these annotations should already exist in the document or if they're pointing out what needs to be added. The key issue is understanding if the current ckpt-200 val data represents a successful run or if there's a mismatch between what's recorded and what should be marked as failed due to missing resume checkpoints.

Let me take a practical approach: the ckpt-200 val result from v2 is legitimate since that experiment completed successfully, so I shouldn't retroactively mark it as failed. But I do need to add the missing entries—the ckpt-6200 and ckpt-6400 test results for seed123, plus the 4B seed123 test result. I'll check the comprehensive results summary to see what's currently documented there. that ckpt-200 might not actually exist in the training checkpoint directory, which would make any evaluation results using it invalid. I should flag this entry with a note about the missing checkpoint. For the 4B seed123 test section, I need to figure out where it belongs in the document structure since val_sweep_compilation.md might not be the right place for it. I should add the 4B seed123 test result after the 4B seed123 validation section in comprehensive_results_summary.md. For the val_sweep_compilation.md edits, I need to handle the ckpt-200 annotation carefully—since the resume directory might not actually contain that checkpoint, I should add a note rather than modify the table directly, but I'm uncertain whether the eval data is from a valid source.

For the test entries, I'll add the ckpt-6200 and ckpt-6400 rows with their failure statuses after the existing ckpt-3000 test entry. I also need to update the JSON section and summary sections to reflect these new test entries. I'm working through the specific edits needed for these documentation files. Looking at the 4B seed123 test results more carefully—the 75.33% accuracy result is marked as "negative," but I need to understand what that label means in context since it's actually above the 72.96% majority baseline. Let me trace through the validation results at different sequence lengths to find the best checkpoint and understand the performance pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "3ff68501-371c-4146-b3dd-86266dcd99fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Nx6XWwiryh1jDZYMHbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18695,
      "cache_read_input_tokens": 22953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18695
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

_source line 12_

Reading all three files to assess current state against the requirements.

Here's what I found:

**val_sweep_compilation.md:**
1. seed123 ckpt-6200/6400 test entries — missing entirely (only ckpt-3000 test exists)
2. s42 ckpt-200 val — shows data (63.52%) with no FAILED annotation
3. 4B seed123 test — no section exists

**comprehensive_results_summary.md:**
- 4B seed123 test result (75.33%) — missing; section 4.4 only has val data

**error_analysis_data.md:**
- No references to ckpt-200 anywhere — clean

Applying fixes now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "ec5298e3-4161-49ce-b13d-d67cc4c4f751",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Nx6XWwiryh1jDZYMHbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18695,
      "cache_read_input_tokens": 22953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18695
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_016LcfDd8bUrprPmSrqhepDm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 |",
  "new_string": "| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "dbd7325c-9594-427f-8947-d4394a9336bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Nx6XWwiryh1jDZYMHbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18695,
      "cache_read_input_tokens": 22953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18695
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

_source line 14 · 2026-05-15T10:13:24.080Z_

<details><summary>↩ Tool result · `toolu_016LcfDd8bUrprPmSrqhepDm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "9eaace8c-8a3d-4d4d-a57f-298ca2ff6f35",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 |",
    "newString": "| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " | Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |",
          " |-----------|-------------|-------------|------------|------------|---------------|",
          "-| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 |",
          "+| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |",
          " | ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |",
          " | ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |",
          " | ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01J2923VSBS3XYDTesQHdfzQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "Notes:\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15",
  "new_string": "Notes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "646373bf-3c95-4ce6-bf48-3b89f3dd6669",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuQ59nXiEkq2GgYcQL53tT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4003,
      "cache_read_input_tokens": 41648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4003
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

_source line 16 · 2026-05-15T10:13:30.801Z_

<details><summary>↩ Tool result · `toolu_01J2923VSBS3XYDTesQHdfzQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "f41c4532-caab-4c2b-ba03-db461b7620f5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "Notes:\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15",
    "newString": "Notes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 6,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " Majority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).",
          " ",
          " Notes:",
          "+- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑",
          " - ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)",
          " - ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)",
          " - 72.96% is the test set majority baseline, not val — corrected 2026-05-15"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01WM2xmKpU9MBYJ4HTP1WnEA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n\n---",
  "new_string": "| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "81091c31-87c6-4d52-a3f0-5da9abb863ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJsHrREvfb1fL5x9Pq4oWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 45651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 18 · 2026-05-15T10:13:36.093Z_

<details><summary>↩ Tool result · `toolu_01WM2xmKpU9MBYJ4HTP1WnEA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "f7ae261a-f825-4c32-a259-435b47750d41",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n\n---",
    "newString": "| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 99,
        "oldLines": 6,
        "newStart": 99,
        "newLines": 8,
        "lines": [
          " | Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |",
          " |-----------|-------------|-------------|------------|------------|---------------|",
          " | ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |",
          "+| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |",
          "+| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01FfJqcPcNGGcQ7MAzMjrzkk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "Notes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference",
  "new_string": "Notes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "94df937a-21c4-485d-b1ad-ec5834edde31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpgPM9qGBk8pJDhAMr6jaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 46087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 20 · 2026-05-15T10:13:44.134Z_

<details><summary>↩ Tool result · `toolu_01FfJqcPcNGGcQ7MAzMjrzkk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "795ef608-e679-450d-a25d-d2441a43487a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "Notes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference",
    "newString": "Notes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 6,
        "newStart": 82,
        "newLines": 18,
        "lines": [
          " ",
          " ---",
          " ",
          "+## 3c. 4B seed123 Test@5120 (n=9784)",
          "+",
          "+| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |",
          "+|-----------|-------------|-------------|------------|------------|---------------|",
          "+| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |",
          "+",
          "+Notes:",
          "+- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp",
          "+- Only +2.37pp above majority baseline — negative result",
          "+",
          "+---",
          "+",
          " ## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)",
          " ",
          " | Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 21_

Now update the summary table and JSON in val_sweep_compilation.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "f798af0e-fc4b-47b4-9b01-b844dff0241a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QS9C3Cux7pAkwL8LSEvBnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 46488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Fe7u2fDAYLMGtMtKodvPEi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |",
  "new_string": "| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "37635187-4e11-4a04-881c-9ba03f51d8d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QS9C3Cux7pAkwL8LSEvBnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 46488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
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

_source line 23 · 2026-05-15T10:13:50.033Z_

<details><summary>↩ Tool result · `toolu_01Fe7u2fDAYLMGtMtKodvPEi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "49020bf6-de71-4d47-9356-a2760f31a63f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |",
    "newString": "| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 124,
        "oldLines": 6,
        "newStart": 124,
        "newLines": 7,
        "lines": [
          " | 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |",
          " | 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |",
          " | 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |",
          "+| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |",
          " | 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |",
          " | 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 24_

Now add the 4B seed123 test to the JSON section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "8a75e42c-a25f-45ab-927d-9a589ab40ce0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JaKWYKzFzzBjGF1myx7t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 46947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
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

<details open><summary>🔧 Tool call — Edit · `toolu_01U4aWAcnQd16b5oVzjHbZ2Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "  \"8b_seed123_val8192\": {",
  "new_string": "  \"4b_seed123_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-800\": {\"accuracy\": 75.33, \"f1_macro\": null, \"f1_pass\": null, \"f1_fail\": null, \"exp_id\": \"negative-result\", \"note\": \"val-best, barely above baseline\"}\n    }\n  },\n  \"8b_seed123_val8192\": {"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "5009148f-55fb-4cab-aedd-652b577a9992",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JaKWYKzFzzBjGF1myx7t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 46947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
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

_source line 26 · 2026-05-15T10:13:55.161Z_

<details><summary>↩ Tool result · `toolu_01U4aWAcnQd16b5oVzjHbZ2Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "cd5831e4-1c90-40a0-b745-5d701e44bfd5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "  \"8b_seed123_val8192\": {",
    "newString": "  \"4b_seed123_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-800\": {\"accuracy\": 75.33, \"f1_macro\": null, \"f1_pass\": null, \"f1_fail\": null, \"exp_id\": \"negative-result\", \"note\": \"val-best, barely above baseline\"}\n    }\n  },\n  \"8b_seed123_val8192\": {",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 176,
        "oldLines": 6,
        "newStart": 176,
        "newLines": 12,
        "lines": [
          "       \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}",
          "     }",
          "   },",
          "+  \"4b_seed123_test5120\": {",
          "+    \"majority_baseline\": 72.96,",
          "+    \"checkpoints\": {",
          "+      \"ckpt-800\": {\"accuracy\": 75.33, \"f1_macro\": null, \"f1_pass\": null, \"f1_fail\": null, \"exp_id\": \"negative-result\", \"note\": \"val-best, barely above baseline\"}",
          "+    }",
          "+  },",
          "   \"8b_seed123_val8192\": {",
          "     \"majority_baseline\": 75.88,",
          "     \"checkpoints\": {"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 27_

Now update comprehensive_results_summary.md — add 4B seed123 test after section 4.4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "8cead05e-c3d9-426e-962c-9d9b9be57d33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgP9x3maozrJBBnM8YbNMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 47492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01FGNVQFXHgD3N4Xsh7NBW5A`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md",
  "old_string": "Key finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.5 CLS 8B seed42",
  "new_string": "Key finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.4b CLS 4B seed123 — Test (val-selected ckpt-800, @5120)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Source |\n|-------|-----------|----------|----------|--------|\n| test@5120 | 800 (val-best) | 75.33% | — | negative result |\n\n⚠️ Negative result: 75.33% is only +2.37pp above majority baseline (72.96%). Val-best ckpt-800 (87.92%) → test 75.33% = 12.59pp val-test gap. Much worse than seed42 4B v5 (test 83.63%) and 8B models (test ~85%).\n\n### 4.5 CLS 8B seed42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "1f4b1475-84a0-4e53-8c87-88df1479f0ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgP9x3maozrJBBnM8YbNMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 47492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 29 · 2026-05-15T10:14:05.055Z_

<details><summary>↩ Tool result · `toolu_01FGNVQFXHgD3N4Xsh7NBW5A`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "649c4056-e6c2-476c-b642-d314cc439efb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md",
    "oldString": "Key finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.5 CLS 8B seed42",
    "newString": "Key finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.4b CLS 4B seed123 — Test (val-selected ckpt-800, @5120)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Source |\n|-------|-----------|----------|----------|--------|\n| test@5120 | 800 (val-best) | 75.33% | — | negative result |\n\n⚠️ Negative result: 75.33% is only +2.37pp above majority baseline (72.96%). Val-best ckpt-800 (87.92%) → test 75.33% = 12.59pp val-test gap. Much worse than seed42 4B v5 (test 83.63%) and 8B models (test ~85%).\n\n### 4.5 CLS 8B seed42",
    "originalFile": "# Comprehensive Results Summary\n\n> Generated: 2026-05-15 (updated). All numbers sourced from registry (DONE + success only).\n> Excluded: `cls8b-seed123-ckpt3000-val8192-eval` (old training artifact, invalid).\n\n---\n\n## 1. Dataset\n\n| Split | Samples | Class Balance | Majority Baseline |\n|-------|---------|---------------|-------------------|\n| Train | 15,290 | pass 52% / fail 48% | 52.0% |\n| Val | 1,896 | — | — |\n| Test (function) | 1,890 | — | 51.75% |\n| Test (repo) | 9,784 | — | 72.96% |\n| Val (repo) | 9,335 | — | ~75.9% |\n\n5 mutation types: operator_swap, return_value, boundary_removal, variable_swap, off_by_one.\nSource: `mvp-b-data-prep`\n\n---\n\n## 2. Function-level Results (per-test, 1890 test samples)\n\n### 2.1 CLS 4B — 5 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-----------|----------|-----------|----------|--------|\n| 42 | 87.83 | 88.06 | 87.59 | 89.45 | 86.71 | 86.20 | 89.04 | `multi-seed-core` |\n| 123 | 89.52 | 89.64 | 89.40 | 91.76 | 87.63 | 87.34 | 91.56 | `multi-seed-core` |\n| 456 | 87.88 | 87.53 | 88.21 | 93.60 | 82.21 | 83.12 | 93.97 | `multi-seed-core` |\n| 789 | 89.00 | 88.90 | 89.10 | 93.30 | 84.90 | 85.20 | 93.40 | `cls-seed789` |\n| 0 | 87.94 | 87.79 | 88.08 | 92.13 | 83.84 | 84.20 | 92.32 | `cls-seed0` |\n| **Mean** | **88.43** | **88.38** | **88.48** | | | | | |\n| **Std** | **0.78** | **0.88** | **0.68** | | | | | |\n\n### 2.2 CWM 4B — 5 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-------------|-----------|----------|-----------|----------|--------|\n| 42 | 87.51 | 87.15 | 87.86 | — | 93.24 | 81.80 | 82.75 | 93.64 | `per-test-precision-recall` |\n| 123 | 87.20 | 86.95 | 87.44 | 84.44 | — | — | — | — | `cwm-seed123` |\n| 456 | 86.98 | 86.66 | 87.29 | 84.02 | 92.26 | 81.70 | 82.52 | 92.65 | `cwm-seed456` |\n| 789 | 86.67 | 86.74 | 86.60 | 83.97 | 89.37 | 84.25 | 84.09 | 89.25 | `cwm-seed789` |\n| 0 | 87.57 | 87.18 | 87.93 | 84.29 | 93.45 | 81.70 | 82.71 | 93.86 | `cwm-seed0` |\n| **Mean** | **87.19** | **86.94** | **87.42** | **84.18** | | | | | |\n| **Std** | **0.37** | **0.22** | **0.52** | **0.21** | | | | | |\n\n### 2.3 CLS 8B — 3 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-----------|----------|-----------|----------|--------|\n| 42 | 90.48 | 90.86 | 90.06 | 90.22 | 91.51 | 90.76 | 89.36 | `cls8b-eval-seed42` |\n| 123 | 89.37 | 89.54 | 89.19 | 91.20 | 87.93 | 87.54 | 90.90 | `cls8b-eval-seed123` |\n| 456 | 88.31 | 88.20 | 88.41 | 92.29 | 84.46 | 84.72 | 92.43 | `cls8b-seed456` |\n| **Mean** | **89.39** | **89.53** | **89.22** | | | | | |\n| **Std** | **1.09** | **1.33** | **0.83** | | | | | |\n\n### 2.4 CWM 8B — 3 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Source |\n|------|----------|---------|---------|-------------|--------|\n| 42 | 87.67 | 87.57 | 87.77 | 84.39 | `model-size-scaling-cwm8b` |\n| 123 | 86.98 | 86.83 | 87.13 | 84.13 | `cwm8b-seed123` |\n| 456 | 86.24 | 85.96 | 86.51 | 82.80 | `cwm8b-seed456` |\n| **Mean** | **86.96** | **86.79** | **87.14** | **83.77** | |\n| **Std** | **0.72** | **0.82** | **0.63** | **0.86** | |\n\n### 2.5 CLS vs CWM Comparison\n\n| Config | CLS Acc (mean) | CWM Acc (mean) | Gap (pp) | Seeds |\n|--------|---------------|----------------|----------|-------|\n| 4B | 88.43 ± 0.78 | 87.19 ± 0.37 | **+1.24** | 5 vs 5 |\n| 8B | 89.39 ± 1.09 | 86.96 ± 0.72 | **+2.43** | 3 vs 3 |\n\nGap widens from +1.24pp (4B) to +2.43pp (8B) — supports complexity hypothesis.\n\n### 2.6 Model Size Scaling (4B → 8B)\n\n| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |\n|--------|---------|---------|-------------------|\n| CLS | 88.43 | 89.39 | **+0.96** |\n| CWM | 87.19 | 86.96 | **−0.23** |\n\nCLS benefits from scaling; CWM does not (bottleneck is generative complexity, not model capacity).\n\n---\n\n## 3. Trajectory-level Results (1032 variants, 5 seeds)\n\n| Seed | Accuracy | Unresolved F1 | Resolved F1 | Consistency | Source |\n|------|----------|---------------|-------------|-------------|--------|\n| 42 | 85.66 | 87.50 | 83.18 | 79.94 | `traj-level-finetuned` |\n| 123 | 85.47 | 87.00 | 83.52 | 78.59 | `traj-level-seed123` |\n| 456 | 87.40 | 88.70 | 85.80 | 78.80 | `traj-level-seed456` |\n| 789 | 87.31 | 88.27 | 86.17 | 76.74 | `traj-level-seed789` |\n| 0 | 85.66 | 87.37 | 83.41 | 79.55 | `traj-level-seed0` |\n| **Mean** | **86.30** | **87.77** | **84.42** | **78.72** | |\n| **Std** | **0.97** | **0.68** | **1.45** | **1.26** | |\n\n### CLS vs TRAJ (variant-level, clustered bootstrap)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp | `5-paired-clustered-bootstrap` |\n| 95% CI | [−1.71, +0.84] | `5-paired-clustered-bootstrap` |\n| p-value | 0.499 (not significant) | `5-paired-clustered-bootstrap` |\n| TOST p-value (±2pp margin) | 0.0071 (equivalent) | `5-paired-clustered-bootstrap` |\n\nPer-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29.\n\n**Conclusion**: CLS and TRAJ are statistically equivalent at variant level. Per-test's advantage is diagnostic granularity (which test fails), not raw accuracy.\n\n---\n\n## 4. Repo-level Results (majority baseline: 72.96%)\n\n### 4.1 CLS 4B seed42 — Test Set (v5, home-1x5090, transformers 4.57.6)\n\nmax_seq_length=2048, eval_samples=9,784, unparseable=132 (1.3%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | vs Baseline (pp) | Source |\n|-----------|----------|----------|---------|---------|-------------------|--------|\n| 600 | 76.74 | 73.74 | 64.88 | 82.61 | +3.78 | `repo-level-cls-v5` |\n| 4000 | 81.51 | 72.56 | 56.90 | 88.23 | +8.55 | `repo-level-cls-v5` |\n| 4200 | 80.64 | 72.10 | 56.66 | 87.54 | +7.68 | `repo-level-cls-v5` |\n| 4400 | 82.11 | 73.94 | 59.34 | — | +9.15 | `repo-level-cls-v5` |\n| **4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39** | `repo-level-cls-v5` |\n\nBest: ckpt-4600 (both accuracy and F1 macro).\n\n### 4.2 CLS 4B seed42 — Val Set (v5, home, max_seq_length=2048)\n\neval_samples=9,335, unparseable=1,883 (20.2%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |\n|-----------|----------|----------|---------|---------|--------|\n| 600 | 77.25 | 70.81 | 57.11 | 84.52 | `repo-level-cls-v5` |\n| 4000 | 83.32 | 70.26 | 50.56 | 89.97 | `repo-level-cls-v5` |\n| 4200 | 82.82 | 69.54 | 49.43 | 89.65 | `repo-level-cls-v5` |\n| 4400 | 83.49 | 71.63 | 53.29 | 89.97 | `repo-level-cls-v5` |\n| **4600** | **83.63** | **71.72** | **53.36** | **90.07** | `repo-level-cls-v5` |\n\nVal-test consistent: both best at ckpt-4600.\n\n### 4.3 CLS 4B seed42 — Test Set (v5-conda, westd, transformers 4.57.6)\n\nApple-to-apple environment match with CWM v12. eval_samples=9,784, unparseable=132 (1.35%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |\n|-----------|----------|----------|---------|---------|--------|\n| 200 | 52.96 | 52.89 | 51.02 | 54.76 | `repo-level-cls-v5-conda` |\n| 400 | 78.43 | 68.41 | 50.61 | 86.21 | `repo-level-cls-v5-conda` |\n| **600** | **76.37** | **71.17** | **58.93** | **83.41** | `repo-level-cls-v5-conda` |\n\nBest accuracy: ckpt-400 (78.43%). Best F1 macro: ckpt-600 (71.17%).\nHome v5 ckpt-600 (76.74%) vs conda v5-conda ckpt-600 (76.37%): only 0.37pp diff → environment difference negligible.\n\n### 4.4 CLS 4B seed123 — Val Only (home)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | Truncated | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-----------|--------|\n| val@2048 | 200 | 62.51 | 55.54 | 37.94 | 73.14 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 400 | 80.72 | 67.03 | 45.78 | 88.27 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 600 | 76.78 | 66.81 | 48.63 | 85.00 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 800 | 81.81 | 69.14 | 49.37 | 88.91 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 1000 | 82.30 | 67.63 | 45.84 | 89.42 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 400 | 82.57 | 71.24 | 53.18 | 89.29 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 600 | 79.18 | 70.73 | 55.00 | 86.45 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 800 | 83.70 | 73.31 | 56.70 | 90.00 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@5120 | 400 | 86.01 | 79.66 | 68.30 | 91.02 | 0 | 234 | `repo-level-cls-seed123-home` |\n| val@5120 | 600 | 81.89 | 77.01 | 66.43 | 87.60 | 0 | 234 | `repo-level-cls-seed123-home` |\n| **val@5120** | **800** | **87.92** | **81.95** | **71.57** | **92.33** | **0** | **234** | `repo-level-cls-seed123-home` |\n\nKey finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|\n| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@5120 | 400 | 80.47 | 75.84 | — | — | — | 5120 | `repo-level-cls-8b-conda` |\n| test@2048 | 400 | 84.52 | 80.89 | — | — | — | 2048 | `repo-level-cls-8b-conda` |\n| test@2048 | 600 | 78.51 | — | — | — | — | 2048 | `repo-level-cls-8b-conda` |\n| test@8192 | 400 | 84.79 | 81.18 | 72.93 | 89.43 | 0 | 8192 | `cls8b-s42-ckpt400-test8192-eval` |\n| test@8192 | 600 | 79.05 | 75.12 | 65.24 | 85.00 | 0 | 8192 | `cls8b-s42-ckpt600-test8192-eval` |\n| test@8192 | 800 | 83.53 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| test@8192 | 1000 | 83.52 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| test@8192 | 1200 | 83.84 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| **test@8192** | **1400** | **85.47** | — | — | — | **0** | **8192** | `cls8b-s42-test-sweep` |\n| test@8192 | 1600 | 84.99 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n\nTest-best: ckpt-1400 @ 8192 → **85.47% (+12.51pp vs majority baseline)**.\nVal-best: ckpt-1000 @ 8192 → **88.23%** (test=83.52%).\n8B s42 test-best (85.47%) vs 4B best (82.35% v5 ckpt-4600) = **+3.12pp scaling gain**.\n\n### 4.6 CLS 8B seed123 — Repo-level (westd, @8192)\n\n**Val sweep:**\n\n| Checkpoint | Accuracy | Status |\n|-----------|----------|--------|\n| **3000** | **88.69%** | **val-best** |\n| 6200 | 87.52% | |\n| 6400 | 87.48% | |\n| 6600 | 87.23% | |\n| 6633 | — | ⏳ running |\n\n**Test @8192 (ckpt-3000, val-best):**\n\n| Metric | Value |\n|--------|-------|\n| Accuracy | 85.60% |\n| F1 Macro | 78.38% |\n| Fail F1 | 65.89% |\n| Pass F1 | 90.87% |\n| Fail Precision | 91.65% |\n| Fail Recall | 51.44% |\n| Pass Precision | 84.52% |\n| Pass Recall | 98.26% |\n| vs Majority Baseline | +12.64pp |\n\n### 4.7 CLS 4B seed42 — v5 Extended Eval\n\n| Split | Checkpoint | Accuracy |\n|-------|-----------|----------|\n| val | 4400 | 89.96% |\n| **val** | **4600** | **90.07%** ← val-best |\n| test | 4400 | 83.24% |\n| test | 4600 | 83.63% |\n\n### 4.8 Multi-seed 8B Repo-level Comparison\n\n| Seed | Val-best Ckpt | Val Acc | Test Acc | CWM Test | CLS−CWM Gap |\n|------|--------------|---------|----------|----------|-------------|\n| s42 | ckpt-1000 | 88.23% | 83.52% | 58.04% | 25.48pp |\n| seed123 | ckpt-3000 | 88.69% | 85.60% | 59.09% | 26.51pp |\n| **Mean** | — | **88.46%** | **84.56%** | **58.57%** | **25.99pp** |\n\n### 4.9 Repo-level Early Versions (for reference)\n\n| Experiment | Accuracy | F1 Macro | Status | Source |\n|-----------|----------|----------|--------|--------|\n| CLS v4 (4B, early stop) | 66.11 | 56.61 | Below baseline (72.96%) | `repo-level-cls-v4` |\n| CWM v10 (invalid) | 69.91 | 46.71 | 93% unparseable (max_new_tokens=64) | `repo-level-cwm-v10` |\n\n---\n\n## 5. Zero-shot LLM Judge Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | vs Baseline (pp) | vs Fine-tuned 4B (pp) | Source |\n|-------|----------|---------|---------|-------------------|------------------------|--------|\n| Qwen3-8B | 64.40 | 72.20 | 50.50 | +12.65 | −24.03 | `llm-judge-8b-zeroshot` |\n| Qwen3-32B | 71.69 | 75.91 | 65.68 | +19.94 | −16.74 | `llm-judge-32b-zeroshot` |\n\nBoth models heavily biased toward predicting FAIL. 8B→32B scaling = +7.29pp, but still far below fine-tuned 4B (88.43%).\n\n---\n\n## 6. Statistical Analyses\n\n### 6.1 Block Correlation (ICC)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| ICC | 0.1909 | `block-corr-empirical` |\n| ICC p-value | < 0.0001 | `block-corr-empirical` |\n| Design Effect (DEFF) | 3.97 | `block-corr-empirical` |\n| Overall error rate | 12.49% | `block-corr-empirical` |\n| All-correct problems (observed) | 46 | `block-corr-empirical` |\n| All-correct problems (expected i.i.d.) | 16.35 | `block-corr-empirical` |\n| Inference precision | bfloat16 | `block-corr-empirical` |\n\nSignificant block correlation: tests within the same problem are NOT independent. DEFF=3.97 means effective sample size is ~4x smaller than nominal.\n\n### 6.2 Oracle F2P Stratified Analysis\n\n| # Tests per Problem | % of Problems | Block Advantage (pp) | Source |\n|---------------------|---------------|----------------------|--------|\n| T=1 | 68.7% | −0.09 (none) | `oracle-f2p-stratified` |\n| T=2 | 19.1% | +31.69 | `oracle-f2p-stratified` |\n| T=3–5 | 7.1% | +40.74 | `oracle-f2p-stratified` |\n| T≥6 | 5.1% | +40.06 | `oracle-f2p-stratified` |\n| **Overall** | | **+10.93** | `oracle-f2p-stratified` |\n\nT2 problems contribute 55.3% of overall block advantage despite being only 19.1% of problems.\n\n### 6.3 Per-test Diagnostic (CWM seed42)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Best mutation type | return_value (97.26%) | `per-test-precision-recall` |\n| Worst mutation type | off_by_one (82.56%) | `per-test-precision-recall` |\n| Perfect problems (114 total) | 48 (42.1%) | `per-test-precision-recall` |\n| Median problem fail-F1 | 94.12% | `per-test-precision-recall` |\n| FP count | 58 | `per-test-precision-recall` |\n| FN count | 178 | `per-test-precision-recall` |\n\n---\n\n## 7. Simulation Results (MVP-A)\n\n| Scenario | i.i.d. Advantage | Block Advantage | Pass? | Source |\n|----------|-----------------|-----------------|-------|--------|\n| P2P reg=5% | −1.0% | −0.5% | FAIL | `mvp-a-oracle-sim` |\n| P2P reg=10% | +13.2% | +8.3% | PASS | `mvp-a-oracle-sim` |\n| P2P reg=20% | +35.7% | +27.8% | PASS | `mvp-a-oracle-sim` |\n\nReal SWE-bench F2P distribution: median T=1, mean T=3, P75=2, P90=3.\n\n---\n\n## 8. Summary of Key Findings\n\n| Finding | Evidence |\n|---------|----------|\n| CLS > CWM at function-level | 4B: +1.24pp (88.43 vs 87.19), 8B: +2.43pp (89.39 vs 86.96) |\n| CLS scaling benefit (4B→8B) | +0.96pp (88.43→89.39) |\n| CWM no scaling benefit | −0.23pp (87.19→86.96) |\n| CLS-CWM gap widens with scale | 4B: 1.24pp → 8B: 2.43pp |\n| CLS ≈ TRAJ at variant level | gap=−0.45pp, TOST p=0.007 |\n| Per-test advantage is diagnostic | granularity, not raw accuracy |\n| Fine-tuned 4B >> zero-shot 32B | 88.43% vs 71.69% (+16.74pp) |\n| Repo-level 8B > 4B | 85.47% vs 82.35% (+3.12pp), updated with full s42 test sweep |\n| 8B multi-seed repo-level | mean test 84.56%, CLS−CWM gap ~26pp |\n| 4B v5 extended eval | val-best 90.07% (ckpt-4600), test 83.63% |\n| max_seq_length critical for repo | @2048: 20% unparseable → @5120: 0% |\n| Block correlation significant | ICC=0.19, DEFF=3.97 |\n| Per-test advantage needs reg≥10% | 5% regression → no advantage |\n",
    "structuredPatch": [
      {
        "oldStart": 177,
        "oldLines": 6,
        "newStart": 177,
        "newLines": 14,
        "lines": [
          " - @4096: 1,406 unparseable (15.1%), best acc=83.70%",
          " - @5120: 0 unparseable, best acc=87.92%",
          " ",
          "+### 4.4b CLS 4B seed123 — Test (val-selected ckpt-800, @5120)",
          "+",
          "+| Split | Checkpoint | Accuracy | F1 Macro | Source |",
          "+|-------|-----------|----------|----------|--------|",
          "+| test@5120 | 800 (val-best) | 75.33% | — | negative result |",
          "+",
          "+⚠️ Negative result: 75.33% is only +2.37pp above majority baseline (72.96%). Val-best ckpt-800 (87.92%) → test 75.33% = 12.59pp val-test gap. Much worse than seed42 4B v5 (test 83.63%) and 8B models (test ~85%).",
          "+",
          " ### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)",
          " ",
          " | Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |"
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

_source line 30_

Now verify the edits look correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "18e45376-4cf6-4f85-8f54-098e464aea87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEtefyvdCWEsKggLwGNVVq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 47841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_017r6YfU4ghTEZHAY9vaS3AQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "offset": 0,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "391bbc38-e8f4-40c3-99be-37ee14db9b82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEtefyvdCWEsKggLwGNVVq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 47841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
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

_source line 32 · 2026-05-15T10:14:09.000Z_

<details><summary>↩ Tool result · `toolu_017r6YfU4ghTEZHAY9vaS3AQ`</summary>

```text
0	# Eval Sweep Compilation — exec-sim-repair-verifier
1	
2	Generated: 2026-05-15 (updated)
3	
4	---
5	
6	## 1. 8B s42 Val@8192 Sweep (n=9335)
7	
8	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
9	|-----------|-------------|-------------|------------|------------|---------------|
10	| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |
11	| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |
12	| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |
13	| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |
14	| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |
15	| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |
16	| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |
17	| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |
18	
19	**Val best = ckpt-1000 (88.23%)** — confirmed.
20	
21	Majority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).
22	
23	Notes:
24	- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑
25	- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)
26	- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)
27	- 72.96% is the test set majority baseline, not val — corrected 2026-05-15
28	
29	---
30	
31	## 2. 8B s42 Test@8192 Sweep (n=9784)
32	
33	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
34	|-----------|-------------|-------------|------------|------------|---------------|
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "74419497-dbfb-4b0a-9ccb-a71812c2fffc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
      "content": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|",
      "numLines": 35,
      "startLine": 0,
      "totalLines": 210
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01HfQZV3p64wj9Mv6giKH3PP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "offset": 80,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "886d2b69-f830-46aa-a139-d41290c8413c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEtefyvdCWEsKggLwGNVVq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 47841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
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

_source line 34 · 2026-05-15T10:14:09.943Z_

<details><summary>↩ Tool result · `toolu_01HfQZV3p64wj9Mv6giKH3PP`</summary>

```text
80	- Val-selected ckpt-4600 test = 83.63%
81	- Val-test gap consistent with 8B pattern
82	
83	---
84	
85	## 3c. 4B seed123 Test@5120 (n=9784)
86	
87	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
88	|-----------|-------------|-------------|------------|------------|---------------|
89	| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |
90	
91	Notes:
92	- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp
93	- Only +2.37pp above majority baseline — negative result
94	
95	---
96	
97	## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)
98	
99	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
100	|-----------|-------------|-------------|------------|------------|---------------|
101	| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |
102	| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |
103	| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |
104	| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |
105	| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |
106	
107	**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.
108	
109	### 8B seed123 Test@8192
110	
111	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
112	|-----------|-------------|-------------|------------|------------|---------------|
113	| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |
114	| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |
115	| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |
116	
117	---
118	
119	## 5. Summary
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "2279c6b6-feac-4a9c-9ea9-365a307d1c2a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
      "content": "- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---\n\n## 5. Summary",
      "numLines": 40,
      "startLine": 80,
      "totalLines": 210
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01CADN1Sy3q44afK9t9Y1Q8u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md",
  "offset": 175,
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
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "13ace426-9a01-4468-825d-f4108a43a805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEtefyvdCWEsKggLwGNVVq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 47841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
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

_source line 36 · 2026-05-15T10:14:10.426Z_

<details><summary>↩ Tool result · `toolu_01CADN1Sy3q44afK9t9Y1Q8u`</summary>

```text
175	Key finding: max_seq_length dramatically affects unparseable rate and accuracy.
176	- @2048: 1,883 unparseable (20.2%), best acc=82.30%
177	- @4096: 1,406 unparseable (15.1%), best acc=83.70%
178	- @5120: 0 unparseable, best acc=87.92%
179	
180	### 4.4b CLS 4B seed123 — Test (val-selected ckpt-800, @5120)
181	
182	| Split | Checkpoint | Accuracy | F1 Macro | Source |
183	|-------|-----------|----------|----------|--------|
184	| test@5120 | 800 (val-best) | 75.33% | — | negative result |
185	
186	⚠️ Negative result: 75.33% is only +2.37pp above majority baseline (72.96%). Val-best ckpt-800 (87.92%) → test 75.33% = 12.59pp val-test gap. Much worse than seed42 4B v5 (test 83.63%) and 8B models (test ~85%).
187	
188	### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)
189	
190	| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |
191	|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|
192	| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |
193	| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |
194	| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "71b5de42-9380-4b31-9077-946ad7b89341",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md",
      "content": "Key finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.4b CLS 4B seed123 — Test (val-selected ckpt-800, @5120)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Source |\n|-------|-----------|----------|----------|--------|\n| test@5120 | 800 (val-best) | 75.33% | — | negative result |\n\n⚠️ Negative result: 75.33% is only +2.37pp above majority baseline (72.96%). Val-best ckpt-800 (87.92%) → test 75.33% = 12.59pp val-test gap. Much worse than seed42 4B v5 (test 83.63%) and 8B models (test ~85%).\n\n### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|\n| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |",
      "numLines": 20,
      "startLine": 175,
      "totalLines": 343
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

所有修改已完成。汇总：

### val_sweep_compilation.md — 3 处修改
1. **s42 ckpt-200 val**: 添加 ⚠️ 标记和 Notes 说明 "FAILED: resume 目录无 ckpt-200，v2 数据存疑"
2. **seed123 ckpt-6200/6400 test**: 在 test 表中添加两行，标注 "v1 failed (--max_samples 8192), v2 重跑中"
3. **4B seed123 test**: 新增 §3c 节，记录 ckpt-800 test acc=75.33% (negative result, +2.37pp vs baseline)；同步更新 Summary 表和 JSON

### comprehensive_results_summary.md — 1 处修改
4. **§4.4b**: 在 4B seed123 val (§4.4) 之后插入 test 结果，标注 75.33% 为 negative result

### error_analysis_data.md — 无修改
无 ckpt-200 引用，文档干净。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "uuid": "4b319ead-c1a4-45c3-8395-a39da6fd0e8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HF8qWtPDzEkinKYFGRHv4n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2742,
      "cache_read_input_tokens": 48457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2742
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

_source line 38_

所有修改已完成。汇总：

### val_sweep_compilation.md — 3 处修改
1. **s42 ckpt-200 val**: 添加 ⚠️ 标记和 Notes 说明 "FAILED: resume 目录无 ckpt-200，v2 数据存疑"
2. **seed123 ckpt-6200/6400 test**: 在 test 表中添加两行，标注 "v1 failed (--max_samples 8192), v2 重跑中"
3. **4B seed123 test**: 新增 §3c 节，记录 ckpt-800 test acc=75.33% (negative result, +2.37pp vs baseline)；同步更新 Summary 表和 JSON

### comprehensive_results_summary.md — 1 处修改
4. **§4.4b**: 在 4B seed123 val (§4.4) 之后插入 test 结果，标注 75.33% 为 negative result

### error_analysis_data.md — 无修改
无 ckpt-200 引用，文档干净。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 138922,
  "duration_api_ms": 139790,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "6c9bb68d-4f50-436d-a171-15d72f316cf0",
  "total_cost_usd": 0.6295830000000001,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 39358,
    "cache_read_input_tokens": 405405,
    "output_tokens": 7192,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39358,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 303,
        "cache_read_input_tokens": 48457,
        "cache_creation_input_tokens": 2742,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2742
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 963,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001033,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 7192,
      "cacheReadInputTokens": 405405,
      "cacheCreationInputTokens": 39358,
      "webSearchRequests": 0,
      "costUSD": 0.62855,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "593191b6-a708-4b27-bf26-ccc2073b4261"
}
```

</details>

---
