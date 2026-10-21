# data update compilation seed123 test v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_data_update-compilation-seed123-test-v2_20260515T103347.log`
- **Structured JSON:** [`7e9b161d3ac736f5aba0.json`](../../sessions/7e/7e9b161d3ac736f5aba0.json)

## Before a recorded user message

16 recorded events

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
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
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
  "uuid": "8cd53980-7f8e-49e8-a977-656e987e1fec",
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
  "uuid": "bc83842b-25d8-404b-815e-45390e7fc54a",
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the two files to understand their current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "24d1bffb-6dc8-4703-b5e4-d8e11d81b9e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1KPYkwyJSSfVQPxa85Asd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11141,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11141
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01BSQnx8s2FgTGw22FVnoGuK`</summary>

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
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "25bc4df0-3bb9-48a1-b52d-e3fa2d6df8a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1KPYkwyJSSfVQPxa85Asd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11141,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11141
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

_source line 6 · 2026-05-15T10:33:57.632Z_

<details><summary>↩ Tool result · `toolu_01BSQnx8s2FgTGw22FVnoGuK`</summary>

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
11	| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |
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
25	- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑
26	- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)
27	- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)
28	- 72.96% is the test set majority baseline, not val — corrected 2026-05-15
29	
30	---
31	
32	## 2. 8B s42 Test@8192 Sweep (n=9784)
33	
34	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
35	|-----------|-------------|-------------|------------|------------|---------------|
36	| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |
37	| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |
38	| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |
39	| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |
40	| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |
41	| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |
42	| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |
43	
44	Majority baseline accuracy = 72.96% (test set, n=9784).
45	
46	Notes:
47	- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)
48	- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)
49	- Val-test disagreement: val-best ckpt-1000 is not test-best
50	- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)
51	
52	---
53	
54	## 3. 4B v5 Val@5120 Sweep (n=9335)
55	
56	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
57	|-----------|-------------|-------------|------------|------------|---------------|
58	| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |
59	| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |
60	| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |
61	| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |
62	| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |
63	
64	**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.
65	
66	4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).
67	
68	---
69	
70	## 3b. 4B v5 Test@5120 (n=9784)
71	
72	| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |
73	|-----------|-------------|-------------|------------|------------|---------------|
74	| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |
75	| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |
76	
77	Majority baseline accuracy = 72.96% (test set, n=9784).
78	
79	Notes:
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
120	
121	| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |
122	|--------|----------|----------|----------|----------------|
123	| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |
124	| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |
125	| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |
126	| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |
127	| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |
128	| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |
129	| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |
130	
131	---
132	
133	## 6. JSON (for plotting)
134	
135	```json
136	{
137	  "8b_s42_val8192": {
138	    "majority_baseline": 75.88,
139	    "checkpoints": {
140	      "ckpt-200":  {"accuracy": 63.52, "f1_macro": 61.17, "f1_pass": 70.7,  "f1_fail": 51.6,  "exp_id": "cls8b-s42-ckpt200-val8192-eval-v2"},
141	      "ckpt-400":  {"accuracy": 80.96, "f1_macro": null,  "f1_pass": null,  "f1_fail": null,  "exp_id": "repo-level-cls-8b-conda"},
142	      "ckpt-600":  {"accuracy": 85.00, "f1_macro": null,  "f1_pass": null,  "f1_fail": null,  "exp_id": "repo-level-cls-8b-conda"},
143	      "ckpt-800":  {"accuracy": 84.50, "f1_macro": 79.20, "f1_pass": null,  "f1_fail": null,  "exp_id": "cls8b-s42-ckpt800-val8192-eval"},
144	      "ckpt-1000": {"accuracy": 88.23, "f1_macro": 82.72, "f1_pass": 92.5,  "f1_fail": 73.0,  "exp_id": "cls8b-s42-ckpt1000-val8192-eval"},
145	      "ckpt-1200": {"accuracy": 87.76, "f1_macro": 81.25, "f1_pass": 92.3,  "f1_fail": 70.2,  "exp_id": "cls8b-s42-ckpt1200-val8192-v3"},
146	      "ckpt-1400": {"accuracy": 85.97, "f1_macro": 77.15, "f1_pass": 91.34, "f1_fail": 62.95, "exp_id": "cls8b-s42-ckpt1400-val8192-eval"},
147	      "ckpt-1600": {"accuracy": 86.75, "f1_macro": 78.94, "f1_pass": 91.76, "f1_fail": 66.12, "exp_id": "cls8b-s42-ckpt1600-val8192-v2"}
148	    }
149	  },
150	  "8b_s42_test8192": {
151	    "majority_baseline": 72.96,
152	    "checkpoints": {
153	      "ckpt-400":  {"accuracy": 84.79, "f1_macro": 81.18, "f1_pass": 89.43, "f1_fail": 72.93, "exp_id": "cls8b-s42-ckpt400-test8192-eval"},
154	      "ckpt-600":  {"accuracy": 79.05, "f1_macro": 75.12, "f1_pass": 85.00, "f1_fail": 65.24, "exp_id": "cls8b-s42-ckpt600-test8192-eval"},
155	      "ckpt-800":  {"accuracy": 83.53, "f1_macro": 78.97, "f1_pass": 88.77, "f1_fail": 69.17, "exp_id": "cls8b-s42-ckpt800-test8192-eval"},
156	      "ckpt-1000": {"accuracy": 83.52, "f1_macro": 77.50, "f1_pass": 89.14, "f1_fail": 65.85, "exp_id": "cls8b-s42-ckpt1000-test8192-eval"},
157	      "ckpt-1200": {"accuracy": 83.84, "f1_macro": 77.47, "f1_pass": 89.45, "f1_fail": 65.49, "exp_id": "cls8b-s42-ckpt1200-test8192-eval"},
158	      "ckpt-1400": {"accuracy": 85.47, "f1_macro": 78.90, "f1_pass": 90.67, "f1_fail": 67.13, "exp_id": "cls8b-s42-ckpt1400-test8192-eval"},
159	      "ckpt-1600": {"accuracy": 84.99, "f1_macro": 78.94, "f1_pass": 90.22, "f1_fail": 67.65, "exp_id": "cls8b-s42-ckpt1600-test8192-eval"}
160	    }
161	  },
162	  "4b_v5_val5120": {
163	    "majority_baseline": 75.88,
164	    "checkpoints": {
165	      "ckpt-600":  {"accuracy": 82.82, "f1_macro": 79.81, "f1_pass": 87.60, "f1_fail": 72.03, "exp_id": "cls4b-v5-ckpt600-val5120-eval"},
166	      "ckpt-4000": {"accuracy": 89.84, "f1_macro": 84.25, "f1_pass": 93.64, "f1_fail": 74.85, "exp_id": "cls4b-v5-ckpt4000-val5120-eval"},
167	      "ckpt-4200": {"accuracy": 89.06, "f1_macro": 83.07, "f1_pass": 93.1,  "f1_fail": 73.0,  "exp_id": "cls4b-v5-val-sweep-ckpt4200"},
168	      "ckpt-4400": {"accuracy": 89.96, "f1_macro": 84.94, "f1_pass": 93.64, "f1_fail": 76.25, "exp_id": "cls4b-v5-val-sweep-ckpt4400-v3"},
169	      "ckpt-4600": {"accuracy": 90.07, "f1_macro": 85.04, "f1_pass": 93.71, "f1_fail": 76.37, "exp_id": "cls4b-v5-val-sweep-ckpt4600"}
170	    }
171	  },
172	  "4b_v5_test5120": {
173	    "majority_baseline": 72.96,
174	    "checkpoints": {
175	      "ckpt-4400": {"accuracy": 83.24, "f1_macro": 74.44, "f1_pass": 89.44, "f1_fail": 59.45, "exp_id": "cls4b-v5-ckpt4400-test5120-eval"},
176	      "ckpt-4600": {"accuracy": 83.63, "f1_macro": 75.63, "f1_pass": 89.59, "f1_fail": 61.67, "exp_id": "cls4b-v5-ckpt4600-test5120-eval"}
177	    }
178	  },
179	  "4b_seed123_test5120": {
180	    "majority_baseline": 72.96,
181	    "checkpoints": {
182	      "ckpt-800": {"accuracy": 75.33, "f1_macro": null, "f1_pass": null, "f1_fail": null, "exp_id": "negative-result", "note": "val-best, barely above baseline"}
183	    }
184	  },
185	  "8b_seed123_val8192": {
186	    "majority_baseline": 75.88,
187	    "checkpoints": {
188	      "ckpt-3000": {"accuracy": 88.69, "f1_macro": 81.73, "f1_pass": 93.0,  "f1_fail": 70.5,  "exp_id": "cls8b-seed123-ckpt3000-val8192-eval"},
189	      "ckpt-6200": {"accuracy": 87.52, "f1_macro": 79.26, "f1_pass": 92.35, "f1_fail": 66.16, "exp_id": "cls8b-seed123-ckpt6200-val8192-eval"},
190	      "ckpt-6400": {"accuracy": 87.48, "f1_macro": 79.66, "f1_pass": 92.27, "f1_fail": 67.04, "exp_id": "cls8b-seed123-ckpt6400-val8192-eval"},
191	      "ckpt-6600": {"accuracy": 87.23, "f1_macro": 79.02, "f1_pass": 92.14, "f1_fail": 65.9,  "exp_id": "cls8b-seed123-ckpt6600-val8192-eval"},
192	      "ckpt-6633": {"accuracy": 87.10, "f1_macro": 78.79, "f1_pass": 92.07, "f1_fail": 65.52, "exp_id": "cls8b-seed123-ckpt6633-val8192-eval"}
193	    }
194	  },
195	  "8b_seed123_test8192": {
196	    "majority_baseline": 72.96,
197	    "checkpoints": {
198	      "ckpt-3000": {"accuracy": 85.60, "f1_macro": 78.38, "f1_pass": 90.87, "f1_fail": 65.89, "exp_id": "cls8b-seed123-ckpt3000-test8192-eval-v2"}
199	    }
200	  },
201	  "4b_v5_test5120": {
202	    "majority_baseline": 72.96,
203	    "checkpoints": {
204	      "ckpt-4400": {"accuracy": 83.24, "f1_macro": 74.44, "f1_pass": 89.44, "f1_fail": 59.45, "exp_id": "cls4b-v5-ckpt4400-test5120-eval"},
205	      "ckpt-4600": {"accuracy": 83.63, "f1_macro": 75.63, "f1_pass": 89.59, "f1_fail": 61.67, "exp_id": "cls4b-v5-ckpt4600-test5120-eval"}
206	    }
207	  }
208	}
209	```
210	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "8e5d14f6-54f3-4589-b84e-fcdadeffafd7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
      "content": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"4b_seed123_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-800\": {\"accuracy\": 75.33, \"f1_macro\": null, \"f1_pass\": null, \"f1_fail\": null, \"exp_id\": \"negative-result\", \"note\": \"val-best, barely above baseline\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_012q7LGYDkMuPCgg3zXtmGN3`</summary>

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
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "788a67a3-0562-4c92-91af-41109c27633a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1KPYkwyJSSfVQPxa85Asd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11141,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11141
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

_source line 8 · 2026-05-15T10:33:57.837Z_

<details><summary>↩ Tool result · `toolu_012q7LGYDkMuPCgg3zXtmGN3`</summary>

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
195	| val@5120 | 400 | 80.47 | 75.84 | — | — | — | 5120 | `repo-level-cls-8b-conda` |
196	| test@2048 | 400 | 84.52 | 80.89 | — | — | — | 2048 | `repo-level-cls-8b-conda` |
197	| test@2048 | 600 | 78.51 | — | — | — | — | 2048 | `repo-level-cls-8b-conda` |
198	| test@8192 | 400 | 84.79 | 81.18 | 72.93 | 89.43 | 0 | 8192 | `cls8b-s42-ckpt400-test8192-eval` |
199	| test@8192 | 600 | 79.05 | 75.12 | 65.24 | 85.00 | 0 | 8192 | `cls8b-s42-ckpt600-test8192-eval` |
200	| test@8192 | 800 | 83.53 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
201	| test@8192 | 1000 | 83.52 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
202	| test@8192 | 1200 | 83.84 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
203	| **test@8192** | **1400** | **85.47** | — | — | — | **0** | **8192** | `cls8b-s42-test-sweep` |
204	| test@8192 | 1600 | 84.99 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |
205	
206	Test-best: ckpt-1400 @ 8192 → **85.47% (+12.51pp vs majority baseline)**.
207	Val-best: ckpt-1000 @ 8192 → **88.23%** (test=83.52%).
208	8B s42 test-best (85.47%) vs 4B best (82.35% v5 ckpt-4600) = **+3.12pp scaling gain**.
209	
210	### 4.6 CLS 8B seed123 — Repo-level (westd, @8192)
211	
212	**Val sweep:**
213	
214	| Checkpoint | Accuracy | Status |
215	|-----------|----------|--------|
216	| **3000** | **88.69%** | **val-best** |
217	| 6200 | 87.52% | |
218	| 6400 | 87.48% | |
219	| 6600 | 87.23% | |
220	| 6633 | — | ⏳ running |
221	
222	**Test @8192 (ckpt-3000, val-best):**
223	
224	| Metric | Value |
225	|--------|-------|
226	| Accuracy | 85.60% |
227	| F1 Macro | 78.38% |
228	| Fail F1 | 65.89% |
229	| Pass F1 | 90.87% |
230	| Fail Precision | 91.65% |
231	| Fail Recall | 51.44% |
232	| Pass Precision | 84.52% |
233	| Pass Recall | 98.26% |
234	| vs Majority Baseline | +12.64pp |
235	
236	### 4.7 CLS 4B seed42 — v5 Extended Eval
237	
238	| Split | Checkpoint | Accuracy |
239	|-------|-----------|----------|
240	| val | 4400 | 89.96% |
241	| **val** | **4600** | **90.07%** ← val-best |
242	| test | 4400 | 83.24% |
243	| test | 4600 | 83.63% |
244	
245	### 4.8 Multi-seed 8B Repo-level Comparison
246	
247	| Seed | Val-best Ckpt | Val Acc | Test Acc | CWM Test | CLS−CWM Gap |
248	|------|--------------|---------|----------|----------|-------------|
249	| s42 | ckpt-1000 | 88.23% | 83.52% | 58.04% | 25.48pp |
250	| seed123 | ckpt-3000 | 88.69% | 85.60% | 59.09% | 26.51pp |
251	| **Mean** | — | **88.46%** | **84.56%** | **58.57%** | **25.99pp** |
252	
253	### 4.9 Repo-level Early Versions (for reference)
254	
255	| Experiment | Accuracy | F1 Macro | Status | Source |
256	|-----------|----------|----------|--------|--------|
257	| CLS v4 (4B, early stop) | 66.11 | 56.61 | Below baseline (72.96%) | `repo-level-cls-v4` |
258	| CWM v10 (invalid) | 69.91 | 46.71 | 93% unparseable (max_new_tokens=64) | `repo-level-cwm-v10` |
259	
260	---
261	
262	## 5. Zero-shot LLM Judge Baselines
263	
264	| Model | Accuracy | Fail F1 | Pass F1 | vs Baseline (pp) | vs Fine-tuned 4B (pp) | Source |
265	|-------|----------|---------|---------|-------------------|------------------------|--------|
266	| Qwen3-8B | 64.40 | 72.20 | 50.50 | +12.65 | −24.03 | `llm-judge-8b-zeroshot` |
267	| Qwen3-32B | 71.69 | 75.91 | 65.68 | +19.94 | −16.74 | `llm-judge-32b-zeroshot` |
268	
269	Both models heavily biased toward predicting FAIL. 8B→32B scaling = +7.29pp, but still far below fine-tuned 4B (88.43%).
270	
271	---
272	
273	## 6. Statistical Analyses
274	
275	### 6.1 Block Correlation (ICC)
276	
277	| Metric | Value | Source |
278	|--------|-------|--------|
279	| ICC | 0.1909 | `block-corr-empirical` |
280	| ICC p-value | < 0.0001 | `block-corr-empirical` |
281	| Design Effect (DEFF) | 3.97 | `block-corr-empirical` |
282	| Overall error rate | 12.49% | `block-corr-empirical` |
283	| All-correct problems (observed) | 46 | `block-corr-empirical` |
284	| All-correct problems (expected i.i.d.) | 16.35 | `block-corr-empirical` |
285	| Inference precision | bfloat16 | `block-corr-empirical` |
286	
287	Significant block correlation: tests within the same problem are NOT independent. DEFF=3.97 means effective sample size is ~4x smaller than nominal.
288	
289	### 6.2 Oracle F2P Stratified Analysis
290	
291	| # Tests per Problem | % of Problems | Block Advantage (pp) | Source |
292	|---------------------|---------------|----------------------|--------|
293	| T=1 | 68.7% | −0.09 (none) | `oracle-f2p-stratified` |
294	| T=2 | 19.1% | +31.69 | `oracle-f2p-stratified` |
295	| T=3–5 | 7.1% | +40.74 | `oracle-f2p-stratified` |
296	| T≥6 | 5.1% | +40.06 | `oracle-f2p-stratified` |
297	| **Overall** | | **+10.93** | `oracle-f2p-stratified` |
298	
299	T2 problems contribute 55.3% of overall block advantage despite being only 19.1% of problems.
300	
301	### 6.3 Per-test Diagnostic (CWM seed42)
302	
303	| Metric | Value | Source |
304	|--------|-------|--------|
305	| Best mutation type | return_value (97.26%) | `per-test-precision-recall` |
306	| Worst mutation type | off_by_one (82.56%) | `per-test-precision-recall` |
307	| Perfect problems (114 total) | 48 (42.1%) | `per-test-precision-recall` |
308	| Median problem fail-F1 | 94.12% | `per-test-precision-recall` |
309	| FP count | 58 | `per-test-precision-recall` |
310	| FN count | 178 | `per-test-precision-recall` |
311	
312	---
313	
314	## 7. Simulation Results (MVP-A)
315	
316	| Scenario | i.i.d. Advantage | Block Advantage | Pass? | Source |
317	|----------|-----------------|-----------------|-------|--------|
318	| P2P reg=5% | −1.0% | −0.5% | FAIL | `mvp-a-oracle-sim` |
319	| P2P reg=10% | +13.2% | +8.3% | PASS | `mvp-a-oracle-sim` |
320	| P2P reg=20% | +35.7% | +27.8% | PASS | `mvp-a-oracle-sim` |
321	
322	Real SWE-bench F2P distribution: median T=1, mean T=3, P75=2, P90=3.
323	
324	---
325	
326	## 8. Summary of Key Findings
327	
328	| Finding | Evidence |
329	|---------|----------|
330	| CLS > CWM at function-level | 4B: +1.24pp (88.43 vs 87.19), 8B: +2.43pp (89.39 vs 86.96) |
331	| CLS scaling benefit (4B→8B) | +0.96pp (88.43→89.39) |
332	| CWM no scaling benefit | −0.23pp (87.19→86.96) |
333	| CLS-CWM gap widens with scale | 4B: 1.24pp → 8B: 2.43pp |
334	| CLS ≈ TRAJ at variant level | gap=−0.45pp, TOST p=0.007 |
335	| Per-test advantage is diagnostic | granularity, not raw accuracy |
336	| Fine-tuned 4B >> zero-shot 32B | 88.43% vs 71.69% (+16.74pp) |
337	| Repo-level 8B > 4B | 85.47% vs 82.35% (+3.12pp), updated with full s42 test sweep |
338	| 8B multi-seed repo-level | mean test 84.56%, CLS−CWM gap ~26pp |
339	| 4B v5 extended eval | val-best 90.07% (ckpt-4600), test 83.63% |
340	| max_seq_length critical for repo | @2048: 20% unparseable → @5120: 0% |
341	| Block correlation significant | ICC=0.19, DEFF=3.97 |
342	| Per-test advantage needs reg≥10% | 5% regression → no advantage |
343	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "d1162984-89de-4c6f-8a34-2cc19927bedd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_results_summary.md",
      "content": "# Comprehensive Results Summary\n\n> Generated: 2026-05-15 (updated). All numbers sourced from registry (DONE + success only).\n> Excluded: `cls8b-seed123-ckpt3000-val8192-eval` (old training artifact, invalid).\n\n---\n\n## 1. Dataset\n\n| Split | Samples | Class Balance | Majority Baseline |\n|-------|---------|---------------|-------------------|\n| Train | 15,290 | pass 52% / fail 48% | 52.0% |\n| Val | 1,896 | — | — |\n| Test (function) | 1,890 | — | 51.75% |\n| Test (repo) | 9,784 | — | 72.96% |\n| Val (repo) | 9,335 | — | ~75.9% |\n\n5 mutation types: operator_swap, return_value, boundary_removal, variable_swap, off_by_one.\nSource: `mvp-b-data-prep`\n\n---\n\n## 2. Function-level Results (per-test, 1890 test samples)\n\n### 2.1 CLS 4B — 5 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-----------|----------|-----------|----------|--------|\n| 42 | 87.83 | 88.06 | 87.59 | 89.45 | 86.71 | 86.20 | 89.04 | `multi-seed-core` |\n| 123 | 89.52 | 89.64 | 89.40 | 91.76 | 87.63 | 87.34 | 91.56 | `multi-seed-core` |\n| 456 | 87.88 | 87.53 | 88.21 | 93.60 | 82.21 | 83.12 | 93.97 | `multi-seed-core` |\n| 789 | 89.00 | 88.90 | 89.10 | 93.30 | 84.90 | 85.20 | 93.40 | `cls-seed789` |\n| 0 | 87.94 | 87.79 | 88.08 | 92.13 | 83.84 | 84.20 | 92.32 | `cls-seed0` |\n| **Mean** | **88.43** | **88.38** | **88.48** | | | | | |\n| **Std** | **0.78** | **0.88** | **0.68** | | | | | |\n\n### 2.2 CWM 4B — 5 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-------------|-----------|----------|-----------|----------|--------|\n| 42 | 87.51 | 87.15 | 87.86 | — | 93.24 | 81.80 | 82.75 | 93.64 | `per-test-precision-recall` |\n| 123 | 87.20 | 86.95 | 87.44 | 84.44 | — | — | — | — | `cwm-seed123` |\n| 456 | 86.98 | 86.66 | 87.29 | 84.02 | 92.26 | 81.70 | 82.52 | 92.65 | `cwm-seed456` |\n| 789 | 86.67 | 86.74 | 86.60 | 83.97 | 89.37 | 84.25 | 84.09 | 89.25 | `cwm-seed789` |\n| 0 | 87.57 | 87.18 | 87.93 | 84.29 | 93.45 | 81.70 | 82.71 | 93.86 | `cwm-seed0` |\n| **Mean** | **87.19** | **86.94** | **87.42** | **84.18** | | | | | |\n| **Std** | **0.37** | **0.22** | **0.52** | **0.21** | | | | | |\n\n### 2.3 CLS 8B — 3 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Pass Prec | Pass Rec | Fail Prec | Fail Rec | Source |\n|------|----------|---------|---------|-----------|----------|-----------|----------|--------|\n| 42 | 90.48 | 90.86 | 90.06 | 90.22 | 91.51 | 90.76 | 89.36 | `cls8b-eval-seed42` |\n| 123 | 89.37 | 89.54 | 89.19 | 91.20 | 87.93 | 87.54 | 90.90 | `cls8b-eval-seed123` |\n| 456 | 88.31 | 88.20 | 88.41 | 92.29 | 84.46 | 84.72 | 92.43 | `cls8b-seed456` |\n| **Mean** | **89.39** | **89.53** | **89.22** | | | | | |\n| **Std** | **1.09** | **1.33** | **0.83** | | | | | |\n\n### 2.4 CWM 8B — 3 seeds\n\n| Seed | Accuracy | Pass F1 | Fail F1 | Exact Match | Source |\n|------|----------|---------|---------|-------------|--------|\n| 42 | 87.67 | 87.57 | 87.77 | 84.39 | `model-size-scaling-cwm8b` |\n| 123 | 86.98 | 86.83 | 87.13 | 84.13 | `cwm8b-seed123` |\n| 456 | 86.24 | 85.96 | 86.51 | 82.80 | `cwm8b-seed456` |\n| **Mean** | **86.96** | **86.79** | **87.14** | **83.77** | |\n| **Std** | **0.72** | **0.82** | **0.63** | **0.86** | |\n\n### 2.5 CLS vs CWM Comparison\n\n| Config | CLS Acc (mean) | CWM Acc (mean) | Gap (pp) | Seeds |\n|--------|---------------|----------------|----------|-------|\n| 4B | 88.43 ± 0.78 | 87.19 ± 0.37 | **+1.24** | 5 vs 5 |\n| 8B | 89.39 ± 1.09 | 86.96 ± 0.72 | **+2.43** | 3 vs 3 |\n\nGap widens from +1.24pp (4B) to +2.43pp (8B) — supports complexity hypothesis.\n\n### 2.6 Model Size Scaling (4B → 8B)\n\n| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |\n|--------|---------|---------|-------------------|\n| CLS | 88.43 | 89.39 | **+0.96** |\n| CWM | 87.19 | 86.96 | **−0.23** |\n\nCLS benefits from scaling; CWM does not (bottleneck is generative complexity, not model capacity).\n\n---\n\n## 3. Trajectory-level Results (1032 variants, 5 seeds)\n\n| Seed | Accuracy | Unresolved F1 | Resolved F1 | Consistency | Source |\n|------|----------|---------------|-------------|-------------|--------|\n| 42 | 85.66 | 87.50 | 83.18 | 79.94 | `traj-level-finetuned` |\n| 123 | 85.47 | 87.00 | 83.52 | 78.59 | `traj-level-seed123` |\n| 456 | 87.40 | 88.70 | 85.80 | 78.80 | `traj-level-seed456` |\n| 789 | 87.31 | 88.27 | 86.17 | 76.74 | `traj-level-seed789` |\n| 0 | 85.66 | 87.37 | 83.41 | 79.55 | `traj-level-seed0` |\n| **Mean** | **86.30** | **87.77** | **84.42** | **78.72** | |\n| **Std** | **0.97** | **0.68** | **1.45** | **1.26** | |\n\n### CLS vs TRAJ (variant-level, clustered bootstrap)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp | `5-paired-clustered-bootstrap` |\n| 95% CI | [−1.71, +0.84] | `5-paired-clustered-bootstrap` |\n| p-value | 0.499 (not significant) | `5-paired-clustered-bootstrap` |\n| TOST p-value (±2pp margin) | 0.0071 (equivalent) | `5-paired-clustered-bootstrap` |\n\nPer-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29.\n\n**Conclusion**: CLS and TRAJ are statistically equivalent at variant level. Per-test's advantage is diagnostic granularity (which test fails), not raw accuracy.\n\n---\n\n## 4. Repo-level Results (majority baseline: 72.96%)\n\n### 4.1 CLS 4B seed42 — Test Set (v5, home-1x5090, transformers 4.57.6)\n\nmax_seq_length=2048, eval_samples=9,784, unparseable=132 (1.3%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | vs Baseline (pp) | Source |\n|-----------|----------|----------|---------|---------|-------------------|--------|\n| 600 | 76.74 | 73.74 | 64.88 | 82.61 | +3.78 | `repo-level-cls-v5` |\n| 4000 | 81.51 | 72.56 | 56.90 | 88.23 | +8.55 | `repo-level-cls-v5` |\n| 4200 | 80.64 | 72.10 | 56.66 | 87.54 | +7.68 | `repo-level-cls-v5` |\n| 4400 | 82.11 | 73.94 | 59.34 | — | +9.15 | `repo-level-cls-v5` |\n| **4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39** | `repo-level-cls-v5` |\n\nBest: ckpt-4600 (both accuracy and F1 macro).\n\n### 4.2 CLS 4B seed42 — Val Set (v5, home, max_seq_length=2048)\n\neval_samples=9,335, unparseable=1,883 (20.2%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |\n|-----------|----------|----------|---------|---------|--------|\n| 600 | 77.25 | 70.81 | 57.11 | 84.52 | `repo-level-cls-v5` |\n| 4000 | 83.32 | 70.26 | 50.56 | 89.97 | `repo-level-cls-v5` |\n| 4200 | 82.82 | 69.54 | 49.43 | 89.65 | `repo-level-cls-v5` |\n| 4400 | 83.49 | 71.63 | 53.29 | 89.97 | `repo-level-cls-v5` |\n| **4600** | **83.63** | **71.72** | **53.36** | **90.07** | `repo-level-cls-v5` |\n\nVal-test consistent: both best at ckpt-4600.\n\n### 4.3 CLS 4B seed42 — Test Set (v5-conda, westd, transformers 4.57.6)\n\nApple-to-apple environment match with CWM v12. eval_samples=9,784, unparseable=132 (1.35%)\n\n| Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Source |\n|-----------|----------|----------|---------|---------|--------|\n| 200 | 52.96 | 52.89 | 51.02 | 54.76 | `repo-level-cls-v5-conda` |\n| 400 | 78.43 | 68.41 | 50.61 | 86.21 | `repo-level-cls-v5-conda` |\n| **600** | **76.37** | **71.17** | **58.93** | **83.41** | `repo-level-cls-v5-conda` |\n\nBest accuracy: ckpt-400 (78.43%). Best F1 macro: ckpt-600 (71.17%).\nHome v5 ckpt-600 (76.74%) vs conda v5-conda ckpt-600 (76.37%): only 0.37pp diff → environment difference negligible.\n\n### 4.4 CLS 4B seed123 — Val Only (home)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | Truncated | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-----------|--------|\n| val@2048 | 200 | 62.51 | 55.54 | 37.94 | 73.14 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 400 | 80.72 | 67.03 | 45.78 | 88.27 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 600 | 76.78 | 66.81 | 48.63 | 85.00 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 800 | 81.81 | 69.14 | 49.37 | 88.91 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@2048 | 1000 | 82.30 | 67.63 | 45.84 | 89.42 | 1,883 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 400 | 82.57 | 71.24 | 53.18 | 89.29 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 600 | 79.18 | 70.73 | 55.00 | 86.45 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@4096 | 800 | 83.70 | 73.31 | 56.70 | 90.00 | 1,406 | — | `repo-level-cls-seed123-home` |\n| val@5120 | 400 | 86.01 | 79.66 | 68.30 | 91.02 | 0 | 234 | `repo-level-cls-seed123-home` |\n| val@5120 | 600 | 81.89 | 77.01 | 66.43 | 87.60 | 0 | 234 | `repo-level-cls-seed123-home` |\n| **val@5120** | **800** | **87.92** | **81.95** | **71.57** | **92.33** | **0** | **234** | `repo-level-cls-seed123-home` |\n\nKey finding: max_seq_length dramatically affects unparseable rate and accuracy.\n- @2048: 1,883 unparseable (20.2%), best acc=82.30%\n- @4096: 1,406 unparseable (15.1%), best acc=83.70%\n- @5120: 0 unparseable, best acc=87.92%\n\n### 4.4b CLS 4B seed123 — Test (val-selected ckpt-800, @5120)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Source |\n|-------|-----------|----------|----------|--------|\n| test@5120 | 800 (val-best) | 75.33% | — | negative result |\n\n⚠️ Negative result: 75.33% is only +2.37pp above majority baseline (72.96%). Val-best ckpt-800 (87.92%) → test 75.33% = 12.59pp val-test gap. Much worse than seed42 4B v5 (test 83.63%) and 8B models (test ~85%).\n\n### 4.5 CLS 8B seed42 — Conda (westd, transformers 4.57.6)\n\n| Split | Checkpoint | Accuracy | F1 Macro | Fail F1 | Pass F1 | Unparseable | max_seq_len | Source |\n|-------|-----------|----------|----------|---------|---------|-------------|-------------|--------|\n| val@8192 | 200 | 63.52 | 61.17 | 51.60 | 70.70 | 9 | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 400 | 80.96 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@8192 | 600 | 85.00 | — | — | — | — | 8192 | `repo-level-cls-8b-conda` |\n| val@5120 | 400 | 80.47 | 75.84 | — | — | — | 5120 | `repo-level-cls-8b-conda` |\n| test@2048 | 400 | 84.52 | 80.89 | — | — | — | 2048 | `repo-level-cls-8b-conda` |\n| test@2048 | 600 | 78.51 | — | — | — | — | 2048 | `repo-level-cls-8b-conda` |\n| test@8192 | 400 | 84.79 | 81.18 | 72.93 | 89.43 | 0 | 8192 | `cls8b-s42-ckpt400-test8192-eval` |\n| test@8192 | 600 | 79.05 | 75.12 | 65.24 | 85.00 | 0 | 8192 | `cls8b-s42-ckpt600-test8192-eval` |\n| test@8192 | 800 | 83.53 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| test@8192 | 1000 | 83.52 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| test@8192 | 1200 | 83.84 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n| **test@8192** | **1400** | **85.47** | — | — | — | **0** | **8192** | `cls8b-s42-test-sweep` |\n| test@8192 | 1600 | 84.99 | — | — | — | 0 | 8192 | `cls8b-s42-test-sweep` |\n\nTest-best: ckpt-1400 @ 8192 → **85.47% (+12.51pp vs majority baseline)**.\nVal-best: ckpt-1000 @ 8192 → **88.23%** (test=83.52%).\n8B s42 test-best (85.47%) vs 4B best (82.35% v5 ckpt-4600) = **+3.12pp scaling gain**.\n\n### 4.6 CLS 8B seed123 — Repo-level (westd, @8192)\n\n**Val sweep:**\n\n| Checkpoint | Accuracy | Status |\n|-----------|----------|--------|\n| **3000** | **88.69%** | **val-best** |\n| 6200 | 87.52% | |\n| 6400 | 87.48% | |\n| 6600 | 87.23% | |\n| 6633 | — | ⏳ running |\n\n**Test @8192 (ckpt-3000, val-best):**\n\n| Metric | Value |\n|--------|-------|\n| Accuracy | 85.60% |\n| F1 Macro | 78.38% |\n| Fail F1 | 65.89% |\n| Pass F1 | 90.87% |\n| Fail Precision | 91.65% |\n| Fail Recall | 51.44% |\n| Pass Precision | 84.52% |\n| Pass Recall | 98.26% |\n| vs Majority Baseline | +12.64pp |\n\n### 4.7 CLS 4B seed42 — v5 Extended Eval\n\n| Split | Checkpoint | Accuracy |\n|-------|-----------|----------|\n| val | 4400 | 89.96% |\n| **val** | **4600** | **90.07%** ← val-best |\n| test | 4400 | 83.24% |\n| test | 4600 | 83.63% |\n\n### 4.8 Multi-seed 8B Repo-level Comparison\n\n| Seed | Val-best Ckpt | Val Acc | Test Acc | CWM Test | CLS−CWM Gap |\n|------|--------------|---------|----------|----------|-------------|\n| s42 | ckpt-1000 | 88.23% | 83.52% | 58.04% | 25.48pp |\n| seed123 | ckpt-3000 | 88.69% | 85.60% | 59.09% | 26.51pp |\n| **Mean** | — | **88.46%** | **84.56%** | **58.57%** | **25.99pp** |\n\n### 4.9 Repo-level Early Versions (for reference)\n\n| Experiment | Accuracy | F1 Macro | Status | Source |\n|-----------|----------|----------|--------|--------|\n| CLS v4 (4B, early stop) | 66.11 | 56.61 | Below baseline (72.96%) | `repo-level-cls-v4` |\n| CWM v10 (invalid) | 69.91 | 46.71 | 93% unparseable (max_new_tokens=64) | `repo-level-cwm-v10` |\n\n---\n\n## 5. Zero-shot LLM Judge Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | vs Baseline (pp) | vs Fine-tuned 4B (pp) | Source |\n|-------|----------|---------|---------|-------------------|------------------------|--------|\n| Qwen3-8B | 64.40 | 72.20 | 50.50 | +12.65 | −24.03 | `llm-judge-8b-zeroshot` |\n| Qwen3-32B | 71.69 | 75.91 | 65.68 | +19.94 | −16.74 | `llm-judge-32b-zeroshot` |\n\nBoth models heavily biased toward predicting FAIL. 8B→32B scaling = +7.29pp, but still far below fine-tuned 4B (88.43%).\n\n---\n\n## 6. Statistical Analyses\n\n### 6.1 Block Correlation (ICC)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| ICC | 0.1909 | `block-corr-empirical` |\n| ICC p-value | < 0.0001 | `block-corr-empirical` |\n| Design Effect (DEFF) | 3.97 | `block-corr-empirical` |\n| Overall error rate | 12.49% | `block-corr-empirical` |\n| All-correct problems (observed) | 46 | `block-corr-empirical` |\n| All-correct problems (expected i.i.d.) | 16.35 | `block-corr-empirical` |\n| Inference precision | bfloat16 | `block-corr-empirical` |\n\nSignificant block correlation: tests within the same problem are NOT independent. DEFF=3.97 means effective sample size is ~4x smaller than nominal.\n\n### 6.2 Oracle F2P Stratified Analysis\n\n| # Tests per Problem | % of Problems | Block Advantage (pp) | Source |\n|---------------------|---------------|----------------------|--------|\n| T=1 | 68.7% | −0.09 (none) | `oracle-f2p-stratified` |\n| T=2 | 19.1% | +31.69 | `oracle-f2p-stratified` |\n| T=3–5 | 7.1% | +40.74 | `oracle-f2p-stratified` |\n| T≥6 | 5.1% | +40.06 | `oracle-f2p-stratified` |\n| **Overall** | | **+10.93** | `oracle-f2p-stratified` |\n\nT2 problems contribute 55.3% of overall block advantage despite being only 19.1% of problems.\n\n### 6.3 Per-test Diagnostic (CWM seed42)\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Best mutation type | return_value (97.26%) | `per-test-precision-recall` |\n| Worst mutation type | off_by_one (82.56%) | `per-test-precision-recall` |\n| Perfect problems (114 total) | 48 (42.1%) | `per-test-precision-recall` |\n| Median problem fail-F1 | 94.12% | `per-test-precision-recall` |\n| FP count | 58 | `per-test-precision-recall` |\n| FN count | 178 | `per-test-precision-recall` |\n\n---\n\n## 7. Simulation Results (MVP-A)\n\n| Scenario | i.i.d. Advantage | Block Advantage | Pass? | Source |\n|----------|-----------------|-----------------|-------|--------|\n| P2P reg=5% | −1.0% | −0.5% | FAIL | `mvp-a-oracle-sim` |\n| P2P reg=10% | +13.2% | +8.3% | PASS | `mvp-a-oracle-sim` |\n| P2P reg=20% | +35.7% | +27.8% | PASS | `mvp-a-oracle-sim` |\n\nReal SWE-bench F2P distribution: median T=1, mean T=3, P75=2, P90=3.\n\n---\n\n## 8. Summary of Key Findings\n\n| Finding | Evidence |\n|---------|----------|\n| CLS > CWM at function-level | 4B: +1.24pp (88.43 vs 87.19), 8B: +2.43pp (89.39 vs 86.96) |\n| CLS scaling benefit (4B→8B) | +0.96pp (88.43→89.39) |\n| CWM no scaling benefit | −0.23pp (87.19→86.96) |\n| CLS-CWM gap widens with scale | 4B: 1.24pp → 8B: 2.43pp |\n| CLS ≈ TRAJ at variant level | gap=−0.45pp, TOST p=0.007 |\n| Per-test advantage is diagnostic | granularity, not raw accuracy |\n| Fine-tuned 4B >> zero-shot 32B | 88.43% vs 71.69% (+16.74pp) |\n| Repo-level 8B > 4B | 85.47% vs 82.35% (+3.12pp), updated with full s42 test sweep |\n| 8B multi-seed repo-level | mean test 84.56%, CLS−CWM gap ~26pp |\n| 4B v5 extended eval | val-best 90.07% (ckpt-4600), test 83.63% |\n| max_seq_length critical for repo | @2048: 20% unparseable → @5120: 0% |\n| Block correlation significant | ICC=0.19, DEFF=3.97 |\n| Per-test advantage needs reg≥10% | 5% regression → no advantage |\n",
      "numLines": 343,
      "startLine": 1,
      "totalLines": 343
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:

1. Update the seed123 test ckpt-6200 and ckpt-6400 rows in val_sweep_compilation.md (Section 4, line 114-115)
2. Update the JSON section for 8b_seed123_test8192
3. Check comprehensive_results_summary.md for seed123 test data that might need updating

Let me make the edits to val_sweep_compilation.md first. I need to update:
- Line 114: ckpt-6200 test row


- Line 115: ckpt-6400 test row
- The JSON section for 8b_seed123_test8192 (line 196-199)

For comprehensive_results_summary.md, I'm looking at section 4.6 where ckpt-6633 is marked as running for validation, but the test section only shows ckpt-3000. I should check if the test curve data needs updating to include the newer checkpoints. Let me start making these edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "7cd155ee-e32c-4672-b118-63e058472809",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171nduTimiorfgbNsm7qxXY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14818,
      "cache_read_input_tokens": 22982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14818
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

### Assistant

_source line 10_

更新 val_sweep_compilation.md 中三处：test 表格行、JSON 数据块。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "5bd06e10-cda5-4337-a3d0-3629d977e1bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171nduTimiorfgbNsm7qxXY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14818,
      "cache_read_input_tokens": 22982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14818
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_019NHj96VofrYKipHJdyo8mw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |",
  "new_string": "| ckpt-6200 | 84.70 | 77.01 | 90.31 | 63.71 | cls8b-seed123-ckpt6200-test8192-eval-v2 |\n| ckpt-6400 | 85.08 | 77.91 | 90.49 | 65.32 | cls8b-seed123-ckpt6400-test8192-eval-v2 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "fa9c0a7b-e43e-4788-a8b9-4e3408957363",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171nduTimiorfgbNsm7qxXY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14818,
      "cache_read_input_tokens": 22982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14818
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

_source line 12 · 2026-05-15T10:34:11.683Z_

<details><summary>↩ Tool result · `toolu_019NHj96VofrYKipHJdyo8mw`</summary>

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
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "c0c1dc8c-7742-4f1a-bdb1-615025735cd3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |",
    "newString": "| ckpt-6200 | 84.70 | 77.01 | 90.31 | 63.71 | cls8b-seed123-ckpt6200-test8192-eval-v2 |\n| ckpt-6400 | 85.08 | 77.91 | 90.49 | 65.32 | cls8b-seed123-ckpt6400-test8192-eval-v2 |",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"4b_seed123_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-800\": {\"accuracy\": 75.33, \"f1_macro\": null, \"f1_pass\": null, \"f1_fail\": null, \"exp_id\": \"negative-result\", \"note\": \"val-best, barely above baseline\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 111,
        "oldLines": 8,
        "newStart": 111,
        "newLines": 8,
        "lines": [
          " | Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |",
          " |-----------|-------------|-------------|------------|------------|---------------|",
          " | ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |",
          "-| ckpt-6200 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |",
          "-| ckpt-6400 | — | — | — | — | v1 failed (--max_samples 8192), v2 重跑中 |",
          "+| ckpt-6200 | 84.70 | 77.01 | 90.31 | 63.71 | cls8b-seed123-ckpt6200-test8192-eval-v2 |",
          "+| ckpt-6400 | 85.08 | 77.91 | 90.49 | 65.32 | cls8b-seed123-ckpt6400-test8192-eval-v2 |",
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01KVWC1jRNRjDoSyVuhSG7Ee`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
  "old_string": "  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },",
  "new_string": "  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"},\n      \"ckpt-6200\": {\"accuracy\": 84.70, \"f1_macro\": 77.01, \"f1_pass\": 90.31, \"f1_fail\": 63.71, \"exp_id\": \"cls8b-seed123-ckpt6200-test8192-eval-v2\"},\n      \"ckpt-6400\": {\"accuracy\": 85.08, \"f1_macro\": 77.91, \"f1_pass\": 90.49, \"f1_fail\": 65.32, \"exp_id\": \"cls8b-seed123-ckpt6400-test8192-eval-v2\"}\n    }\n  },"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "fcb82626-319e-43cc-8647-df27af737729",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171nduTimiorfgbNsm7qxXY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14818,
      "cache_read_input_tokens": 22982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14818
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

_source line 14 · 2026-05-15T10:34:15.625Z_

<details><summary>↩ Tool result · `toolu_01KVWC1jRNRjDoSyVuhSG7Ee`</summary>

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
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "fb4b2fe7-4cbb-4a3e-848e-ba025d24ab55",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/val_sweep_compilation.md",
    "oldString": "  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },",
    "newString": "  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"},\n      \"ckpt-6200\": {\"accuracy\": 84.70, \"f1_macro\": 77.01, \"f1_pass\": 90.31, \"f1_fail\": 63.71, \"exp_id\": \"cls8b-seed123-ckpt6200-test8192-eval-v2\"},\n      \"ckpt-6400\": {\"accuracy\": 85.08, \"f1_macro\": 77.91, \"f1_pass\": 90.49, \"f1_fail\": 65.32, \"exp_id\": \"cls8b-seed123-ckpt6400-test8192-eval-v2\"}\n    }\n  },",
    "originalFile": "# Eval Sweep Compilation — exec-sim-repair-verifier\n\nGenerated: 2026-05-15 (updated)\n\n---\n\n## 1. 8B s42 Val@8192 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-200 | 63.52 | 61.17 | 70.7 | 51.6 | cls8b-s42-ckpt200-val8192-eval-v2 ⚠️ |\n| ckpt-400 | 80.96 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_400 |\n| ckpt-600 | 85.00 | — | — | — | repo-level-cls-8b-conda → val_8192.ckpt_600 |\n| ckpt-800 | 84.50 | 79.20 | — | — | cls8b-s42-ckpt800-val8192-eval |\n| **ckpt-1000** | **88.23** | **82.72** | **92.5** | **73.0** | cls8b-s42-ckpt1000-val8192-eval |\n| ckpt-1200 | 87.76 | 81.25 | 92.3 | 70.2 | cls8b-s42-ckpt1200-val8192-v3 |\n| ckpt-1400 | 85.97 | 77.15 | 91.34 | 62.95 | cls8b-s42-ckpt1400-val8192-eval |\n| ckpt-1600 | 86.75 | 78.94 | 91.76 | 66.12 | cls8b-s42-ckpt1600-val8192-v2 |\n\n**Val best = ckpt-1000 (88.23%)** — confirmed.\n\nMajority baseline accuracy = 75.88% (val set, n=9335) → gap = +12.35 pp (ckpt-1000).\n\nNotes:\n- ⚠️ ckpt-200: FAILED: resume 目录无 ckpt-200。v2 数据来自 cls8b-s42-ckpt200-val8192-eval-v2，结果存疑\n- ckpt-400/600 only have accuracy (from early sweep in repo-level-cls-8b-conda)\n- ckpt-800 only has accuracy + f1_macro (partial eval, no per-class F1)\n- 72.96% is the test set majority baseline, not val — corrected 2026-05-15\n\n---\n\n## 2. 8B s42 Test@8192 Sweep (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-400 | 84.79 | 81.18 | 89.43 | 72.93 | cls8b-s42-ckpt400-test8192-eval |\n| ckpt-600 | 79.05 | 75.12 | 85.00 | 65.24 | cls8b-s42-ckpt600-test8192-eval |\n| ckpt-800 | 83.53 | 78.97 | 88.77 | 69.17 | cls8b-s42-ckpt800-test8192-eval |\n| ckpt-1000 | 83.52 | 77.50 | 89.14 | 65.85 | cls8b-s42-ckpt1000-test8192-eval |\n| ckpt-1200 | 83.84 | 77.47 | 89.45 | 65.49 | cls8b-s42-ckpt1200-test8192-eval |\n| **ckpt-1400** | **85.47** | **78.90** | **90.67** | **67.13** | cls8b-s42-ckpt1400-test8192-eval |\n| ckpt-1600 | 84.99 | 78.94 | 90.22 | 67.65 | cls8b-s42-ckpt1600-test8192-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Test best = ckpt-1400 (85.47% acc, 78.90 f1_macro)\n- ckpt-1400 has highest F1_pass (90.67) and highest accuracy, but F1_fail (67.13) trails ckpt-400 (72.93)\n- Val-test disagreement: val-best ckpt-1000 is not test-best\n- ckpt-1600 test = 84.99% — sweep complete (8 val + 7 test checkpoints)\n\n---\n\n## 3. 4B v5 Val@5120 Sweep (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-600 | 82.82 | 79.81 | 87.60 | 72.03 | cls4b-v5-ckpt600-val5120-eval |\n| ckpt-4000 | 89.84 | 84.25 | 93.64 | 74.85 | cls4b-v5-ckpt4000-val5120-eval |\n| ckpt-4200 | 89.06 | 83.07 | 93.1 | 73.0 | cls4b-v5-val-sweep-ckpt4200 |\n| ckpt-4400 | 89.96 | 84.94 | 93.64 | 76.25 | cls4b-v5-val-sweep-ckpt4400-v3 |\n| **ckpt-4600** | **90.07** | **85.04** | **93.71** | **76.37** | cls4b-v5-val-sweep-ckpt4600 |\n\n**4B val-best = ckpt-4600 (90.07%, f1_macro=85.04%)** — confirmed with full eval.\n\n4B v5 majority baseline = 75.88% (val set) → gap = +14.19 pp (ckpt-4600).\n\n---\n\n## 3b. 4B v5 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-4400 | 83.24 | 74.44 | 89.44 | 59.45 | cls4b-v5-ckpt4400-test5120-eval |\n| ckpt-4600 | 83.63 | 75.63 | 89.59 | 61.67 | cls4b-v5-ckpt4600-test5120-eval |\n\nMajority baseline accuracy = 72.96% (test set, n=9784).\n\nNotes:\n- Val-selected ckpt-4600 test = 83.63%\n- Val-test gap consistent with 8B pattern\n\n---\n\n## 3c. 4B seed123 Test@5120 (n=9784)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-800 (val-best) | 75.33 | — | — | — | negative result: barely above majority baseline (72.96%) |\n\nNotes:\n- Val-best ckpt-800 (val=87.92%) → test=75.33%, val-test gap = 12.59pp\n- Only +2.37pp above majority baseline — negative result\n\n---\n\n## 4. Cross-seed Reference: 8B seed123 Val@8192 (n=9335)\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| **ckpt-3000** | **88.69** | 81.73 | 93.0 | 70.5 | cls8b-seed123-ckpt3000-val8192-eval |\n| ckpt-6200 | 87.52 | 79.26 | 92.35 | 66.16 | cls8b-seed123-ckpt6200-val8192-eval |\n| ckpt-6400 | 87.48 | 79.66 | 92.27 | 67.04 | cls8b-seed123-ckpt6400-val8192-eval |\n| ckpt-6600 | 87.23 | 79.02 | 92.14 | 65.9 | cls8b-seed123-ckpt6600-val8192-eval |\n| ckpt-6633 | 87.10 | 78.79 | 92.07 | 65.52 | cls8b-seed123-ckpt6633-val8192-eval |\n\n**seed123 val-best = ckpt-3000 (88.69%)** — later checkpoints all lower, confirming peak at ckpt-3000.\n\n### 8B seed123 Test@8192\n\n| Checkpoint | Accuracy (%) | F1_macro (%) | F1_pass (%) | F1_fail (%) | Source exp_id |\n|-----------|-------------|-------------|------------|------------|---------------|\n| ckpt-3000 | 85.60 | 78.38 | 90.87 | 65.89 | cls8b-seed123-ckpt3000-test8192-eval-v2 |\n| ckpt-6200 | 84.70 | 77.01 | 90.31 | 63.71 | cls8b-seed123-ckpt6200-test8192-eval-v2 |\n| ckpt-6400 | 85.08 | 77.91 | 90.49 | 65.32 | cls8b-seed123-ckpt6400-test8192-eval-v2 |\n\n---\n\n## 5. Summary\n\n| Config | Best Ckpt | Accuracy | F1_macro | Gap vs Majority |\n|--------|----------|----------|----------|----------------|\n| 8B s42 val@8192 | ckpt-1000 | 88.23 | 82.72 | +12.35 pp |\n| 8B s42 test@8192 | ckpt-1400 | 85.47 | 78.90 | +12.51 pp |\n| 4B v5 val@5120 | ckpt-4600 | 90.07 | 85.04 | +14.19 pp |\n| 4B v5 test@5120 (val-selected) | ckpt-4600 | 83.63 | 75.63 | +10.67 pp |\n| 4B seed123 test@5120 (val-selected) | ckpt-800 | 75.33 | — | +2.37 pp ⚠️ |\n| 8B seed123 val@8192 | ckpt-3000 | 88.69 | 81.73 | +12.81 pp |\n| 8B seed123 test@8192 (val-selected) | ckpt-3000 | 85.60 | 78.38 | +12.64 pp |\n\n---\n\n## 6. JSON (for plotting)\n\n```json\n{\n  \"8b_s42_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-200\":  {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_pass\": 70.7,  \"f1_fail\": 51.6,  \"exp_id\": \"cls8b-s42-ckpt200-val8192-eval-v2\"},\n      \"ckpt-400\":  {\"accuracy\": 80.96, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-600\":  {\"accuracy\": 85.00, \"f1_macro\": null,  \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"repo-level-cls-8b-conda\"},\n      \"ckpt-800\":  {\"accuracy\": 84.50, \"f1_macro\": 79.20, \"f1_pass\": null,  \"f1_fail\": null,  \"exp_id\": \"cls8b-s42-ckpt800-val8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_pass\": 92.5,  \"f1_fail\": 73.0,  \"exp_id\": \"cls8b-s42-ckpt1000-val8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_pass\": 92.3,  \"f1_fail\": 70.2,  \"exp_id\": \"cls8b-s42-ckpt1200-val8192-v3\"},\n      \"ckpt-1400\": {\"accuracy\": 85.97, \"f1_macro\": 77.15, \"f1_pass\": 91.34, \"f1_fail\": 62.95, \"exp_id\": \"cls8b-s42-ckpt1400-val8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_pass\": 91.76, \"f1_fail\": 66.12, \"exp_id\": \"cls8b-s42-ckpt1600-val8192-v2\"}\n    }\n  },\n  \"8b_s42_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-400\":  {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_pass\": 89.43, \"f1_fail\": 72.93, \"exp_id\": \"cls8b-s42-ckpt400-test8192-eval\"},\n      \"ckpt-600\":  {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_pass\": 85.00, \"f1_fail\": 65.24, \"exp_id\": \"cls8b-s42-ckpt600-test8192-eval\"},\n      \"ckpt-800\":  {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_pass\": 88.77, \"f1_fail\": 69.17, \"exp_id\": \"cls8b-s42-ckpt800-test8192-eval\"},\n      \"ckpt-1000\": {\"accuracy\": 83.52, \"f1_macro\": 77.50, \"f1_pass\": 89.14, \"f1_fail\": 65.85, \"exp_id\": \"cls8b-s42-ckpt1000-test8192-eval\"},\n      \"ckpt-1200\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_pass\": 89.45, \"f1_fail\": 65.49, \"exp_id\": \"cls8b-s42-ckpt1200-test8192-eval\"},\n      \"ckpt-1400\": {\"accuracy\": 85.47, \"f1_macro\": 78.90, \"f1_pass\": 90.67, \"f1_fail\": 67.13, \"exp_id\": \"cls8b-s42-ckpt1400-test8192-eval\"},\n      \"ckpt-1600\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_pass\": 90.22, \"f1_fail\": 67.65, \"exp_id\": \"cls8b-s42-ckpt1600-test8192-eval\"}\n    }\n  },\n  \"4b_v5_val5120\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-600\":  {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_pass\": 87.60, \"f1_fail\": 72.03, \"exp_id\": \"cls4b-v5-ckpt600-val5120-eval\"},\n      \"ckpt-4000\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_pass\": 93.64, \"f1_fail\": 74.85, \"exp_id\": \"cls4b-v5-ckpt4000-val5120-eval\"},\n      \"ckpt-4200\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_pass\": 93.1,  \"f1_fail\": 73.0,  \"exp_id\": \"cls4b-v5-val-sweep-ckpt4200\"},\n      \"ckpt-4400\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_pass\": 93.64, \"f1_fail\": 76.25, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4400-v3\"},\n      \"ckpt-4600\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_pass\": 93.71, \"f1_fail\": 76.37, \"exp_id\": \"cls4b-v5-val-sweep-ckpt4600\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  },\n  \"4b_seed123_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-800\": {\"accuracy\": 75.33, \"f1_macro\": null, \"f1_pass\": null, \"f1_fail\": null, \"exp_id\": \"negative-result\", \"note\": \"val-best, barely above baseline\"}\n    }\n  },\n  \"8b_seed123_val8192\": {\n    \"majority_baseline\": 75.88,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_pass\": 93.0,  \"f1_fail\": 70.5,  \"exp_id\": \"cls8b-seed123-ckpt3000-val8192-eval\"},\n      \"ckpt-6200\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_pass\": 92.35, \"f1_fail\": 66.16, \"exp_id\": \"cls8b-seed123-ckpt6200-val8192-eval\"},\n      \"ckpt-6400\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_pass\": 92.27, \"f1_fail\": 67.04, \"exp_id\": \"cls8b-seed123-ckpt6400-val8192-eval\"},\n      \"ckpt-6600\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_pass\": 92.14, \"f1_fail\": 65.9,  \"exp_id\": \"cls8b-seed123-ckpt6600-val8192-eval\"},\n      \"ckpt-6633\": {\"accuracy\": 87.10, \"f1_macro\": 78.79, \"f1_pass\": 92.07, \"f1_fail\": 65.52, \"exp_id\": \"cls8b-seed123-ckpt6633-val8192-eval\"}\n    }\n  },\n  \"8b_seed123_test8192\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}\n    }\n  },\n  \"4b_v5_test5120\": {\n    \"majority_baseline\": 72.96,\n    \"checkpoints\": {\n      \"ckpt-4400\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_pass\": 89.44, \"f1_fail\": 59.45, \"exp_id\": \"cls4b-v5-ckpt4400-test5120-eval\"},\n      \"ckpt-4600\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_pass\": 89.59, \"f1_fail\": 61.67, \"exp_id\": \"cls4b-v5-ckpt4600-test5120-eval\"}\n    }\n  }\n}\n```\n",
    "structuredPatch": [
      {
        "oldStart": 195,
        "oldLines": 7,
        "newStart": 195,
        "newLines": 9,
        "lines": [
          "   \"8b_seed123_test8192\": {",
          "     \"majority_baseline\": 72.96,",
          "     \"checkpoints\": {",
          "-      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"}",
          "+      \"ckpt-3000\": {\"accuracy\": 85.60, \"f1_macro\": 78.38, \"f1_pass\": 90.87, \"f1_fail\": 65.89, \"exp_id\": \"cls8b-seed123-ckpt3000-test8192-eval-v2\"},",
          "+      \"ckpt-6200\": {\"accuracy\": 84.70, \"f1_macro\": 77.01, \"f1_pass\": 90.31, \"f1_fail\": 63.71, \"exp_id\": \"cls8b-seed123-ckpt6200-test8192-eval-v2\"},",
          "+      \"ckpt-6400\": {\"accuracy\": 85.08, \"f1_macro\": 77.91, \"f1_pass\": 90.49, \"f1_fail\": 65.32, \"exp_id\": \"cls8b-seed123-ckpt6400-test8192-eval-v2\"}",
          "     }",
          "   },",
          "   \"4b_v5_test5120\": {"
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

_source line 15_

val_sweep_compilation.md 已更新完成。

关于 comprehensive_results_summary.md：Section 4.6 的 seed123 test 部分（line 222-234）只记录了 val-best ckpt-3000 的 test 结果，没有 ckpt-6200/6400 的 test 行——这是合理的，因为那个表格只展示 val-selected checkpoint 的 test 性能。ckpt-6200/6400 不是 val-best，属于 sweep 补充数据，只需在 val_sweep_compilation.md 中记录即可，comprehensive_results_summary.md 无需更新。

补充观察：ckpt-6400 test (85.08%) 接近 ckpt-3000 test (85.60%)，差距仅 0.52pp，但 f1_macro 低 0.47pp (77.91 vs 78.38)。val-best ckpt-3000 仍然是 test-best，val-test 选择一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "uuid": "7d77965c-b57e-4064-be9b-bc608f899ef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MdYKvMDgRVCeTv3BWiYZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1311,
      "cache_read_input_tokens": 37800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1311
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

_source line 16_

val_sweep_compilation.md 已更新完成。

关于 comprehensive_results_summary.md：Section 4.6 的 seed123 test 部分（line 222-234）只记录了 val-best ckpt-3000 的 test 结果，没有 ckpt-6200/6400 的 test 行——这是合理的，因为那个表格只展示 val-selected checkpoint 的 test 性能。ckpt-6200/6400 不是 val-best，属于 sweep 补充数据，只需在 val_sweep_compilation.md 中记录即可，comprehensive_results_summary.md 无需更新。

补充观察：ckpt-6400 test (85.08%) 接近 ckpt-3000 test (85.60%)，差距仅 0.52pp，但 f1_macro 低 0.47pp (77.91 vs 78.38)。val-best ckpt-3000 仍然是 test-best，val-test 选择一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 29734,
  "duration_api_ms": 30660,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "8e776f9c-95a6-42b1-bcfe-02635eb9ee11",
  "total_cost_usd": 0.247726,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 27270,
    "cache_read_input_tokens": 72623,
    "output_tokens": 1595,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27270,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 278,
        "cache_read_input_tokens": 37800,
        "cache_creation_input_tokens": 1311,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1311
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 992,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001077,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1595,
      "cacheReadInputTokens": 72623,
      "cacheCreationInputTokens": 27270,
      "webSearchRequests": 0,
      "costUSD": 0.246649,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "56b9ebc6-39eb-40bf-916b-354d321c7340"
}
```

</details>

---
